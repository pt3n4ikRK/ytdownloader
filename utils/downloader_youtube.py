import asyncio
import os
from pathlib import Path
import time

from pytubefix import YouTube

from utils.warnings import *

download_dir = Path(os.getenv("DOWNLOAD_PATH", "downloads"))
# create directory
download_dir.mkdir(exist_ok=True)


class ServiceVideo:
    def __init__(self, url, resolution):
        self.url = url
        self.resolution = resolution

    async def service_video(self):
        confirm_video = False
        confirm_audio = False
        try:
            # a short dialogue with the user
            ask_video = input("You want install video? (y/n): ")
            if ask_video.lower() == "y":
                await video_message("USER CONFIRM")
                confirm_video = True
            else:
                await video_message("USER DECLINED")

            ask_audio = input("\nYou want install audio? (y/n): ")
            if ask_audio.lower() == "y":
                await audio_message("USER CONFIRM")
                confirm_audio = True
            else:
                await audio_message("USER DECLINED")

            print(f"started at {time.strftime('%X')}")

            # Wait until both tasks are completed (should take
            # around 2 seconds.)
            if confirm_video:
                await asyncio.create_task(self.download_video())

            if confirm_audio:
                await asyncio.create_task(self.download_audio())
            print(f"finished at {time.strftime('%X')}")

        except Exception as e:
            await error(e)

    async def download_video(self):
        try:
            yt_link = YouTube(self.url)

            # Download
            yt_link.streams.filter(resolution=self.resolution).first().download(str(download_dir), filename_prefix="[VIDEO] ")
            await video_message_successful(yt_link)

        except Exception as e:
            await error(e)

    async def download_audio(self):
        try:
            yt_link = YouTube(self.url)
            yt_link.streams.get_audio_only().download(str(download_dir), filename_prefix="[AUDIO]")
            await audio_message_successful(yt_link)
        except Exception as e:
            await error(e)
