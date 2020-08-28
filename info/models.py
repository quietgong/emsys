import os

from django.conf import settings
from django.db import models

class Post(models.Model):
    objects = None
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    upload_files = models.FileField(null=True, blank=True, verbose_name='파일')
    filename = models.CharField(max_length=64, null=True, verbose_name='첨부파일명')
    def delete(self, *args, **kargs):
        if self.upload_files:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.upload_files.path))
        super(Post, self).delete(*args, **kargs)

    def __str__(self):
        return self.subject