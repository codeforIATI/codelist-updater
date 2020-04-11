import csv

import requests

from helpers import Importer


url = 'https://morph.io/codeforIATI/humanitarian-emergency-codelists/' + \
      'data.csv?key=wFTSIH61nwMjLBhphd4T' + \
      '&query=select+%2A+from+%22GLIDE_numbers%22'
lookup = [
    ('code', 'GLIDE_number'),
    ('codeforiati:event-code', 'Event_Code'),
    ('codeforiati:event_en', 'Event'),
    ('codeforiati:country-code', 'Country_Code'),
    ('codeforiati:country_en', 'Country'),
    ('codeforiati:date', 'Date'),
    ('codeforiati:glide-serial', 'Glide_Serial')
]

r = requests.get(url)
reader = csv.DictReader(r.iter_lines(decode_unicode=True))
codes = list(reader)
codes.insert(0, {
    'GLIDE_number': 'EP-2020-000012-001',
    'Event_Code': 'EP',
    'Event': 'Epidemic',
    'Country_Code': '---',
    'Country': '(Non-Localized)',
    'Date': '2020-01-06',
    'Glide_Serial': '2020-000012',
})

Importer('GLIDENumber', 'codes', lookup, repo='Unofficial-Codelists', source_data=codes)
