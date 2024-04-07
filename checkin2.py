import pygame
import os
import sys
import subprocess
from tempfile import gettempdir
from boto3 import Session
from botocore.exceptions import BotoCoreError, ClientError
from contextlib import closing

# Set the working directory to the script's directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialize pygame mixer
pygame.init()
pygame.mixer.init()

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

    
