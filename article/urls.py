from django.urls import path
from . import views
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article'),
    path('add-article', views.AddArticleView.as_view(), name='add-article'),
    path('article/edit-article/<int:pk>',
         views.UpdateArticleView.as_view(), name='edit-article'),
    path('article/delete-article/<int:pk>',
         views.DeleteArticleView.as_view(), name='delete-article')
]
