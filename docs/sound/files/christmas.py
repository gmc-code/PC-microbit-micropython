'''
Press A to get a new song; it loops by default.
Touch the logo to stop a song.
Press B to play all; press again to stop when a song finishes.
based on https://www.christmasmusicsongs.com
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

o_come_o_come_emmanuel = [
    'A4:4',
    'C5:4','E5:4','E5:4','E5:4',
    'D5:4','F5:4','E5:4','D5:4',
    'C5:12','D5:4',
    
    'E5:4','C5:4','A4:4','C5:4',
    'D5:4','B4:4','A4:4','G4:4',
    'A4:12','D5:4',
    
    'D5:4','A4:4','A4:4','B4:4',
    'C5:8','B4:4','A4:4',
    'G4:12','C5:4', 
    
    'D5:4','E5:4','E5:4','E5:4',
    'D5:4','F5:4','E5:4','D5:4',
    'C5:12','G5:4',
        
    'G5:12','E5:4', 
    'E5:12','E5:4',
    'D5:4','F5:4','E5:4','D5:4',
    
    'C5:12','D5:4',
    'E5:4','C5:4','A4:4','C5:4',
    'D5:4','B4:4','A4:4','G4:4',
    'A4:28' 
]

good_king_wenceslas = [
    'C5:4','C5:4','C5:4','D5:4',
    'C5:4','C5:4','G4:8',
    'A4:4','G4:4','A4:4','B4:4',
    'C5:8','C5:8',

    'C5:4','C5:4','C5:4','D5:4',
    'C5:4','C5:4','G4:8',
    'A4:4','G4:4','A4:4','B4:4',
    'C5:8','C5:8',

    'G5:4','F5:4','E5:4','D5:4',
    'E5:4','D5:4','C5:8',
    'A4:4','G4:4','A4:4','B4:4',
    'C5:8','C5:8',

    'G4:4','G4:4','A4:4','B4:4',
    'C5:4','C5:4','D5:8',
    'G5:4','F5:4','E5:4','D5:4',
    'C5:8','F5:8','C5:16'
]

away_in_a_manger = [
    'G4:4',
    'G4:6','F4:2','E4:4',
    'E4:4','D4:4','C4:4',
    'C4:4','B3:4','A3:4',
    'G3:8','G3:4',
    
    'G3:6','A3:2','G3:4',
    'G3:4','D4:4','B3:4',
    'A3:4','G3:4','C4:4',
    'E4:8','G4:4',

    'G4:6','F4:2','E4:4',
    'E4:4','D4:4','C4:4',
    'C4:4','B3:4','A3:4',
    'G3:8','G3:4',
    
    'F4:6','E4:2','D4:4',
    'E4:4','D4:4','C4:4',
    'D4:4','A3:4','B3:4',
    'C4:16',
]

ding_dong_merrily_on_high = [
    'G4:4','G4:4','A4:2','G4:2','F#4:2','E4:2',
    'D4:12','D4:4',
    'E4:4','G4:4','G4:4','F#4:4',
    'G4:8','G4:8',

    'G4:4','G4:4','A4:2','G4:2','F#4:2','E4:2',
    'D4:12','D4:4',
    'E4:4','G4:4','G4:4','F#4:4',
    'G4:8','G4:8',

    'D5:6','C5:2','B4:2','C5:2','D5:2','B4:2',
    'C5:6','B4:2','A4:2','B4:2','C5:2','A4:2',
    'B4:6','A4:2','G4:2','A4:2','B4:2','G4:2',
    'A4:6','G4:2','F#4:2','G4:2','A4:2','F#4:2',
 
    'G4:6','F#4:2','E4:2','F#4:2','G4:2','E4:2',
    'F#4:6','E4:2','D:4','D:4',
    'E4:4','G4:4','G4:4','F#4:4',
    'G4:8','G:8'
]

# Create a dictionary with the BPM and notes for each song
songs_dict = {
    'good_king_wenceslas': {'bpm': 140, 'notes': good_king_wenceslas},   
    'away_in_a_manger': {'bpm': 120, 'notes': away_in_a_manger},
    'ding_dong_merrily_on_high': {'bpm': 160, 'notes': ding_dong_merrily_on_high},
    'o_come_o_come_emmanuel': {'bpm': 140, 'notes': o_come_o_come_emmanuel},   
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

def do_tune(current_song_index, play_loop=True, play_wait=False):
    sleep(200)
    song_name = songs[current_song_index]
    song = songs_dict[song_name]
    # Set the tempo
    music.set_tempo(ticks=4, bpm=song['bpm'])
    # Play the current song
    display.scroll(song_name.upper().replace("_", " "), delay=60, loop=play_loop, wait=False)
    music.play(song['notes'], loop=play_loop, wait=play_wait)
    
while True:
    if button_a.was_pressed():
        # Move to the next song
        current_song_index = advance_song_counter(current_song_index)
        music.stop()
        # loop the current song
        do_tune(current_song_index, play_loop=True, play_wait=False)
    elif button_b.was_pressed():
        # Stop any currently playing song
        while True:
            # Move to the next song
            current_song_index = advance_song_counter(current_song_index)
            music.stop()
            # play the current song
            do_tune(current_song_index, play_loop=False, play_wait=True)
            if button_b.was_pressed():
                break
    elif pin_logo.is_touched():
        # Stop any currently playing song from A button pressing
        music.stop()
    sleep(10)


