# 1-hour-mp3-creator
Basic python scripts for bulk downloading music from YouTube and processing them to 1 hour music

# How to install
First clone this repository to a new folder .

    git clone https://github.com/yasarkaancan/1-hour-mp3-creator.git

Install the python requirements from requirements.txt

    pip install -r requirements.txt

You're ready to create video's !
If you want to download video's and convert them to mp3, open links.txt and instert the video links line by line and run bulkdownloader.py by :

    python bulkdownloader.py

Or you can also transfer your mp3 files to input folder and continue from there.
Then run main.py so videos in input folder converts in to 60 minute video. ( be aware that after converting videos script will delete the input mp3 file for cleanup purposes.)

    python main.py
