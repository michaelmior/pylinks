# Django settings for pylinks project.
import os

import dj_database_url

PYLINKS_HOME = os.environ.get("PYLINKS_HOME", None)
DEBUG = True if os.environ.get("DJANGO_DEBUG", None) == "1" else False

ALLOWED_HOSTS = os.environ.get("HOSTNAMES", "").split(",")
SITE_DOMAIN = ALLOWED_HOSTS[0]
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

db_config = dj_database_url.config()
db_config["ATOMIC_REQUESTS"] = True
DATABASES = {"default": db_config}

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"

HAYSTACK_CONNECTIONS = {
    "default": {
        "ENGINE": "haystack.backends.whoosh_backend.WhooshEngine",
        "PATH": os.path.abspath(os.path.join(os.path.dirname(__file__), "index")),
        "INCLUDE_SPELLING": True,
    },
}
HAYSTACK_SIGNAL_PROCESSOR = "haystack.signals.RealtimeSignalProcessor"

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = "en-us"

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = "UTC"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "en-us"

SITE_ID = 1
APPEND_SLASH = True

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
    #    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ["DJANGO_SECRET_KEY"]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": (
                "pylinks.main.context_processors.site",
                "django.template.context_processors.static",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
            ),
        },
    },
]


MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

if not os.environ.get("ROLLBAR_DISABLED", False):
    MIDDLEWARE.append("rollbar.contrib.django.middleware.RollbarNotifierMiddleware")

ROOT_URLCONF = "pylinks.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "pylinks.wsgi.application"

INSTALLED_APPS = [
    "pylinks.main",
    "pylinks.links",
    "pylinks.feeds",
    "pylinks.search",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    "haystack",
    "grappelli",
    "django.contrib.admin",
    "gunicorn",
]

if os.environ.get("UPLOADCARE_SECRET"):
    INSTALLED_APPS.append("pyuploadcare.dj")

GRAPPELLI_ADMIN_TITLE = "Link database"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {"require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}},
    "handlers": {
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        }
    },
    "loggers": {
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    },
}

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
STATIC_ROOT = "static"
STATIC_URL = "/static/"
MEDIA_ROOT = "media"
MEDIA_URL = "/media/"

ROLLBAR = {}
if os.environ.get("ROLLBAR_ACCESS_TOKEN"):
    ROLLBAR = {
        "access_token": os.environ["ROLLBAR_ACCESS_TOKEN"],
        "environment": "development" if DEBUG else "production",
        "branch": "master",
        "root": os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)),
    }

# Note that uploads will not work if these are not set, but we need to be
# able to run without specified values so we can build the app image
UPLOADCARE = {
    "pub_key": os.environ.get("UPLOADCARE_PUB_KEY"),
    "secret": os.environ.get("UPLOADCARE_SECRET"),
}

GA_PROPERTY_ID = os.environ.get("GA_PROPERTY_ID", None)
