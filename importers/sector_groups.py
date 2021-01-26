from .helpers import Importer


def run():
    url = 'https://codeforiati.org/dac-sector-groups/sectors_groups.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
        ('codeforiati:category-code', 'category_code'),
        ('codeforiati:category-name_en', 'category_name_en'),
        ('codeforiati:category-name_fr', 'category_name_fr'),
        ('codeforiati:sector-code', 'sector_code'),
        ('codeforiati:sector-name_en', 'sector_name_en'),
        ('codeforiati:sector-name_fr', 'sector_name_fr'),
    ]
    Importer('SectorGroup', url, lookup)


if __name__ == '__main__':
    run()
