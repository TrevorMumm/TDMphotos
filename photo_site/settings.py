import os
from pathlib import Path
import dj_database_url
import boto3
from botocore.client import Config
import logging
logging.basicConfig(level=logging.DEBUG)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '1426d0cce42daef045a372232931d4a8f0fedf109ca07283'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'tdm-photography.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'gallery',  # Add the gallery app here
    'storages',
]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "static")
# ]

# IBM Cloud Object Storage settings
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_ACCESS_KEY_ID = '438d6622d4884310a88160cac5ae0ae8'
AWS_SECRET_ACCESS_KEY = '1426d0cce42daef045a372232931d4a8f0fedf109ca07283'
AWS_STORAGE_BUCKET_NAME = 'photographysite'
AWS_S3_ENDPOINT_URL = 'https://s3.us-south.cloud-object-storage.appdomain.cloud'
AWS_S3_REGION_NAME = 'us-south'  # Region name for the Dallas region
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.us-south.cloud-object-storage.appdomain.cloud'

BACKGROUND_IMAGE_URL = 'https://s3.us-south.cloud-object-storage.appdomain.cloud/photographysite/media/welcome_backgrounds/Northern_Lights_Eau_Claire_WI-4.jpg'
BACKGROUND_IMAGE_2_URL = 'https://s3.us-south.cloud-object-storage.appdomain.cloud/photographysite/media/welcome_backgrounds/Black_Crowned_NightHeron_w__Fish_FINAL.png'
BACKGROUND_IMAGE_3_URL = 'https://s3.us-south.cloud-object-storage.appdomain.cloud/photographysite/media/welcome_backgrounds/GOAT_UltraSharpMacroBubble-8_FINAL.jpg'
BACKGROUND_IMAGE_4_URL = 'https://s3.us-south.cloud-object-storage.appdomain.cloud/photographysite/media/welcome_backgrounds/Tan_Bison_Irvine_Park_FINAL.png'


# Configure boto3 client separately
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    endpoint_url=AWS_S3_ENDPOINT_URL,
    config=Config(s3={'addressing_style': 'virtual'}),
    region_name=AWS_S3_REGION_NAME
)
boto3.resource('s3').meta.client = s3_client

# Ensure boto3 uses this client
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Media files settings
MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static files settings
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')



MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = 'photo_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'photo_site.context_processor.custom_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'photo_site.wsgi.application'
ASGI_APPLICATION = 'photo_site.asgi.application'

DATABASES = {
    'default': dj_database_url.config(default='sqlite:///db.sqlite3')
}

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

# DATABASES = {
#     'default': {
#         'default' : dj_database_url.config(
#             default='postgresql://mumm:fit.ant.god-09@localhost:5432/mydb',
#             conn_max_age=600
#         ),
#     'ENGINE': 'django.db.backends.postgresql',
#     'NAME': 'mydb',
#     'USER': 'mumm',
#     'PASSWORD': 'fit.ant.god-09',
#     'HOST': 'localhost',
#     'PORT': '5432',
#     }
    
# }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import django_heroku
django_heroku.settings(locals())
# settings.py