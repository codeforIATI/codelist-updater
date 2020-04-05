from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/media-types/' + \
      'master/media-types.csv'
lookup = [
    ('code', 'Media Type'),
    ('category', 'Type'),
]
source_to_xml('FileFormat', url, lookup)
