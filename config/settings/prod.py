from .base import *

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ALLOWED_HOSTS = ['15.164.187.80', 'emsys.site']
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
DEBUG = False

STATIC_URL = '/static/'

MEDIA_ROOT = (BASE_DIR)
MEDIA_URL = '/media/'