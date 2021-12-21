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

        # at least 2 playlists given
        if len(self.playlists) >= 2:

            # get the songs that are shared by all given playlists
            self.commonSongs = self.playlists[0].intersection(*self.playlists[1:])

        return self.commonSongs

    # returns a set of every song that a given user put in any of their playlists
    def getAllUsersSongs(self, userName):

        # get all their playlists
        allPlaylists = self.sc.getUsersPlaylists(userName)

        # get all songs in each playlist
        songsForEachPlaylist = [self.sc.getPlaylistSongIds(i) for i in allPlaylists]

        if len(songsForEachPlaylist) >= 2:

            return songsForEachPlaylist[0].union(*songsForEachPlaylist[1:])


fun = commonPlaylistCreator()
fun.selectPlaylistsToAdd(["https://open.spotify.com/playlist/3WYyBELipwA9Yor7Mi2Yxn?si=16d3a1dbc872491a",
                          "https://open.spotify.com/playlist/7I8h4qLgJlMY9ULeV4tm9s?si=7f3017de8fda4df9"])


jacobSsSongs = fun.getAllUsersSongs("22dy6fh47auzribtpln7bbtey")
calebsSongs = fun.getAllUsersSongs("calebyouknowwho")
mySongs = fun.getAllUsersSongs("863inomibrih149ibc1kr1hgi")
katSongs = fun.getAllUsersSongs("katythenerd1")

#print("caleb has ", len(calebsSongs), " songs")

#print("jacob has ", len(jacobSsSongs), " songs")

print("Mark has ", len(mySongs), " songs")

print("Kat has ", len(katSongs), " songs")

fun.playlists = [mySongs, katSongs]
theSongsWeHaveInCommon = fun.getCommon()

print("we have ", len(theSongsWeHaveInCommon), " songs in common")

