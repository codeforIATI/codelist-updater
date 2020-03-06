import shutil
from collections import OrderedDict
from datetime import date
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
today = str(date.today())


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
    tmpl_path = join('templates', 'generic-codelist-item.xml')
    xml = ET.parse(tmpl_path, etparser).getroot()
    if 'name_en' not in keys:
        xml.remove(xml.find('name'))
    if 'description_en' not in keys:
        xml.remove(xml.find('description'))
    if 'category' not in keys:
        xml.remove(xml.find('category'))
    return xml


def update_codelist_item(codelist_item, code_dict):
    # update code
    if not codelist_item.find('code').text:
        codelist_item.find('code').text = code_dict['code']
    if 'category' in code_dict:
        # update category
        codelist_item.find('category').text = code_dict['category']

    if 'name_en' in code_dict:
        for name_el in codelist_item.findall('name/narrative'):
            if name_el.get('{http://www.w3.org/XML/1998/namespace}lang') == 'fr':
                name_el.text = str_update(name_el.text, code_dict.get('name_fr'))
            else:
                name_el.text = str_update(name_el.text, code_dict.get('name_en'))

    if 'description_en' in code_dict:
        for description_el in codelist_item.findall('description/narrative'):
            if description_el.get('{http://www.w3.org/XML/1998/namespace}lang') == 'fr':
                if code_dict['description_fr']:
                    description_el.text = str_update(description_el.text, code_dict['description_fr'])
                else:
                    codelist_item.find('description').remove(description_el)
            else:
                description_el.text = str_update(description_el.text, code_dict['description_en'])

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

    if not source_data:
        r = requests.get(source_url)
        reader = csv.DictReader(r.iter_lines(decode_unicode=True))
        source_data = [{
            k: x.get(v) for k, v in lookup.items()
        } for x in reader if x[lookup['code']]]

    source_data_dict = OrderedDict([(source_data_row['code'].upper(), source_data_row) for source_data_row in source_data])

    old_codelist_els = old_xml.xpath('//codelist-item')
    while old_codelist_els:
        old_codelist_el = old_codelist_els.pop(0)
        old_codelist_code = old_codelist_el.find('code').text.upper()
        # peek at the first code
        if source_data_dict:
            new_code_dict = list(source_data_dict.values())[0]
            if new_code_dict['code'].upper() != old_codelist_code and not old_xml.xpath('//codelist-item/code[text()="{}"]/..'.format(new_code_dict['code'])):
                # add a new code, with activation date of today
                new_codelist_item = create_codelist_item(new_code_dict.keys())
                new_codelist_item = update_codelist_item(new_codelist_item, new_code_dict)
                new_codelist_item.attrib['status'] = 'active'
                new_codelist_item.attrib['activation-date'] = today
                codelist_items.append(new_codelist_item)
                source_data_dict.popitem(last=False)
                # push the last popped item onto the front of the queue
                old_codelist_els.insert(0, old_codelist_el)
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
            # it's a newly withdrawn code, so mark the withdrawal date
            # as today, and copy it
            old_codelist_el.attrib['status'] = 'withdrawn'
            old_codelist_el.attrib['withdrawal-date'] = today
            codelist_items.append(old_codelist_el)

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
