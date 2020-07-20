import os as _os
import importlib as _importlib


files = _os.listdir(_os.path.dirname(__file__))
__all__ = [f[:-3] for f in files
           if f.endswith('.py')
           and not f.startswith('_')]
for mod in __all__:
    _importlib.import_module('{}.{}'.format(__name__, mod))


del files, mod, _os, _importlib
