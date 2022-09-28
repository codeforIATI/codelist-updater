from .helpers import Importer, fetch

# https://github.com/IATI/ckanext-iati/blob/d1a8776181c494eed0fd33c85f44878c88349613/ckanext/iati/lists.py#L27-L38
REGISTRY_ORGANISATION_TYPES = [
    ('80', 'Academic, Training and Research'),
    ('60', 'Foundation'),
    ('10', 'Government'),
    ('21', 'International NGO'),
    ('40', 'Multilateral'),
    ('22', 'National NGO'),
    ('15', 'Other Public Sector'),
    ('70', 'Private Sector'),
    ('30', 'Public Private Partnership'),
    ('23', 'Regional NGO'),
]
ORG_TYPES = dict([(i[1], i[0]) for i in REGISTRY_ORGANISATION_TYPES])


def run():
    url = 'https://iatiregistry.org/publisher/download/json'
    lookup = [
        ('@status', '@status'),
        ('code', 'IATI Organisation Identifier'),
        ('name_en', 'Publisher'),
        ('codeforiati:organisation-type-code', 'Organization Type Code'),
        ('codeforiati:organisation-type', 'Organization Type'),
        ('codeforiati:hq-country-or-region', 'HQ Country or Region'),
        ('codeforiati:registry-identifier', 'Registry Identifier'),
    ]
    data = fetch(url).json()
    publishers = []
    for publisher in data:
        publisher['@status'] = 'active'
        publisher['Organization Type Code'] = ORG_TYPES.get(publisher['Organization Type'])
        publisher['Registry Identifier'] = publisher['Datasets Link'].rsplit('/', 1)[-1]
        publishers.append(publisher)
    Importer('ReportingOrganisation', None, lookup, source_data=publishers)


if __name__ == '__main__':
    run()
