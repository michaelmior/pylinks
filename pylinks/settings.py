# Django settings for pylinks project.
import os
import dj_database_url

PYLINKS_HOME = os.environ.get('PYLINKS_HOME', None)
DEBUG = True if os.environ.get('DJANGO_DEBUG', None) == '1' else False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = os.environ.get('HOSTNAMES', '').split(',')
SITE_DOMAIN = ALLOWED_HOSTS[0]
SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True

db_config = dj_database_url.config()
db_config['ATOMIC_REQUESTS'] = True
DATABASES = {'default': db_config}

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': os.environ.get('BONSAI_URL') or
               os.environ.get('SEARCHBOX_URL') or
               'http://localhost:9200/',
        'INDEX_NAME': 'documents',
    },
}
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

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
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'pylinks.main.context_processors.site',

    'django.core.context_processors.static',
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

if not os.environ.get('ROLLBAR_DISABLED', False):
    MIDDLEWARE_CLASSES.append('rollbar.contrib.django.middleware.RollbarNotifierMiddleware')

ROOT_URLCONF = 'pylinks.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'pylinks.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = [
    'pylinks.main',
    'pylinks.links',
    'pylinks.feeds',
    'pylinks.search',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'haystack',
    'grappelli',
    'django.contrib.admin',
    'gunicorn',
    'storages',
    's3_folder_storage',
    'analytics',
]

if not os.environ.get('UPLOADCARE_DISABLED', False):
    INSTALLED_APPS.append('pyuploadcare.dj')

GRAPPELLI_ADMIN_TITLE = 'Link database'

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

if os.environ.get('AWS_ACCESS_KEY_ID'):
    DEFAULT_FILE_STORAGE = 's3_folder_storage.s3.DefaultStorage'
    DEFAULT_S3_PATH = 'media'
    STATICFILES_STORAGE = 's3_folder_storage.s3.StaticStorage'
    STATIC_S3_PATH = 'static'
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['AWS_STORAGE_BUCKET_NAME']
    AWS_S3_SECURE_URLS = False
    AWS_QUERYSTRING_AUTH = False

    # Avoid using subdomains
    from boto.s3.connection import OrdinaryCallingFormat
    AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()

    MEDIA_ROOT = '/%s/' % DEFAULT_S3_PATH
    MEDIA_URL = '//s3.amazonaws.com/%s/%s/' % \
            (AWS_STORAGE_BUCKET_NAME, DEFAULT_S3_PATH)
    STATIC_ROOT = "/%s/" % STATIC_S3_PATH
    STATIC_URL = '//s3.amazonaws.com/%s/%s/' % \
            (AWS_STORAGE_BUCKET_NAME, STATIC_S3_PATH)
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
else:
    STATIC_ROOT = 'static'
    STATIC_URL = '/static/'
    MEDIA_ROOT = 'media'
    MEDIA_URL = '/media/'

ROLLBAR = {
    'access_token': os.environ['ROLLBAR_ACCESS_TOKEN'],
    'environment': 'development' if DEBUG else 'production',
    'branch': 'master',
    'root': os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
} if not os.environ.get('ROLLBAR_DISABLED', False) else {}

UPLOADCARE = {
    'pub_key': os.environ['UPLOADCARE_PUB_KEY'],
    'secret': os.environ['UPLOADCARE_SECRET']
} if not os.environ.get('UPLOADCARE_DISABLED', False) else {}
