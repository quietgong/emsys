from django.urls import path
from mypage import views
app_name = 'mypage'

urlpatterns = [
    path('change_pw', views.password_edit_view, name='password_edit'),

]