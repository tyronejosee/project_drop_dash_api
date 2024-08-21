"""Settings for config project (Base)."""

import os
from pathlib import Path
from datetime import timedelta
import environ


BASE_DIR = Path(__file__).resolve().parent.parent.parent


env = environ.Env()
environ.Env.read_env(".env.dev")


SALES_TAX_RATE = 0.10
DRIVER_TAX_RATE = 0.02


BASE_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

PROJECT_APPS = [
    "apps.restaurants",
    "apps.drivers",
    "apps.finances",
    "apps.home",
    "apps.reviews",
    "apps.users",
    "apps.orders",
    "apps.payments",
    "apps.promotions",
    "apps.jobs",
    "apps.deliveries",
    "apps.blogs",
    "apps.locations",
    "apps.utilities",
]

THIRD_APPS = [
    "rest_framework",
    "djoser",
    "social_django",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
    "django_filters",
    "simple_history",
    "drf_spectacular",
]

INSTALLED_APPS = BASE_APPS + PROJECT_APPS + THIRD_APPS

MIDDLEWARE = [
    "social_django.middleware.SocialAuthExceptionMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "simple_history.middleware.HistoryRequestMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.Argon2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2PasswordHasher",
    "django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher",
    "django.contrib.auth.hashers.BCryptSHA256PasswordHasher",
]


# Keep this key hidden,it is exposed for sharing code to avoid developers having to generate it again
# ENCRYPT_KEY = env("ENCRYPT_KEY")
ENCRYPT_KEY = b"UxzFA2QzSu_1-mJkxiWvMgG3TuMT0us_Glz2Guv-4iw="


LANGUAGE_CODE = "en-us"
TIME_ZONE = "America/Santiago"
USE_I18N = True
USE_TZ = True


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticatedOrReadOnly"
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_CONTENT_LANGUAGE": "en",
    "DEFAULT_PAGINATION_CLASS": "apps.utilities.pagination.LimitSetPagination",
    "DEFAULT_FILTER_BACKENDS": [
        "rest_framework.filters.SearchFilter",
        "django_filters.rest_framework.DjangoFilterBackend",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "3/second",
        "user": "60/minute",
        "daily": "1000/day",
    },
    "NUM_PROXIES": None,
    "PAGE_SIZE": 25,
    "SEARCH_PARAM": "q",
    "ORDERING_PARAM": "order",
}


AUTH_USER_MODEL = "users.User"

CORS_ALLOW_HEADERS = [
    "Authorization",
    "Content-Type",
    "accept",
    "accept-encoding",
    "content-disposition",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "SET_USERNAME_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{uid}/{token}",
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_RETYPE": True,
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{uid}/{token}",
    "ACTIVATION_URL": "activate/{uid}/{token}",
    "SEND_ACTIVATION_EMAIL": True,
    "SOCIAL_AUTH_TOKEN_STRATEGY": "djoser.social.token.jwt.TokenStrategy",
    "SOCIAL_AUTH_ALLOWED_REDIRECT_URIS": [
        "http://localhost:8000/google",
        "http://localhost:8000/facebook",
    ],
    "SERIALIZERS": {
        "user_create": "apps.users.serializers.UserWriteSerializer",
        "user": "apps.users.serializers.UserWriteSerializer",
        "current_user": "apps.users.serializers.UserWriteSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
    },
}

SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("Bearer",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=10080),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=30),
    "ROTATE_REFRESFH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
}

AUTHENTICATION_BACKENDS = (
    "social_core.backends.google.GoogleOAuth2",
    "social_core.backends.facebook.FacebookOAuth2",
    "django.contrib.auth.backends.ModelBackend",
)

SPECTACULAR_SETTINGS = {
    "TITLE": "Drop Dash (API)",
    "DESCRIPTION": "A home delivery platform that allows users to search for and purchase products from local restaurants near their homes, place orders, and schedule deliveries. Provides access to restaurants to manage their menus, receive orders, and handle their meals through the platform. Inspired by platforms like Rappi and Uber Eats",
    "VERSION": "v1",
    "LICENSE": {
        "name": "Apache Licence 2.0",
        "url": "https://github.com/tyronejosee/project_drop_dash_api/blob/main/LICENSE",
    },
    "CONTACT": {"name": "Developer", "url": "https://github.com/tyronejosee"},
    # "SCHEMA_PATH_PREFIX": r"^/api/v\d+",
    # "SCHEMA_PATH_PREFIX_TRIM": True,
    "SERVE_INCLUDE_SCHEMA": False,
    "TAGS": [
        {
            "name": "company",
            "description": "All company data",
        },
        {
            "name": "pages",
            "description": "Operations related to pages",
        },
        {
            "name": "keywords",
            "description": "Operations related to keywords",
        },
        {
            "name": "restaurants",
            "description": "Operations related to restaurants",
        },
        {
            "name": "categories",
            "description": "Operations related to categories",
        },
        {
            "name": "foods",
            "description": "Operations related to foods",
        },
        {
            "name": "reviews",
            "description": "Operations related to reviews",
        },
        {
            "name": "orders",
            "description": "Operations related to orders",
        },
        {
            "name": "drivers",
            "description": "Operations related to drivers",
        },
        {
            "name": "promotions",
            "description": "Operations related to promotions",
        },
        {
            "name": "coupons",
            "description": "Operations related to coupons",
        },
        {
            "name": "countries",
            "description": "Operations related to countries",
        },
        {
            "name": "states",
            "description": "Operations related to states",
        },
        {
            "name": "cities",
            "description": "Operations related to cities",
        },
        {
            "name": "revenues",
            "description": "Operations related to revenues",
        },
        {
            "name": "posts",
            "description": "Operations related to posts",
        },
        {
            "name": "socials",
            "description": "Operations related to socials",
        },
        {
            "name": "tokens",
            "description": "Operations related to tokens",
        },
        {
            "name": "users",
            "description": "Operations related to users",
        },
        {
            "name": "accounts",
            "description": "Operations related to accounts",
        },
        {
            "name": "positions",
            "description": "Operations related to positions",
        },
        {
            "name": "applicants",
            "description": "Operations related to applicants",
        },
        {
            "name": "workers",
            "description": "Operations related to workers",
        },
    ],
}
