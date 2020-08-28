from django.urls import path
from notice_sw import views
app_name = 'notice_sw'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
]