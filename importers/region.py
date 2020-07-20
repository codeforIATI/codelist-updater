import csv

from .helpers import Importer, fetch


def run():
    url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
          'master/data/recipients.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
    ]
    r = fetch(url)
    reader = csv.DictReader(r.iter_lines(decode_unicode=True))
    regions = [x for x in reader
               if x['income_group'] == 'Part I unallocated by income']
    Importer('Region', None, lookup, source_data=regions)


if __name__ == '__main__':
    run()
