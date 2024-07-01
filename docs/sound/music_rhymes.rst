==========================
Music Nursery Rhymes
==========================

Row your boat
------------------

| The notes are below, but are not usable due to marking the duration of 1.34 for notes in a triplet. This is interpreted as 134 instead of 1.34.

.. code-block:: python
    
    '''incorrect code'''
    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=120)
    row_your_boat = ['c4:4', 'c:4', 'c:3', 'd:1', 'e:4',
                    'e:3', 'd:1', 'e:3', 'f:1', 'g:8',
                    'c5:1.34', 'c:1.34', 'c:1.34', 'g4:1.34', 'g:1.34', 'g:1.34',
                    'e:1.34', 'e:1.34', 'e:1.34', 'c:1.34', 'c:1.34', 'c:1.34',
                    'g:3', 'f:1', 'e:3', 'd:1', 'c:8']

    while True:
        music.play(row_your_boat)
        sleep(1000)


| The solution is to multiply all the durations by 3 and to adjust the ticks by multiplying by 3.

.. code-block:: python
    
    from microbit import *
    import music

    music.set_tempo(ticks=12, bpm=120)
    row_your_boat = ['c4:12', 'c:12', 'c:9', 'd:3', 'e:12', 
                    'e:9', 'd:3', 'e:9', 'f:3', 'g:24', 
                    'c5:4', 'c:4', 'c:4', 'g4:4', 'g:4', 'g:4', 
                    'e:4', 'e:4', 'e:4', 'c:4', 'c:4', 'c:4', 
                    'g:9', 'f:3', 'e:9', 'd:3', 'c:24']

    while True:
        music.play(row_your_boat)
        sleep(1000)

----

Nursery Rhyme tunes
---------------------

| Play the tunes and see if you can identify them.
| Use the A button to play a new song, and loop it. Use the Logo to stop it.
| Use the B button to play all the songs. Pressing the B button again will stop the playin at the end of the current song.

.. code-block:: python
    
    from microbit import *
    import music
    import random


    twinkle_twinkle = ['c4:4', 'c:4', 'g:4', 'g:4', 'a:4', 'a:4', 'g:8',
        'f:4', 'f:4', 'e:4', 'e:4', 'd:4', 'd:4', 'c:8', 'g:4', 'g:4',
        'f:4', 'f:4', 'e:4', 'e:4', 'd:8', 'g:4', 'g:4', 'f:4', 'f:4',
        'e:4', 'e:4', 'd:8', 'c:4', 'c:4', 'g:4', 'g:4', 'a:4', 'a:4',
        'g:8', 'f:4', 'f:4', 'e:4', 'e:4', 'd:4', 'd:4', 'c:8'
    ]
    baa_baa_black_sheep = ['g4:4', 'g:4', 'd5:4', 'd:4', 'e:2', 'e:2',
        'e:2', 'e:2', 'd:4', 'r:4', 'c:4', 'c:4', 'b4:4', 'b:4',
        'a:4', 'a:4', 'g:4', 'r:4', 'd5:4', 'd:2', 'd:2', 'c:4',
        'c:4', 'b4:4', 'b:2', 'b:2', 'a:4', 'r:4', 'd5:4', 'd:2',
        'd:2', 'c:2', 'c:2', 'c:2', 'c:2', 'b4:4', 'b:2', 'b:2',
        'a:4', 'r:4', 'g:4', 'g:4', 'd5:4', 'd:4', 'e:2', 'e:2',
        'e:2', 'e:2', 'd:4', 'r:4', 'c:4', 'c:4', 'b4:4', 'b:4',
        'a:4', 'a:4', 'g:4', 'r:4'
    ]
    row_your_boat = ['c4:12', 'c:12', 'c:9', 'd:3', 'e:12', 'e:9', 'd:3',
        'e:9', 'f:3', 'g:24', 'c5:4', 'c:4', 'c:4', 'g4:4', 'g:4',
        'g:4', 'e:4', 'e:4', 'e:4', 'c:4', 'c:4', 'c:4', 'g:9', 'f:3',
        'e:9', 'd:3', 'c:24'
    ]
    itsy_bitsy_spider = ['c4:2', 'f:4', 'f:2', 'f:4', 'g:2', 'a:6', 'a:4',
        'a:2', 'g:4', 'f:2', 'g:4', 'a:2', 'f:6', 'r:4', 'f:2', 'a:6',
        'a:4', 'bb:2', 'c5:6', 'c:6', 'bb4:4', 'a:2', 'bb:4', 'c5:2',
        'a4:6', 'r:6', 'f:6', 'f:4', 'g:2', 'a:6', 'a:6', 'g:4',
        'f:2', 'g:4', 'a:2', 'f:6', 'c:4', 'c:2', 'f:4', 'f:2', 'f:4',
        'g:2', 'a:6', 'a:4', 'a:2', 'g:4', 'f:2', 'g:4', 'a:2', 'f:6',
        'r:4'
    ]
    old_macdonald = ['g4:4', 'g:4', 'g:4', 'd:4', 'e:4', 'e:4', 'd:8',
        'b:4', 'b:4', 'a:4', 'a:4', 'g:12', 'd:4', 'g:4', 'g:4',
        'g:4', 'd:4', 'e:4', 'e:4', 'd:8', 'b:4', 'b:4', 'a:4', 'a:4',
        'g:12', 'd:2', 'd:2', 'g:4', 'g:4', 'g:4', 'd:2', 'd:2',
        'g:4', 'g:4', 'g:8', 'g:2', 'g:2', 'g:4', 'g:2', 'g:2', 'g:4',
        'g:2', 'g:2', 'g:2', 'g:2', 'g:4', 'g:4', 'g:4', 'g:4', 'g:4',
        'd:4', 'e:4', 'e:4', 'd:8', 'b:4', 'b:4', 'a:4', 'a:4',
        'g:16'
    ]
    mary_had_a_little_lamb = ['b4:4', 'a:4', 'g:4', 'a:4', 'b:4', 'b:4',
        'b:8', 'a:4', 'a:4', 'a:8', 'b:4', 'd5:4', 'd:8', 'b4:4',
        'a:4', 'g:4', 'a:4', 'b:4', 'b:4', 'b:4', 'b:4', 'a:4', 'a:4',
        'b:4', 'a:4', 'g:16'
    ]
    hickory_dickory_dock = ['f#4:2', 'g:2', 'a:2', 'g:2', 'f#:2', 'e:2',
        'f#:6', 'r:4', 'f#:2', 'f#:4', 'a:2', 'g:4', 'e:2', 'f#:6',
        'r:4', 'f#:2', 'f#:4', 'f#:2', 'a:4', 'a:2', 'g:4', 'g:2',
        'b:6', 'a:2', 'b:2', 'a:2', 'g:2', 'f#:2', 'e:2', 'd:6',
        'r:6'
    ]
    jack_and_jill = ['e4:4', 'e:2', 'e:4', 'e:2', 'a:4', 'a:2', 'a:4',
        'a:2', 'b:4', 'b:2', 'b:4', 'b:2', 'c#5:6', 'a4:6', 'e4:4',
        'e:2', 'e:4', 'e:2', 'f#:4', 'f#:2', 'f#:4', 'f#:2', 'e:4',
        'd:2', 'c#:4', 'b3:2', 'a:6', 'a:6'
    ]
    humpty_dumpty = ['e4:4', 'g:2', 'f:4', 'a:2', 'g:2', 'a:2', 'b:2',
        'c5:4', 'r:2', 'e4:4', 'g:2', 'f:4', 'a:2', 'g:2', 'e:2',
        'c:2', 'd:4', 'r:2', 'e:2', 'e:2', 'g:2', 'f:2', 'f:2', 'a:2',
        'g:2', 'a:2', 'b:2', 'c5:4', 'r:2', 'e:2', 'e:2', 'c:2',
        'f:2', 'f:2', 'e:2', 'd:2', 'c:2', 'b4:2', 'c5:6'
    ]

    # dictionary with details for each song
    songs_dict = {
        "twinkle_twinkle": {"ticks": 4, "bpm": 140, "notes": twinkle_twinkle},
        "baa_baa_black_sheep": {"ticks": 4, "bpm": 140, "notes": baa_baa_black_sheep},
        "row_your_boat": {"ticks": 12, "bpm": 140, "notes": row_your_boat},
        "itsy_bitsy_spider": {"ticks": 4, "bpm": 180, "notes": itsy_bitsy_spider},
        "old_macdonald": {"ticks": 4, "bpm": 120, "notes": old_macdonald},
        "mary_had_a_little_lamb": {"ticks": 4, "bpm": 140, "notes": mary_had_a_little_lamb},
        "hickory_dickory_dock": {"ticks": 4, "bpm": 160, "notes": hickory_dickory_dock},
        "jack_and_jill": {"ticks": 4, "bpm": 140, "notes": jack_and_jill},
        "humpty_dumpty": {"ticks": 4, "bpm": 120, "notes": humpty_dumpty},
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
        music.set_tempo(ticks=song["ticks"], bpm=song['bpm'])
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

