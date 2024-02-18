from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("toggle_movie_list/", views.toggle_movie_list, name="toggle_movie_list"),
    path("my_list", views.my_list, name="my_list"),
    path("search", views.search, name="search"),
    path("users", views.users, name="users")
]