from .helpers import Importer


def run():
    url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
          'master/data/channel_codes.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
    ]
    Importer('CRSChannelCode', url, lookup)


if __name__ == '__main__':
    run()
