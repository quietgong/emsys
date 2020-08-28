from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import Question

def list(request):
    """
    academic 목록 출력
    """
    # 입력 파라미터
    page = request.GET.get('page', '1') # 페이지
    kw = request.GET.get('kw', '') # 검색어
    so = request.GET.get('so', '공통') # 정렬기준

    # 정렬
    if so == '공통':
        question_list = Question.objects.filter(grade='공통')
    elif so == '1학년':
        question_list = Question.objects.filter(grade='1학년')
    elif so == '2학년':
        question_list = Question.objects.filter(grade='2학년')
    elif so == '3학년':
        question_list = Question.objects.filter(grade='3학년')
    else:
        question_list = Question.objects.filter(grade='4학년')

    # 검색
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) | # 제목검색
            Q(content__icontains=kw) |  # 내용검색
            Q(author__username__icontains=kw) |  # 질문 글쓴이검색
            Q(answer__author__username__icontains=kw) # 답변 글쓴이검색
        ).distinct()

    # 페이징처리
    paginator = Paginator(question_list, 10) # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list': page_obj, 'page': page, 'kw': kw, 'so': so} # page, kw, so가 추가되었다.

    return render(request, 'academic/question_list.html', context)

def detail(request, question_id):
    """
    academic 내용 출력
    """
    question = get_object_or_404(Question, pk=question_id)
    context = {'question': question}
    return render(request, 'academic/question_detail.html', context)