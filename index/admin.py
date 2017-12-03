from django.contrib import admin
from .models import Article, Work, User


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'tag', 'type', 'pub_time')
    search_fields = ('title',)
    list_filter = ('type', 'tag')


class ShowAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_time', 'url', 'img_url')
    search_fields = ('title',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'rank', 'create_time')
    search_fields = ('username',)
    list_filter = ('rank',)




admin.site.register(Article, PostAdmin)
admin.site.register(Work, ShowAdmin)
admin.site.register(User, UserAdmin)

