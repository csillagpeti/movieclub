import requests
import time
import os
from dotenv import load_dotenv


def fetch_movie_titles(api_key, page= 1):
    base_url = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    movies = []

    params = {"page": page}
    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch page {page}: {response.status_code}")

    data = response.json()
    for movie in data.get("results", []):
        movie_entry = {
        "title": movie.get("title", "No Title"),
        "poster_path": movie.get("poster_path", "No Path"),
        "overview": movie.get("overview", "No overview"),
        "release_date": movie.get("release_date", "No Release Date"),
        "vote_average": movie.get("vote_average", "No Votes"),
        "id": movie.get("id", "No Id"),
    }
        movies.append(movie_entry)
    total_pages = data.get("total_pages", 1)
    current_page = data.get("page", 1)
    return movies, total_pages, current_page

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("TMDB_API_KEY")
    movie_titles = fetch_movie_titles(api_key)

    for title in movie_titles:
        print(title)


def search_movie_titles(api_key, queryString=None, page= 1):
    base_url = "https://api.themoviedb.org/3/search/movie"
    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    movies = []

    params = {"page": page, "query": queryString}
    response = requests.get(base_url, headers=headers, params=params)
    if response.status_code != 200:
        print(f"Failed to fetch page {page}: {response.status_code}")

    data = response.json()
    for movie in data.get("results", []):
        movie_entry = {
        "title": movie.get("title", "No Title"),
        "poster_path": movie.get("poster_path", "No Path"),
        "overview": movie.get("overview", "No overview"),
        "release_date": movie.get("release_date", "No Release Date"),
        "vote_average": movie.get("vote_average", "No Votes"),
        "id": movie.get("id", "No Id"),
    }
        movies.append(movie_entry)
    total_pages = data.get("total_pages", 1)
    current_page = data.get("page", 1)
    return movies, total_pages, current_page, queryString

if __name__ == "__main__":
    load_dotenv()
    api_key = os.getenv("TMDB_API_KEY")
    movie_titles = fetch_movie_titles(api_key)

    for title in movie_titles:
        print(title)