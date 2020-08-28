from django.urls import path
from notice_sw7up import views
app_name = 'notice_sw7up'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.detail, name='detail'),
]