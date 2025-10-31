from setuptools import setup, find_packages

setup(
    name="yt_downloader",
    version="1.0.0",
    description="Async YouTube video/audio downloader with colorized output",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="pt3n4ik",
    author_email="ruslkliui@gmail.com",
    url="https://github.com/pt3n4ikRK/ytdownloader.git",
    packages=find_packages(),
    install_requires=[
        "pytubefix>=1.0.0",
        "colorama>=0.4.6",
        "asyncio>=3.4.3"
    ],
    entry_points={
        "console_scripts": [
            "yt-downloader=yt_downloader.main:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: WINDOWS",
    ],
    python_requires=">=3.7",
    keywords="youtube downloader async video audio",
)
