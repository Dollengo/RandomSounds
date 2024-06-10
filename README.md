# Random String Generator and Player

- This Python script generates a random string, converts it to speech, and plays the speech as audio. It uses the `randomstrings` module to generate the random string, the `gTTS` (Google Text-to-Speech) library to convert the string to speech, and the `pygame` library to play the audio.

## Code Explanation

- The script begins by importing the necessary modules:

`
from randomstrings import generate_and_shuffle_strings
import pygame as pg
from gtts import gTTS`

### The pygame mixer is then initialized with `pg.mixer.init()`

### Next, the script generates a random string by calling the generate_and_shuffle_strings function from the randomstrings module. This function generates a list of 10 random strings, each of length 10, concatenates all the strings in the list twice to form a single string, and then randomly shuffles all the characters in the single string.

- The random string is then converted to speech using the gTTS library, which is an interface to Google’s Text to Speech API. - The speech is saved as an mp3 file.
`
random_string = generate_and_shuffle_strings()
tts = gTTS(text=random_string, lang='en')
filename = f"{random_string}.mp3"
tts.save(filename)`
- More information in frequently asked questions.
Finally, the script loads the mp3 file into the pygame mixer and plays it. It continues to play the audio as long as the mixer is busy.
`
pg.mixer.music.load(filename)
pg.mixer.music.play()
while pg.mixer.music.get_busy() == True:
    continue`
  
### And that’s it! This script generates a random string, converts it to speech, and plays the speech as audio.
