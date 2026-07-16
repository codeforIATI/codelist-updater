import csv

from .helpers import Importer, fetch

NO_COUNTRY_ASSIGNED = '(No country assigned)'


def _split_code_name(value):
    """Split a "<code> - <name>" string as used in the dashboard CSV,
    e.g. "40 - Multilateral" or "GB - United Kingdom...". Either side
    may be the literal string "None" or empty when unset."""
    code, _, name = value.partition(' - ')
    return (code if code and code != 'None' else None,
            name if name and name != 'None' else None)


def run():
    url = 'https://dashboard.iatistandard.org/generated/data/csv/publishers.csv'
    lookup = [
        ('@status', '@status'),
        ('code', 'IATI Organisation Identifier'),
        ('name_en', 'Publisher'),
        ('codeforiati:organisation-type-code', 'Organization Type Code'),
        ('codeforiati:organisation-type', 'Organization Type'),
        ('codeforiati:hq-country-or-region', 'HQ Country or Region'),
        ('codeforiati:registry-identifier', 'Registry Identifier'),
    ]

    r = fetch(url)
    reader = csv.DictReader(r.iter_lines(decode_unicode=True))
    publishers = []
    for row in reader:
        org_type_code, org_type_name = _split_code_name(row['Organisation Type'])
        _, hq_country_name = _split_code_name(row['HQ Country'])

        publishers.append({
            '@status': 'active',
            'IATI Organisation Identifier': row['Reporting Org Identifier Registered'],
            'Publisher': row['Publisher Name'],
            'Organization Type Code': org_type_code,
            'Organization Type': org_type_name,
            'HQ Country or Region': hq_country_name or NO_COUNTRY_ASSIGNED,
            'Registry Identifier': row['Publisher Short Name'],
        })

    Importer('ReportingOrganisation', None, lookup, source_data=publishers)


if __name__ == '__main__':
    run()
