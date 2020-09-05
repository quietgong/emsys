from django import forms

from info.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['subject', 'content', 'upload_files', ]
        labels = {
            'subject': '제목',
            'content': '내용',
            'upload_files': '파일',
        }
        # widget 항목 삭제 (목적 : 디자인 영역과 서버 영역 분리)