import shutil
from collections import OrderedDict
from os.path import join
import re
import subprocess

import requests
from lxml import etree as ET
import csv


"""

Converts codelist files from external sources into the format used by IATI.

Note not all external codelists are converted automatically yet.

"""
etparser = ET.XMLParser(encoding='utf-8', remove_blank_text=True)


# Adapted from code at http://effbot.org/zone/element-lib.htm
def indent(elem, level=0, shift=2):
    i = '\n' + level * ' ' * shift
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + ' ' * shift
        if not elem.tail or not elem.tail.strip():
            # hack to remove trailing newline
            if level:
                elem.tail = i
        for elem in elem:
            indent(elem, level + 1, shift)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def str_update(current, proposed):
    if current and proposed and re.split(r'[\s|\xa0]+', current) == re.split(r'[\s|\xa0]+', proposed):
        return current
    elif proposed:
        return proposed.replace('\r', '').replace('.  ', '. ').strip()
    return None


def create_codelist_item(keys):
    xml = ET.Element('codelist-item')
    xml.set('status', 'active')
    if 'code' in keys:
        xml.append(ET.Element('code'))
    if 'name_en' in keys:
        name = ET.Element('name')
        name.append(ET.Element('narrative'))
        xml.append(name)
    if 'description_en' in keys:
        description = ET.Element('description')
        description.append(ET.Element('narrative'))
        xml.append(description)
    if 'category' in keys:
        xml.append(ET.Element('category'))
    return xml


def update_codelist_item(codelist_item, code_dict):
    for k, v in code_dict.items():
        if '_' in k:
            el, lang = k.split('_')
            if lang == 'en':
                narrative = codelist_item.xpath(
                    f'{el}/narrative[not(@xml:lang)]')[0]
            else:
                narrative = codelist_item.xpath(
                    f'{el}/narrative[@xml:lang="{lang}"]')
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
                    parent = codelist_item.find(el)
                    narrative = ET.Element('narrative')
                    narrative.set(
                        '{http://www.w3.org/XML/1998/namespace}lang',
                        lang)
                    parent.append(narrative)
                else:
                    continue
            narrative.text = v
        elif k == 'withdrawal-date':
            if v:
                codelist_item.set(k, v)
                codelist_item.set('status', 'withdrawn')
        else:
            codelist_item.find(k).text = v.strip()
    return codelist_item


def reset_repo(repo, tmpl_name):
    if not repo:
        repo = 'IATI-Codelists-NonEmbedded'
    repo = 'https://codeforIATIbot:${GITHUB_TOKEN}@github.com/' + \
           f'codeforIATI/{repo}.git'
    shutil.rmtree('codelist_repo', ignore_errors=True)
    subprocess.run(f'git clone {repo} codelist_repo && ' +
                   f'cd codelist_repo && ' +
                   f'git branch {tmpl_name}-update && ' +
                   f'git checkout {tmpl_name}-update && '
                   f'git pull origin {tmpl_name}-update', shell=True)


def source_to_xml(tmpl_name, source_url, lookup, repo=None, source_data=None):
    reset_repo(repo, tmpl_name)
    old_xml = ET.parse(join('codelist_repo', 'xml', '{}.xml'.format(tmpl_name)), etparser)

    tmpl_path = join('templates', '{}.xml'.format(tmpl_name))
    xml = ET.parse(tmpl_path, etparser)
    codelist_items = xml.find('codelist-items')

    if source_data:
        source_data = [{
             k: x[k] for k in lookup.keys()
         } for x in source_data]
    else:
        r = requests.get(source_url)
        reader = csv.DictReader(r.iter_lines(decode_unicode=True))
        source_data = [{
            k: x.get(v) for k, v in lookup.items()
        } for x in reader if x[lookup['code']]]

    source_data_dict = OrderedDict([(source_data_row['code'].upper(), source_data_row) for source_data_row in source_data])

    old_codelist_els = old_xml.xpath('//codelist-item')
    while True:
        if not old_codelist_els and not source_data_dict:
            break
        if old_codelist_els:
            old_codelist_el = old_codelist_els[0]
            old_codelist_code = old_codelist_el.find('code').text.upper()
        else:
            old_codelist_code = None
        if source_data_dict:
            new_code_dict = list(source_data_dict.values())[0]
            if new_code_dict['code'].upper() != old_codelist_code and not old_xml.xpath('//codelist-item/code[text()="{}"]/..'.format(new_code_dict['code'])):
                # add a new code
                new_codelist_item = create_codelist_item(new_code_dict.keys())
                new_codelist_item = update_codelist_item(new_codelist_item, new_code_dict)
                # new_codelist_item.attrib['activation-date'] = today
                codelist_items.append(new_codelist_item)
                source_data_dict.popitem(last=False)
                continue

        if old_codelist_code in source_data_dict:
            # it's in the current codes, so update it
            new_code_dict = source_data_dict[old_codelist_code]
            updated_codelist_item = update_codelist_item(old_codelist_el, new_code_dict)
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

    output_path = join('codelist_repo', 'xml', '{}.xml'.format(tmpl_name))
    for el in xml.iter('*'):
        if el.text is not None:
            if not el.text.strip():
                # force tag self-escaping
                el.text = None
    indent(xml.getroot(), 0, 4)
    xml.write(output_path, encoding='utf-8', pretty_print=True)
    push_changes(tmpl_name)


def push_changes(tmpl_name):
    subprocess.run('./update.sh ' + tmpl_name, shell=True)
