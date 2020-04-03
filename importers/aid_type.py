from collections import OrderedDict

from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/aid_types.csv'
lookup = OrderedDict([
    ('code', 'code'),
    ('name_en', 'name_en'),
    ('name_fr', 'name_fr'),
    ('description_en', 'description_en'),
    ('description_fr', 'description_fr'),
    ('category', 'category'),
])
source_to_xml('AidType', url, lookup)
