from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect

from ..models import Post

@login_required(login_url='accounts:login')
def vote_post(request, post_id):
    """
    취업 질문추천등록
    """
    post = get_object_or_404(Post, pk=post_id)

    if request.user in post.voter.all():
        post.voter.remove(request.user)
    else:
        post.voter.add(request.user)
    return redirect('recruit:detail', post_id=post.id)