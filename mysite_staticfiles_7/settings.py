import os
from pathlib import Path
from django.utils.translation import gettext_lazy as _
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-w4klo4p2tbuy_f@&q3569s8j(4xq6tivs(%6=zm&a&am7^23=t'

# =============================================================
# 🧠 OTOMATISASI INFRASTRUKTUR: LAPTOP (LOKAL) VS RAILWAY (CLOUD)
# =============================================================
IS_RAILWAY = 'RAILWAY_ENVIRONMENT' in os.environ

if IS_RAILWAY:
    DEBUG = True
    ALLOWED_HOSTS = ['*']
    CSRF_TRUSTED_ORIGINS = ['https://pelatihlumba.up.railway.app', 'https://*.railway.app']

    # 🎯 Database Cloud (Supabase PostgreSQL via Railway)
    DATABASES = {
        'default': dj_database_url.config(
            default=os.environ.get('DATABASE_URL'),
            conn_max_age=600
        )
    }

    # 🎯 Storage Cloud (Kirim file fisik ke Bucket Supabase secara permanen)
    STORAGES = {
        "default": {
            "BACKEND": "django_storage_supabase.storage.SupabaseStorage",
            "OPTIONS": {
                "supabase_url": "https://optadautrggmdmqgwkfy.supabase.co",
                "supabase_key": os.environ.get("SUPABASE_KEY"), # Membaca variabel di Railway
                "bucket_name": "blog-image", # FIX: Sesuai nama bucket di foto lu (tanpa 's')
            },
        },
        "staticfiles": {
            "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
        },
    }
else:
    DEBUG = True
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    
    # 🎯 BALIKIN KE REKREASI LOKAL: Hubungkan kembali ke MySQL lu biar data gak ilang!
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'db_dolphines',
            'USER': 'root',
            'PASSWORD': 'blacksider2026',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    
    # Storage Lokal: Simpan di folder media laptop biasa
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
        },
    }
# =============================================================

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_storage_supabase',
    'ckeditor',
    'blog',
    'about',
    'contact',
    'accounts',
    'project',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', # Tetap aman di sini
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
        'DIRS': [ BASE_DIR / 'templates'],
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

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },
    { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' },
]

# Internationalization
USE_I18N = True
LANGUAGE_CODE = 'id'
LANGUAGE = [
    ('id', _('Indonesian')),
    ('en', _('English')),
]
LOCALE_PATHS = [
    BASE_DIR / 'locale',
]

TIME_ZONE = 'UTC'
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

LOGIN_REDIRECT_URL = '/'