from django.shortcuts import render

from notice_sw.models import Post


def index(request):
    """
    학과 공지 목록 출력
    """
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list}
    return render(request, 'notice_sw/post_list.html', context)

def detail(request, post_id):
    """
    학과 공지 내용 출력
    """
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'notice_sw/post_detail.html', context)