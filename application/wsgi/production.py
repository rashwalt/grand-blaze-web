# -*- mode: Python; -*-
import os
import sys

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if path not in sys.path:
   sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings_production'

#from devtool import monitor
#monitor.start()

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
