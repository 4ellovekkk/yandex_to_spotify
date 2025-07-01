import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Your Spotify app credentials
SPOTIPY_CLIENT_ID = ""
SPOTIPY_CLIENT_SECRET = ""
SPOTIPY_REDIRECT_URI = "http://127.0.0.1:8888/webhook"

# Create Spotify client with user authorization
scope = "user-library-modify"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope,
    )
)

# Read your track list
added_count = 0

with open("playlist_tracks.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "—" not in line:
            continue
        title, artist = line.strip().split("—")
        query = f"track:{title.strip()} artist:{artist.strip()}"
        results = sp.search(q=query, type="track", limit=1)
        items = results["tracks"]["items"]
        if items:
            uri = items[0]["uri"]
            sp.current_user_saved_tracks_add([uri])
            print(f"Added to Liked Songs: {title.strip()} — {artist.strip()}")
            added_count += 1
        else:
            print(f"Not found: {title.strip()} — {artist.strip()}")

print(f"\n Total tracks added to Liked Songs: {added_count}")
# Create Spotify client with user authorization
scope = "playlist-modify-public playlist-modify-private"
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=SPOTIPY_CLIENT_ID,
        client_secret=SPOTIPY_CLIENT_SECRET,
        redirect_uri=SPOTIPY_REDIRECT_URI,
        scope=scope,
    )
)

# Create a new playlist
user_id = sp.current_user()["id"]
playlist_name = "Imported from Yandex Music"
playlist = sp.user_playlist_create(user=user_id, name=playlist_name, public=False)
playlist_id = playlist["id"]

# Read your track list
track_uris = []

with open("playlist_tracks.txt", "r", encoding="utf-8") as f:
    for line in f:
        if "—" not in line:
            continue
        title, artist = line.strip().split("—")
        query = f"track:{title.strip()} artist:{artist.strip()}"
        results = sp.search(q=query, type="track", limit=1)
        items = results["tracks"]["items"]
        if items:
            uri = items[0]["uri"]
            track_uris.append(uri)
            print(f"Found: {title.strip()} — {artist.strip()}")
        else:
            print(f"Not found: {title.strip()} — {artist.strip()}")

# Add found tracks to playlist
if track_uris:
    sp.playlist_add_items(playlist_id, track_uris)
    print(f"Added {len(track_uris)} tracks to your new Spotify playlist!")
else:
    print("No tracks were added.")
