from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils import timezone

from inquiry.forms import PostForm

@login_required(login_url='accounts:login')
def index(request):
    """
    inquiry 글등록
    """
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.create_date = timezone.now()
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'inquiry/post_form.html', context)