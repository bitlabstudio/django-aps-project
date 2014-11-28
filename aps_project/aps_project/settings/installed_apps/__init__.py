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
    'aps_bom',
    'aps_process',
    'aps_purchasing',
    'aps_production',
    'debug_toolbar',
    'django_extensions',
    'django_libs',
    'mailer',
    'rapid_prototyping',
    'south',
]

INTERNAL_APPS = [
    'aps_project',
]

INSTALLED_APPS = DJANGO_APPS + EXTERNAL_APPS + INTERNAL_APPS

from .aps_bom import *  # NOQA
from .auth import *  # NOQA
from .rapid_prototyping import *  # NOQA
from .debug_toolbar import *  # NOQA
