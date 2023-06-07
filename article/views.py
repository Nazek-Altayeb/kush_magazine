from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article, Category
from .forms import ArticleForm, EditArticleForm, CategoryForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

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


class UpdateArticleView(UpdateView):
    model = Article
    form_class = EditArticleForm
    template_name = 'update-article.html'


class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'delete-article.html'
    success_url = reverse_lazy('home')


class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add-category.html'


def CategoryView(request, catg):
    category_articles = Article.objects.filter(category=catg.replace('-', ''))
    return render(request, 'categories.html', {'catg': catg.title().replace('-', ''), 'category_articles': category_articles})
