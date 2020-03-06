from helpers import source_to_xml


url = 'https://raw.githubusercontent.com/datasets/language-codes/' + \
      'master/data/language-codes-full.csv'
language_lookup = {
    'code': 'alpha2',
    'name_en': 'English',
}
source_to_xml('Language', url, language_lookup)
