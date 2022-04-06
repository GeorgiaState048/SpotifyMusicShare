import os
import requests
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

#keys needed from spotify developement, it is stored in the .env file
SPOTIFY_KEY = os.getenv("CLIENT_ID")
SECRET_KEY = os.getenv("CLIENT_SECRET")


def Spotify(playlist_id):
    """
    function to grab details from a playlist
    """
    Base_url = "https://api.spotify.com/v1/playlists/{playlist_id}"
    params = {"client_id": SPOTIFY_KEY,
               "client_secret": SECRET_KEY}
    response = requests.get(params = params)


    response_json = response.json()
    playlist_name = response_json["name"]
    description = response_json["description"]


#In oreder to get images it would need to grab url, height, width
    images = []
    for i in images:
        requirements = ["url", "height", "width"]
        images.append(requirements)

    results = {
        "name": playlist_name,
        "images": images,
        "description": description

    }
    return results