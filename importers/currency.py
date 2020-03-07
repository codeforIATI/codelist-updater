from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/currency-codes/' + \
      'master/data/codes-all.csv'
currency_lookup = {
    'code': 'AlphabeticCode',
    'name_en': 'Currency',
    'withdrawal-date': 'WithdrawalDate',
}
source_to_xml('Currency', url, currency_lookup)
