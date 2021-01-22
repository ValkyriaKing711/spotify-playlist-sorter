# spotify-playlist-sorter
Sorts Spotify playlists in my preferred order.

The script uses nightly [spotify.py](https://github.com/mental32/spotify.py). Install it with `pip install -U git+https://github.com/mental32/spotify.py#egg=spotify`.


### Usage
* Create a [Spotify application](https://developer.spotify.com/dashboard/).
*To avoid any issues, set your redirect URI to something you know doesn't work. `http://localhost` should be fine.*
* Open `credentials.py` and fill in the information it needs.
* Run the script.
* Open the link you're given and authorize the application if needed.
* Once you're redirected, copy the URL from your browser and paste it in the terminal.
* To obtain a playlist's URI, right click it in Spotify, hover over *Share* and choose *Copy Spotify URI*.

The script saves your Spotify refresh token in a file called `auth`. It's used to authorize your account on future runs, removing the need to go through the entire authorization flow every time.


### Local files
Spotify's API seems to be a bit dumb when it comes to local files in playlists. Once they fix things, I'll add support for local files. For now you'll just get a `400` response if your playlist has any local tracks in it.