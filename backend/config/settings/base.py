# -*- coding: utf-8 -*-
""" Base Django settings"""

import environ

ROOT_DIR = environ.Path(__file__) - 3
APPS_DIR = ROOT_DIR.path("api")
ENVIRONMENT = environ.Env()

READ_DOT_ENV_FILE = ENVIRONMENT.bool("DJANGO_READ_DOT_ENV_FILE", default=False)
if READ_DOT_ENV_FILE:
    DOT_ENV_FILE = str(ROOT_DIR.path(".env"))
    ENVIRONMENT.read_env(DOT_ENV_FILE)

DEBUG = ENVIRONMENT.bool("DJANGO_DEBUG", False)

ALLOWED_HOSTS = []


# APP CONFIGURATION
# ------------------------------------------------------------------------------

DJANGO_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
)
THIRD_PARTY_APPS = ("django_filters", "import_export")

LOCAL_APPS = ()

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE CONFIGURATION
# ------------------------------------------------------------------------------

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

# TEMPLATES CONFIGURATION
# ------------------------------------------------------------------------------

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": (APPS_DIR.path("templates"),),
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "config.wsgi.application"


# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
DATABASES = {"default": ENVIRONMENT.db("DATABASE_URL")}
DATABASES["default"]["ATOMIC_REQUESTS"] = True

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Europe/Berlin"

DATETIME_FORMAT = "D d. M Y H:i"

USE_I18N = True

USE_L10N = False

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = (str(ROOT_DIR.path("static")),)

# Django import / export CONFIGURATION
# ------------------------------------------------------------------------------
# https://django-import-export.readthedocs.io/en/stable/installation.html#settings
IMPORT_EXPORT_USE_TRANSACTIONS = True
