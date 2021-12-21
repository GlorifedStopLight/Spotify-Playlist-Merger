from SpotifyWrapper import *


# class used to create common playlists
class commonPlaylistCreator:

    def __init__(self):
        self.commonSongs = None
        self.playlists = []
        self.user = None
        self.userPassword = None
        self.sc = SpotifyConnection("83bc298d7d524091b2e3d1b410d4e62c", "baeb26ab559f408b9c1e96ad77a34966")

    # takes an array of playlists ids saves them to the instance of this object
    def selectPlaylistsToAdd(self, playlistNames):

        # each given playlist
        for playlistID in playlistNames:

            # save the songs in each playlist
            self.playlists.append(self.sc.getPlaylistSongIds(playlistID))

    # creates an empty playlist
    def makeNewEmptyPlaylist(self):
        pass

    # save the common songs that are in all given playlists (call AFTER selectPlaylistsToAdd)
    def getCommon(self):
        print(len(self.playlists[0]))
        print(len(self.playlists[1]))

        # at least 2 playlists given
        if len(self.playlists) >= 2:

            # get the songs that are shared by all given playlists
            self.commonSongs = self.playlists[0].intersection(*self.playlists[1:])

        return self.commonSongs


fun = commonPlaylistCreator()
fun.selectPlaylistsToAdd(["https://open.spotify.com/playlist/3WYyBELipwA9Yor7Mi2Yxn?si=16d3a1dbc872491a",
                          "https://open.spotify.com/playlist/7I8h4qLgJlMY9ULeV4tm9s?si=7f3017de8fda4df9"])

commonSongLinks = fun.getCommon()

fixedLinks = set("https://open.spotify.com/track/" + i.split("/")[-1] for i in commonSongLinks)

print(fixedLinks)
print(len(fixedLinks), "common songs")

# https://open.spotify.com/track/3Pj6u2KTgepyyidp5xfbHp?si=3cda388d55114143
# https://api.spotify.com/v1/tracks/3Pj6u2KTgepyyidp5xfbHp

# 3Pj6u2KTgepyyidp5xfbHp?si=3cda388d55114143
# 3Pj6u2KTgepyyidp5xfbHp
