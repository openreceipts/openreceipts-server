from __future__ import absolute_import
import os
import dj_database_url

DATABASE_URL = ''
from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
    }
}

DATABASES['default'] =  dj_database_url.config()
