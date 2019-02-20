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

ALLOWED_HOSTS = ['www.strinj.com', 'localhost']


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
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases



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


# Static files (CSS, JavaScript, Image)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

# load variables from local if it's a local env
if 'BUCKETEER_AWS_ACCESS_KEY_ID' not in os.environ:
    try:
        from local_settings import *
    except ImportError:
        print 'import settings problem!'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
    }
}


# prod env
if 'BUCKETEER_AWS_ACCESS_KEY_ID' in os.environ:
    DATABASES['default']['NAME'] = os.environ['HEROKU_POSTGRESQL_NAME']
    DATABASES['default']['USER'] = os.environ['HEROKU_POSTGRESQL_USER']
    DATABASES['default']['PASSWORD'] = os.environ['HEROKU_POSTGRESQL_PW']
    DATABASES['default']['HOST'] = os.environ['HEROKU_POSTGRESQL_HOST']
    DATABASES['default']['PORT'] = os.environ['HEROKU_POSTGRESQL_PORT']
    AWS_ACCESS_KEY_ID = os.environ['BUCKETEER_AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['BUCKETEER_AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['BUCKETEER_BUCKET_NAME']
# local
else:
    DATABASES['default']['NAME'] = HEROKU_POSTGRESQL_NAME_LC
    DATABASES['default']['USER'] = HEROKU_POSTGRESQL_USER_LC
    DATABASES['default']['PASSWORD'] = HEROKU_POSTGRESQL_PW_LC
    DATABASES['default']['HOST'] = HEROKU_POSTGRESQL_HOST_LC
    DATABASES['default']['PORT'] = HEROKU_POSTGRESQL_PORT_LC
    AWS_ACCESS_KEY_ID = BUCKETEER_AWS_ACCESS_KEY_ID_LC
    AWS_SECRET_ACCESS_KEY = BUCKETEER_AWS_SECRET_ACCESS_KEY_LC
    AWS_STORAGE_BUCKET_NAME = BUCKETEER_BUCKET_NAME_LC

AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_LOCATION = 'media'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

########## to be deleted ##########################################
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'sixerr/static'),
# ]
# STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
########## to be deleted ##########################################







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

# replace database settings to use posgress on Heroku
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)

# setup upload directory for Gig model
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
#MEDIA_URL = 'https://bucketeer-935c55d6-c0d5-4764-ad10-72daed5b3527.s3.amazonaws.com/media/'

SECURE_SSL_REDIRECT=False



assert len(SECRET_KEY) > 20, 'Please set SECRET_KEY in local_settings.py'
