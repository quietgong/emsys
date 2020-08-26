from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve

from emsys.views import base_views

urlpatterns = [
    path('emsys/', include('emsys.urls')),
    path('common/', include('common.urls')),
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'), # '/' 에 해당하는 path
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += [
    re_path(r'^%s(?P.*)$' % re.escape(settings.STATIC_URL.lstrip('/')), serve,
            kwargs={'document_root': settings.STATIC_ROOT})
]

handler404 = 'common.views.page_not_found'