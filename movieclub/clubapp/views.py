from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from .fetch_tmdb import fetch_movie_titles
from .models import User, Movie

# Create your views here.

def index(request):
    user_movie_ids = set()
    if request.user.is_authenticated:
        user_movie_ids = set(request.user.movies.values_list('movie_id', flat=True))

    movies, current_page, total_pages = fetch_movie_titles(settings.TMDB_API_KEY)

    for movie in movies:
        movie['in_user_list'] = movie['id'] in user_movie_ids
        
    return render(request, "clubapp/index.html", {"movies": movies, "total_pages": total_pages, "current_page": current_page})

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "clubapp/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "clubapp/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "clubapp/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "clubapp/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "clubapp/register.html")

@login_required
def toggle_movie_list(request):
    movie_id = request.POST.get("movie_id")
    movie_title = request.POST.get("movie_title")

    if not movie_id or not movie_title:
        return HttpResponse('Movie ID and title are required.', status=400)
    
    movie, created = Movie.objects.get_or_create(movie_id=movie_id, defaults={'movie_title': movie_title})

    if movie in request.user.movies.all():
        request.user.movies.remove(movie)
        action = "removed"
    else:
        request.user.movies.add(movie)
        action = "added"
    
    return HttpResponse(action, status=200)