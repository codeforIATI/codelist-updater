from helpers import Importer


url = 'https://raw.githubusercontent.com/datasets/media-types/' + \
      'master/media-types.csv'
lookup = [
    ('code', 'Media Type'),
    ('category', 'Type'),
]
Importer('FileFormat', url, lookup)
