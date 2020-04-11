from helpers import Importer


url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/finance_type_categories.csv'
lookup = [
    ('code', 'code'),
    ('name_en', 'name_en'),
    ('name_fr', 'name_fr'),
]
Importer('FinanceType-category', url, lookup)
