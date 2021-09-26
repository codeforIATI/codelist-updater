from .helpers import Importer


def run():
    url = 'https://raw.githubusercontent.com/datasets/' + \
          'dac-and-crs-code-lists/main/data/finance_type_categories.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
    ]
    Importer('FinanceType-category', url, lookup)


if __name__ == '__main__':
    run()
