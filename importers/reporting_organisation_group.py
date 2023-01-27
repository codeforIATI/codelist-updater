from .helpers import Importer


def run():
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vSZ9wDOHbA5xDD0FSdVOiTP9ZZIzPaTdjiuGCtHYcQGM_TX80ESB5-SZFmomiNSHAS1Knfu2Jab1gIW/pub?gid=0&single=true&output=csv'
    lookup = [
        ('code', 'Code'),
        ('name_en', 'Name_EN'),
        ('codeforiati:group-code', 'Group Code'),
        ('codeforiati:group-name_en', 'Group Name_EN'),
        ('codeforiati:group-name_fr', 'Group Name_FR'),
        ('codeforiati:group-name_es', 'Group Name_ES'),
        ('codeforiati:group-name_pt', 'Group Name_PT'),
    ]
    Importer('ReportingOrganisationGroup', url, lookup)


if __name__ == '__main__':
    run()
