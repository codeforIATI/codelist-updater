import csv

import requests

from helpers import source_to_xml


sector_url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
             'master/data/sectors.csv'
r = requests.get(sector_url)
reader = csv.DictReader(r.iter_lines(decode_unicode=True))
sector_prefixes = list(set([s['code'][:3] for s in reader]))

url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
      'master/data/sector_categories.csv'
lookup = {
    'code': 'code',
    'name_en': 'name_en',
    'name_fr': 'name_fr',
}
r = requests.get(url)
reader = csv.DictReader(r.iter_lines(decode_unicode=True))
categories = [cat for cat in reader
              if cat['code'] in sector_prefixes]
source_to_xml('SectorCategory', None, lookup, source_data=categories)
