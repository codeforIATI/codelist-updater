from helpers import Importer


url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/flow_types.csv'
lookup = [
    ('code', 'code'),
    ('name_en', 'name_en'),
    ('name_fr', 'name_fr'),
    ('description_en', 'description_en'),
    ('description_fr', 'description_fr'),
]
Importer('FlowType', url, lookup)
