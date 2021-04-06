from .helpers import Importer


def run():
    url = 'https://docs.google.com/spreadsheets/d/1o1SQDqfFTBgUJO2k83mfFlLtgpwUUkEbc3gjRgIWJSo/export?format=csv&id=1o1SQDqfFTBgUJO2k83mfFlLtgpwUUkEbc3gjRgIWJSo&gid=1574305742'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
        ('url', 'url'),
        ('@status', 'status'),
    ]
    Importer('HumanitarianGlobalClusters', url, lookup)


if __name__ == '__main__':
    run()
