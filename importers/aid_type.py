from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/aid_types.csv'
lookup = {
    'code': 'code',
    'category': 'category',
    'name_en': 'name_en',
    'name_fr': 'name_fr',
    'description_en': 'description_en',
    'description_fr': 'description_fr',
}
source_to_xml('AidType', url, lookup)
