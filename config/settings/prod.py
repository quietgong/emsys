from .base import *

ALLOWED_HOSTS = ['3.34.213.119', 'emsys.site']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = []
DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'emsys',
        'USER': 'dbmasteruser',
        'PASSWORD': 'nx%K;b)2]Dx+otNC&ah,LBoB|82d1ghP',
        'HOST': 'ls-e7085ef971e2ab19fa06e7e909875e07e8c80e2e.cnibbhagbaiv.ap-northeast-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}