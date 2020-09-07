from django.urls import path
from info import views
from info.basic import start_views

app_name = 'info'

urlpatterns = [
    path('', start_views.index, name='index'),
    path('intro', views.intro, name='intro'),
    path('list', views.list, name='list'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('download/<int:pk>', views.download, name="info_download"),
    path('sitepolicy', views.sitepolicy, name="sitepolicy"),

    path('post/create/', views.post_create, name='post_create'),
    path('post/modify/<int:post_id>/', views.post_modify, name='post_modify'),
    path('post/delete/<int:post_id>/', views.post_delete, name='post_delete'),
]