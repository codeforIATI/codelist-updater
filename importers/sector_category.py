from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/sector_categories.csv'
lookup_no_category = {
    'code': 'code',
    'name_en': 'name_en',
    'name_fr': 'name_fr',
    'description_en': 'description_en',
    'description_fr': 'description_fr',
}
source_to_xml('SectorCategory', url, lookup_no_category)
