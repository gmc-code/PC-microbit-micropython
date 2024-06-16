==========================
Music
==========================

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html

.. py:module:: music

.. admonition:: Warning

    | For use of the buzzer on the **breadboard**, set the speaker to **off** so that the in-built speaker does not also play sounds.
    | For use of the inbuilt speaker on the **V2 microbit**, set the speaker to **on**.

----

Library
----------------------------------------

| Put ``import music`` at the top under ``from microbit import *``.

.. code-block:: python

    from microbit import *
    import music

----

Play notes
----------------------------------------

.. py:function::  music.play(notes, pin=pin0, wait=True, loop=False)

    | Play the notes.
    | The notes can be a string, such as 'c1:4', or a list of notes as strings, such as ['c', 'd', 'e']
    | The duration and octave values are reset to their defaults before the music is played.
    | The output pin can be used to override the default pin0. Use pin=None to prevent sounds being played.
    | If wait is set to True, playing is blocking, and the music will be played to the end.
    | If loop is set to True, the music repeats until stop is called.

----

Notes
----------------------------------------

| An individual note is specified thus: ``NOTE[octave][:duration]``.
| Notes are the letters a to g. Lower case or upper case are the same.
| If the octave is left out it defaults to 4 (containing middle C).
| If the duration is left out it defaults to 4 (a crotchet).
| For example, **a2:4** refers to the note “A” in octave 2 that lasts for four ticks (a tick is an arbitrary length of time defined by a tempo setting function). If the note name **R** is used then it is treated as a rest (silence).
| Accidentals (flats and sharps) are denoted by the b (flat - a lower case b) and # (sharp - a hash symbol).
| For example, **Ab** is A-flat and **C#** is C-sharp.
| The octave and duration parameters are states that carry over to subsequent notes until re-specified. 
| The tempo can be set using ``music.set_tempo(ticks=4, bpm=120)``

| Use ``music.play(note)`` to play a note in the ``note`` variable.

.. code-block:: python

    from microbit import *
    import music

    note = 'c4:8'
    music.play(note)

| Use ``music.play(notes)`` to play a list of notes in the ``notes_list`` variable.
| The code below plays a list of notes that use various forms to specify them.

.. code-block:: python

    from microbit import *
    import music

    notes_list = ['c4:1', 'e:4', 'g:8', 'c:2', 'e5', 'g4','f#','eb']

    music.set_tempo(ticks=4, bpm=240)
    music.play(notes_list)

----

.. admonition:: Tasks

    #. Play the 5 notes: c, e, g, e, c.
    #. Play the 5 notes: e, f#, g, a, b

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play the 5 notes: c, e, g, e, c.

                .. code-block:: python

                    from microbit import *
                    import music

                    notes_list = ['c', 'e', 'g', 'e', 'c']

                    while True:
                        music.play(notes_list)
                        sleep(1000)

            .. tab-item:: Q2

                Play the 5 notes: e, f#, g, a, b.

                .. code-block:: python

                    from microbit import *
                    import music

                    notes_list = ['e', 'f#', 'g', 'a', 'b']

                    while True:
                        music.play(notes_list)
                        sleep(1000)

----

**V2** speaker
---------------------

| By default sound output will be via the edge connector on pin0 and the **V2** built-in speaker. 
| The **V2** built-in speaker can be turned off or on without affecting playing via pin0.
| When flashing a new script to the microbit, the **V2** built-in speaker will be on, unless the code sets it to off.

.. py:function::  speaker.off()

    Use off() to turn off the speaker. This does not disable sound output to an edge connector pin.

.. py:function::  speaker.on()

    Use on() to turn on the speaker.

.. admonition:: Note

    | The docs suggest that there is a test for the speaker status via ``speaker.is_on()``.
    | However, ``print(help(speaker))`` does not list it as being available yet (as of July 2022).
    | See: https://microbit-micropython.readthedocs.io/en/v2-docs/microbit_micropython_api.html

----

**V2** volume
---------------------

.. py:function:: set_volume(volume)

    | Configure the output volume of the microbit speaker and pins.
    | **volume** is an integer between 0 and 255.

| The code below increases the volume and plays a C note in octave 4 for 2 ticks at each volume.

.. code-block:: python

    from microbit import *
    import music


    note = "c4:2"
    for v in range(0, 255, 25):
        set_volume(v)
        music.play(note)


| The code below increases the volume and plays a C note in octave 4 for 2 ticks at each volume.
| The A button can be pressed to exit the for-loop then the while loop using ``break``.
| Pressing the reset button on the back of the microbit will restart the code.

.. code-block:: python

    from microbit import *
    import music


    note = "c4:2"
    while True:
        for v in range(0, 255, 25):
            set_volume(v)
            music.play(note)
            if button_a.is_pressed():
                break
        if button_a.is_pressed():
            break

----

Less common music controls
------------------------------

.. py:function::  music.stop(pin=pin0)

    | Stops all music playback on the built-in speaker and any pin outputting sound. 
    | An optional argument can be provided to specify a pin, eg. music.stop(pin=pin1).

.. py:function::  music.reset()

    | Resets the state of the following attributes as listed:
    | ticks = 4; bpm = 120; duration = 4; octave = 4

.. py:function::  music.set_tempo(ticks=4, bpm=120)

    | Sets the tempo for playback.
    | A number of ticks, expressed as an integer, make a beat. The default is 4 ticks per beat.
    | Each beat is to be played at a certain frequency, beats per minute, expressed as an integer. The default is 120 bpm.

| Examples of use:
| music.set_tempo() - reset the tempo to default of ticks = 4, bpm = 120
| music.set_tempo(ticks=8) - change the beat to 8 ticks
| music.set_tempo(bpm=240) - just change the tempo to 240 beats per minute

| The length of a beat in milliseconds is (60 sec * 1000 / bpm). 
| For the default value of 120 bpm, that's 60000/120 or 1 beat in 500 milliseconds.

.. py:function::  music.get_tempo()

    Gets the current tempo as a tuple of integers: (bpm, ticks).

| To display the tuple from get_tempo it can be converted to a string:

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=240)
    tempo_data = str(music.get_tempo())
    display.scroll(tempo_data)

| Each value in the tuple can be accessed using its index as shown below:

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=2, bpm=120)
    tempo_data = music.get_tempo()
    bpm = tempo_data[0]
    ticks = tempo_data[1]
    display.scroll(bpm)
    display.scroll(ticks)

----

.. admonition:: Tasks

    #. Play the 5 notes: c, e, g, e, c with a tempo of 120, 180 and 240bpm. 
    #. Design a function that takes the 5 notes: c, e, g, e, c, as one parameter; takes a tempo list of 120, 240, 360 , 480 and 600 bpm as a second parameter and a third parameter: sleep_time with default value 1000. Use a repeat loop to set the tempo and play the notes_list.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play the 5 notes: c, e, g, e, c with a tempo of 120, 180 and 240bpm. 

                .. code-block:: python

                    from microbit import *
                    import music

                    notes_list = ['c4:4', 'e', 'g', 'e', 'c']

                    while True:
                        music.set_tempo(bpm=120) 
                        music.play(notes_list)
                        sleep(1000)
                        music.set_tempo(bpm=180) 
                        music.play(notes_list)
                        sleep(1000)
                        music.set_tempo(bpm=240) 
                        music.play(notes_list)
                        sleep(1000)

            .. tab-item:: Q2

                Design a function that takes the 5 notes: c, e, g, e, c, as one parameter; takes a tempo list of 120, 240, 360 , 480 and 600 bpm as a second parameter and a third parameter: sleep_time with default value 1000. Use a repeat loop to set the tempo and play the notes_list.
 
                .. code-block:: python

                    from microbit import *
                    import music

                    notes_list = ['c4:4', 'e', 'g', 'e', 'c']
                    tempo_list = [120, 240, 360, 480, 600]

                    def tempo_play(notes_list, tempo_list, sleep_time=1000):
                        for tempo in tempo_list:
                            music.set_tempo(bpm=tempo)
                            music.play(notes_list)
                            sleep(sleep_time)
                        
                    while True:
                        tempo_play(notes_list, tempo_list, sleep_time=1000)

----

Tuple unpacking for advanced users
-------------------------------------

| For advanced users, tuple unpacking can be used instead of indices: ``bpm, ticks = music.get_tempo()``.
| See: https://www.w3schools.com/python/python_tuples_unpack.asp

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=2, bpm=120)
    bpm, ticks = music.get_tempo()
    display.scroll(bpm)
    display.scroll(ticks)

----

Scales
----------------------------------------

| The lists below are the notes of scales.
| Press A or B to play a different scale.


.. code-block:: python

    from microbit import *
    import music

    c_major = ['c', 'd', 'e', 'f', 'g', 'a', 'b', 'c']
    e_minor = ['e', 'f#', 'g', 'a', 'b', 'c', 'd', 'e']

    while True:
        if button_a.is_pressed():
            music.play(c_major)
        elif button_b.is_pressed():
            music.play(e_minor)
        sleep(1000)

----

.. admonition:: Tasks

    #. Play the 8 notes of D_major. See: https://www.pianoscales.org/_major.html
    #. Play the 8 notes of F_minor. See: https://www.pianoscales.org/_minor.html
    #. Play the D_major scale when the A button is pressed and the F_minor scale when the B button is pressed.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play the 8 notes of D_major.

                .. code-block:: python

                    from microbit import *
                    import music

                    d_major = ["D", "E", "F#", "G", "A", "B", "C#", "D"]

                    while True:
                        music.play(d_major)
                        sleep(1000)


            .. tab-item:: Q2

                Play the 8 notes of F_minor.

                .. code-block:: python

                    from microbit import *
                    import music

                    f_minor = ["F", "G", "Ab", "Bb", "C", "Db", "Eb", "F"]

                    while True:
                        music.play(f_minor)
                        sleep(1000)


            .. tab-item:: Q3

                Play the D_major scale when the A button is pressed and the F_minor scale when the B button is pressed.

                .. code-block:: python

                    from microbit import *
                    import music

                    d_major = ["D", "E", "F#", "G", "A", "B", "C#", "D"]
                    f_minor = ["F", "G", "Ab", "Bb", "C", "Db", "Eb", "F"]

                    while True:
                        if button_a.is_pressed():
                            music.play(d_major)
                        elif button_b.is_pressed():
                            music.play(f_minor)
                        sleep(1000)

----

Custom tunes
------------------

| Guess the nursery rhyme.

.. code-block:: python

    from microbit import *
    import music

    speaker.off()
    music.set_tempo(ticks=4, bpm=240)
    notes_list = ['e', 'd', 'c', 'd', 'e', 'e','e','d','d','d','e','g','g','e','d','c','d','e','e','e','d','d','e','d','c']
    

    while True:
        music.play(notes_list)
        sleep(1000)

| Try out these Christmas tunes.

.. code-block:: python
        
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
            # Get the current song
            do_tune(current_song_index)
        elif button_b.was_pressed():
            # Stop any currently playing song
            while True:
                # Move to the next song
                current_song_index = advance_song_counter(current_song_index)
                music.stop()
                # Get the current song
                do_tune(current_song_index, play_loop=False, play_wait=True)
                if button_b.was_pressed():
                    break
        elif pin_logo.is_touched():
            # Stop any currently playing song
            music.stop()
            # again
            # do_tune(current_song_index)
        sleep(10)


