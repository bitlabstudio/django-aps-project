# flake8: noqa
from aps_project import settings
from django.core.management import setup_environ
setup_environ(settings)

from development_fabfile.fabfile import *
