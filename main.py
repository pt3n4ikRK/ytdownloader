import asyncio
from utils.downloader import ServiceVideo

async def main():
    while True:
        try:
            url = input("Link on your video (or back / exit): ")
            if url.lower() == "back":
                await start_page()
            elif url.lower() == "exit":
                break
            await ServiceVideo(url).service_video()
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
