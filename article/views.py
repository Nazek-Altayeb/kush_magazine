from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.views.generic.edit import FormMixin
from .models import Article, Topic
from .forms import ArticleForm, EditArticleForm, TopicForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.utils import html
from django.contrib import messages
from django.db.models import Q


# home page view
class HomeView(ListView):
    """
    Renders all objects of article model
    """
    model = Article
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        topics = Topic.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['topics'] = topics
        return context


# detailed article view
class ArticleDetailView(FormMixin, DetailView):
    """
    Renders specific article
    """
    model = Article
    form_class = CommentForm
    template_name = 'article.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data(
            *args, **kwargs)
        article = get_object_or_404(Article, id=self.kwargs['pk'])
        context["article.body"] = article.body
        total_likes = article.total_likes()
        liked = False
        favourite = False
        if article.likes.filter(id=self.request.user.id).exists():
            liked = True
        context["total_likes"] = total_likes
        context["liked"] = liked
        if article.favourites.filter(id=self.request.user.id).exists():
            favourite = True
        context["favourite"] = favourite
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


# create article view
class AddArticleView(CreateView):
    """
    Create new article
    """
    model = Article
    form_class = ArticleForm
    template_name = 'add-article.html'

    # Source:
    # https://github.com/Kathrin-ddggxh/woohoo-haiku/blob/main/haikus/views.py
    def form_valid(self, form):
        form.instance.author = self.request.user
        msg = "Your article was created successfully"
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super(CreateView, self).form_valid(form)


# update article view 
class UpdateArticleView(UpdateView):
    """
    update existing article
    """
    model = Article
    form_class = EditArticleForm
    template_name = 'update-article.html'

    # Source:
    # https://github.com/Kathrin-ddggxh/woohoo-haiku/blob/main/haikus/views.py
    def form_valid(self, form):
        form.instance.author = self.request.user
        msg = "Your article has been updated successfully"
        messages.add_message(self.request, messages.SUCCESS, msg)
        return super(UpdateView, self).form_valid(form)


# delete article view
class DeleteArticleView(DeleteView):
    """
    Delete specific article
    """
    model = Article
    template_name = 'delete-article.html'
    success_url = reverse_lazy('home')


# create topic view
class AddTopicView(CreateView):
    """
    Create new topic
    """
    model = Topic
    form_class = TopicForm
    template_name = 'add-topic.html'


# topic view 
def TopicView(request, tpc):
    """
    retrive articles according to specific topic
    """
    topic_articles = Article.objects.filter(topic=tpc)
    return render(
        request, 'topics.html', {
            'tpc': tpc.title(), 'topic_articles': topic_articles})


# like article view
def LikeView(request, pk):
    """
    Increase like counter after clicking the like icon
    """
    article = get_object_or_404(Article, id=request.POST.get('article-id'))
    liked = False
    if article.likes.filter(id=request.user.id).exists():
        article.likes.remove(request.user)
        liked = False
    else:
        article.likes.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))


# save article view
def BookmarkView(request, pk):
    """
    save article to user profile
    """
    article = get_object_or_404(Article, id=request.POST.get('article-id'))
    favourite = False
    if article.favourites.filter(id=request.user.id).exists():
        article.favourites.remove(request.user)
        favourite = False
    else:
        article.favourites.add(request.user)
        favourite = True
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))


# search for article/s view
def SearchArticleView(request):
    """
    Search for article according to author or article title or article topic
    """
    if request.method == "POST":
        searched = request.POST['searched']
        query = (Q(title__icontains=searched) |
                  Q(topic__icontains=searched) |
                  Q(author__username__icontains=searched))
        articles = Article.objects.filter(query)
        return render(request, 'search-article.html',
                      {'searched': searched, 'articles': articles})
    else:
        return HttpResponseRedirect(reverse('home'))


# delete article view
def DeleteView(request, pk):
    """
    Remove article
    """
    article = get_object_or_404(Article, id=request.POST.get('article-id'))
    article.delete()
    msg = "Your article has been deleted"
    messages.add_message(request, messages.SUCCESS, msg)
    return HttpResponseRedirect(reverse('home'))


# custom 404 view
def Custom_404(request, exception):
    """
    Render page-not-found
    """
    return render(request, '404.html', status=404)