from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Article

# Create your views here.


class HomeView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'


class AddArticleView(CreateView):
    model = Article
    template_name = 'add-article.html'
    fields = '__all__'
