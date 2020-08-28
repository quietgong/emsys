import mimetypes
import os
import urllib

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import QuestionForm
from ..models import Question

@login_required(login_url='common:login')
def question_create(request):
    """
    academic 질문등록
    """
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.author = request.user
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    question.filename = request.FILES['upload_files'].name
            question.save()
            return redirect('academic:detail', question_id=question.id)
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'academic/question_form.html', context)

@login_required(login_url='common:login')
def question_modify(request, question_id):
    """
    academic 질문수정
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('academic:detail', question_id=question.id)

    if request.method == "POST":
        file_change_check = request.POST.get('fileChange', False)
        file_check = request.POST.get('upload_files-clear', False)
        if file_check or file_change_check:
            os.remove(os.path.join(settings.MEDIA_ROOT, question.upload_files.path))

        form = QuestionForm(request.POST, request.FILES, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    question.filename = request.FILES['upload_files'].name
            question.author = request.user
            question.modify_date = timezone.now()
            question.save()
            return redirect('academic:detail', question_id=question.id)
    else:
        form = QuestionForm(instance=question)
    context={'form': form}
    return render(request, 'academic/question_form.html', context)

@login_required(login_url='common:login')
def question_delete(request, question_id):
    """
    academic 질문삭제
    """
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('academic:detail', question_id=question.id)
    question.delete()
    return redirect('academic:list')

@login_required(login_url='common:login')
def question_download_view(request, pk):
    question = get_object_or_404(Question, pk=pk)
    url = question.upload_files.url[1:]
    file_url = urllib.parse.unquote(url)

    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(question.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404