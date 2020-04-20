from django.db import models
import os
from django.utils import timezone


def upload_path(instance, filename):
    now = timezone.now()
    filename_base, filename_ext = os.path.splitext(filename)
    return 'images/{}{}'.format(now.strftime('%Y%m%d%H%M%S'), filename_ext.lower())


class Cars(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    picture = models.FileField(upload_to=upload_path, default="default_photo.jpg", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Cars'
