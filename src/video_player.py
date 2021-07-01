"""A video player class."""
import random

from .video_library import VideoLibrary

currentVideo = ""
currentVideoString = ""
pause = False
listOfPlaylists = []
videoLibrary = self._video_library.get_all_videos()

class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.totalPlaylists = {}
        self.userPlaylists = {}

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        videoList = []
        for video in self._video_library.get_all_videos():
            string1 = video._title + " ("
            string2 = video._video_id + ") "
            string3 = str(list(video._tags))
            removeChar = "',"
            for char in removeChar:
                string3 = string3.replace(char, "")
            masterString = string1 + string2 + string3
            videoList.append(masterString)

        print("Here's a list of all available videos: ")
        for item in sorted(videoList):
            print(item)

    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        global currentVideo
        global currentVideoString
        global playVideo
        if currentVideo == "":
            playVideo = self._video_library.get_video(video_id)
            if playVideo is not None:
                currentVideo = str(playVideo.title)
                print("Playing video: " + str(playVideo.title))

                # Stores which video is currently playing for later use in show_playing
                tagString = str(list(playVideo.tags))
                removeChar = "',"
                for char in removeChar:
                    tagString = tagString.replace(char, "")
                currentVideoString = currentVideo + " (" + playVideo.video_id + ") " + str(tagString)
            else:
                print("Cannot play video: Video does not exist")
        else:
            newPlayVideo = self._video_library.get_video(video_id)
            if newPlayVideo is not None:
                print("Stopping video: " + currentVideo)
                print("Playing video: " + str(newPlayVideo.title))
                currentVideo = str(newPlayVideo._title)

                # Stores which video is currently playing for later use in show_playing
                tagString = str(list(playVideo.tags))
                removeChar = "',"
                for char in removeChar:
                    tagString = tagString.replace(char, "")
                currentVideoString = currentVideo + " (" + newPlayVideo.video_id + ") " + str(tagString)
            else:
                print("Cannot play video: Video does not exist")

    def stop_video(self):
        """Stops the current video."""

        global currentVideo
        if currentVideo != "":
            print("Stopping video: " + currentVideo)
            currentVideo = ""
        else:
            print("Cannot stop video: No video is currently playing")


    def play_random_video(self):
        """Plays a random video from the video library."""
        listOfVideoIds = ["funny_dogs_video_id", "amazing_cats_video_id", "another_cat_video_id", "life_at_google_video_id", "nothing_video_id"]
        randInt = random.randint(0, 4)
        randomVideoId = listOfVideoIds[randInt]

        self.play_video(randomVideoId)


    def pause_video(self):
        """Pauses the current video."""
        global currentVideo
        global pause
        if pause is False and currentVideo != "":
            print("Pausing video: " + currentVideo)
            pause = True
        elif pause is True and currentVideo != "":
            print("Video already paused: " + currentVideo)
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        """Resumes playing the current video."""
        global currentVideo
        global pause
        if pause is True:
            print("Continuing video: " + currentVideo)
            pause = False
        else:
            if currentVideo != "":
                print("Cannot continue video: Video is not paused")
            else:
                print("Cannot continue video: No video is currently playing")


    def show_playing(self):
        """Displays video currently playing."""
        global currentVideoString
        if pause is False and currentVideo != "":
            print("Currently playing: " + currentVideoString)
        elif pause is True and currentVideo != "":
            print("Currently playing: " + currentVideoString + " - PAUSED")
        else:
            print("No video is currently playing")

    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        for char in playlist_name:
            if char == " ":
                playlist_name = playlist_name.replace(char, "")

        playlistName = playlist_name.lower()
        if playlistName not in self.totalPlaylists:
            self.totalPlaylists[playlistName] = []
            self.userPlaylists[playlistName] = playlist_name
            print("Successfully created new playlist: ", self.userPlaylists)
        else:
            print("Cannot create playlist: A playlist with the same name already exists")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        edited = playlist_name.lower()
        if edited in self.userPlaylists.keys():
            if self._video_library.get_video(video_id) is not None and self._video_library.get_video(video_id) in self.totalPlaylists:
                print("Cannot add video to " + playlist_name + ": Video already added")
            elif self._video_library.get_video(video_id) is not None and not self._video_library.get_video(video_id) in self.totalPlaylists:
                print("Added video to " + playlist_name + ": ", self._video_library.get_video(video_id).title)
            else:
                print("Cannot add video to " + playlist_name + ": Video does not exist")
        else:
            print("Cannot add video to " + playlist_name + ": Playlist does not exist")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        global videoLibrary
        searchResults = []
        searched = search_term.lower()
        for item in videoLibrary:
            if searched in item._title.lower():
                for char in item:
                    if char == "'" or char ==",":
                        item = item.replace(char, "")
                searchResults.append(item)
        if len(searchResults) > 0:
                print("Here are the results for " + search_term + ": ")
        num = 1
        for item in searchResults:
            print(" " + str(num) + ") ", item)
        print("Would you like to play any of the above? If yes, specify the number of the video.")
        print("If your answer is not a valid number, we will assume it's a no.")

        userInput = input()
        global flag
        flag = False
        numbers = "1234567890"
        for char in userInput:
            if char not in numbers:
                flag = False
                break
            else:
                flag = True
        # if flag is True and int(userInput) > 0 and int(userInput) <= len(searchResults):
        #     self.play_video(searchResults[int(userInput) - 1]._video_id)
        else:
            print("No search results for " + search_term)

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
