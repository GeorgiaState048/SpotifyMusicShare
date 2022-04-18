"""tmdb and mediawiki API functions"""
import os
import requests
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def get_movie_data(external_id):
    """returns info about a movie"""
    base_url = "https://api.themoviedb.org/3/movie/"+external_id+ \
        "?api_key=" + os.getenv("TMDB_KEY") + "&language=en-US"
    response = requests.get(base_url)
    response_json = response.json()
    genre_ids = response_json['genres']
    genres = []
    for i in genre_ids:
        genres.append(i['name'])
    title = response_json['title']
    overview = response_json['overview']
    genre_names = ', '.join(genres)
    picture = "https://image.tmdb.org/t/p/w500" + response_json['poster_path']
    date = response_json['release_date'][0:4]
    production_company = response_json['production_companies'][0]['name']
    return  [title, overview, genre_names, picture, date, production_company]

def wiki_page(title, year):
    """wikipedia api"""
    movie = title + " " + year
    base_url = "https://en.wikipedia.org/w/api.php"
    query_params = {
        "action": "opensearch",
        "search": movie,
        "format": "json",
    }

    the_response = requests.get(base_url, params=query_params)
    json_response = the_response.json()
    return json_response[3][0]
