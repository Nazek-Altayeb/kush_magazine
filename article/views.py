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

    """def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['categories'] = categories
        return context"""


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'

    def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        context['categories'] = categories
        article = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = article.total_likes()
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
            context["total_likes"] = total_likes
            context["liked"] = liked

        return context


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
    category_articles = Article.objects.filter(category=catg)
    return render(request, 'categories.html', {'catg': catg.title(), 'category_articles': category_articles})


def LikeView(request, pk):
    article = get_object_or_404(Article, id=request.POST.get('article-id'))
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))


