from django.contrib import admin
from .models import Article

# Register your models here.


class Articles(admin.ModelAdmin):
    list_display = ('title',  'pub_date', 'category')

admin.site.register(Article, Articles)
