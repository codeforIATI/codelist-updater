import csv

from .helpers import Importer, fetch

def run():
    url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vTXYj1IPNYkdwf21XQSRTixGwAQRTJENERUSGRvYa_RILTIKjGQ6vlmr_nUNukXIRkjAY8TbJP6VK4g/pub?gid=711009742&single=true&output=csv'

    r = fetch(url)
    fieldnames = [
        '',
        'codeforiati:group-code',
        'codeforiati:group-name_en',
        'codeforiati:category-code',
        'codeforiati:category-name_en',
        'code',
        'name_en',
        'codeforiati:cofog-class',
        'codeforiati:cofog-group',
        'codeforiati:cofog-division',
        'description_en'
        ]
    reader = csv.DictReader(r.iter_lines(decode_unicode=True), fieldnames=fieldnames)
    sectors_cofog = [row for i, row in enumerate(reader) if i > 2]
    lookup = [
        ('code', 'code'),
        ('name_en', 'name_en'),
        ('description_en', 'description_en'),
        ('codeforiati:category-code', 'codeforiati:category-code'),
        ('codeforiati:category-name_en', 'codeforiati:category-name_en'),
        ('codeforiati:group-code', 'codeforiati:group-code'),
        ('codeforiati:group-name_en', 'codeforiati:group-name_en'),
        ('codeforiati:cofog-class', 'codeforiati:cofog-class'),
        ('codeforiati:cofog-group', 'codeforiati:cofog-group'),
        ('codeforiati:cofog-division', 'codeforiati:cofog-division')
    ]
    Importer('SectorCOFOG', None, lookup, source_data=sectors_cofog, order_by='code/text()', sort_attrs=True)


if __name__ == '__main__':
    run()
