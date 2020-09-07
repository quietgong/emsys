from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from django.shortcuts import render, get_object_or_404

from ..models import Post


def list(request):
    """
    recruit 목록 출력
    """
    # 입력 파라미터
    kw = request.GET.get('kw', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recommend':
        post_list = Post.objects.annotate(num_voter=Count('voter')).order_by('-num_voter', 'specific_id')
    elif so == 'popular':
        post_list = Post.objects.annotate(num_answer=Count('answer')).order_by('-num_answer', 'specific_id')
    elif so == 'history':
        post_list = Post.objects.order_by('-specific_id')
    else:  # recent
        post_list = Post.objects.order_by('specific_id')

    # 검색
    if kw:
        post_list = post_list.filter(
            Q(title__icontains=kw)  # 제목검색
        ).distinct()

    context = {'post_list': post_list, 'kw': kw, 'so': so}  # page, kw, so가 추가되었다.

    return render(request, 'recruit/post_list.html', context)

@login_required(login_url='accounts:login')
def detail(request, post_id):
    """
    학과 공지 내용 출력
    """
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'recruit/post_detail.html', context)