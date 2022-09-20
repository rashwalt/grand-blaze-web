# -*- coding: utf-8 -*-
# 開発用の設定
import os
from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grand_blaze',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': '',
    },
}

DEBUG = True

SITE_DOMAIN = os.environ.get('', '127.0.0.1:8620')

MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'static')
MEDIA_URL = 'http://'+ SITE_DOMAIN +'/static'

STATICFILES_DIRS = (
    MEDIA_ROOT,
)

INTERNAL_IPS = ('127.0.0.1',)

INSTALLED_APPS += (
    'debug_toolbar',
)

DEBUG_TOOLBAR_PANELS = ( 
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = { 
    'INTERCEPT_REDIRECTS': False,
    #'SHOW_TOOLBAR_CALLBACK': custom_show_toolbar,
    'HIDE_DJANGO_SQL': False,
    'ENABLE_STACKTRACES': True,
}

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'TIMEOUT' : 3600,
    },
}

## ロギング
#import logging
#logging.basicConfig(level=logging.DEBUG,
#                    format='%(asctime)s %(levelname)-8s %(message)s',
#                    datefmt='%a, %d %b %Y %H:%M:%S',
#                    filename='/tmp/gokudo.log',
#                    filemode='a')

# テスト時はsouthのマイグレーションを実行しない
#SOUTH_TESTS_MIGRATE = False

PREPEND_WWW = False

