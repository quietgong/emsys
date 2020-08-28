from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import Post, Comment

@login_required(login_url='common:login')
def comment_create_post(request, post_id):
    """
    activity 질문댓글등록
    """
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.create_date = timezone.now()
            comment.post = post
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('activity:detail', post_id=comment.post.id), comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'activity/comment_form.html', context)

@login_required(login_url='common:login')
def comment_modify_post(request, comment_id):
    """
    activity 질문댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('{}#comment_{}'.format(
            resolve_url('activity:detail', post_id=comment.post.id), comment.id))

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('activity:detail', post_id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'activity/comment_form.html', context)

@login_required(login_url='common:login')
def comment_delete_post(request, comment_id):
    """
    activity 질문댓글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('activity:detail', post_id=comment.post_id)
    else:
        comment.delete()
    return redirect('activity:detail', post_id=comment.post_id)

@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    """
    activity 답글댓글수정
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('activity:detail', post_id=comment.answer.post.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modify_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('activity:detail', post_id=comment.answer.post.id), comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'activity/comment_form.html', context)


@login_required(login_url='common:login')
def comment_delete_answer(request, comment_id):
    """
    activity 답글댓글삭제
    """
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('activity:detail', post_id=comment.answer.post.id)
    else:
        comment.delete()
    return redirect('activity:detail', post_id=comment.answer.post.id)