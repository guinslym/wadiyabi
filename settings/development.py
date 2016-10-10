import os

from .base import *
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'p-h93iwrvc0+3e%m9)8(b(ml1clqwih^u=7p%p+o$ln$^458kn'

DEBUG=True
TEMPLATE_DEBUG_MODE = True

DEV_APPS = (
    'debug_toolbar',
)
INSTALLED_APPS = BASE_APPS + DEV_APPS + THIRD_PARTY_APPS + LOCAL_APPS


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.cache.CacheMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    #'whitenoise.middleware.WhiteNoiseMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# LOGGING
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(name)s %(process)d %(thread)d %(message)s'
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'clear': {
            'format': '%(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'error_log': {
            'level': 'ERROR',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR+'/logs/dev.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 10,
            'formatter': 'standard'
        },
        'debug_log': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': BASE_DIR+'/logs/dev.log',
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 10,
            'formatter': 'standard'
        }
    },
    'loggers': {
        'debugmess': {
            'handlers': ['debug_log'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['error_log'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.requests': {
            'handlers': ['error_log'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django': {
            'handlers': ['error_log'],
            'level': 'ERROR',
            'propagate': False,
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'

# Always use IPython for shell_plus
SHELL_PLUS = "ipython"

# Need to add DebugToolbarMiddleware
SHELL_PLUS_PRE_IMPORTS = (
    #('module.submodule1', ('class1', 'function2')),
    #('module.submodule2', 'function3'),
    ('applications.delivrem', '*'),
    ('applications.delivrem.models', '*')
)

# print SQL queries in shell_plus
SHELL_PLUS_PRINT_SQL = False
