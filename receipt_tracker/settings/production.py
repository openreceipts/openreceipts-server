from __future__ import absolute_import
import os
import dj_database_url

#DATABASE_URL = ''
from .base import *

SECRET_KEY = os.environ['SECRET_KEY']
DATABASE_URL = os.environ['DATABASE_URL']
GOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}

DATABASES['default'] =  dj_database_url.config()

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static_files"),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


CRISPY_TEMPLATE_PACK = 'bootstrap3'
