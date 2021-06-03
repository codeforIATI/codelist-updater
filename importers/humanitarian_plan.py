from .helpers import Importer


def run():
    url = 'https://codeforiati.org/humanitarian-plan-codelist/humanitarian-plan.csv'
    lookup = [
        ('code', 'Plan code'),
        ('name_en', 'Plan name'),
        ('codeforiati:plan-type', 'Plan type'),
        ('codeforiati:plan-year', 'Plan year'),
        ('codeforiati:plan-start-date', 'Start date'),
        ('codeforiati:plan-end-date', 'End date'),
    ]
    Importer('HumanitarianPlan', url, lookup)


if __name__ == '__main__':
    run()
