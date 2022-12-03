from pytube import YouTube, Playlist
from sys import argv
import os
import sys
import options

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
    choice = input("\nWhat are you downloading?\n(P)laylist, (S)ingle video, (H)elp: ")
    if choice.lower() != "p" and choice.lower() != "s" and choice.lower() != "h":
        print("Make sure to enter a character within the parameters!")
        error = True
    else:
        error = False

# Brings up user input
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

# Acts on user input
match choice.lower():

    # Downloads a playlist
    case "p":
        options.get_playlist(url, path)

    # Downloads a single video
    case "s":
        options.get_video(url, path)

    # Help page
    case "h":
        options.show_help()