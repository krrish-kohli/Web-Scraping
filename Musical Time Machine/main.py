from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

SPOTIPY_CLIENT_ID = os.environ.get("YOUR_SPOTIPY_CLIENT_ID")
SPOTIPY_CLIENT_SECRET = os.environ.get("YOUR_SPOTIPY_CLIENT_SECRET")

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}

scope = "playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET, redirect_uri="https://example.com/", cache_path="token.txt", username="krrish kohli"))

user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/", headers=header)
webpage = response.text

soup = BeautifulSoup(webpage, 'html.parser')

song_name = soup.select("li ul li h3")
# print(song_name)

songs = [song.getText().strip() for song in song_name]

song_uri = []
year = date.split("-")[0]

for song in songs:
    result = sp.search(f"track: {song} year: {year}", type="track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"Billboard top 100 {date}", public=True, collaborative=False)
playlist_id = playlist["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=song_uri)
