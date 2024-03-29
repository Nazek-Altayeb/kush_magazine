from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path(
        "article/<int:pk>", views.ArticleDetailView.as_view(), name="article"),
    path("search/", views.SearchArticleView, name="search-article"),
    path("add-article", views.AddArticleView.as_view(), name="add-article"),
    path("add-topic", views.AddTopicView.as_view(), name="add-topic"),
    path(
        "article/edit-article/<int:pk>",
        views.UpdateArticleView.as_view(),
        name="edit-article",
    ),
    path(
        "article/delete-article/<int:pk>",
        views.DeleteArticleView.as_view(),
        name="delete-article",
    ),
    path("delete/<int:pk>", views.DeleteView, name="delete"),
    path("topic/<str:tpc>", views.TopicView, name="topic"),
    path("like/<int:pk>", views.LikeView, name="like-article"),
    path("bookmark/<int:pk>", views.BookmarkView, name="bookmark-article"),
    path("404", views.Custom_404, name="404"),
]
