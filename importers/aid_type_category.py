from helpers import Importer


url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/aid_type_categories.csv'
lookup = [
    ('code', 'code'),
    ('name_en', 'name_en'),
    ('name_fr', 'name_fr'),
    ('description_en', 'description_en'),
    ('description_fr', 'description_fr'),
]
Importer('AidType-category', url, lookup)
