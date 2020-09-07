from django.urls import path
from inquiry import views

app_name = 'inquiry'

urlpatterns = [
    path('', views.index, name='post_create'),
]