from .helpers import Importer


def run():
    url = 'https://codeforiati.org/country-region-codes-scraper/country_region_codes.csv'
    lookup = [
        ('code', 'M49 Code'),
        ('name_en', 'Country or Area'),
        ('name_ar', 'Country or Area_AR'),
        ('name_es', 'Country or Area_ES'),
        ('name_fr', 'Country or Area_FR'),
        ('name_ru', 'Country or Area_RU'),
        ('name_zh', 'Country or Area_ZH'),
        ('codeforiati:iso-alpha-2-code', 'ISO-alpha2 Code'),
        ('codeforiati:iso-alpha-3-code', 'ISO-alpha3 Code'),
        ('codeforiati:global-code', 'Global Code'),
        ('codeforiati:global-name_en', 'Global Name'),
        ('codeforiati:global-name_ar', 'Global Name_AR'),
        ('codeforiati:global-name_es', 'Global Name_ES'),
        ('codeforiati:global-name_fr', 'Global Name_FR'),
        ('codeforiati:global-name_ru', 'Global Name_RU'),
        ('codeforiati:global-name_zh', 'Global Name_ZH'),
        ('codeforiati:region-code', 'Region Code'),
        ('codeforiati:region-name_en', 'Region Name'),
        ('codeforiati:region-name_ar', 'Region Name_AR'),
        ('codeforiati:region-name_es', 'Region Name_ES'),
        ('codeforiati:region-name_fr', 'Region Name_FR'),
        ('codeforiati:region-name_ru', 'Region Name_RU'),
        ('codeforiati:region-name_zh', 'Region Name_ZH'),
        ('codeforiati:sub-region-code', 'Sub-region Code'),
        ('codeforiati:sub-region-name_en', 'Sub-region Name'),
        ('codeforiati:sub-region-name_ar', 'Sub-region Name_AR'),
        ('codeforiati:sub-region-name_es', 'Sub-region Name_ES'),
        ('codeforiati:sub-region-name_fr', 'Sub-region Name_FR'),
        ('codeforiati:sub-region-name_ru', 'Sub-region Name_RU'),
        ('codeforiati:sub-region-name_zh', 'Sub-region Name_ZH'),
        ('codeforiati:intermediate-region-code', 'Intermediate Region Code'),
        ('codeforiati:intermediate-region-name_en', 'Intermediate Region Name'),
        ('codeforiati:intermediate-region-name_ar', 'Intermediate Region Name_AR'),
        ('codeforiati:intermediate-region-name_es', 'Intermediate Region Name_ES'),
        ('codeforiati:intermediate-region-name_fr', 'Intermediate Region Name_FR'),
        ('codeforiati:intermediate-region-name_ru', 'Intermediate Region Name_RU'),
        ('codeforiati:intermediate-region-name_zh', 'Intermediate Region Name_ZH'),
    ]
    Importer('RegionM49', url, lookup)


if __name__ == '__main__':
    run()
