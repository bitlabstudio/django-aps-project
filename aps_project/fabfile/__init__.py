# flake8: noqa
import os

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "aps_project.settings")

from development_fabfile.fabfile import *
