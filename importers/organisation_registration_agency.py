from time import sleep

from .helpers import Importer, fetch


def run():
    def refresh_data():
        # Ensure we’re fetch the latest data, by hitting the
        # _update_lists endpoint a few times.
        #
        # For more details, see:
        # https://github.com/OpenDataServices/org-ids/issues/256
        refresh_url = 'https://org-id.guide/_update_lists'
        for x in range(6):
            fetch(refresh_url)
            sleep(0.5)

    refresh_data()

    url = 'http://org-id.guide/download.json'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name/en'),
        ('description_en', 'description/en'),
        ('@public-database', 'access/availableOnline'),
        ('@status', '@status'),
        ('category', 'coverage'),
        ('url', 'url')
    ]

    r = fetch(url)
    data = r.json()
    registration_agencies = []
    for registration_agency in data['lists']:
        registration_agencies.append({
            '@status': 'withdrawn' if registration_agency.get('deprecated') is True else 'active',
            'code': registration_agency['code'],
            'name/en': registration_agency['name']['en'],
            'description/en': registration_agency['description']['en'],
            'access/availableOnline': {False: '0', True: '1'}[bool(registration_agency['access'].get('availableOnline', False))],
            'coverage': ";".join(registration_agency['coverage']) if registration_agency['coverage'] is not None else '',
            'url': registration_agency['url']
        })
    Importer('OrganisationRegistrationAgency', None, lookup, source_data=registration_agencies, order_by='code/text()', sort_attrs=True)


if __name__ == '__main__':
    run()
