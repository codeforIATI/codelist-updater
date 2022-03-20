from .helpers import Importer, fetch

def run():
    url = 'http://org-id.guide/download.json'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name/en'),
        ('description_en', 'description/en'),
        ('@public-database', 'access/availableOnline'),
        ('category', 'coverage'),
        ('url', 'url')
    ]

    r = fetch(url)
    data = r.json()
    registration_agencies = []
    for registration_agency in data['lists']:
        registration_agencies.append({
            'code': registration_agency['code'],
            'name/en': registration_agency['name']['en'].strip(),
            'description/en': registration_agency['description']['en'].strip(),
            'access/availableOnline': {False: '0', True: '1'}[bool(registration_agency['access'].get('availableOnline', False))],
            'coverage': ",".join(registration_agency['coverage']) if registration_agency['coverage'] is not None else '',
            'url': registration_agency['url']
        })
    Importer('OrganisationRegistrationAgency', None, lookup, source_data=registration_agencies)


if __name__ == '__main__':
    run()
