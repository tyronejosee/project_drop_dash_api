"""Settings for config project (Local)."""

from .base import *


CORS_ORIGIN_ALLOW_ALL = True

# INSTALLED_APPS.append("debug_toolbar")

# MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
