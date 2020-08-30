from django.shortcuts import render

from notice_sw.models import Post


def list(request):
    """
    학과 공지 목록 출력
    """
    post_list = Post.objects.order_by('specific_id')
    context = {'post_list': post_list}
    return render(request, 'notice_sw/post_list.html', context)

def detail(request, post_id):
    """
    학과 공지 내용 출력
    """
    return render(request, 'notice_sw/post_detail.html', context)