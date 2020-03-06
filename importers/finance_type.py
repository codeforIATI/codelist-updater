import csv

import requests

from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/finance_types.csv'
lookup = {
    'code': 'code',
    'category': 'category',
    'name_en': 'name_en',
    'name_fr': 'name_fr',
    'description_en': 'description_en',
    'description_fr': 'description_fr',
}
r = requests.get(url)
reader = csv.DictReader(r.iter_lines(decode_unicode=True))
finance_types = []
for finance_type in reader:
    if finance_type['name_en'] == '':
        finance_type['name_en'] = finance_type['description_en']
    if finance_type['name_fr'] == '':
        finance_type['name_fr'] = finance_type['description_fr']
    finance_types.append(finance_type)
source_to_xml('FinanceType', None, lookup, source_data=finance_types)
