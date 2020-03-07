import csv
import re

import requests

from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/currency-codes/' + \
      'master/data/codes-all.csv'
lookup = {
    'code': 'AlphabeticCode',
    'name_en': 'Currency',
    'withdrawal-date': 'WithdrawalDate',
}
r = requests.get(url)
reader = csv.DictReader(r.iter_lines(decode_unicode=True))
currencies = []
for currency in reader:
    if re.match(r'^\d{4}-\d{2}$', currency['WithdrawalDate']):
        currency['WithdrawalDate'] += '-01'
    currencies.append(currency)
source_to_xml('Currency', None, lookup, source_data=currencies)
