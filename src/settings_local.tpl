# -*- coding: utf8 -*-

import os

from settings import *

PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

MANAGERS = ADMINS

DATABASES = {
    'default': {
        # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3'
        # or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'flisoltweets.db'),
    }
}

# MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)

#INSTALLED_APPS += (
#'debug_toolbar',
#'django_nose',
#)

# Django Debug Toolbar Configurations
#INTERNAL_IPS = ('127.0.0.1',)

#DEBUG_TOOLBAR_CONFIG = {
#    'INTERCEPT_REDIRECTS': False,
#}

# Django Nome
#TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# NOSE_ARGS = ['--with-notify']
