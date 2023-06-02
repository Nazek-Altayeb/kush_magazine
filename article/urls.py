from django.urls import path
from . import views
from .views import HomeView, ArticleDetailView, AddArticleView, UpdateArticleView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('add-article', AddArticleView.as_view(), name='add-article'),
    path('article/edit-article/<int:pk>',
         UpdateArticleView.as_view(), name='edit-article')
]
