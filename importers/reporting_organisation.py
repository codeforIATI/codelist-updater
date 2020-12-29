from .helpers import Importer


def run():
    url = 'https://iatiregistry.org/publisher/download_list/csv'
    lookup = [
        ('code', 'IATI Organisation Identifier'),
        ('name_en', 'Publisher'),
        ('codeforiati:organisation-type', 'Organization Type'),
        ('codeforiati:hq-country-or-region', 'HQ Country or Region'),
    ]
    Importer('ReportingOrganisation', url, lookup)


if __name__ == '__main__':
    run()
