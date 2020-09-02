from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.static import serve
from info.basic import start_views
from django.contrib.auth import views as auth_views

urlpatterns = [
                  path('academic/', include('academic.urls')),
                  path('accounts/', include('accounts.urls')),
                  path('info/', include('info.urls')),
                  path('notice/', include('notice.urls')),
                  path('notice_sw/', include('notice_sw.urls')),
                  path('notice_sw7up/', include('notice_sw7up.urls')),
                  path('activity/', include('activity.urls')),
                  path('contest/', include('contest.urls')),
                  path('admin/', admin.site.urls),
                  path('', start_views.index, name='index'),
                  path('intro', start_views.intro, name='intro'),

                  url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
                  url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),

                  # 비밀번호 찾기
                  path('accounts/reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/reset_password.html"),
                       name="reset_password"),
                  path('accounts/reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="accounts/reset_password_done.html"),
                       name="password_reset_done"),
                  path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="accounts/reset_password_confirm.html"),
                       name="password_reset_confirm"),
                  path('accounts/reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/reset_password_complete.html"),
                       name="password_reset_complete"),
              ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
handler404 = 'accounts.views.page_not_found'