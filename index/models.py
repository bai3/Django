from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20, default='note')
    tag = models.CharField(max_length=100)
    pub_time = models.DateTimeField(default=timezone.now)
    body = models.TextField()

    class Meta:
        ordering = ('-pub_time',)

    def __unicode__(self):
        return self.title
