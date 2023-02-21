from django.shortcuts import render
from .models import Article     # models.py에서 Article을 가져온다

# Create your views here.
def index(request):
    articles = Article.objects.all()    # Article을 가져온다(?)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)
 