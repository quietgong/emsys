from django import forms
from recruit.models import Post, Comment, Answer

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        labels = {
            'title': '제목',
            'content': '내용',
        }
        # widget 항목 삭제 (목적 : 디자인 영역과 서버 영역 분리)

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }