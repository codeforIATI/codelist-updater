import csv

from .helpers import Importer, fetch


def run():
    url = 'https://codeforiati.org/humanitarian-emergency-codelists/glide-emergencies.csv'
    lookup = [
        ('code', 'GLIDE_number'),
        ('url', 'URL'),
        ('codeforiati:event-code', 'Event_Code'),
        ('codeforiati:event_en', 'Event'),
        ('codeforiati:country-code', 'Country_Code'),
        ('codeforiati:country_en', 'Country'),
        ('codeforiati:date', 'Date'),
        ('codeforiati:glide-serial', 'Glide_Serial'),
    ]

    r = fetch(url)
    reader = csv.DictReader(r.iter_lines(decode_unicode=True))
    codes = list(reader)
    codes.insert(0, {
        'GLIDE_number': 'EP-2020-000012-001',
        'URL': '',
        'Event_Code': 'EP',
        'Event': 'Epidemic',
        'Country_Code': '---',
        'Country': '(Non-Localized)',
        'Date': '2020-01-06',
        'Glide_Serial': '2020-000012',
    })

    Importer('GLIDENumber', 'codes', lookup, source_data=codes)


if __name__ == '__main__':
    run()
