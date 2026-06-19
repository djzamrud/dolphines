import os
from pathlib import Path
from django.conf import settings
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w4klo4p2tbuy_f@&q3569s8j(4xq6tivs(%6=zm&a&am7^23=t'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True

# ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'blacksider.pythonanywhere.com']


# ==========================================
# 🧠 SELEKSI OTOMATIS: LAPTOP VS PRODUCTION SERVER
# ==========================================
# Kita cek apakah file ini berjalan di server PythonAnywhere (punya folder 'blacksider')
if 'blacksider' in str(BASE_DIR):
    DEBUG = False
    ALLOWED_HOSTS = ['blacksider.pythonanywhere.com']
    
    # Di server PythonAnywhere gratisan, kita pakai SQLite absolut yang kemarin sukses
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/home/blacksider/dolphines/db.sqlite3',
        }
    }
else:
    # Ini settingan khusus saat kamu ngoding di VS Code LAPTOP kamu
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    
    # Di laptop, Django kamu bebas pakai MySQL lokal kamu
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_dolphines',
            'USER' : 'root',
            'PASSWORD' : 'blacksider2026',
            'HOST' : 'localhost',
            'PORT' : '3306',
        }
    }
# ==========================================

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'blog',
    'about',
    'contact',
    'accounts',
    'project',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mysite_staticfiles_7.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [ BASE_DIR/ 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'mysite_staticfiles_7.context_processors.global_nav',
                'mysite_staticfiles_7.context_processors.bg_global',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite_staticfiles_7.wsgi.application'


# Database
# https://docs.djangoproject.com/en/6.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'db_dolphines',
#         'USER' : 'root',
#         'PASSWORD' : 'blacksider2026',
#         'HOST' : 'localhost',
#         'PORT' : '3306',
        
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/6.0/ref/settings/#auth-password-validators

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

# fitur penerjemah:
USE_I18N = True
LANGUAGE_CODE = 'id'
LANGUAGE = [

    ('id', _('Indonesian')),
    ('en', _('English')),

]
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

# Internationalization
# https://docs.djangoproject.com/en/6.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/6.0/howto/static-files/

STATIC_URL = 'static/'
import os
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(settings.BASE_DIR, 'media')

LOGIN_REDIRECT_URL = '/'
