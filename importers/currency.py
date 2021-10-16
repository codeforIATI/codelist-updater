from .helpers import Importer


def run():
    url = 'https://codeforiati.org/currency-codes/currency_codes.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name'),
    ]
    Importer('Currency', url, lookup)


if __name__ == '__main__':
    run()
