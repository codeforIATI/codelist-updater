from .helpers import Importer


def run():
    url = 'https://raw.githubusercontent.com/datasets/' + \
          'dac-and-crs-code-lists/main/data/flow_types.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
        ('description_en', 'description_en'),
        ('description_fr', 'description_fr'),
    ]
    Importer('FlowType', url, lookup)


if __name__ == '__main__':
    run()
