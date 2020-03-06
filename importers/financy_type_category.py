import csv

import requests

from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/finance_type_categories.csv'
lookup_no_desc = {
    'code': 'code',
    'name_en': 'name_en',
    'name_fr': 'name_fr',
}
r = requests.get(url)
reader = csv.DictReader(r.iter_lines(decode_unicode=True))
finance_type_categories = []
for finance_type_category in reader:
    if finance_type_category['code'] == '0':
        continue
    finance_type_categories.append(finance_type_category)
source_to_xml('FinanceType-category', None, lookup_no_desc,
              source_data=finance_type_categories)
