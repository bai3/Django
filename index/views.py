from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .models import Article
from markdown import markdown
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.


def index(request):
    amount = Article.objects.count()
    tag_amount = Article.objects.values('tag').distinct().count()
    type_amount = Article.objects.values('type').distinct().count()
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


def article(request, id):
    amount = Article.objects.count()
    tag_amount = Article.objects.values('tag').distinct().count()
    type_amount = Article.objects.values('type').distinct().count()
    tempalte = get_template('index/article.html')
    detail = Article.objects.get(id=id)
    detail.body = markdown(detail.body)
    html = tempalte.render(locals())
    return HttpResponse(html)


def allarticles(request):
    amount = Article.objects.count()
    tag_amount = Article.objects.values('tag').distinct().count()
    type_amount = Article.objects.values('type').distinct().count()
    tempalte = get_template('index/articlesList.html')
    articles = Article.objects.all()
    paginator = Paginator(articles, 10)
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)
    html = tempalte.render(locals())
    return HttpResponse(html)

