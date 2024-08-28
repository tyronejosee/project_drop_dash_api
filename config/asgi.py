"""ASGI config for config project."""

import os
from config.environment import SETTINGS_MODULE

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", SETTINGS_MODULE)

application = get_asgi_application()
