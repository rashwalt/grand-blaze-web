# -*- coding: utf-8 -*-
# 開発用の設定
import os
from settings import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'grand_blaze_stage',
        'USER': 'webapp',
        'PASSWORD': '***',
        'HOST': '',
        'PORT': '',
        'OPTIONS': {
               "init_command": "SET storage_engine=INNODB",
        }  
    },
}

DEBUG = False

SITE_DOMAIN = 'dev.grand-blaze.com'

MEDIA_ROOT = '/var/www/html/grb2/application/static'
MEDIA_URL = 'http://'+ SITE_DOMAIN +'/static'
STATIC_ROOT = '/var/www/html/grb2/application/media'

STATICFILES_DIRS = (
    os.path.join(os.path.abspath(os.path.dirname(__file__) + '/..'), 'static'),
)

STATIC_DIRS = (
    os.path.join(os.path.abspath(os.path.dirname(__file__) + '/..'), 'static'),
)

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    },
}

PREPEND_WWW = False
