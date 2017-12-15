from django.contrib import admin
from .models import Comment

# Register your models here.


class CommentAdmin(admin.ModelAdmin):
    list_display = ('create_time', 'name', 'content')

admin.site.register(Comment, CommentAdmin)