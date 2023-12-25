'''
Press A to get a new song. Press B to stop. Touch the logo to replay a song.
'''
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

we_wish_you_a_merry_christmas = [
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

god_rest_ye_merry_gentlemen = [
    'E4:4',
    'E4:4','B4:4','B4:4','A4:4',
    'G4:4','F#4:4','E4:4','D4:4',
    'E4:4','F#4:4','G4:4','A4:4',
    'B4:12','E4:4',

    'E4:4','B4:4','B4:4','A4:4',
    'G4:4','F#4:4','E4:4','D4:4',
    'E4:4','F#4:4','G4:4','A4:4',
    'B4:12','B4:4',

    'C5:4','A4:4','B4:4','C5:4',
    'D5:4','E5:4','B4:4','A4:4',
    'G4:4','E4:4','F#4:4','G4:4',
    'A4:8','G4:4','A4:4',

    'B4:8','C5:4','B4:4',
    'B4:4','A4:4','G4:4','F#4:4',
    'E4:8','G4:2','F#4:2','E4:4',
    'A4:8','G4:4','A4:4',
    
    'B4:4','C5:4','D5:4','E5:4',
    'B4:4','A4:4','G4:4','F#4:4',
    'E4:28',
]

# Create a dictionary with the BPM and notes for each song
songs_dict = {
     
    'jingle_bells': {'bpm': 180, 'notes': jingle_bells},
    'we_wish_you_a_merry_christmas': {'bpm': 140, 'notes': we_wish_you_a_merry_christmas},
    'silent_night': {'bpm': 100, 'notes': silent_night},
    'we_three_kings': {'bpm': 120, 'notes': we_three_kings},
    'god_rest_ye_merry_gentlemen': {'bpm': 180, 'notes': god_rest_ye_merry_gentlemen}
}

# Put the song names into a list
songs = list(songs_dict.keys())

def get_song_from_not_playing(songs, current_song):
    choices = [song for song in songs if song != current_song]
    return random.choice(choices)
    
# Function to shuffle a list
def shuffle_list(lst):
    for i in range(len(lst)-1, 0, -1):
        j = random.randint(0, i)
        lst[i], lst[j] = lst[j], lst[i]
    return lst
    
# Randomly sort the song list  
songs = shuffle_list(songs)

# Index to keep track of the current song
current_song_index = -1

def advance_song_counter(current_song_index):
    current_song_index = (current_song_index + 1) % len(songs)
    return current_song_index

def do_tune(current_song_index):
    sleep(200)
    song_name = songs[current_song_index]
    song = songs_dict[song_name]
    # Set the tempo
    music.set_tempo(ticks=4, bpm=song['bpm'])
    # Play the current song
    music.play(song['notes'], wait=False)
    display.scroll(song_name.upper(), delay=60, wait=False)
    
while True:
    if button_a.was_pressed():
        # Move to the next song
        current_song_index = advance_song_counter(current_song_index)
        music.stop()
        # Get the current song
        do_tune(current_song_index)
    elif button_b.was_pressed():
        # Stop any currently playing song
        music.stop()
    elif pin_logo.is_touched():
        # Stop any currently playing song
        music.stop()
        # again
        do_tune(current_song_index)
    sleep(10)


