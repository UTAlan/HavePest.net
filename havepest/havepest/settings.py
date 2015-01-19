import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_NAME = 'HavePest.net'

DEBUG = False
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = ['.havepest.net']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'havepest',
    'home',
    'photos',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.contrib.auth.context_processors.auth',
)

TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
ROOT_URLCONF = 'havepest.urls'
WSGI_APPLICATION = 'havepest.wsgi.application'
TIME_ZONE = 'America/Chicago'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = '/home/hpwt/havepest.net/public/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

try:
	from local_settings import *
except ImportError:
	pass
