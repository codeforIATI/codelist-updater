from os import listdir
from os.path import join, dirname

import importers


files = listdir(join(dirname(__file__), 'importers'))
all_importers = [f[:-3] for f in files
                 if f.endswith('.py')
                 and not f.startswith('_')]

for importer_name in importers.__all__:
    try:
        getattr(importers, importer_name).run()
    except ConnectionError:
        print('Error running the {} importer'.format(importer_name))
