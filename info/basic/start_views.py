from django.shortcuts import render
from notice.models import Post as notice_post
from recruit.models import Post as recruit_post
from greeting.models import Post as greeting_post
from notice_sw.models import Post as notice_sw_post
from notice_sw7up.models import Post as notice_sw7up_post

def index(request):
    notice_post_list = notice_post.objects.order_by('-create_date')[:4]
    notice_sw_post_list = notice_sw_post.objects.order_by('-specific_id')[:4]
    notice_sw7up_post_list = notice_sw7up_post.objects.order_by('-specific_id')[:4]
    recruit_post_list = recruit_post.objects.order_by('-specific_id')[:4]
    greeting_post_list = greeting_post.objects.order_by('-create_date')[:4]
    context = {'notice_post_list': notice_post_list,
               'notice_sw_post_list': notice_sw_post_list,
               'notice_sw7up_post_list': notice_sw7up_post_list,
               'recruit_post_list': recruit_post_list,
               'greeting_post_list' : greeting_post_list}
    return render(request, 'info/index.html', context)