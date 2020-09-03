from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Post

def list(request):
    """
    notice_sw 목록 출력
    """
    post_list = Post.objects.order_by('specific_id')
    context = {'post_list': post_list}
    return render(request, 'notice_sw/post_list.html', context)

def detail(request, post_id):
    """
    학과 공지 내용 출력
    """
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'notice_sw/post_detail.html', context)