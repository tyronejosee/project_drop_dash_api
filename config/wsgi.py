"""WSGI config for config project."""

import os
from .environment import SETTINGS_MODULE

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)

application = get_wsgi_application()
