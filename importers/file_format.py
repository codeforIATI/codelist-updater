from .helpers import Importer


def run():
    url = 'https://raw.githubusercontent.com/datasets/media-types/' + \
          'master/media-types.csv'
    lookup = [
        ('code', 'Media Type'),
        ('category', 'Type'),
    ]
    Importer('FileFormat', url, lookup)


if __name__ == '__main__':
    run()
