"""Settings for config project (Local)."""

import os
import sys

from .base import *  # noqa: F403
from .base import BASE_DIR, env  # noqa: F401


CORS_ORIGIN_ALLOW_ALL = True

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

if "test" in sys.argv:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": env("POSTGRES_DB", default="dropdash_db"),
            "USER": env("POSTGRES_USER", default="dropdash_user"),
            "PASSWORD": env("POSTGRES_PASSWORD", default="dropdash_password"),
            "HOST": "db",
            "PORT": "5432",
        }
    }
