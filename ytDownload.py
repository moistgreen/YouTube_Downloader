from pytube import YouTube, Playlist
from sys import argv
import os
import sys

# Creates config file if one doesn't exist
path = os.getcwd()
pathConfig = path + "\config.txt"
if not(os.path.exists(pathConfig)):
    print("Creating config.txt...")
    f = open("config.txt", "wt")
    f.write("path=" + str(path))
    f.close()
    print("Done.")

# Gets user input for parameters
error = True
while error == True:
    choice = input("\n(P)laylist, (S)ingle video, (H)elp: ")
    if choice.lower() != "p" and choice.lower() != "s" and choice.lower() != "h":
        print("Make sure to enter a character within the parameters!")
        error = True
    else:
        error = False

if choice.lower() != "h":
    path = input("Download Path: ")
    url = input("URL: ")
    print("")

# Set path to config default if none is specified
if path == "":
    f = open("config.txt", "rt")
    path = f.readline()
    path = path.replace("path=", "")
    f.close()

# Downloads a playlist
if choice.lower() == "p":
    pl = Playlist(url)  
    links = pl.video_urls
    
    try:
        playlistTitle = pl.title
        path = path + "\\" + playlistTitle
        print("PLAYLIST")
        os.mkdir(path)

         # download videos to path
        for link in links:
            yt = YouTube(link)
            yd = yt.streams.get_highest_resolution()
            title = yt.title
            print("Downloading ~ " + str(title))
            yd.download(path)
            print("Finished download @ " + path + "\n")
    except:
        print("ERROR: Make sure your URL/Path are correct. See help page for more info.\n")
        sys.exit

# Downloads a single video
elif choice.lower() == "s":
    try:
        yt = YouTube(url)
        yd = yt.streams.get_highest_resolution()
        title = yt.title

        # download video to path
        print("Downloading ~ " + str(title))
        yd.download(path)
        print("Finished download @ " + path + "\n")
    except:
        print("ERROR: Make sure your URL/Path are correct. See help page for more info.\n")
        sys.exit

# Help page
if choice.lower() == "h":
    print("\n--Help page--\n"
          "Choose mode:\n"
            "\t\"P\" = Download all videos in a playlist\n"
            "\t\"S\" = Download a singular video\n"
            "\t\"H\" = Opens this page\n\n"
          "Downloading:\n"
            "\tPath = a valid directory path for your downloads. If left blank it will use the path in the config.txt file.\n"
            "\tURL = (Playlist) the URL of the PLAYLIST you wanna download. (Singular) the URL of the video you wanna download.\n")