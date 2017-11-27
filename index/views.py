from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .models import Article, Work
from markdown import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def page_not_found(request):
    template = get_template('404.html')
    return HttpResponse(template)


def common():
    work_total = Work.objects.count()
    amount = Article.objects.count()
    tag_amount = Article.objects.values('tag').distinct().count()
    type_amount = Article.objects.values('type').distinct().count()
    return work_total, amount, tag_amount, type_amount


# 首页
def index(request):
    total = common()
    light = 1
    template = get_template('index/index.html')
    articles = Article.objects.all()
    for article in articles:
        article.body = markdown(article.body)
    paginator = Paginator(articles, 3)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    html = template.render(locals())
    return HttpResponse(html)


# 文章详情
def article(request, id):
    light = 2
    total = common()
    tempalte = get_template('index/article.html')
    detail = Article.objects.get(id=id)
    detail.body = markdown(detail.body)
    html = tempalte.render(locals())
    return HttpResponse(html)


# 文章目录
def allarticles(request):
    total = common()
    tempalte = get_template('index/articlesList.html')
    articles = Article.objects.all()
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    light = 2
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    html = tempalte.render(locals())
    return HttpResponse(html)


# 作品展示
def show(request):
    light = 3
    works = Work.objects.all()
    total = common()
    template = get_template('index/show.html')
    html = template.render(locals())
    return HttpResponse(html)
