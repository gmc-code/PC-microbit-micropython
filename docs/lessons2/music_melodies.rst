==========================
Music
==========================

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html

.. py:module:: music

Built in music
----------------------------------------

| There are built-in melodies that can be found by typing ``music.``
| Melodies can be played using ``music.play(melody)``.

.. code-block:: python

    from microbit import *
    import music

    music.play(music.POWER_UP)


| The code below uses a for-loop to loop through each melody in the ``melodies_list`` and play it.
| For a list of built-in meodies see: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html

.. code-block:: python

    from microbit import *
    import music

    melodies_list = [music.DADADADUM, music.POWER_DOWN]
    for melody in melodies_list:
        music.play(melody)

----

All Built in melodies
----------------------------------------

| This code plays all the melodies.
| the A-button can be used to stop all sounds by first breaking out of the ``for`` loop, then the ``while True`` loop.

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
            if button_a.is_pressed():
                break
        if button_a.is_pressed():
            break
----

.. admonition:: Tasks

    #. Play any 3 melodies using a list.
    #. Use the choice function to randomly pick melodies from a melody list. See: https://www.w3schools.com/python/ref_random_choice.asp

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play any 3 melodies using a list.

                .. code-block:: python

                    from microbit import *
                    import music

                    melodies_list = [music.POWER_UP, music.DADADADUM, music.POWER_DOWN]
                    for melody in melodies_list:
                        music.play(melody)

            .. tab-item:: Q2

                Use the choice function to randomly pick melodies from a melody list. See: https://www.w3schools.com/python/ref_random_choice.asp

                .. code-block:: python

                    from microbit import *
                    import random
                    import music

                    melodies_list = [music.POWER_UP, music.DADADADUM, music.POWER_DOWN]

                    while True:
                        music.play(random.choice(melodies_list))
                        sleep(1000)

----

Sound effects using pitch
----------------------------------------

.. py:function::  music.pitch(frequency, duration=-1, pin=pin0, wait=True)

    | Plays a pitch at the integer frequency given for the duration specified in milliseconds.
    | Only one pitch can be played on one pin at any one time.
    | If duration is negative the pitch is played continuously until either the blocking call is interrupted or, in the case of a background call, a new frequency is set or stop is called.
    | An optional argument to specify the output pin can be used to override the default of pin0. pin=None causes no sound to play.
    | If wait is set to True, this function is blocking.

   
| The code below inreases the pitch in steps of 16 with playing duration of 20 ms.

.. code-block:: python
    
    from microbit import *
    import music

    for freq in range(880, 1760, 16):
        music.pitch(freq, duration=20)

----

.. admonition:: Tasks

    #. Modify the code to increase the pitch in steps of 32 with a duration of 40.
    #. Modify the code to decrease the pitch instead.
    #. Modify the code to increase then decrease the pitch.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to increase the pitch in steps of 32 with a duration of 40.

                .. code-block:: python

                    from microbit import *
                    import music

                    for freq in range(880, 1760, 32):
                        music.pitch(freq, duration=40)

            .. tab-item:: Q2

                Modify the code to decrease the pitch instead.

                .. code-block:: python

                    from microbit import *
                    import music

                    for freq in range(1760, 880, -16):
                        music.pitch(freq, duration=20)

            .. tab-item:: Q3

                Modify the code to increase then decrease the pitch.

                .. code-block:: python

                    from microbit import *
                    import music

                    for freq in range(880, 1760, 16):
                        music.pitch(freq, duration=20)
                    for freq in range(1760, 880, -16):
                        music.pitch(freq, duration=20)

----

Note frequencies
------------------

| The table below has the frequencies for notes from A to A over 2 octaves.
| The frequency of any note is doubled when going up one octave.

======= =========
Note    Frequency
======= =========                
A	    440
B flat	466
B	    494
C	    523
C sharp	554
D	    587
D sharp	622
E	    659
F	    698
F sharp	740
G	    784
A flat	831
A	    880
B flat	932
B	    988
C	    1046
C sharp	1108
D	    1174
D sharp	1244
E	    1318
F	    1396
F sharp	1480
G	    1568
A flat	1662
A	    1760
======= ========= 

----

| The code uses a for-loop to play each frequency.
| the A-button can be pressed to exit the while loop using ``break``.
| Pressing the reset button on the back of the microbit will restart the code.

.. code-block:: python

    from microbit import *
    import music

    Am_freqs = [440, 494, 523, 587, 659, 698, 784, 880]
    timing = 400
    while True:
        for freq in Am_freqs:
            music.pitch(freq, duration=timing)
        if button_a.is_pressed():
            break

----

.. admonition:: Tasks

    #. Modify the code to play the pitches of the E minor scale. See: https://www.piano-keyboard-guide.com/e-minor-scale.html.
    #. Modify the code to play the pitches of the D major scale. See: http://www.piano-keyboard-guide.com/d-major-scale.html.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to play the pitches of the E minor scale. See: https://www.piano-keyboard-guide.com/e-minor-scale.html.

                .. code-block:: python

                    from microbit import *
                    import music

                    Em_freqs = [659, 740, 784, 880, 988, 1046, 1174, 1318]
                    timing = 400
                    while True:
                        for freq in Em_freqs:
                            music.pitch(freq, duration=timing)
                        if button_a.is_pressed():
                            break

            .. tab-item:: Q2

                Modify the code to play the pitches of the D major scale. See: http://www.piano-keyboard-guide.com/d-major-scale.html.

                .. code-block:: python

                    from microbit import *
                    import music

                    D_freqs = [587, 659, 740, 784, 880, 988, 1108, 1174]
                    timing = 400
                    while True:
                        for freq in D_freqs:
                            music.pitch(freq, duration=timing)
                        if button_a.is_pressed():
                            break


