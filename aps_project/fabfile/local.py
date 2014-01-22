"""Fabric commands that are run locally."""
from fabric.api import local
from development_fabfile.fabfile.local import create_db
from development_fabfile.fabfile.local import drop_db


def dumpdata():
    """Dumps everything.

    Remember to add new dumpdata commands for new apps here so that you always
    get a full initial dump when running this task.

    """
    local('python2.7 ./manage.py dumpdata --indent 4 --natural auth --exclude auth.permission > aps_project/fixtures/bootstrap_auth.json')  # NOPEP8
    local('python2.7 ./manage.py dumpdata --indent 4 --natural sites > aps_project/fixtures/bootstrap_sites.json')  # NOQA
    local('python2.7 ./manage.py dumpdata --indent 4 --natural aps_bom > aps_project/fixtures/bootstrap_aps_bom.json')  # NOQA


def loaddata():
    local('python2.7 manage.py loaddata aps_project/fixtures/bootstrap_auth.json')  # NOPEP8
    local('python2.7 manage.py loaddata aps_project/fixtures/bootstrap_sites.json')  # NOPEP8
    local('python2.7 manage.py loaddata aps_project/fixtures/bootstrap_aps_bom.json')  # NOPEP8


def migrate():
    """
    In rare occasions, we might want to do migrations on its own.
    Since we defined a custom order for them, we'll add this command to be used
    instead of `./manage.py migrate` instead.

    """
    local('python2.7 manage.py migrate ')


def rebuild():
    """Deletes and re-creates the local database."""
    drop_db()
    create_db()
    local('python2.7 manage.py syncdb --noinput')
    migrate()
    loaddata()
