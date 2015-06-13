# -*- coding: UTF-8 -*-
from base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'chekingpets.sqlite3'),
    }
}