from .helpers import Importer, fetch


def run():
    url = 'https://unstats.un.org/SDGAPI/v1/sdg/Indicator/List'
    lookup = [
        ('code', 'code'),
        ('name_en', 'description'),
        ('category', 'target'),
    ]

    indicators = fetch(url).json()
    Importer('UNSDG-Indicators', None, lookup, source_data=indicators)


if __name__ == '__main__':
    run()
