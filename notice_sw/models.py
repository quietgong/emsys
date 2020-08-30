from django.db import models

class Post(models.Model):
    objects = None
    specific_id = models.IntegerField()
    title = models.CharField(max_length=200)
    link = models.TextField()

    def __str__(self):
        return self.title