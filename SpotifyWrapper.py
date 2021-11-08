import json

import requests


class SpotifyConnection:
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

    def getPlaylist(self, link):
        # Get the ID for the playlist
        playlist_id = self.__getPlaylistID(link)

        endpoint = 'https://api.spotify.com/v1/playlists/' + playlist_id + '/tracks'
        headers = {
            'Authorization': 'Bearer {token}'.format(token=self.access_token),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        playlist = set()
        fetched_total = 0
        fetched_cycle = 50

        while fetched_cycle == 50:
            parameters = {
                "market": "ES",
                "fields": "items(track(href))",
                "limit": 50,
                "offset": fetched_total
            }

            response = requests.get(endpoint, params=parameters, headers=headers).json()

            fetched_cycle = len(response['items'])
            fetched_total += fetched_cycle
            for track in response['items']:
                playlist.add(track['track']['href'])

        return playlist

    # returns true if string1 comes before string2 when sorted
    def stringLessThanString(self, string1, string2) -> bool:

        # string1 < string2
        if [string1, string2] == [string1, string2].sort():

            # string1 less than string2 is True
            return True

        # string1 > string2
        else:

            # string1 less than string2 is False
            return False

    # Gets the playlist ID from the link
    def __getPlaylistID(self, link):
        parsed = link.split('/')  # Parse on /
        payload = parsed[-1]  # Parse out parameters
        playlist_id = payload.split('?')[0]  # Get the ID

        return playlist_id  # Return it
