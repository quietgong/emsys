from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField()
    specific_id = models.CharField(max_length=25)
    content = models.TextField()
    date = models.CharField(max_length=20)
    voter = models.ManyToManyField(User, blank=True, related_name='Notice_sw7up_voter')  # voter 추가
    hits = models.PositiveIntegerField(default=0)

    @property
    def update_counter(self):
        self.hits += 1
        self.save()

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Notice_sw7up_author_answer')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='Notice_sw7up_voter_answer')  # voter 추가
    def __str__(self):
        return self.content

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Notice_sw7up_comment_author')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.content
