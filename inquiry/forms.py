from django import forms
from inquiry.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        labels = {
            'content': '내용',
        }