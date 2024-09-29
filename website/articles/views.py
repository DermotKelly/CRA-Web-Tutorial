from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def articles(request):
    return render (request, 'articles/articles.html')

def article(request, pk):
    return render (request, 'articles/article.html') 


def createArticle (request):
    form = ArticleForm

    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles')

    context = {'form':form}
    return render (request, 'articles/article_form.html', context)