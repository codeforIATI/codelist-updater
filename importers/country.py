import csv

import requests

from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/country-codes/' + \
      'master/data/country-codes.csv'
country_lookup = {
    'code': 'code',
    'name_en': 'name_en',
    'name_fr': 'name_fr',
}
r = requests.get(url)
reader = csv.DictReader(r.iter_lines(decode_unicode=True))
countries = [{
    'code': x['code'],
    'name_en': x['name_en'],
    'name_fr': x['name_fr'],
} for x in reader]
countries = sorted(countries, key=lambda x: x['name_en'])
source_to_xml('Country', 'countries', country_lookup, source_data=countries)
