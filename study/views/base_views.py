from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from ..models import Post

@login_required(login_url='accounts:login')
def list(request):
    """
    study 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    so = request.GET.get('so', '공통') # 정렬기준

    # 정렬
    if so == '공통':
        post_list = Post.objects.filter(grade='공통')
    elif so == '1학년':
        post_list = Post.objects.filter(grade='1학년')
    elif so == '2학년':
        post_list = Post.objects.filter(grade='2학년')
    elif so == '3학년':
        post_list = Post.objects.filter(grade='3학년')
    else:
        post_list = Post.objects.filter(grade='4학년')

    # 검색
    if kw:
        post_list = post_list.filter(
            Q(subject__icontains=kw) | # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw) # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(post_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'post_list': page_obj, 'page': page, 'kw': kw, 'so': so} # page, kw, so가 추가되었다.

    return render(request, 'study/post_list.html', context)

def detail(request, post_id):
    """
    study 내용 출력
    """
    post = get_object_or_404(Post, pk=post_id)
    context = {'post': post}
    return render(request, 'study/post_detail.html', context)