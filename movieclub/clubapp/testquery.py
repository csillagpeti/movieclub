import requests
import os
from dotenv import load_dotenv

url = "https://api.themoviedb.org/3/trending/tv/day?language=en-US"

TMDB_API_KEY = os.getenv('TMDB_API_KEY')

headers = {
    "accept": "application/json",
    "Authorization": TMDB_API_KEY,
}

params = {
    "page": 1
}

response = requests.get(url, headers=headers, params=params)

with open ('response.json', 'a') as f:
    f.write(response.text)