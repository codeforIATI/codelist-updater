from .helpers import Importer


def run():
    url = 'https://docs.google.com/spreadsheets/d/1SxSircxhXMZCe0PWafCht-whjBdI9UqoeFeSUbiLGc4/export?format=csv&id=1SxSircxhXMZCe0PWafCht-whjBdI9UqoeFeSUbiLGc4&gid=0'
    lookup = [
        ('code', 'HRinfo ID'),
        ('name_en', 'Preferred Term'),
        ('name_fr', 'Preferred Term (fr)'),
        ('url', 'Homepage'),
    ]
    Importer('HumanitarianGlobalClusters', url, lookup)


if __name__ == '__main__':
    run()
