from collections import OrderedDict

from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/aid_type_categories.csv'
lookup = OrderedDict([
    ('code', 'code'),
    ('name_en', 'name_en'),
    ('name_fr', 'name_fr'),
    ('description_en', 'description_en'),
    ('description_fr', 'description_fr'),
])
source_to_xml('AidType-category', url, lookup)
