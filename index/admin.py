from django.contrib import admin
from .models import Article
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'pub_time')

admin.site.register(Article, PostAdmin)
