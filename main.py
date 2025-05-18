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


async def download_video(url):
    try:
        yt_link = YouTube(url)
        yt_link.streams.get_highest_resolution().download(str(download_dir), filename_prefix="[VIDEO]")
        print(f"{Fore.GREEN}[SUCCESS]{Fore.RESET} Video {yt_link.title} downloaded")
    except Exception as e:
        print(f"{Fore.RED}[ERROR]{Fore.RESET} {e}")


async def main():
    while True:
        try:
            url = input("Link on video (or exit): ")
            if url.lower() == "exit":
                break
            await service_video(url)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
