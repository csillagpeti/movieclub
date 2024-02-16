from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.conf import settings
from .fetch_tmdb import fetch_movie_titles
from .models import User, Movie

import json

# Create your views here.

def index(request):
    user_movie_ids = set()
    if request.user.is_authenticated:
        user_movie_ids = set(request.user.movies.values_list('movie_id', flat=True))

    movies, current_page, total_pages = fetch_movie_titles(settings.TMDB_API_KEY)

    for movie in movies:
        movie['in_user_list'] = movie['id'] in user_movie_ids
    print('Index movies: ', movies)
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
    print(request.body)
    data = json.loads(request.body)
    movie_id = data.get("movie_id")
    movie_title = data.get("movie_title")
    movie_poster_path = data.get("movie_poster_path")
    movie_overview = data.get("movie_overview")
    movie_release_date = data.get("movie_release_date")
    movie_vote_average = data.get("movie_vote_average")


    if not movie_id or not movie_title:
        return HttpResponse('Movie ID and title are required.', status=400)
    
    movie, created = Movie.objects.get_or_create(
        movie_id=movie_id, 
        defaults={
            'movie_title': movie_title,
            'movie_poster_path': movie_poster_path,
            'movie_overview': movie_overview,
            'movie_release_date': movie_release_date,
            'movie_vote_average': movie_vote_average
            })

    if movie in request.user.movies.all():
        request.user.movies.remove(movie)
        action = "removed"
    else:
        request.user.movies.add(movie)
        action = "added"
    
    return JsonResponse({'action': action})

def my_list(request):
    if request.user.is_authenticated:
        movies = []
        user_movies = request.user.movies.all()
        print('User movies: ', user_movies)
        for movie in user_movies:
            movie_entry = {
                "title": movie.movie_title if movie.movie_title else "No Title",
                "poster_path": movie.movie_poster_path if movie.movie_poster_path else "No Path",
                "overview": movie.movie_overview if movie.movie_overview else "No overview",
                "release_date": movie.movie_release_date if movie.movie_release_date else "No Release Date",
                "vote_average": movie.movie_vote_average if movie.movie_vote_average else "No Votes",
                "id": movie.movie_id if movie.movie_id else "No Movie ID",
                "in_user_list": True
            }
            movies.append(movie_entry)
        print('User movies: ', movies)


        
    return render(request, "clubapp/my_list.html", {"movies": movies})