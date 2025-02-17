"""
Django settings for core project.

Generated by "django-admin startproject" using Django 5.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path
from datetime import timedelta
from celery.schedules import crontab, schedule

# Build paths inside the project like this: BASE_DIR / "subdir".
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-llnxng%r-v&l=8@ob_8_%g@f-fgy+p%6e@=z^qyd=+sa8%s+^p"

# SECURITY WARNING: don"t run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['10.0.2.2', '172.16.1.15', 
                '127.0.0.1', 'localhost', '*']

AUTH_USER_MODEL = "account.User"
# Application definition
UNICODE_JSON = True

INSTALLED_APPS = [
    'channels',
    'django_celery_beat',
    "geopy",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    "rest_framework",    
    "corsheaders",
    "pandas",
    # "scikit-learn",
    "scipy",
    "seaborn",
    "numpy",

    "rest_framework_simplejwt",
    "django_extensions",
    "account.apps.AccountConfig",
    "deliverer.apps.DelivererConfig",
    "food.apps.FoodConfig",
    "notification.apps.NotificationConfig",
    "order.apps.OrderConfig",
    "restaurant.apps.RestaurantConfig",
    "review.apps.ReviewConfig",
    "social.apps.SocialConfig",
    "utils.apps.UtilsConfig", 
]

CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

ASGI_APPLICATION = "core.asgi.application"
# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             'hosts': [('127.0.0.1', 6379)]
#         }
#     }
# }

# settings.py

RECOMMENDER_MODEL_PATH = os.path.join(BASE_DIR, 'w_rc_sys', 'ml_models', 'dish_recommender.pkl')


CELERY_BROKER_URL = 'redis://localhost:6379/0'  
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = "Asia/Ho_Chi_Minh"  
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_BEAT_SCHEDULE = {
    'check-and-expire-requests-every-10-minutes': {
        'task': 'order.tasks.check_and_expire_requests',
        'schedule': crontab(minute='*/1'), 
    },
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',  
    },
}

REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_CLASSES": [
        # "account.throttles.OTPThrottle",
        "rest_framework.throttling.ScopedRateThrottle"
    ],

    "DEFAULT_THROTTLE_RATES": {
        "anon": "1/m",
        "otp": "1/45s",
    },
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    # 'DEFAULT_PAGINATION_CLASS': {
    #     'food_delivery_backend.utils.pagination.CustomPagination'
    # }
}

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=24),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1000),
}


WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "food_db",
        "USER": "root",
        "PASSWORD": "Duc.2003",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "Asia/Ho_Chi_Minh"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIR = [
    BASE_DIR / "static/"
]
MEDIA_URL = "images/"
MEDIA_ROOT = BASE_DIR / "static/images/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
