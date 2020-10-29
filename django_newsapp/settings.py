"""
Django settings for django_newsapp project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PWA_SERVICE_WORKER_PATH = os.path.join(BASE_DIR, 'newsapp/static/newsapp', 'serviceworker.js')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(qm*9%)ui9lk&s#bcyvrwr5j)c!=!s*3bb!)8k!83pzcl(bjzu'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '10.0.2.2']


# Application definition

INSTALLED_APPS = [
    'newsapp.apps.NewsappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pwa',
    'webpush',
    'crispy_forms',
    'crispy_forms_materialize',
    'materializecssform'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_newsapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # For Web push
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

WSGI_APPLICATION = 'django_newsapp.wsgi.application'

#Webpush Settings - https://github.com/safwanrahman/django-webpush
#To create Vapid Public & Private Key, refer - https://github.com/web-push-libs/vapid/tree/main/python
WEBPUSH_SETTINGS = {
    "VAPID_PUBLIC_KEY": "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEJaUfQKrcKpsqUvdXJuyTJCkTRxGkfwKFE0i+qubXt74MTm7pRahURD7gmEBE7C7s9bV+LndM/Cb1vf0U/cFXHA==",
    "VAPID_PRIVATE_KEY":"MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgQAgwkuAoForlH1dimB1PzViova2rpzhFkxfkQnlayp6hRANCAAQlpR9AqtwqmypS91cm7JMkKRNHEaR/AoUTSL6q5te3vgxObulFqFREPuCYQETsLuz1tX4ud0z8JvW9/RT9wVcc",
    "VAPID_ADMIN_EMAIL": "akash.shrivastava136@gmail.com"
}

{
    "BACKEND": "django_jinja.backend.Jinja2",
    "OPTIONS": {
      'extensions': ['webpush.jinja2.WebPushExtension'],
    }
},


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,  'static')
]

# Default layout to use with "crispy_forms"
CRISPY_TEMPLATE_PACK = 'materialize_css_forms'
MATERIALIZECSS_ICON_SET = 'fontawesome'

LOGIN_REDIRECT_URL = 'news-home'
