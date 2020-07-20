import csv

from .helpers import Importer, fetch


def run():
    url = 'https://raw.githubusercontent.com/datasets/dac-crs-codes/' + \
          'master/data/collaboration_types.csv'
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('name_fr', 'name_fr'),
        ('description_en', 'description_en'),
        ('description_fr', 'description_fr'),
    ]

    r = fetch(url)
    reader = csv.DictReader(r.iter_lines(decode_unicode=True))
    collaboration_types = []

    # hack to split name into name and description.
    # This is just a workaround for an issue with the source data.
    for collaboration_type in reader:
        collaboration_type['description_fr'] = None
        for lang in ['en', 'fr']:
            collaboration_type['description_' + lang] = None
            name_and_desc = collaboration_type['name_' + lang].split('. ', 1)
            if len(name_and_desc) > 1:
                collaboration_type['name_' + lang] = name_and_desc[0] + '.'
                collaboration_type['description_' + lang] = name_and_desc[1]
        collaboration_types.append(collaboration_type)
    Importer('CollaborationType', None, lookup, source_data=collaboration_types)


if __name__ == '__main__':
    run()
