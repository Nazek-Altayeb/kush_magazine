from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Article
from .forms import ArticleForm, EditArticleForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.


class HomeView(ListView):
    model = Article
    template_name = 'home.html'


""" def get_context_data(self, *args, **kwargs):
        categories = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['categories'] = categories
        return context
        ...............
        artc = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = artc.total_likes()
        liked = False
        if artc.likes.filter(id=self.request.user.id).exist()
        liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context"""


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article.html'

    def get_context_data(self, *args, **kwargs):
        # categories = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        # context['categories'] = categories
        artc = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = artc.total_likes()
        liked = False
        if artc.likes.filter(id=self.request.user.id).exist():
            liked = True
            context["total_likes"] = total_likes
            context["liked"] = liked

        return context


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


"""class AddCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'add-Category.html'
    # fields = '__all__'"""


def LikeView(request, pk):
    article = get_object_or_404(Article, id=request.POST.get('article_id'))
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article'), args=[str(pk)])
