from django.urls import path
from notice_sw import views
app_name = 'notice_sw'

urlpatterns = [
    path('', views.list, name='list'),
    path('<int:post_id>/', views.detail, name='detail'),
]