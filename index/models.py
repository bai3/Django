from django.db import models
from django.utils import timezone

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10)
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date',)

    def __unicode__(self):
        return self.title
