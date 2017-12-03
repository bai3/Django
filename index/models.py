from django.db import models
from django.utils import timezone

# Create your models here.


# 文章数据库
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name="文章标题")
    type = models.CharField(max_length=20, default='note', verbose_name="文章类别")
    tag = models.CharField(max_length=100, verbose_name="文章标签")
    pub_time = models.DateTimeField(default=timezone.now, verbose_name="文章创建时间")
    body = models.TextField(verbose_name="文章内容")

    class Meta:
        ordering = ('-pub_time',)

    def __unicode__(self):
        return self.title


# 作品展示数据库
class Work(models.Model):
    title = models.CharField(max_length=100, verbose_name="作品标题")
    pub_time = models.DateTimeField(default=timezone.now, verbose_name="更新时间")
    des = models.CharField(max_length=400, verbose_name="作品描述")
    img_url = models.URLField(max_length=200, verbose_name="作品展示图片地址")
    github_url = models.URLField(default="https://github.com/bai3", verbose_name="github地址")
    url = models.URLField(default="http://39.108.84.239/", verbose_name="项目地址")

    class Meta:
        ordering = ('-pub_time',)

    def __unicode__(self):
        return self.title


# 用户表
class User(models.Model):
    username = models.CharField(max_length=50, verbose_name="用户名")
    password = models.CharField(max_length=50, verbose_name="密码")
    email = models.EmailField(max_length=30, null=True, blank=True, verbose_name="用户邮箱")
    mobile = models.CharField(max_length=20, null=True, blank=True, verbose_name="注册手机号码")
    rank = models.CharField(max_length=2, choices=(("1", u"普通会员"), ("2", "VIP会员"), ("3", "SVIP会员"),
                                                   ("4", "管理员"), ("5", "站长")), default="1", verbose_name="会员等级")
    create_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")

    class Meta:
        ordering = ('rank',)

    def __unicode__(self):
        return self.username


