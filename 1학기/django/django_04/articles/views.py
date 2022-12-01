import re
from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe,
require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
@require_safe   # method=='GET'인 애들만 실행하게 걸러줌
def index(request):
    # DB에 전체 데이터를 조회
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == 'POST':
        # create
        form = ArticleForm(request.POST)
        if form.is_valid():     # 유효성 검사를 통과하면
            article = form.save()         # form을 저장
            return redirect('articles:detail', article.pk) 
    else:
        # new
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    # variable routing으로 받은 pk 값으로 데이터를 조회
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=pk)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():     # 유효성 검사 통과했을 때
            form.save()
            return redirect('articles:detail', article.pk)  
    else:
        article = Article.objects.get(pk=pk)
        form = ArticleForm(instance=article)    # 기존 값을 출력해야하기 때문에 article을 기본값 입력
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)

