import csv

from .helpers import Importer, fetch


def run():
    url = 'https://codeforiati.org/country-codes/country_codes.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
        ('@status', 'status'),
    ]
    r = fetch(url)
    reader = csv.DictReader(r.iter_lines(decode_unicode=True))
    countries = [{
        'code': x['code'],
        'name_en': x['name_en'],
        'name_fr': x['name_fr'],
        'status': 'active' if x.get('active') == 'True' else 'withdrawn',
    } for x in reader]
    countries.append({
        'code': 'XK',
        'name_en': 'Kosovo',
        'name_fr': '',
        'status': 'active'
    })
    countries = sorted(countries, key=lambda x: x['name_en'])
    Importer('Country', 'countries', lookup, source_data=countries)


if __name__ == '__main__':
    run()
