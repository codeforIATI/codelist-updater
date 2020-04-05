from helpers import source_to_xml


url = 'https://morph.io/codeforIATI/country-region-codes-scraper/' + \
      'data.csv?key=wFTSIH61nwMjLBhphd4T' + \
      '&query=select+%2A+from+%22swdata%22'
lookup = [
    ('code', 'M49 Code'),
    ('name_en', 'Country or Area'),
    ('name_ar', 'Country or Area_AR'),
    ('name_es', 'Country or Area_ES'),
    ('name_fr', 'Country or Area_FR'),
    ('name_ru', 'Country or Area_RU'),
    ('name_zh', 'Country or Area_ZH'),
    ('iso-alpha-2-code', 'ISO-alpha2 Code'),
    ('iso-alpha-3-code', 'ISO-alpha3 Code'),
    ('global-code', 'Global Code'),
    ('global-name_en', 'Global Name'),
    ('global-name_ar', 'Global Name_AR'),
    ('global-name_es', 'Global Name_ES'),
    ('global-name_fr', 'Global Name_FR'),
    ('global-name_ru', 'Global Name_RU'),
    ('global-name_zh', 'Global Name_ZH'),
    ('region-code', 'Region Code'),
    ('region-name_en', 'Region Name'),
    ('region-name_ar', 'Region Name_AR'),
    ('region-name_es', 'Region Name_ES'),
    ('region-name_fr', 'Region Name_FR'),
    ('region-name_ru', 'Region Name_RU'),
    ('region-name_zh', 'Region Name_ZH'),
    ('sub-region-code', 'Sub-region Code'),
    ('sub-region-name_en', 'Sub-region Name'),
    ('sub-region-name_ar', 'Sub-region Name_AR'),
    ('sub-region-name_es', 'Sub-region Name_ES'),
    ('sub-region-name_fr', 'Sub-region Name_FR'),
    ('sub-region-name_ru', 'Sub-region Name_RU'),
    ('sub-region-name_zh', 'Sub-region Name_ZH'),
    ('intermediate-region-code', 'Intermediate Region Code'),
    ('intermediate-region-name_en', 'Intermediate Region Name'),
    ('intermediate-region-name_ar', 'Intermediate Region Name_AR'),
    ('intermediate-region-name_es', 'Intermediate Region Name_ES'),
    ('intermediate-region-name_fr', 'Intermediate Region Name_FR'),
    ('intermediate-region-name_ru', 'Intermediate Region Name_RU'),
    ('intermediate-region-name_zh', 'Intermediate Region Name_ZH'),
]
source_to_xml('AreaCodeM49', url, lookup, repo='Unofficial-Codelists')
