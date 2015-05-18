# -*- coding: utf-8 -*-
from .base import *

DEBUG = True
TEMPLATE_DEBUG = True



# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'taskbuster_db',
        'USER': 'damienhe',
        'PASSWORD': 'ducker12',
        'HOST': 'localhost',
        'PORT': '',
    }
}