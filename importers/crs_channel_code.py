from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/channel_codes.csv'
lookup_no_desc = {
    'code': 'code',
    'name_en': 'name_en',
    'name_fr': 'name_fr',
}
source_to_xml('CRSChannelCode', url, lookup_no_desc)
