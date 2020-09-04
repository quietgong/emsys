from django.urls import path

from .views import base_views, comment_views, vote_views, answer_views

app_name = 'notice_sw7up'

urlpatterns = [

    path('<int:post_id>/', base_views.detail, name='detail'),

    path('post/list/', base_views.list, name='list'),
    # answer_views.py
    path('answer/create/<int:post_id>/', answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/', answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # comment_views.py
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create, name='comment_create'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify, name='comment_modify'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete, name='comment_delete'),

    # vote_views.py
    path('vote/post/<int:post_id>/', vote_views.vote_post, name='vote_post'),

]