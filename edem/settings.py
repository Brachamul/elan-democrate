# -*- coding: utf-8 -*-

"""
Django settings for the edem project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
	'django_admin_bootstrapped', # bootstrap that admin !
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'django_gravatar', # django-gravatar2
	'markdown_deux', # github.com/trentm/django-markdown-deux
	'auth_with_one_time_code', 
	'membres',
	'fichiers_adherents',
	'tableau_de_bord',
	'aggregateur',
	'datascope', # différents affichages de données pour les utilisateurs
	'mandats',
	'notifications',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# Deployment checklist stuff
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
X_FRAME_OPTIONS = 'DENY'

ROOT_URLCONF = 'edem.urls'

WSGI_APPLICATION = 'edem.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3',
		'NAME': os.path.join(BASE_DIR, 'edem_database.sqlite3'),
	}
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'fr-FR'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_L10N = True

FIRST_DAY_OF_WEEK = 1 # Lundi, et pas Dimanche comme pour les ricains

# USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join((BASE_DIR), "_static_root")
MEDIA_ROOT = os.path.join((BASE_DIR), "_media_root")
STATICFILES_DIRS = (
	os.path.join((BASE_DIR), "static", "static"),
)

# Template location

TEMPLATE_DIRS = (
	os.path.join((BASE_DIR), "static", "templates"),
)

from django.contrib import messages
from django.contrib.messages import constants as message_constants
MESSAGE_LEVEL = messages.DEBUG

MESSAGE_TAGS = { messages.ERROR: 'danger' }

LOGIN_URL = 'connexion'
LOGOUT_URL = 'deconnexion'
LOGIN_REDIRECT_URL = 'accueil'


LOGGING = {
	'version': 1,
	'disable_existing_loggers': True,
	'formatters': {
		'standard': {
			'format': '%(asctime)s %(levelname)s %(name)s %(message)s'
		},
	},
	'handlers': {
		'default': {
			'level':'DEBUG',
			'class':'logging.handlers.RotatingFileHandler',
			'filename': 'log_loggidy.log',
			'maxBytes': 1024*1024*5, # 5 MB
			'backupCount': 5,
			'formatter':'standard',
		},  
		'request_handler': {
				'level':'DEBUG',
				'class':'logging.handlers.RotatingFileHandler',
				'filename': 'log_django_request.log',
				'maxBytes': 1024*1024*5, # 5 MB
				'backupCount': 5,
				'formatter':'standard',
		},
	},
	'loggers': {

		'': {
			'handlers': ['default'],
			'level': 'DEBUG',
			'propagate': True
		},
		'django.request': { # Stop SQL debug from logging to main logger
			'handlers': ['request_handler'],
			'level': 'DEBUG',
			'propagate': False
		},
	}
}




### Paramètres personnalisés

POSTS_PER_PAGE = 12 # nombre de posts qui s'affichent en page d'accueil
PROFONDEUR_MAXIMALE_DES_COMMENTAIRES = 6 # niveau max de décente dans l'affichage des commentaires pour une même page
DUREE_D_ACTIVITE = 2 # Nombre d'années d'activité des adhérents après leur dernière cotisation (année actuelle - année de cotisation > x)

AUTHENTICATION_BACKENDS = ('auth_with_one_time_code.backend.OneTimeCodeBackend',) # Pas personnalisé, juste là pour info
AUTH_CODE_LENGTH = 6 # longueur du code d'authentification, par exemple '6' donne 'J2DH92'
AUTH_CODE_LIFESPAN = 1 # les codes d'authentification sont valides X heures
AUTH_CODE_MAXIMUM_ATTEMPS = 3 # au bout de 3 essais, le code expire

HELP_EMAIL_ADRESS = "[ Demandez à Antoine de créer une adresse d'aide, on en a pas encore ! ]"

# API EMBEDLY
EMBEDLY_KEY = "111e2b3ee0714950ad122d221fa7d444"


# FRONT-END IMPORTS, using context_processors.py
IMPORT_JQUERY = '<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>'
IMPORT_BOOTSTRAP_JS = '<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/js/bootstrap.min.js"></script>'
IMPORT_BOOTSTRAP_CSS = '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css">'



##########################
#  Settings localisables :
##########################

# import local_settings if exist
try: from local_settings import *
except ImportError: pass

## Custom, adresse du site utilisée pour envoyer les liens de connexion dans les mails, overridé par local settings
# SITE_URL = "http://localhost:8000"

## Standard, authentification pour l'envoi de mail
# ALLOWED_HOSTS = [SITE_URL,]

## Standard, authentification pour l'envoi de mail
# EMAIL_SUBJECT_PREFIX = "[Élan Démocrate] "
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_HOST_USER = "patate@gmail.com"
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_PASSWORD = 'azerty12345'

## Standard SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = ''

## Standard SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = False