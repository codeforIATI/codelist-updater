from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/language-codes/' + \
      'master/data/language-codes-full.csv'
lookup = [
    ('code', 'alpha2'),
    ('name_en', 'English'),
    ('name_fr', 'French'),
]
source_to_xml('Language', url, lookup, order_by='code/text()')
