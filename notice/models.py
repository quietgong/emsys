import os

from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    objects = None
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Notice_author')
    upload_files = models.FileField(null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    hits = models.PositiveIntegerField(default=0)

    @property
    def update_counter(self):
        self.hits += 1
        self.save()
    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
        super(Post, self).delete(*args, **kargs)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Notice_author_answer')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='Notice_voter_answer')  # voter 추가

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Notice_comment_author')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)