from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from .models import Article, Topic
from .forms import ArticleForm, EditArticleForm, TopicForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

# Create your views here.


class HomeView(ListView):
    model = Article
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        topics = Topic.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['topics'] = topics
        return context


class ArticleDetailView(FormMixin, DetailView):
    model = Article
    form_class = CommentForm
    template_name = 'article.html'    

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        article = get_object_or_404(Article, id=self.kwargs['pk'])
        total_likes = article.total_likes()
        liked = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        comments = article.comments.order_by("-date_and_time")
        context["comments"] = comments


        return context


    def post(self, request, pk, *args, **kwargs):
        article = get_object_or_404(Article, id=request.POST.get('article-id'))
        comments = article.comments
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment_form.instance.user = request.user
            comment.article = article
            comment.save()
        else:
            comment_form = CommentForm()

        return HttpResponseRedirect(reverse('article', args=[str(pk)]))


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


class AddTopicView(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = 'add-topic.html'


def TopicView(request, tpc):
    topic_articles = Article.objects.filter(topic=tpc)
    return render(request, 'topics.html', {'tpc': tpc.title(), 'topic_articles': topic_articles})


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


def DeleteView(request, pk):
    article = get_object_or_404(Article, id=request.POST.get('article-id'))
    article.delete()
    return HttpResponseRedirect(reverse('home'))


