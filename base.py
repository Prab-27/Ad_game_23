# adventure_game.py


import pygame
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing
import os
import sys
import subprocess
from tempfile import gettempdir

print("Current working directory:", os.getcwd())

import os
current_directory = os.getcwd()
print("Current working directory:", current_directory)


# Create a client using the credentials and region defined in your AWS credentials file
session = Session(profile_name="default")
polly = session.client("polly")

try:
    # Request speech synthesis
    response = polly.synthesize_speech(
        Text="Hello world!",
        OutputFormat="mp3",
        VoiceId="Joanna"
    )
except (BotoCoreError, ClientError) as error:
    # The service returned an error, exit gracefully
    print(error)
    sys.exit(-1)

# Access the audio stream from the response
if "AudioStream" in response:
    # Use contextlib.closing to ensure the stream is closed properly
    with closing(response["AudioStream"]) as stream:
        output = os.path.join(gettempdir(), "speech.mp3")
        try:
            # Write the audio stream to a local file
            with open(output, "wb") as file:
                file.write(stream.read())
        except IOError as error:
            # Could not write to file, exit gracefully
            print(error)
            sys.exit(-1)
else:
    # The response didn't contain audio data, exit gracefully
    print("Could not stream audio")
    sys.exit(-1)

# Play the audio using the platform's default player
if sys.platform == "win32":
    os.startfile(output)
else:
    # Works on macOS and Linux (Darwin = macOS, xdg-open = Linux)
    opener = "open" if sys.platform == "darwin" else "xdg-open"
    subprocess.call([opener, output])



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




def intro_scene():
    print("Welcome to the Adventure Game!")
    print("You find yourself in a mysterious room.")
    print("Choose your next move: [north, south, east, west]")

def explore_room(direction):
    if direction == "north":
        print("You discover a treasure chest!")
    elif direction == "south":
        print("You encounter a ferocious dragon!")
    elif direction == "east":
        print("You find a hidden passage.")
    elif direction == "west":
        print("You see a locked door.")
    else:
        print("Invalid direction. Try again.")

if __name__ == "__main__":
    intro_scene()
    user_input = input("Enter a direction: ")
    explore_room(user_input) 