from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def new(request):
  return render(request, 'articles/new.html')

def index(request):
  articles = Article.objects.all()
  context = {
    'articles':articles,
  }
  return render(request, 'articles/index.html', context)

def create(request):
  title = request.GET.get('title')
  content = request.GET.get('content')
  article = Article(title=title, content=content)
  article.save()
  return redirect("articles:detail", article.pk)

def detail(request, pk):
  articles = Article.objects.get(pk=pk)
  context = {
    'articles':articles,
  }
  return render(request, 'articles/detail.html', context)

def delete(request, pk):
  article = Article.objects.get(pk=pk)
  article.delete()
  return redirect('articles:index')

def edit(request, pk):
  articles = Article.objects.get(pk=pk)
  context = {
    'articles':articles,
  }
  return render(request, 'articles/edit.html', context)

def update(request, pk):
  articles = Article.objects.get(pk=pk)
  articles.title = request.POST.get('title')
  articles.content = request.POST.get('content')
  articles.save()
  return redirect('articles:detail', articles.pk)