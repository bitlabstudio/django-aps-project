"""Settigns for the auth app."""
from django.core.urlresolvers import reverse_lazy


LOGIN_REDIRECT_URL = reverse_lazy('aps_project_home')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')
