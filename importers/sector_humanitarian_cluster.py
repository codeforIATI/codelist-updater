import csv

from .helpers import Importer, fetch


def run():
    url = 'https://gist.githubusercontent.com/markbrough/57106a152dbb26a6f4544a77c6768a64/raw/dac5-clusters-mapping.csv'
    lookup = [
        ('code', 'code'),
        ('name', 'name'),
        ('category', 'cluster_code'),
        ('codeforiati:cluster', 'cluster_name'),
    ]

    Importer('SectorCategoryHumanitarianGlobalCluster', url, lookup)


if __name__ == '__main__':
    run()
