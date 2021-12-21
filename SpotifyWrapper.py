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

    # takes a playlist id and returns a set of the songs in the playlist
    def getPlaylistSongIds(self, link):

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
            "limit": 100,
            "offset": 0
        }

        # initialize set of songs
        playlistSongs = set()

        response = requests.get(endpoint, params=parameters, headers=headers).json()

        # add each song from given playlist to set
        for song in response['items']:
            playlistSongs.add(song["track"]["href"])

        while len(response['items']) == parameters['limit']:

            # add to the offset to get all the songs
            parameters['offset'] += parameters['limit']

            # get batch of songs with new offset
            response = requests.get(endpoint, params=parameters, headers=headers).json()

            # add each song from given playlist to set
            for song in response['items']:
                playlistSongs.add(song["track"]["href"])

        return playlistSongs

    # Gets the playlist ID from the link
    def __getPlaylistID(self, link):
        parsed = link.split('/')  # Parse on /
        payload = parsed[-1]  # Parse out parameters
        playlist_id = payload.split('?')[0]  # Get the ID

        return playlist_id  # Return it

    # gets the playlist ids of a given user
    def getUsersPlaylists(self, userId):
        parameters = {
            "fields": "items(href)",
            "limit": 20,
            "offset": 0
        }

        headers = {
            'Authorization': 'Bearer {token}'.format(token=self.access_token),
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        # set endpoint using user id
        endpoint = 'https://api.spotify.com/v1/users/' + userId + '/playlists'

        response = requests.get(endpoint, params=parameters, headers=headers).json()

        # a set of all the user's songs
        allUserPlaylists = set()

        for i in response['items']:
            allUserPlaylists.add(i['href'])

        while len(response['items']) == parameters['limit']:

            parameters['offset'] += parameters['limit']

            response = requests.get(endpoint, params=parameters, headers=headers).json()

            # add batch of playlists to all playlists
            for i in response['items']:
                allUserPlaylists.add(i['href'])

        return allUserPlaylists