"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 5.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# For dev mode
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-2b!5wgj*q-20j2$3e1t=m$)ebr3p9)_*qaw+wth+y!f1^@90@n'

# SECURITY WARNING: don't run with debug turned on in production!

# DEBUG = os.environ.get('DEBUG') == '1' # This isnt working... It breaks the static files
DEBUG = False
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myblog',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "core/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


DB_DATABASE= os.environ.get("POSTGRES_DB")
DB_USER= os.environ.get("POSTGRES_USER")
DB_PASSWORD= os.environ.get("POSTGRES_PASSWORD")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")

DB_IS_AVAIL = all([
    DB_DATABASE
    , DB_USER
    , DB_PASSWORD
    , DB_HOST
    , DB_PORT
])

POSTGRES_READY = str(os.environ.get('POSTGRES_READY')) == '1'


if DB_IS_AVAIL and POSTGRES_READY:
    DATABASES = {
        'default': {
            "ENGINE" : 'django.db.backends.postgresql'
            , "NAME" : DB_DATABASE 
            , "USER" : DB_USER
            , "PASSWORD" : DB_PASSWORD
            , "HOST" : DB_HOST
            , "PORT" : DB_PORT
        }
    }


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# STATICFILES_DIRS = [

#     os.path.join(BASE_DIR, "core/static/"),
# ]
# print(['SDASDasdaSDAD'])
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "core/static")
]


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STORAGES = {
    "staticfiles": {
        "BACKEND": 'whitenoise.storage.CompressedStaticFilesStorage',
    },
}
print([STATIC_ROOT])

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
