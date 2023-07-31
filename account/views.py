from django.views import generic
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from article.models import Article


class RegisterView(generic.CreateView):
    """
    Render log in page after registeration
    """
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')


def ProfileView(request):
    """
    Render logged in user profile
    """
    user_articles = Article.objects.filter(author=request.user)
    user_name = request.user
    bookmarked_articles = Article.objects.filter(favourites__in=[request.user])
    return render(
        request, 'profile.html', {
            'user_articles': user_articles,
            'bookmarked_articles': bookmarked_articles,
            'user_name': user_name})
