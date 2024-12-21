import yt_dlp
from song_list import song_list
from mp3_convertor import convert_webm_to_mp3
import os

ydl_opts = {
    'format': 'bestaudio/best', 
    'outtmpl': 'downloaded_audio.%(ext)s',
}


for song_url, song_name in song_list:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song_url])
        print('before')
        convert_webm_to_mp3('downloaded_audio.webm', f'mp3_folder\\{song_name}')
        os.remove('downloaded_audio.webm')