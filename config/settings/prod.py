from .base import *

ALLOWED_HOSTS = ['15.164.187.80', 'emsys.site']
DEBUG = False

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static") #개발시 스태틱파일을 모아서 복사해줄 디렉토리

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR),"static", "media")

STATICFILES_DIRS = [
    os.path.join(os.path.dirname(BASE_DIR),"static", "static_dirs"),
    os.path.join(os.path.dirname(BASE_DIR),"static", "media"),
]