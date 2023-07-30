from django.urls import path
from . import views
from .views import RegisterView, ProfileView

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("profile/", ProfileView, name="profile"),
]
