from pytube import YouTube, Playlist
import os
import sys
import errno

# Downloads a playlist
def get_playlist(url, path):
    
    # Variables
    pl = Playlist(url)  
    links = pl.video_urls
    
    try:
        # User can create a path
        if not(os.path.exists(path)):
            c = input("Path not found. Create path? (y/n): ")
            if c.lower() == 'y':
                print(f"Creating path: {path}\n")
                os.mkdir(path)
            else:
                print("Exiting...")
                sys.exit()

        # download videos to path
        videoCount = 0
        for link in links:
            yt = YouTube(link)
            yd = yt.streams.get_highest_resolution()
            title = yt.title
            print("Downloading - " + str(title))
            yd.download(path)
            videoCount += 1
        print(f"Finished downloading {videoCount} video(s) to {path}\n")

    # ERROR File not found
    except FileNotFoundError as error: print("ERROR: Cannot find path named " + "\"" + error.filename + "\"")

    # ERROR Everything else
    except Exception as error: print("ERROR: Ensure your URL and path are correct. See help page for more info\n")

# Downloads a video
def get_video(url, path):

    try:
        # Variables
        yt = YouTube(url)
        yd = yt.streams.get_highest_resolution()
        title = yt.title

        # User can create a path
        if not(os.path.exists(path)):
            c = input("Path not found. Create path? (y/n): ")
            if c.lower() == 'y':
                print(f"Creating path: {path}\n")
                os.mkdir(path)
            else:
                print("Exiting...")
                sys.exit()

        # download video to path
        print("Downloading - " + str(title))
        yd.download(path)
        print("Finished download @ " + path + "\n")

    # ERROR File not found
    except FileNotFoundError as error: print("ERROR: Cannot find path named " + "\"" + error.filename + "\"")

    # ERROR Everything else
    except Exception as error: print("ERROR: Ensure your URL and path are correct. See help page for more info\n")

# Shows the help page
def show_help():
    print(f"\n{'Help Page':-^39}\n"
        "Choose mode:\n"
            "\t\"P\" = Download all videos in a playlist\n"
            "\t\"S\" = Download a singular video\n"
            "\t\"H\" = Opens this page\n\n"
        "Downloading:\n"
            "\tPath = a valid directory path for your downloads. If left blank it will use the path in the config.txt file.\n"
            "\tURL = (Playlist) the URL of the PLAYLIST you wanna download. (Singular) the URL of the VIDEO you wanna download.\n")