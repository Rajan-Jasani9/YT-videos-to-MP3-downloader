from moviepy import AudioFileClip

# Function to convert webm to mp3
def convert_webm_to_mp3(webm_file, mp3_file):
    # Load the webm file
    audio = AudioFileClip(webm_file)
    
    # Write the audio to an mp3 file
    audio.write_audiofile(mp3_file, codec='mp3')
    print(f"Conversion complete: {mp3_file}")
