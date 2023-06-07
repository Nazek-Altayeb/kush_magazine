from django.urls import path
from .views import HomeView, ArticleDetailView, AddArticleView, UpdateArticleView, DeleteArticleView, AddCategoryView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('add-article', AddArticleView.as_view(), name='add-article'),
    path('add-category', AddCategoryView.as_view(), name='add-category'),
    path('article/edit-article/<int:pk>',
         UpdateArticleView.as_view(), name='edit-article'),
    path('article/delete-article/<int:pk>',
         DeleteArticleView.as_view(), name='delete-article'),
    path('category/<str:catg>', CategoryView, name='category')
    # path('like/<int:pk>', LikeView, name='like_article')
]
