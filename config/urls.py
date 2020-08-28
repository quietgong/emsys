from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve
from info.basic import start_views

urlpatterns = [
                  path('academic/', include('academic.urls')),
                  path('common/', include('common.urls')),
                  path('info/', include('info.urls')),
                  path('notice/', include('notice.urls')),
                  path('notice_sw/', include('notice_sw.urls')),
                  path('notice_sw7up/', include('notice_sw7up.urls')),
                  path('activity/', include('activity.urls')),
                  path('contest/', include('contest.urls')),
                  path('mypage/', include('mypage.urls')),
                  path('admin/', admin.site.urls),
                  path('', start_views.index, name='index'),
                  path('intro', start_views.intro, name='intro'),

                  url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
                  url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
              ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
handler404 = 'common.views.page_not_found'