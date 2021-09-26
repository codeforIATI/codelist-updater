import csv

from .helpers import Importer, fetch


def run():
    sector_url = 'https://raw.githubusercontent.com/datasets/' + \
                 'dac-and-crs-code-lists/main/data/sectors.csv'
    r = fetch(sector_url)
    reader = csv.DictReader(r.iter_lines(decode_unicode=True))
    sector_prefixes = list(set([s['code'][:3] for s in reader]))

    url = 'https://raw.githubusercontent.com/datasets/' + \
          'dac-and-crs-code-lists/main/data/sector_categories.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
    ]
    r = fetch(url)
    reader = csv.DictReader(r.iter_lines(decode_unicode=True))
    categories = [cat for cat in reader
                  if cat['code'] in sector_prefixes]
    Importer('SectorCategory', None, lookup, source_data=categories)


if __name__ == '__main__':
    run()
