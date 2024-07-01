==========================
Music
==========================

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html

.. py:module:: music

.. admonition:: Warning

    | For use of the inbuilt speaker on the **V2 microbit**, set the speaker to **on**.
    | For use of an external buzzer on a **breadboard**, set the speaker to **off** so that the in-built speaker does not also play sounds.

Speaker **V2** 
---------------------

| By default sound output will be via the edge connector on pin0 and the **V2** built-in speaker. 
| The **V2** built-in speaker can be turned off or on without affecting playing via pin0.
| When flashing a new script to the microbit, the **V2** built-in speaker will be on, unless the code sets it to off.

.. py:function::  speaker.off()

    Use off() to turn off the speaker. This does not disable sound output to an edge connector pin.

.. py:function::  speaker.on()

    Use on() to turn on the speaker.

----

Music Library
----------------------------------------

| Put ``import music`` at the top under ``from microbit import *``.

.. code-block:: python

    from microbit import *
    import music

----

Play notes
----------------

.. py:function:: music.play(notes, pin=pin0, wait=True, loop=False)

    | Play the music.
    | Music can be a string, such as 'c1:4', or a list of notes as strings, such as ['c', 'd', 'e']
    | The duration and octave values are reset to their defaults (of 4 each) before the music is played.
    | Octaves start on the note "C".
    | The output pin can be used to override the default pin0. pin=None prevents sounds from being played.
    | If wait is set to True, playing is blocking, and the music will be played to the end.
    | If loop is set to True, the music repeats until stop is called. Set wait to False to use this.

| Use ``music.play(note)`` to play a note given by the ``note`` variable.
| The note is written as a string with quotes: 'c4:8'. This is a c note in octave 4 with a duration of 8 ticks (a minim or 2 crotchet beats).

.. code-block:: python

    from microbit import *
    import music

    note = 'c4:8'
    music.play(note)

| Use ``music.play(notes_list)`` to play a list of notes in the ``notes_list`` variable.
| The code below plays a list of notes. The octave changes from 4 to 5.
| Octaves start on the note "C".

.. code-block:: python

    from microbit import *
    import music

    notes_list = ['e4', 'f#', 'g', 'a', 'b', 'c5', 'd', 'e']
    music.play(notes_list)

.. admonition:: Tasks

    #. Play the note e over and over again with 1 second between them.
    #. Play the notes c, e, g over and over again with 1 second between replays.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play the note e.

                .. code-block:: python

                    from microbit import *
                    import music

                    note = 'e'

                    while True:
                        music.play(note)
                        sleep(1000)

            .. tab-item:: Q2

                Play the notes c, e, g over and over again with 1 second between replays. 

                .. code-block:: python

                    from microbit import *
                    import music

                    notes_list = ['c', 'e', 'g']

                    while True:
                        music.play(notes_list)
                        sleep(1000)

----

Notes
----------------------------------------

| An individual note is specified as: ``NOTE[octave][:duration]``.

| Notes are the letters a to g with or without an accidental (`#` for a sharp, `b` for a flat). 
| Lower case or upper case notes are the same. eg. `A` and `a` are the same. 
| **Ab** is A-flat and **C#** is C-sharp.
| Use **r** or **R** for a rest (silence).

| If the octave is left out it defaults to 4 (containing middle C).
| Octaves start on the note "C".
| If the duration is left out it defaults to 4 (a crotchet).
| For example, **a2:4** refers to the note "A" in octave 2 that lasts for four ticks (a tick is an arbitrary length of time defined by a tempo setting function). 

| The octave and duration parameters are states that carry over to subsequent notes until re-specified. 
| e.g. ['c4:1', 'e', 'g:8'] The `e` is octave 4 for 1 tick. The `g` is octave 4 for 8 ticks.

----

.. admonition:: Tasks

    #. Play the 5 notes: c, e, g, e, c in octave 4.
    #. Starting with C in octave 4, play the next 6 notes that are each one semitone higher than the previous note. Use sharps as needed.
    #. Starting with G flat in octave 5, play the next 6 notes that are each one semitone lower than the previous note. Use flats as needed. 

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play the 5 notes: c, e, g, e, c in octave 4.

                .. code-block:: python

                    from microbit import *
                    import music

                    notes_list = ['c4:4', 'e', 'g', 'e', 'c']

                    while True:
                        music.play(notes_list)
                        sleep(1000)

            .. tab-item:: Q2

                Starting with C in octave 4, play the next 6 notes that are each one semitone higher than the previous note. Use sharps as needed. 

                .. code-block:: python

                    from microbit import *
                    import music

                    notes_list = ['C4', 'C#', 'D', 'D#', 'E', 'F', 'F#']

                    while True:
                        music.play(notes_list)
                        sleep(1000)

            .. tab-item:: Q3

                Starting with G flat in octave 5, play the next 6 notes that are each one semitone lower than the previous note. Use flats as needed. 

                .. code-block:: python

                    from microbit import *
                    import music

                    notes_list = ['Gb5', 'F', 'E', 'Eb', 'D', 'Db']

                    while True:
                        music.play(notes_list)
                        sleep(1000)

----

Tempo
----------

.. py:function::  music.set_tempo(ticks=4, bpm=120)

    | Sets the tempo for playback.
    | The number of ticks, expressed as an integer, make a beat. The default is 4 ticks per beat.
    | Each beat is to be played at a certain rate, beats per minute, expressed as an integer. The default is 120 bpm.

| Examples of use:
| music.set_tempo() - reset the tempo to default of ticks = 4, bpm = 120
| music.set_tempo(ticks=8) - change the beat to 8 ticks
| music.set_tempo(bpm=240) - just change the tempo to 240 beats per minute

| The length of a beat in milliseconds is (60 sec * 1000 / bpm). 
| For the default value of 120 bpm, that's 60000/120 or 1 beat in 500 milliseconds, which is 2 beats per second.

| The code below plays a list of notes.
| The tempo can be sped up by changing ticks from 4 to 8 or by changing bpm from 120 to 240.

.. code-block:: python

    from microbit import *
    import music

    notes_list = ['e4', 'f#', 'g', 'a', 'b', 'c5', 'd', 'e']

    music.set_tempo(ticks=4, bpm=120)
    music.play(notes_list)
    music.set_tempo(ticks=8, bpm=120)
    music.play(notes_list)
    music.set_tempo(ticks=8, bpm=240)
    music.play(notes_list)

----

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

.. admonition:: Tasks

    #. Play the 5 notes: c, e, g, e, c with a tempo of 120, 180 and 240bpm without a for-loop.
    #. Play the 3 notes: 'e4:4', 'f#', 'g' with a tempo of 120, 180 and 240bpm using a for-loop for the tempos. 
    #. Design a function that takes the list of 3 notes ['e4:4', 'f#', 'g'] as one parameter; takes a tempo list of 120, 240, 360 , 480 and 600 bpm as a second parameter and a third parameter sleep_time with default value 1000. Use a repeat loop to set the tempo and play the notes_list.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play the 5 notes: c, e, g, e, c with a tempo of 120, 180 and 240bpm without a for-loop. 

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

                Play the 3 notes: 'e4:4', 'f#', 'g' with a tempo of 120, 180 and 240bpm using a for-loop for the tempos. 

                .. code-block:: python

                    from microbit import *
                    import music

                    notes_list = ['e4:4', 'f#', 'g']

                    while True:
                        for tempo in [120, 180, 240]:
                            music.set_tempo(bpm=tempo) 
                            music.play(notes_list)
                            sleep(1000)
        

            .. tab-item:: Q3

                Design a function that takes the list of 3 notes ['e4:4', 'f#', 'g'] as one parameter; takes a tempo list of 120, 240, 360 , 480 and 600 bpm as a second parameter and a third parameter sleep_time with default value 1000. Use a repeat loop to set the tempo and play the notes_list.
 
                .. code-block:: python

                    from microbit import *
                    import music

                    notes_list = ['e4:4', 'f#', 'g']
                    tempo_list = [120, 240, 360, 480, 600]

                    def tempo_play(notes_list, tempo_list, sleep_time=1000):
                        for tempo in tempo_list:
                            music.set_tempo(bpm=tempo)
                            music.play(notes_list)
                            sleep(sleep_time)
                        
                    while True:
                        tempo_play(notes_list, tempo_list, sleep_time=1000)

----

Volume **V2** 
---------------------

.. py:function:: set_volume(volume)

    | Configure the output volume of the microbit speaker and pins.
    | **volume** is an integer between 0 and 255.

| The code below sets the volume at different levels and plays a C note in octave 4 for 2 ticks at each volume.

.. code-block:: python

    from microbit import *
    import music


    note = "c4:2"
    while True:
        set_volume(255)
        music.play(note)
        set_volume(128)
        music.play(note)
        set_volume(64)
        music.play(note)

----

.. admonition:: Tasks

    #. Instead of playing the same note each time, play each different note "c4:2", "e4:2","f#4:2" at a different volume.
    #. Put the 3 sound levels in a list and use a for-loop to set the volume and play the note "c4:2".
    #. To the previous task, add the ability to stop the playing by exiting the ``while True`` loop on pressing the A-button via the use of ``break``. Pressing the reset button on the back of the microbit will restart the code.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Instead of playing the same note each time, play a different note "c4:2", "e4:2","f#4:2" at a different volume.

                .. code-block:: python

                    from microbit import *
                    import music

                    note0 = "c4:2"
                    note1 = "e4:2"
                    note2 = "f#4:2"
                    while True:
                        set_volume(255)
                        music.play(note0)
                        set_volume(128)
                        music.play(note1)
                        set_volume(64)
                        music.play(note2)

            .. tab-item:: Q2

                Put the 3 sound levels in a list and use a for-loop to set the volume and play the note "c4:2".

                .. code-block:: python

                    from microbit import *
                    import music

                    note = "c4:2"
                    volumes = [255, 125, 64]
                    while True:
                        for v in volumes:
                            set_volume(v)
                            music.play(note)

            .. tab-item:: Q3

                To the previous task, add the ability to stop the playing by exiting the ``while True`` loop on pressing the A-button via the use of ``break``. Pressing the reset button on the back of the microbit will restart the code.

                .. code-block:: python

                    from microbit import *
                    import music

                    note = "c4:2"
                    volumes = [255, 125, 64]
                    while True:
                        for v in volumes:
                            set_volume(v)
                            music.play(note)
                        if button_a.was_pressed():
                            break


----

Stop background music
-----------------------------------

.. py:function::  music.stop(pin=pin0)

    | Stops all music playback on the built-in speaker and any pin outputting sound. 
    | An optional argument can be provided to specify a pin, eg. music.stop(pin=pin1).


| In the example below ``wait=False`` so that the music plays in the background.
| In the example below ``loop=True`` so that the music loops forever.
| "A" is scrolled in the background to suggest pressing A to stop the music.

.. code-block:: python

    from microbit import *
    import music

    # Define the melody
    melody1 = ['C4:4', 'C4:4', 'G4:4', 'G4:4', 
                'A4:4', 'A4:4', 'G4:8', 
                'F4:4', 'F4:4', 'E4:4', 'E4:4',
                'D4:4', 'D4:4', 'C4:8']

    # Play the melody
    music.play(melody1, wait=False, loop=True)

    display.scroll("A", wait=False, loop=True)
    while True: # Allow 2 seconds to choose to press the A-button
        sleep(2000)
        if button_a.was_pressed():
            # Stop the melody
            music.stop()
            break

    display.scroll("THE END")

----

.. admonition:: Tasks

    #. Add a rest equivalent to 4 crotchets to the end of the melody above so it provides a pause equivalent to one bar as the melody loops.
    #. Modify the example above to have 2 melodies: melody1 = ['E4:4', 'D:4', 'C:4', 'D:4', 'E:4', 'E:4', 'E:8', 'D:4', 'D:4', 'D:8', 'E:4', 'G:4', 'G:8'] and melody2 = ['E4:4',  'D:4', 'C:4', 'D:4', 'E:4', 'E:4', 'E:4', 'E:4', 'D:4', 'D:4', 'E:4', 'D:4', 'C:16']. Firstly, melody1 loops and can be stopped by the A-button. Then melody2 loops and can be stopped by the B-button.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Instead of playing the same note each time, play a different note "c4:2", "e4:2","f#4:2" for a different volume.

                .. code-block:: python

                    from microbit import *
                    import music

                    # Define the melody
                        melody1 = ['C4:4', 'C4:4', 'G4:4', 'G4:4', 
                                    'A4:4', 'A4:4', 'G4:8', 
                                    'F4:4', 'F4:4', 'E4:4', 'E4:4',
                                    'D4:4', 'D4:4', 'C4:8',
                                    'R:16']

                    # Play the melody
                    music.play(melody1, wait=False, loop=True)

                    display.scroll("A", wait=False, loop=True)
                    while True: # Allow 2 seconds to choose to press the A-button
                        sleep(2000)
                        if button_a.was_pressed():
                            # Stop the melody
                            music.stop()
                            break

                    display.scroll("THE END")

            .. tab-item:: Q2

                Modify the example above to have 2 melodies: melody1 = ['E4:4', 'D:4', 'C:4', 'D:4', 'E:4', 'E:4', 'E:8', 'D:4', 'D:4', 'D:8', 'E:4', 'G:4', 'G:8'] and melody2 = ['E4:4',  'D:4', 'C:4', 'D:4', 'E:4', 'E:4', 'E:4', 'E:4', 'D:4', 'D:4', 'E:4', 'D:4', 'C:16']. Firstly, melody1 loops and can be stopped by the A-button. Then melody2 loops and can be stopped by the B-button.

                .. code-block:: python

                    from microbit import *
                    import music

                    # Define the first melody
                    melody1 = ['E4:4', 'D:4', 'C:4', 'D:4', 
                            'E:4', 'E:4', 'E:8', 
                            'D:4', 'D:4', 'D:8', 
                            'E:4', 'G:4', 'G:8']


                    # Define the second melody
                    melody2 = ['E4:4', 'D:4', 'C:4', 'D:4', 
                            'E:4', 'E:4', 'E:4', 'E:4',
                            'D:4', 'D:4', 'E:4', 'D:4', 
                            'C:16']

                    # Play the first melody
                    music.play(melody1, wait=False, loop=True)

                    display.scroll("A", wait=False, loop=True)
                    while True:  # Allow 2 seconds to choose to press the A-button
                        sleep(2000)
                        if button_a.was_pressed():
                            # Stop the first melody
                            music.stop()
                            break

                    # Play the second melody
                    music.play(melody2, wait=False, loop=True)

                    display.scroll("B", wait=False, loop=True)
                    while True:  # Allow 2 seconds to choose to press the B-button
                        sleep(2000)
                        if button_b.was_pressed():
                            # Stop the second melody
                            music.stop()
                            break

                    display.scroll("THE END")


----

Reset music
-----------------------------------

.. py:function::  music.reset()

    | Resets the state of the following attributes as listed:
    | ticks = 4; bpm = 120; duration = 4; octave = 4

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

    #. Play the 8 notes of D major. See: https://www.pianoscales.org/major.html
    #. Play the 8 notes of F minor. See: https://www.pianoscales.org/minor.html
    #. Play the D major scale when the A-button is pressed and the F minor scale when the B-button is pressed.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play the 8 notes of D major.

                .. code-block:: python

                    from microbit import *
                    import music

                    d_major = ["D", "E", "F#", "G", "A", "B", "C#", "D"]

                    while True:
                        music.play(d_major)
                        sleep(1000)


            .. tab-item:: Q2

                Play the 8 notes of F minor.

                .. code-block:: python

                    from microbit import *
                    import music

                    f_minor = ["F", "G", "Ab", "Bb", "C", "Db", "Eb", "F"]

                    while True:
                        music.play(f_minor)
                        sleep(1000)


            .. tab-item:: Q3

                Play the D major scale when the A-button is pressed and the F minor scale when the B-button is pressed.

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
-----------------

| Make use of these custom dictionaries that store notes and tempos for some short tunes.

.. code-block:: python

    from microbit import *
    import music

    scale = {"name": "Scale", "notes": "C5 B A G F E D C", "tempo": 120}
    reverse = {"name": "Reverse", "notes": "C D E F G A B C5", "tempo": 120}
    mystery = {"name": "Mystery", "notes": "E B C5 A B G A F", "tempo": 120}
    gilroy = {"name": "Gilroy", "notes": "A F E F D G E F", "tempo": 120}
    falling = {"name": "Falling", "notes": "C5 A B G A F G E", "tempo": 120}
    hopeful = {"name": "Hopeful", "notes": "G B A G C5 B A B", "tempo": 120}
    tokyo = {"name": "Tokyo", "notes": "B A G A G F A C5", "tempo": 120}
    paris = {"name": "Paris", "notes": "G F G A - F E D", "tempo": 120}
    rising = {"name": "Rising", "notes": "E D G F B A C5 B", "tempo": 120}
    sitka = {"name": "Sitka", "notes": "C5 G B A F A C5 B", "tempo": 120}


.. admonition:: Challenege

    #. Play each of the custom dictionaries notes.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play each of the custom dictionaries notes.

                .. code-block:: python

                    from microbit import *
                    import music

                    scale = {"name": "Scale", "notes": "C5 B A G F E D C", "tempo": 240}
                    reverse = {"name": "Reverse", "notes": "C D E F G A B C5", "tempo": 240}
                    mystery = {"name": "Mystery", "notes": "E B C5 A B G A F", "tempo": 120}
                    gilroy = {"name": "Gilroy", "notes": "A F E F D G E F", "tempo": 120}
                    falling = {"name": "Falling", "notes": "C5 A B G A F G E", "tempo": 180}
                    hopeful = {"name": "Hopeful", "notes": "G B A G C5 B A B", "tempo": 180}
                    tokyo = {"name": "Tokyo", "notes": "B A G A G F A C5", "tempo": 180}
                    paris = {"name": "Paris", "notes": "G F G A r F E D", "tempo": 180}
                    rising = {"name": "Rising", "notes": "E D G F B A C5 B", "tempo": 180}
                    sitka = {"name": "Sitka", "notes": "C5 G B A F A C5 B", "tempo": 180}

                    # List of scales
                    scales = [scale, reverse, mystery, gilroy, falling, hopeful, tokyo, paris, rising, sitka]

                    # Loop over each scale
                    for selected_scale in scales:
                        # Parse the notes and tempo from the selected scale
                        notes = selected_scale["notes"].split(" ")
                        tempo = selected_scale["tempo"]
                        music.set_tempo(ticks=8, bpm=tempo)
                        music.play(notes, wait=True)
                        sleep(1000)


        