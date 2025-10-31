from colorama import Fore, init

init()


async def video_message(message):
    print(f"{Fore.MAGENTA}[VIDEO]{Fore.RESET} {message}")


async def video_message_successful(yt_link):
    print(f"{Fore.GREEN}[SUCCESS]{Fore.RESET} Video \"{yt_link.title}\" downloaded")


async def info(message):
    print(f"{Fore.LIGHTYELLOW_EX}[INFO]{Fore.RESET} {message}")


async def audio_message(message):
    print(f"{Fore.MAGENTA}[AUDIO]{Fore.RESET} {message}")


async def audio_message_successful(yt_link):
    print(f"{Fore.GREEN}[SUCCESS]{Fore.RESET} Audio \"{yt_link.title}\" downloaded")


async def error(message):
    print(f"{Fore.RED}[ERROR]{Fore.RESET} {message}")
