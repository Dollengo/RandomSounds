from randomstrings import generate_and_shuffle_strings
import pygame as pg

pg.mixer.init()

from gtts import gTTS
random_string = generate_and_shuffle_strings()
tts = gTTS(text=random_string, lang='pt-BR')
filename = f"{random_string}.mp3"
tts.save(filename)
pg.mixer.music.load(filename)
pg.mixer.music.play()
print(f"Phrase: {random_string}.")
while pg.mixer.music.get_busy() == True:
    continue
