import csv

from .helpers import Importer, fetch


def run():
    url = 'https://morph.io/andylolz/country-codes/' + \
          'data.csv?key=wFTSIH61nwMjLBhphd4T' + \
          '&query=select+%2A+from+%22data%22'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
    ]
    r = fetch(url)
    reader = csv.DictReader(r.iter_lines(decode_unicode=True))
    countries = [{
        'code': x['code'],
        'name_en': x['name_en'],
        'name_fr': x['name_fr'],
    } for x in reader]
    countries.append({
        'code': 'XK',
        'name_en': 'Kosovo',
        'name_fr': '',
    })
    countries = sorted(countries, key=lambda x: x['name_en'])
    Importer('Country', 'countries', lookup, source_data=countries)


if __name__ == '__main__':
    run()
