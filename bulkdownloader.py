import os
import pytube
from moviepy.editor import *
import random

# Check logs for existing file

# Import links from links.txt
links = []
for line in open("links.txt", "r").readlines():
    links.append(line.strip())
while len(links) != 0:
    yt_link = random.choice(links)
    yt = pytube.YouTube(yt_link)

    audio_stream = yt.streams.filter(only_audio=True).first()
    downloads_dir = os.path.join("input")
    temp_file = audio_stream.download(output_path=downloads_dir + "/temp", filename="temp")

    audio_clip = AudioFileClip(temp_file)
    folder_dir = os.path.join("input")
    title = yt.title
    audio_clip.write_audiofile(os.path.join(folder_dir, title + ".mp3"))
    os.remove(temp_file)
    os.removedirs(os.path.dirname(temp_file))
    links.remove(yt_link)
else:
    print("No more links to process")
    
# Cleanup
# Clean the links.txt
open("links.txt", "w").close()