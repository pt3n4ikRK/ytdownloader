# 🎬 Async YouTube Downloader

[![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Asynchronous video and audio downloader from YouTube with a colorful interface and interactive menu.

## ✨ Features

- ⚡ Asynchronous loading (does not block the system)
- 🎨 Color interface using Colorama
- 🎵 Separate audio download (mp3)
- 🎥 Separate video download (mp4, 8k)
- 📁 Automatic creation of a folder for downloads
- 🛠 Handling connection errors

## ⚠️ Restrictions
- Maximum video quality: 8k (4320p)
- If you want to download a video higher than 1080p, the program will ask for permission, otherwise the video will be downloaded in 360p quality.
- Support for public videos only (no age restrictions)
- A stable internet connection is required.


## ⚙️ Installation

1. Make sure you have Python 3.7+ installed:
```bash
python --version
```
2. Install the package if you want to use it in other projects:
```bash
pip install git+https://github.com/pt3n4ikRK/ytdownloader.git
```

3. If you have Python, run start.bat, which will install dependencies directly from requirements.txt.

## 🛠 For development:
````bash
git clone https://github.com/pt3n4ikRK/ytdownloader.git
cd ytdownloader
pip install -e .
````
