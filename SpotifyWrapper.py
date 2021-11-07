import requests

class SpotifyConnection():
    def __init__(self, client_id, client_secret):
        # We need our program to request access to spotify
        AUTH_URL = 'https://accounts.spotify.com/api/token'  # Url that provides access
        AUTH_PARAM = {  # The parameters required to get access
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }
        auth_response = requests.post(AUTH_URL, AUTH_PARAM)  # Make the request
        auth_response_data = auth_response.json()  # Convert the response to json

        # Finally, now that we've requested it and formatted data, save the access token
        self.access_token = auth_response_data['access_token']

    def getPlaylist(self, link, items):
        # Get the ID for the playlist
        playlist_id = self.__getPlaylistID(link)

        endpoint = 'https://api.spotify.com/v1/playlists/'+playlist_id+'/tracks'
        headers = {
            'Authorization': 'Bearer {token}'.format(token=self.access_token),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }
        parameters = {
            "market": "ES",
            "fields": "items(track(href))",
            "limit": 50,
            "offset": 0
        }
        response = requests.get(endpoint, params=parameters, headers=headers).json()

        playlist = set()

        for track in response['items']:
            playlist.add(track['track']['href'])

        print(playlist)



    # Gets the playlist ID from the link
    def __getPlaylistID(self, link):
        parsed = link.split('/')  # Parse on /
        payload = parsed[-1]  # Parse out parameters
        playlist_id = payload.split('?')[0]  # Get the ID

        return playlist_id  # Return it
