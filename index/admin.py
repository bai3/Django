from django.contrib import admin
from .models import Article, Work
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'type', 'pub_time')
    search_fields = ('title',)


class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_time', 'url', 'img_url')
    search_fields = ('title',)

admin.site.register(Article, PostAdmin)
admin.site.register(Work, ShowAdmin)
