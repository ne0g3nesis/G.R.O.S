import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)


CLIENT_ID = "c57fc4297ccf4308aec564ab2d463436"
CLIENT_SECRET = "bf0ecc47638e475ab980f7a7a83c32e5"
REDIRECT_URI = "http://127.0.0.1:8888/callback/"

scope = "user-read-private user-read-email"

sp_oauth = SpotifyOAuth(client_id=CLIENT_ID,
                        client_secret=CLIENT_SECRET,
                        redirect_uri=REDIRECT_URI,
                        scope=scope,
                        open_browser=True)

token_info = sp_oauth.get_access_token(as_dict=True)
access_token = token_info["access_token"]

sp = spotipy.Spotify(auth=access_token)

playlist_url = input("Entre l'URL de ta playlist Spotify : ").strip()

def extract_playlist_id(url):
    if "playlist/" in url:
        return url.split("playlist/")[1].split("?")[0]
    else:
        return url

playlist_id = extract_playlist_id(playlist_url)

tracks = []
results = sp.playlist_tracks(playlist_id)
tracks.extend(results['items'])

while results['next']:
    results = sp.next(results)
    tracks.extend(results['items'])

skipped = 0
lines = []

for item in tracks:
    track = item['track']
    if track is None or track.get('artists') is None:
        continue
    title = track.get('name', 'Titre inconnu')
    artists = ", ".join([
        artist['name'] if artist and isinstance(artist.get('name'), str) else 'Artiste inconnu'
        for artist in track['artists']
    ])
    lines.append(f"{title} - {artists}")

with open("tracks.txt", "w", encoding="utf-8") as f:
    f.writelines([line + "\n" for line in lines])
