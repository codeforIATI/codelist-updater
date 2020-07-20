import csv
import re

from .helpers import Importer, fetch


def run():
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
    r = fetch(url)
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
    Importer('Currency', None, lookup,
             source_data=currencies,
             order_by='code/text()')


if __name__ == '__main__':
    run()
