"""Settings for config project (Production)."""

import os
import environ

from .base import *


DEBUG = False


env = environ.Env()
environ.Env.read_env("config/.env")


ALLOWED_HOSTS = [
    "example.com",
    "www.example.com"
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

# DEFAULT_FROM_EMAIL = "FandomHub - API <alt.tyronejose@gmail.com>"
# EMAIL_HOST = env("EMAIL_HOST")
# EMAIL_HOST_USER = env("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")
# EMAIL_PORT = env("EMAIL_PORT")
# EMAIL_USE_TLS = env("EMAIL_USE_TLS")

STATIC_URL = "static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

SECURE_SSL_REDIRECT = True
SECURE_HSTS_SECONDS = 31536000  # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_BROWSER_XSS_FILTER = True

CORS_ALLOWED_ORIGINS = [
    "https://example.com",
    "https://subdomain.example.com",
]

# CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True

CORS_ALLOW_HEADERS = [
    "Authorization",
    "Content-Type",
]
