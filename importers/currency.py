import csv
import re

import requests

from helpers import source_to_xml


yyyy_mm = re.compile(r'^\d{4}-\d{2}$')
yyyy_mm_dd = re.compile(r'^\d{4}-\d{2}-\d{2}$')
url = 'https://raw.githubusercontent.com/datasets/currency-codes/' + \
      'master/data/codes-all.csv'
lookup = [
    ('code', 'AlphabeticCode'),
    ('name_en', 'Currency'),
    ('@withdrawal-date', 'WithdrawalDate'),
    ('@status', 'status'),
]
r = requests.get(url)
reader = csv.DictReader(r.iter_lines(decode_unicode=True))
currencies = []
for currency in reader:
    if currency['AlphabeticCode'] == '':
        continue
    currency['status'] = ''
    if currency['WithdrawalDate'] != '':
        currency['status'] = 'withdrawn'
    if yyyy_mm.match(currency['WithdrawalDate']):
        currency['WithdrawalDate'] += '-01'
    if not yyyy_mm_dd.match(currency['WithdrawalDate']):
        currency['WithdrawalDate'] = ''
    currencies.append(currency)
source_to_xml('Currency', None, lookup,
              source_data=currencies,
              order_by='code/text()')
