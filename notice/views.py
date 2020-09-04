import mimetypes
import os
import urllib

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

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