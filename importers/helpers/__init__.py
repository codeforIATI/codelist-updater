"""
Converts codelist files from external sources into the format used by IATI.
"""
import argparse
from collections import OrderedDict
from io import StringIO
from os.path import join
import subprocess

import requests
from lxml import etree as ET
import csv


class Importer:
    def __init__(self, tmpl_name, source_url, lookup,
                 source_data=None, order_by=None, sort_attrs=False):
        self.tmpl_name = tmpl_name
        self.order_by = order_by
        self.sort_attrs = sort_attrs

        if source_data:
            self.source_data = [OrderedDict([
                 (outp, x[inp]) for outp, inp in lookup
             ]) for x in source_data]
        else:
            code_lookup = [lookup_value for x, lookup_value in lookup
                           if x == 'code'][0]
            r = fetch(source_url)
            reader = csv.DictReader(StringIO(r.content.decode()))
            self.source_data = [OrderedDict([
                (k, x.get(v)) for k, v in lookup
            ]) for x in reader if x[code_lookup]]
        self.run()

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--deploy', action='store_true')
        args = parser.parse_args()
        self.source_to_xml()
        if args.deploy:
            self.push_changes()

    def indent(self, elem, level=0, shift=2):
        """
        Pretty print XML

        Adapted from code at http://effbot.org/zone/element-lib.htm
        """
        i = '\n' + level * ' ' * shift
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + ' ' * shift
            if not elem.tail or not elem.tail.strip():
                # hack to remove trailing newline
                if level:
                    elem.tail = i
            for elem in elem:
                self.indent(elem, level + 1, shift)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    def create_codelist_item(self, keys, xml=None, namespaces=None):
        if not namespaces:
            namespaces = {}
        if xml is None:
            xml = ET.Element('codelist-item')
            xml.set('status', 'active')
        for key in keys:
            lang = None
            if key.startswith('@'):
                continue
            if '_' in key:
                key, lang = key.split('_')
            if xml.xpath(key, namespaces=namespaces):
                continue
            if ':' in key:
                ns, key = key.split(':')
                key = '{{{namespace}}}{key}'.format(
                    namespace=namespaces[ns], key=key)
            el = ET.Element(key)
            if lang:
                el.append(ET.Element('narrative'))
            xml.append(el)
        return xml

    def update_codelist_item(self, codelist_item, code_dict, namespaces=None):
        if not namespaces:
            namespaces = {}
        for k, v in code_dict.items():
            if k.startswith('@'):
                k = k[1:]
                if v:
                    codelist_item.set(k, v)
                continue
            if '_' in k:
                el, lang = k.split('_')
                if lang == 'en':
                    narrative = codelist_item.xpath(
                        f'{el}/narrative[not(@xml:lang)]',
                        namespaces=namespaces)[0]
                else:
                    narrative = codelist_item.xpath(
                        f'{el}/narrative[@xml:lang="{lang}"]',
                        namespaces=namespaces)
                    if narrative:
                        narrative = narrative[0]
                        if not v:
                            if narrative.text:
                                # remove newly empty nodes
                                narrative.getparent().remove(narrative)
                                continue
                            else:
                                # leave existing empty nodes
                                continue
                    elif v:
                        parent = codelist_item.xpath(el, namespaces=namespaces)[0]
                        narrative = ET.Element('narrative')
                        narrative.set(
                            '{http://www.w3.org/XML/1998/namespace}lang',
                            lang)
                        parent.append(narrative)
                    else:
                        continue
            else:
                narrative = codelist_item.xpath(k, namespaces=namespaces)[0]
            narrative.text = v
        return codelist_item

    def source_to_xml(self):
        etparser = ET.XMLParser(encoding='utf-8', remove_blank_text=True)
        try:
            old_xml = ET.parse(
                join('codelist_repo', 'xml', '{}.xml'.format(self.tmpl_name)),
                etparser)
            old_codelist_els = old_xml.xpath('//codelist-item')
        except OSError:
            old_codelist_els = []

        tmpl_path = join('templates', '{}.xml'.format(self.tmpl_name))
        xml = ET.parse(tmpl_path, etparser)
        namespaces = xml.getroot().nsmap
        codelist_items = xml.find('codelist-items')

        source_data_dict = OrderedDict([(source_data_row['code'].upper(), source_data_row) for source_data_row in self.source_data])

        old_codelist_codes = [
            old_codelist_el.find('code').text.upper()
            for old_codelist_el in old_codelist_els]

        while True:
            if not old_codelist_els and not source_data_dict:
                break

            if source_data_dict:
                new_code_dict = list(source_data_dict.values())[0]
                if new_code_dict['code'].upper() not in old_codelist_codes:
                    # add a new code
                    new_codelist_item = self.create_codelist_item(new_code_dict.keys(), namespaces=namespaces)
                    new_codelist_item = self.update_codelist_item(new_codelist_item, new_code_dict, namespaces=namespaces)
                    codelist_items.append(new_codelist_item)
                    source_data_dict.popitem(last=False)
                    continue

            if old_codelist_els:
                old_codelist_el = old_codelist_els[0]
                old_codelist_code = old_codelist_el.find('code').text.upper()
            else:
                old_codelist_code = None

            if old_codelist_code in source_data_dict:
                # it's in the current codes, so update it
                new_code_dict = source_data_dict[old_codelist_code]
                updated_codelist_item = self.create_codelist_item(new_code_dict.keys(), old_codelist_el, namespaces=namespaces)
                updated_codelist_item = self.update_codelist_item(updated_codelist_item, new_code_dict, namespaces=namespaces)
                codelist_items.append(updated_codelist_item)
                del source_data_dict[old_codelist_code]
            elif old_codelist_el.attrib.get('status') == 'withdrawn':
                # it's an old withdrawn code, so just copy it
                codelist_items.append(old_codelist_el)
            elif codelist_items.xpath('//codelist-item/code[text()="{}"]/..'.format(old_codelist_el.find('code').text)):
                # some codelist items are hard-coded, and should just
                # be left as is
                pass
            else:
                old_codelist_el.attrib['status'] = 'withdrawn'
                # old_codelist_el.attrib['withdrawal-date'] = today
                codelist_items.append(old_codelist_el)
            old_codelist_els.pop(0)

        if self.order_by:
            codelist_items[:] = sorted(
                codelist_items,
                key=lambda x: x.xpath(self.order_by))

        if self.sort_attrs:
            for ci in codelist_items:
                sorted_attribs = sorted(ci.attrib.items())
                [ci.attrib.pop(k) for k in ci.attrib.keys()]
                [ci.set(k, v) for k, v in sorted_attribs]

        output_path = join('codelist_repo', 'xml', '{}.xml'.format(self.tmpl_name))
        for el in xml.iter('*'):
            if el.text is not None:
                if not el.text.strip():
                    # force tag self-escaping
                    el.text = None
        self.indent(xml.getroot(), 0, 4)
        xml.write(output_path, encoding='utf-8', pretty_print=True)

    def push_changes(self):
        subprocess.run('./update.sh ' + self.tmpl_name, shell=True)


def fetch(url, *args, **kwargs):
    r = requests.get(url, *args, **kwargs)
    r.raise_for_status()
    return r
