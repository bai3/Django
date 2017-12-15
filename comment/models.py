from django.db import models
from django.utils import timezone


# 网站留言表
class Comment(models.Model):
    name = models.CharField(max_length=20, default="", verbose_name="留言人")
    content = models.TextField(max_length=200, verbose_name="留言内容")
    create_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")

    class Meta:
        ordering = ('id',)

    def __unicode__(self):
        return self.content
