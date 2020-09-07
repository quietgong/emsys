from django.db import models


class Post(models.Model):
    objects = None

    content = models.TextField()

    def __str__(self):
        return self.content