# -*- coding: UTF-8 -*-
from base import *

DEBUG = False

ALLOWED_HOSTS = '*'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'checkingpets',
	'USER': 'charlie',
	'PASSWORD': 'CharlieCag0n',
    }
}

STATIC_ROOT = '/var/apps/checkingpets/static/'

STATIC_URL = '/static/'

MEDIA_ROOT = '/var/apps/checkingpets/media/'

MEDIA_URL = ''
