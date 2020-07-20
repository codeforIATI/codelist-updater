import csv
import re

from .helpers import Importer, fetch


def run():
    url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
          'master/data/sectors.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
        ('description_en', 'description_en'),
        ('description_fr', 'description_fr'),
        ('category', 'category'),
    ]
    r = fetch(url)
    reader = csv.DictReader(r.iter_lines(decode_unicode=True))
    sectors = []
    for sector in reader:
        if sector['voluntary_code'] != '':
            sector['code'] = sector['voluntary_code']
        for txt in ['name_en', 'name_fr', 'description_en', 'description_fr']:
            sector[txt] = re.sub(r'  +', ' ', sector[txt])
        sectors.append(sector)
    sectors = sorted(sectors, key=lambda x: x['code'])
    Importer('Sector', None, lookup, source_data=sectors)


if __name__ == '__main__':
    run()
