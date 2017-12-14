from django.shortcuts import render
from django.http import HttpResponse
from . import models
def index(request):
    # 获取所有的条数
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})
    # 获取某一条
    # article = models.Article.objects.get(pk=1)
    # return render(request, 'blog/index.html', {"article":article})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

















