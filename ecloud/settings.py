"""
Django settings for ecloud project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(ht^gk^k!j!%m#p5jch$_$d=hs140a!3x6*6*^f&kvp^shm92('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cinder',
    'nova',
    'neutron',
    'compute',
    'dashboard',
    'identity',
    'meters',
    'network',
    'storage',
    'settings',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'common.middleware.CommonMiddleware',
]

ROOT_URLCONF = 'ecloud.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'ecloud.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'ecloud',
        'USER': 'root',
        'PASSWORD': 'kevin123',
    },
    'cinder': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'cinder',
        'USER': 'root',
        'PASSWORD': 'kevin123',
    },
    'nova': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'nova',
        'USER': 'root',
        'PASSWORD': 'kevin123',
    },
    'neutron': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'keystone',
        'USER': 'root',
        'PASSWORD': 'kevin123',
    }
}

DATABASE_ROUTERS = ['common.routers.DefaultDatabaseRouter']


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    ('css', os.path.join(STATIC_ROOT, 'css')),
    ('js', os.path.join(STATIC_ROOT, 'js')),
    ('images', os.path.join(STATIC_ROOT, 'images')),
    ('plugins', os.path.join(STATIC_ROOT, 'plugins')),
]

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')    #.replace('\\', '/')

MEDIA_URL = '/media/'

# Self-defined authentication

LOGIN_REDIRECT_URL = '/dashboard/'

LOGOUT_REDIRECT_URL = '/identity/user/login/'

LOGIN_URL = '/identity/user/login/'

AUTH_USER_MODEL = 'identity.User'

AUTHENTICATION_BACKENDS = (
    'common.backends.UserAuthBackend',
)
ANONYMOUS_USER_ID = -1


# Logging configurations

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'standard': {
            'format': ('%(asctime)s [%(pathname)s:%(lineno)d] '
                       '[%(levelname)s]- %(message)s')
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        }
    },

    'handlers': {
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'filters': ['require_debug_true'],
        },
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': r'D:\django_log\default.log',
            'maxBytes': 1024**3*10,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'error': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': r'D:\django_log\error.log',
            'maxBytes': 1024**3*10,
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scripts': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': r'D:\django_log\scripts.log',
            'maxBytes': 1024**3*10,
            'backupCount': 5,
            'formatter': 'standard',
        }
    },

    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'INFO'),
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'default': {
            'handlers': ['default', 'error'],
            'level': 'DEBUG',
            'propagate': False
        },
        'scripts': {
            'handlers': ['scripts'],
            'level': 'INFO',
            'propagate': True
        },
    }
}


# OpenStack
OPENSTACK = {
    'keystone': {
        'host': '10.10.132.161',
        'port': 5000,
        'user': 'admin',
        'pass': '06a29a1b7d84cb7b713a',
        'token_timeout': 12 * 60 * 60,  # keystone token timeout, seconds
        'project_id': 'c5bb6219baf84706aba37bf9f37ea911',   # should active
    },
}


# Celery settings

CELERY_BROKER_URL = 'amqp://myuser:mypassword@10.10.129.72:5672/myvhost'

CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_BACKEND = 'redis://10.10.129.72:6379/3'
CELERY_TASK_SERIALIZER = 'json'

CELERY_TIMEZONE = 'Asia/Shanghai'
