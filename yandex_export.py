from yandex_music import Client

# Optional: authenticate with a token if needed
# client = Client('<your_token>').init()

# Or anonymously for public playlists:
client = Client().init()

username = "username@yandex.ru"
playlist_id = "3"

playlist = client.users_playlists(playlist_id, username)

# Open a file to write the results
with open("playlist_tracks.txt", "w", encoding="utf-8") as file:
    file.write(f"Playlist: {playlist.title}\n\n")

    for track in playlist.tracks:
        track_obj = track.fetch_track()
        title = track_obj.title
        artists = ", ".join(artist.name for artist in track_obj.artists)
        line = f"{title} — {artists}"
        file.write(line + "\n")

print("Track list written to playlist_tracks.txt")
