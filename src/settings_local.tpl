# -*- coding: utf8 -*-

import os

from django.conf.global_settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

PROJECT_PATH = os.path.realpath(os.path.dir(__file__))


DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_PATH, 'flisoltweets.db'),
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

MIDDLEWARE_CLASSES += ()

INSTALLED_APPS += ()
