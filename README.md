# YT-videos-to-MP3-downloader

# Songs Download and Conversion Tool

This Python project allows you to download audio from YouTube videos, convert it to MP3 format, and organize it in a specified folder. It uses `yt-dlp` for downloading and `moviepy` for audio conversion.

## Features
- Download the best quality audio from YouTube videos.
- Convert `.webm` audio files to `.mp3` format.
- Automatically saves the converted MP3 files with custom names in a designated folder.

## Folder Structure
```
SONGS DOWNLOAD
            ├── pycache
            ├── mp3_folder/ # Folder where converted MP3 files are saved
            ├── venv/ # Python virtual environment (optional)
            ├── .gitignore
            ├── main.py # Main script to download and convert songs
            ├── mp3_convertor.py # Script for audio conversion
            ├── requirements.txt # Python dependencies
            ├── song_list.py # List of songs to download
```

## Prerequisites
- Python 3.7 or higher
- Virtual environment (optional but recommended)

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/songs-download.git
   cd songs-download

2. Set up a virtual environment (optional but recommended):

```
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required Python packages:

```pip install -r requirements.txt```

## How to Use
1. Add YouTube URLs and desired MP3 file names to the song_list.py file in the following format:

```
song_list = [
    ('<YouTube URL>', '<Song Name>.mp3'),
]
```

2. Run the main.py script:

```
python main.py
```

3. The converted MP3 files will be saved in the mp3_folder/ directory.

## Dependencies
The following Python libraries are used in this project:

yt-dlp: For downloading YouTube videos.
moviepy: For audio conversion.
To install these dependencies, run:
```
pip install -r requirements.txt
```

## Notes
Ensure the mp3_folder/ directory exists before running the script. You can create it manually:
```
mkdir mp3_folder
```
Temporary .webm files are deleted after conversion.


## Acknowledgements
Inspired by the simplicity of yt-dlp and the versatility of moviepy.

