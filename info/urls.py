from django.urls import path
from info import views
from info.basic import start_views

app_name = 'info'

urlpatterns = [
    path('', start_views.index, name='index'),
    path('list', views.list, name='list'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('download/<int:pk>', views.download, name="info_download"),
    path('sitepolicy', views.sitepolicy, name="sitepolicy")
]