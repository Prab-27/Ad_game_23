import pygame
import os
import sys
import subprocess
from tempfile import gettempdir

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

# Specify the full path to your MP3 file
mp3_file_path = "C:/Users/PRATIKSHA/ad_game/speech.mp3"  # Replace with the actual path

# Load the MP3 file
pygame.mixer.music.load(mp3_file_path)

# Play the audio
pygame.mixer.music.play()

# Wait for the music to finish
pygame.event.wait()

# Clean up
pygame.quit()

# Optionally, you can open the MP3 file using the platform's default player
if sys.platform == "win32":
    os.startfile(mp3_file_path)
else:
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, mp3_file_path])

