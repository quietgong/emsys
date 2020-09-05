import mimetypes
import os
import urllib

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from notice.forms import PostForm
from notice.models import Post


def index(request):
    """
    동아리공지 목록 출력
    """
    post_list = Post.objects.order_by('-create_date')
    context = {'post_list': post_list}
    return render(request, 'notice/post_list.html', context)

@login_required(login_url='accounts:login')
def detail(request, post_id):
    """
    동아리공지 내용 출력
    """
    post = Post.objects.get(id=post_id)
    context = {'post': post}
    return render(request, 'notice/post_detail.html', context)

def post_create(request):
    """
    notice 글등록
    """
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.author = request.user
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    post.filename = request.FILES['upload_files'].name
            post.save()
            return redirect('notice:detail', post_id=post.id)
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'notice/post_form.html', context)

def post_modify(request, post_id):
    """
    notice 글수정
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('notice:detail', post_id=post.id)

    if request.method == "POST":
        file_change_check = request.POST.get('fileChange', False)
        file_check = request.POST.get('upload_files-clear', False)
        if file_check or file_change_check:
            os.remove(os.path.join(settings.MEDIA_ROOT, post.upload_files.path))

        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            if request.FILES:
                if 'upload_files' in request.FILES.keys():
                    post.filename = request.FILES['upload_files'].name
            post.author = request.user
            post.modify_date = timezone.now()
            post.save()
            return redirect('notice:detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    context={'form': form}
    return render(request, 'notice/post_form.html', context)

def post_delete(request, post_id):
    """
    notice 글삭제
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.user != post.author:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('notice:detail', post_id=post.id)
    post.delete()
    return redirect('notice:list')

def download(request, pk):
    post = get_object_or_404(Post, pk=pk)
    url = post.upload_files.url[1:]
    file_url = urllib.parse.unquote(url)

    if os.path.exists(file_url):
        with open(file_url, 'rb') as fh:
            quote_file_url = urllib.parse.quote(post.filename.encode('utf-8'))
            response = HttpResponse(fh.read(), content_type=mimetypes.guess_type(file_url)[0])
            response['Content-Disposition'] = 'attachment;filename*=UTF-8\'\'%s' % quote_file_url
            return response
        raise Http404