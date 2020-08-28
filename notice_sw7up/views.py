from django.shortcuts import render

from notice_sw7up.models import Post


def index(request):
    """
    소중 사업 공지 목록 출력
    """
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list}
    return render(request, 'notice_sw7up/post_list.html', context)

def detail(request, post_id):
    """
    소중 사업 공지 내용 출력
    """
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'notice_sw7up/post_detail.html', context)