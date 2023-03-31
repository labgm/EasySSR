from .base import *

DEBUG = False

ADMINS = (
    ('Victor', 'victor.benedito12@hotmail.com'),
)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
