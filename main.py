import moviepy.editor as mp
import os
import random

# Check logs for existing file
def log_check(fname):
    with open("log.txt", "r") as f:
        if fname in f.read():
            return True
        else:
            return False
        f.close()

# Cleanup
def cleanup(fname):
    os.remove("input/" + fname)

# Logging
def log(fname):
    with open("log.txt", "a") as f:
        f.write(fname + "\n")
        f.close()


files = os.listdir("input")

while len(files) != 0:
    choice = random.choice(files)
    while log_check(choice):
        cleanup(choice)
        choice = random.choice(files)
        
    clip = mp.AudioFileClip("input/" + choice)
    duration = clip.duration
    repeat = round(3600 / duration)

    new_clip = mp.concatenate_audioclips([clip] * repeat)
    new_clip.write_audiofile("output/" + choice)
    log(choice)
    cleanup(choice)
    files = os.listdir("input")
else:
    print("No more files to process")

