from .base import *

PROD_DIR = os.path.dirname(os.path.dirname(__file__))

ALLOWED_HOSTS = ['15.164.187.80', 'emsys.site']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = []
DEBUG = False

STATIC_URL = '/static/'

MEDIA_ROOT = (PROD_DIR)
MEDIA_URL = '/media/'