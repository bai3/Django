from django.db import models
from django.utils import timezone

# Create your models here.


# 文章数据库
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


# 作品展示数据库
class Work(models.Model):
    title = models.CharField(max_length=100)
    pub_time = models.DateTimeField(default=timezone.now)
    des = models.CharField(max_length=400)
    img_url = models.URLField(max_length=200)
    github_url = models.URLField(default="https://github.com/bai3")
    url = models.URLField(default="http://39.108.84.239/")

    class Meta:
        ordering = ('-pub_time',)

    def __unicode__(self):
        return self.title
