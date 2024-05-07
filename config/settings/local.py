"""Settings for config project (Local)."""

import os
import sys
from .base import *


DEBUG = True

SECRET_KEY = env("SECRET_KEY")


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }


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
            "NAME": "dropdash_db",
            "USER": "dropdash_user",
            "PASSWORD": "dropdash_password",
            "HOST": "db",
            "PORT": "5432",
        }
    }


CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://dropdash_redis:6379",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    },
}


EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
