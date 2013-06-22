#!/usr/bin/env python
# encoding=utf-8
# maintainer: Fadiga

import os

from distutils.core import setup
import py2exe

try:
    target = os.environ['PY2EXE_MODE']
except KeyError:
    target = 'multi'

if target == 'single':
    ZIPFILE = None
    BUNDLES = 1
else:
    ZIPFILE = 'shared.lib'
    BUNDLES = 1

setup(windows=[{'script': 'zmain.py', \
                'icon_resources': [(0, 'static\images\logo.ico')]}],
      options={'py2exe': {
                    'includes': ['sip', 'PySide.QtNetwork', 'email', 'werkzeug', 'jinja2'],
                    'packages': ['email', 'werkzeug', 'jinja2'],
                    'compressed': True,
                    'bundle_files': BUNDLES,
                    },
               },
      zipfile=ZIPFILE,
      Version="V.0.1",
)
