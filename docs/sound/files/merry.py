from microbit import *
import music
import random

jingle_bells = [
    'E4:4', 'E4:4', 'E4:8',
    'E4:4', 'E4:4', 'E4:8',
    'E4:4', 'G4:4', 'C4:6', 'D4:2',
    'E4:12', 'R:4',
    'F4:4', 'F4:4', 'F4:6', 'F4:2',
    'F4:4', 'E4:4', 'E4:4', 'E4:2', 'E4:2',
    'E4:4', 'D4:4', 'D4:4', 'E4:4',
    'D4:8', 'G4:8',
    'E4:4', 'E4:4', 'E4:8',
    'E4:4', 'E4:4', 'E4:8',
    'E4:4', 'G4:4', 'C4:6', 'D4:2',
    'E4:12', 'R:4',
    'F4:4', 'F4:4', 'F4:6', 'F4:2',
    'F4:4', 'E4:4', 'E4:4', 'E4:2', 'E4:2',
    'G4:4', 'G4:4', 'F4:4', 'D4:4',
    'C4:16'
]

merry_christmas = [
    'R:4','R:4','D4:4',
    'G4:4','G4:2','A4:2','G4:2','F#4:2',
    'E4:4','E4:4','E4:4',
    'A4:4','A4:2','B4:2','A4:2','G4:2',
    'F#4:4','D4:4','D4:4',
    
    'B4:4','B4:2','C5:2','B4:2','A4:2',
    'G4:4','E4:4','D4:2','D4:2',
    'E4:4','A4:4','F#4:4',
    'G4:8','D4:4',
    'G4:4','G4:4','G4:4',
    
    'F#4:8','F#4:4',
    'G4:4','F#4:4','E4:4',
    'D4:8','A4:4',
    'B4:4','A4:4','G4:4',
    'D5:4','D4:4','D4:2','D4:2',
    'E4:4','A4:4','F#4:4',
    'G4:8',
    
    'D4:4',
    'G4:4','G4:2','A4:2','G4:2','F#4:2',
    'E4:4','E4:4','E4:4',
    'A4:4','A4:2','B4:2','A4:2','G4:2',
    'F#4:4','D4:4','D4:4',
    
    'B4:4','B4:2','C5:2','B4:2','A4:2',
    'G4:4','E4:4','D4:2','D4:2',
    'E4:4','A4:4','F#4:4',
    'G4:8','R:4'
]

silent_night = [
    'G4:6','A4:4','G4:4','E4:12',
    'G4:6','A4:4','G4:4','E4:12',
    'D5:8','D5:4','B4:12',
    'C5:8','C5:4','G4:12',

    'A4:8','A4:4','C5:6','B4:2','A4:4',
    'G4:6','A4:4','G4:4','E4:12',

    'A4:8','A4:4','C5:6','B4:2','A4:4',
    'G4:6','A4:4','G4:4','E4:12',

    'D5:8','D5:4','F5:5','D5:2','B4:4',
    'C5:12','E5:12',
    'C5:6','G4:2','E4:4','G4:6','F4:2','D4:4',
    'C4:16','R:4','R:4'
]

we_three_kings = [
    'E4:4','D4:2','C4:4','A3:2',
    'B3:2','C4:2','C4:2','A3:6',
    'E4:4','D4:2','C4:4','A3:2',
    'B3:2','C4:2','C4:2','A3:6',

    'C4:4','C4:2','D4:4','D4:2',
    'E4:4','E4:2','G4:2','F4:2','E4:2',
    'D4:2','E4:2','D4:2','C4:4','B3:2',
    'A3:6','B3:4','D4:2',

    'C4:4','C4:2','C4:4','G3:2',
    'C4:4','A3:2','C4:6',
    'C4:4','C4:2','C4:4','G3:2',
    'C4:4','A3:2','C4:6',

    'C4:4','C4:2','D4:4','E4:2',
    'F4:4','E4:2','D4:4','E4:2',
    'C4:4','C4:2','C4:4','G3:2',
    'C4:4','A3:2','C4:6',
]

# Put the songs into a list
songs = [jingle_bells, merry_christmas, silent_night, we_three_kings]
song = random.choice(songs)
while True:
    if button_a.was_pressed():
        music.set_tempo(ticks=4, bpm=120)
        # Stop any currently playing song
        music.stop()
        # Choose a random song from the list
        song = random.choice(songs)
        # Play the chosen song
        music.play(song, wait=False)
    elif button_b.was_pressed():
        # Stop any currently playing song
        music.stop()
    elif pin_logo.is_touched():
        # Stop any currently playing song
        music.stop()
        # Set the tempo to twice the speed
        music.set_tempo(ticks=4, bpm=180)
        # Choose a random song from the list
        if not song:
            song = random.choice(songs)
        # Play the chosen song
        music.play(song, wait=False)
    sleep(1000)


