from .helpers import Importer


def run():
    url = 'https://raw.githubusercontent.com/datasets/' + \
          'dac-and-crs-code-lists/main/data/aid_type_categories.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
        ('description_en', 'description_en'),
        ('description_fr', 'description_fr'),
    ]
    Importer('AidType-category', url, lookup)


if __name__ == '__main__':
    run()
