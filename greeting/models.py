from django.contrib.auth.models import User
from django.db import models

class Post(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Greeting_author')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Greeting_author_answer')
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.content

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Greeting_comment_author')
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.content
