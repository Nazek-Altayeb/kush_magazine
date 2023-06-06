from django.urls import path
from article.views import HomeView, ArticleDetailView, AddArticleView, UpdateArticleView, DeleteArticleView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('add-article', AddArticleView.as_view(), name='add-article'),
    # path('add-category', views.AddCategoryView.as_view(), name='add-category'),
    path('article/edit-article/<int:pk>',
         UpdateArticleView.as_view(), name='edit-article'),
    path('article/delete-article/<int:pk>',
         DeleteArticleView.as_view(), name='delete-article'),
    # path('like/<int:pk>', LikeView, name='like_article')
]
