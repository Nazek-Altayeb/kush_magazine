from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm, EditArticleForm
from django.urls import reverse_lazy

# Create your views here.


class HomeView(ListView):
    model = Article
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'


class AddArticleView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'add-article.html'
    # fields = '__all__'


class UpdateArticleView(UpdateView):
    model = Article
    form_class = EditArticleForm
    template_name = 'update-article.html'
    # fields = ['title', 'body']


class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete-article.html'
    success_url = reverse_lazy('home')
