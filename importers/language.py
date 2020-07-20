from .helpers import Importer


def run():
    url = 'https://raw.githubusercontent.com/datasets/language-codes/' + \
          'master/data/language-codes-full.csv'
    lookup = [
        ('code', 'alpha2'),
        ('name_en', 'English'),
        ('name_fr', 'French'),
    ]
    Importer('Language', url, lookup, order_by='code/text()')


if __name__ == '__main__':
    run()
