==========================
Piezo_Buzzer_and_music
==========================

.. py:module:: music

Connections
--------------------------

| The buzzer is usually connected to pin0.

----

Model
----------------------------------------

#.  Place the buzzer first.
#.  Connect with the jumper wires.

.. image:: images/buzzer_bb.png
    :scale: 50 %


.. image:: images/buzzer.jpg
    :scale: 30 %

----

Library
----------------------------------------

| Put ``import music`` at the top.
| See: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html

----

.. py:function::  music.play(music, pin=pin0, wait=True, loop=False)

    Play the music.

    If music can be a string such as, 'c1:4'or a list of notes that are played one after the other to perform a melody.

    The duration and octave values are reset to their defaults before the music is played.

    The output pin can be used to override the default pin0. Use pin=None to prevent sounds being played.

    If wait is set to True, this function is blocking, and the music will be played to the end.

    If loop is set to True, the music repeats until stop is called or the blocking call is interrupted.

.. py:function::  music.stop(pin=pin0)

    Stops all music playback on the built-in speaker and any pin outputting sound. An optional argument can be provided to specify a pin, eg. music.stop(pin1).

.. py:function::  music.reset()
    
    Resets the state of the following attributes in the following way:

    ticks = 4
    bpm = 120
    duration = 4
    octave = 4

----

Notes
----------------------------------------

| An individual note is specified thus: ``NOTE[octave][:duration]``.
| Notes are the letters a to g. Lower case or upper case are the same.
| If the octave is left out it defaults to 4 (containing middle C).
| If the duration is left out it defaults to 4 (a crotchet).
| For example, ``a2:4`` refers to the note “A” in octave 2 that lasts for four ticks (a tick is an arbitrary length of time defined by a tempo setting function). If the note name R is used then it is treated as a rest (silence).
| Accidentals (flats and sharps) are denoted by the b (flat - a lower case b) and # (sharp - a hash symbol). For example, ``Ab`` is A-flat and ``C#`` is C-sharp.
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

    notes_list = ['c4:1', 'e:4', 'g:8', 'c5:2', 'e5', 'g4','f#4','bb3:8']

    music.set_tempo(ticks=4, bpm=240)
    music.play(notes_list)

----

.. admonition:: Tasks

    #. Play a list of notes.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Play a list of notes.

                    .. code-block:: python
                        from microbit import *
                        import music

                        notes_list = ['c4:4', 'e', 'g', 'e', 'g']

                        music.set_tempo(ticks=4, bpm=240)

                        while True:
                            music.play(notes_list)
                            sleep(1000)

----

Scales
----------------------------------------

| The lists below are the notes of scales.
| Press A or B to play a different scale.


.. code-block:: python

    from microbit import *
    import music

    cmajor = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    eminor = ['e', 'f#', 'g', 'a', 'b', 'c', 'd']

    while True:
        if button_a.is_pressed():
            music.play(cmajor)
        elif button_b.is_pressed():
            music.play(eminor)
        sleep(1000)

----

Built in music
----------------------------------------

| There are built in melodies that can be found by typing ``music.``
| Melodies can be played using ``music.play(melody).

.. code-block:: python

    from microbit import *
    import music

    music.play(music.PYTHON)


| The code below uses a for loop to loop through each melody in the ``melodies_list`` and play it.
| For a list of built in meodies see: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html

.. code-block:: python

    from microbit import *
    import music

    melodies_list = [music.PYTHON, music.BADDY, music.CHASE]
    for melody in melodies_list:
        music.play(melody)

----

All Built in melodies
----------------------------------------

| This code plays all the melodies.

.. code-block:: python

    from microbit import *
    import music

    built_in_tunes = [music.DADADADUM, music.ENTERTAINER, music.PRELUDE,
    music.ODE, music.NYAN, music.RINGTONE, music.FUNK, music.BLUES,
    music.BIRTHDAY, music.WEDDING, music.FUNERAL, music.PUNCHLINE,
    music.PYTHON, music.BADDY, music.CHASE, music.BA_DING, 
    music.WAWAWAWAA, music.JUMP_UP, music.JUMP_DOWN, music.POWER_UP,
    music.POWER_DOWN]

    while True:
        for tune in built_in_tunes:
            music.play(tune)
            sleep(1000)


