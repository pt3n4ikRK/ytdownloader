import asyncio

from utils.downloader_youtube import ServiceVideo

based_resolution = "1080p"

async def youtube_service():
    while True:
        try:
            variant = input("1: Download video/audio\n"
                            "2: Settings\n"
                            f"Based Resolution: {based_resolution}\n"
                            "")
            if variant == "1":
                await youtube_download()
            elif variant == "2":
                await youtube_settings()
        except Exception as e:
            print(e)

async def youtube_download():
    while True:
        try:
            url = input("URL (or back): ")
            if url == "back":
                await youtube_settings()
            await ServiceVideo(url, based_resolution).service_video()
        except Exception as e:
            print(e)

async def youtube_settings():
    global based_resolution
    while True:
        try:
            resolution_request = input(f"Selected Resolution: {based_resolution}\n"
                                       "Which resolution need (144p, 240p, 360p, 480p, 720p, 1080p, etc): ")
            based_resolution = resolution_request
            if resolution_request.lower() == "back":
                await youtube_service()
            return based_resolution
        except Exception as e:
            print(e)


async def start_page():
    while True:
        try:
            url = input("Select service: \n"
                        "1: YouTube\n"
                        "")
            if url.lower() == "1":
                await youtube_service()
            elif url.lower() == "exit":
                break
        except Exception as e:
            print(e)


if __name__ == '__main__':
    try:
        asyncio.run(start_page())
    except Exception as e:
        print(e)
