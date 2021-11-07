from SpotifyWrapper import *


# returns true if inputs are sorted
def stringLessThanString(string1, string2) -> bool:

    # string1 < string2
    if [string1, string2] == [string1, string2].sort():

        # string1 less than string2 is True
        return True

    # string1 > string2
    else:

        # string1 less than string2 is False
        return False


def getCommonSongs(playList1: dict, playList2: dict) -> list:

    # indexes of playlists
    index1, index2 = 0, 0

    # common songs
    common = []

    # loop through both until you reach the end of a playlist
    while index1 < len(playList1) and index2 < len(playList2):

        # found common song
        if playList1[index1] == playList2[index2]:

            # save song
            common.append(playList1[index1])

            # next elements
            index1 += 1
            index2 += 1

        # value of index1 is before value of index2
        elif stringLessThanString(playList1[index1], playList2[index2]):

            # next element
            index1 += 1

        # value of index1 is after value of index2
        else:

            # next element
            index2 += 1

    # return common songs from playlist1 and playlist2
    return common


testing = {0: "cat"}

print(testing[0])




