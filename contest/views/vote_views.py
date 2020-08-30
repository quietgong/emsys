from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Post

@login_required(login_url='accounts:login')
def vote_post(request, post_id):
    """
    contest 질문추천등록
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.user == post.author:
        messages.error(request, '본인이 작성한 글은 추천할수 없습니다')
    else:
        post.voter.add(request.user)
    return redirect('contest:detail', post_id=post.id)
