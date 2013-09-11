# coding: utf-8

import os
# This is what manage.py and friends read.
from .project import *

# Easily allow local settings
try:
    if os.environ.get('USER', None) == 'yura':
        from .local import *
    else:
        pass
except ImportError:
    pass
