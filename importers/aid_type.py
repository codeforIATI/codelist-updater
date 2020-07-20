from .helpers import Importer


def run():
    url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
          'master/data/aid_types.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
        ('description_en', 'description_en'),
        ('description_fr', 'description_fr'),
        ('category', 'category'),
    ]
    Importer('AidType', url, lookup)


if __name__ == '__main__':
    run()
