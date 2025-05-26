import asyncio
import os
from pathlib import Path

from colorama import Fore, init
from pytubefix import YouTube

init()

download_dir = Path(os.getenv("DOWNLOAD_PATH", "downloads"))
download_dir.mkdir(exist_ok=True)


async def service_video(url: str):
    try:
        ask_video = input("You want install video? (y/n): ")
        if ask_video.lower() == "y":
            print(f"{Fore.MAGENTA}[VIDEO]{Fore.RESET} YES")
            await download_video(url)
        else:
            print(f"{Fore.MAGENTA}[VIDEO]{Fore.RESET} NO")
        ask_audio = input("\nYou want install audio? (y/n): ")
        if ask_audio.lower() == "y":
            print(f"{Fore.MAGENTA}[AUDIO]{Fore.RESET} YES")
            await download_audio(url)
        else:
            print(f"{Fore.MAGENTA}[AUDIO]{Fore.RESET} NO")


    except Exception as e:
        print(e)


async def download_audio(url):
    try:
        yt_link = YouTube(url)
        yt_link.streams.get_audio_only().download(str(download_dir), filename_prefix="[AUDIO]")
        print(f"{Fore.GREEN}[SUCCESS]{Fore.RESET} Audio from {yt_link.title} downloaded")
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Fore.RESET} {e}")


async def download_video(url, progressive: bool = True):
    try:
        yt_link = YouTube(url)
        resolution = yt_link.streams.get_highest_resolution(progressive=False).resolution
        resolution = str(resolution)
        res_list = ["1440p", "2160p", "4320p"]
        warning_resolution = False

        for i in res_list:

            if resolution == i:
                warning_resolution = True
                print(f"{Fore.MAGENTA}[VIDEO]{Fore.RESET} Video have more than 1080p")
                ask_resolution = input("Your video have resolution more than 1080p "
                                       "can we download this video with highest resolution? (y/n): ")
                if ask_resolution.lower() == "y":
                    print(f"{Fore.MAGENTA}[VIDEO]{Fore.RESET} YES, >> WITH HIGHEST RESOLUTION")
                    progressive = False

        if not warning_resolution:
            print(f"{Fore.MAGENTA}[VIDEO]{Fore.RESET} Video dont have more than 1080p")
        print(f"{Fore.MAGENTA}[VIDEO]{Fore.RESET} YES, >> WITHOUT HIGHEST RESOLUTION")
        yt_link.streams.get_highest_resolution(progressive=progressive).download(str(download_dir),
                                                                                 filename_prefix="[VIDEO]")
        res_result = yt_link.streams.get_highest_resolution(progressive=progressive).resolution
        print(f"{Fore.GREEN}[SUCCESS]{Fore.RESET} Video {yt_link.title} downloaded with {res_result}")

    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Fore.RESET} {e}")


async def main():
    while True:
        try:
            url = input("Link on your video (or back / exit): ")
            if url.lower() == "back":
                await start_page()
            elif url.lower() == "exit":
                break
            await service_video(url)
        except Exception as e:
            print(e)


async def start_page():
    while True:
        try:
            url = input("Select some from this list:\n"
                        "1: Start\n"
                        "")
            if url.lower() == "1":
                await main()
            elif url.lower() == "exit":
                break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        asyncio.run(start_page())
    except KeyboardInterrupt:
        pass
