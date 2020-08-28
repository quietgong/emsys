from django.urls import path
from notice import views
app_name = 'notice'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
    path('download/<int:pk>', views.download, name="notice_download"),
]