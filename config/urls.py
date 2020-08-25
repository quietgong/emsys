from django.contrib import admin
from django.urls import include, path

from emsys.views import base_views

urlpatterns = [
    path('emsys/', include('emsys.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'), # '/' 에 해당하는 path
]
handler404 = 'common.views.page_not_found'