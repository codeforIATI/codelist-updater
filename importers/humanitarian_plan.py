from .helpers import Importer


def run():
    url = 'https://codeforiati.org/humanitarian-plan-codelist/humanitarian-plan.csv'
    lookup = [
        ('code', 'Plan code'),
        ('name_en', 'Plan Name'),
    ]
    Importer('HumanitarianPlan', url, lookup)


if __name__ == '__main__':
    run()
