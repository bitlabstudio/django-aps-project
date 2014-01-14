"""Installed apps for the aps_project project."""
DJANGO_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

EXTERNAL_APPS = [
    'debug_toolbar',
    'django_libs',
    'mailer',
    'south',
    'rapid_prototyping',
]

INTERNAL_APPS = [
    'aps_project',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS

from .rapid_prototyping import *  # NOQA
from .debug_toolbar import *  # NOQA
