import os
from pytubefix import YouTube
from utils.warnings import *
from pathlib import Path

download_dir = Path(os.getenv("DOWNLOAD_PATH", "downloads"))
#create directory
download_dir.mkdir(exist_ok=True)

class ServiceVideo:
    def __init__(self, url):
        self.url = url

    async def service_video(self):
        try:
            # a short dialogue with the user
            ask_video = input("You want install video? (y/n): ")
            if ask_video.lower() == "y":
                await video_message("USER CONFIRM")
                await self.download_video()
            else:
                await video_message("USER DECLINED")

            ask_audio = input("\nYou want install audio? (y/n): ")
            if ask_audio.lower() == "y":
                await audio_message("USER CONFIRM")
                await self.download_audio()
            else:
                await audio_message("USER DECLINED")


        except Exception as e:
            await error(e)

    async def download_video(self, progressive: bool = True):
        try:
            yt_link = YouTube(self.url)
            resolution = yt_link.streams.get_highest_resolution(progressive=False).resolution
            resolution = str(resolution)
            res_list = ["1440p", "2160p", "4320p"] #I take all possible YouTube qualities above 1080p.
            warning_resolution = False

            for i in res_list:
                # Comparison of whether the video has any of those qualities
                if resolution == i:
                    warning_resolution = True
                    await info("Video have resolution more than 1080p")
                    ask_resolution = input("Your video have resolution more than 1080p "
                                           "can we download this video with highest resolution? (y/n): ")
                    if ask_resolution.lower() == "y":
                        await video_message("DOWNLOADING, >> WITH HIGHEST RESOLUTION")
                        progressive = False
                    else:
                        await video_message("DOWNLOADING, >> WITHOUT HIGHEST RESOLUTION")
            if not warning_resolution:
                await info("Video have resolution not more than 1080p")
            # Download
            yt_link.streams.get_highest_resolution(progressive=progressive).download(str(download_dir),
                                                                                     filename_prefix="[VIDEO]")
            # I take the video quality with progressive condition for the final output of the result.
            res_result = yt_link.streams.get_highest_resolution(progressive=progressive).resolution
            await video_message_successful(yt_link, res_result)

        except Exception as e:
            await error(e)


    async def download_audio(self):
        try:
            yt_link = YouTube(self.url)
            yt_link.streams.get_audio_only().download(str(download_dir), filename_prefix="[AUDIO]")
            await audio_message_successful(yt_link)
        except Exception as e:
            await error(e)