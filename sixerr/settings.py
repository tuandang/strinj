"""
Django settings for sixerr project.

Generated by 'django-admin startproject' using Django 1.9.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'erxyb&&yjj9)y*4ju25rg%xsz@ob!j*-^-i-tp_+=hk@szrys@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['www.strinj.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sixerrapp',
    'social_django',
    'storages'
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'sixerr.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'sixerr.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databasess

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.postgresql_psycopg2',

        # local env
        # 'NAME': 'taskbuster_db',
        # 'USER': 'admin',
        # 'PASSWORD': '20110807',
        # 'HOST': '',
        # 'PORT': '',

        # stage env
        #'NAME': 'd3uhf593uqe6h1',
        #'USER': 'obftwydmyouolm',
        #'PASSWORD': 'fecdfeafd0599e18275bb8f3e78f957b975287acf81430f110e49ed2c8d6f383',
        #'HOST': 'ec2-107-20-183-142.compute-1.amazonaws.com',

        # prod env
        'NAME': 'dfpnshb2d1pqps',
        'USER': 'rkgvbcryobnodg',
        'PASSWORD': '1bd423510021bf6a588233f41af95070e3908ef81587afdbbc43904a2726562f',
        'HOST': 'ec2-107-20-167-11.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

#STATIC_URL = '/static/'

AWS_ACCESS_KEY_ID = 'AKIAI5LF3MSVQEWM7GQA'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'cloud-cube'
# AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
# AWS_S3_OBJECT_PARAMETERS = {
#     'CacheControl': 'max-age=86400',
# }
# AWS_LOCATION = 'static'
#
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'mysite/static'),
# ]
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# to serve static files on Heroku
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend'
)

#LOGIN_REDIRECT_URL = 'https://cryptic-brook-75782.herokuapp.com/social/complete/facebook/'

LOGIN_REDIRECT_URL = '/'

SOCIAL_AUTH_FACEBOOK_KEY = '269842407020498'
SOCIAL_AUTH_FACEBOOK_SECRET = '7f7de15749491e53643250916e93bf01'

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'sixerrapp.social_auth_pipeline.save_avatar',  # <--- set the path to the function
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

# replace database settings to use posgress on Heroky
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# setup upload directory for Gig model
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'https://cloud-cube.s3.amazonaws.com/ov6lbnrabqfyov6lbnrabqfy/public/media/'

#SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
SECURE_SSL_REDIRECT=False
