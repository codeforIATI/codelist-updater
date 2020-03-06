from helpers import source_to_xml


url = 'https://morph.io/codeforIATI/country-region-codes-scraper/' + \
      'data.csv?key=wFTSIH61nwMjLBhphd4T' + \
      '&query=select+%2A+from+%22swdata%22'
lookup = {
    'code': 'M49 Code',
    'name_en': 'Country or Area',
    'name_ar': 'Country or Area_AR',
    'name_es': 'Country or Area_ES',
    'name_fr': 'Country or Area_FR',
    'name_ru': 'Country or Area_RU',
    'name_zh': 'Country or Area_ZH',
}
source_to_xml('AreaCodeM49', url, lookup, repo='Unofficial-Codelists')
