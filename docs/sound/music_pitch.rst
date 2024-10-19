==========================
Music pitch
==========================

| See: https://microbit-micropython.readthedocs.io/en/stable/music.html

.. py:module:: music

Sound effects using pitch
----------------------------------------

.. py:function::  music.pitch(frequency, duration=-1, pin=pin0, wait=True)

    | Plays a pitch at the integer frequency given for the duration specified in milliseconds.
    | Only one pitch can be played on one pin at any one time.
    | If duration is negative the pitch is played continuously until either the blocking call is interrupted or, in the case of a background call, a new frequency is set or stop is called.
    | An optional argument to specify the output pin can be used to override the default of pin0. pin=None causes no sound to play.
    | If wait is set to True, this function is blocking.


| The code below increases the pitch in steps of 16 with playing duration of 20 ms.

.. code-block:: python

    from microbit import *
    import music

    for freq in range(880, 1760, 16):
        music.pitch(freq, duration=20)

| The code below alters the pitch as the microbit is tilted sideways.
| ``abs(accelerometer.get_x()) * 4`` uses the absolute function to turn negative values into positive.  Multiplying by 4 increases the maximum pitch that can be produced.
| A-button pressing is required to make the sound.

.. code-block:: python

    from microbit import *
    import music

    while True:
        if button_a.is_pressed():
            music.pitch(abs(accelerometer.get_x()) * 4, 25)

----

.. admonition:: Tasks

    #. Modify the code to increase the pitch in steps of 32 with a duration of 40.
    #. Modify the code to decrease the pitch instead.
    #. Modify the code to increase then decrease the pitch.
    #. Modify the accelerometer code example to include B-button pressing for a duration of 100ms.

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

            .. tab-item:: Q4

                Modify the accelerometer code example to include B-button pressing for a duration of 100ms.

                .. code-block:: python

                    from microbit import *
                    import music

                    while True:
                        if button_a.is_pressed():
                            music.pitch(abs(accelerometer.get_x()) * 4, 25)
                        elif button_b.is_pressed():
                            music.pitch(abs(accelerometer.get_x()) * 4, 100)


----

Note frequencies
------------------

| The table below has the frequencies for notes from A to A over 2 octaves.
| The frequency of any note is doubled when going up one octave.

======= =========
Note    Frequency
======= =========
A4	    440
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
A5 flat	831
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
A6 flat	1662
A	    1760
======= =========

----

| The code uses a for-loop to play each frequency.
| the A-button can be pressed to exit the while-loop using ``break``.
| Pressing the reset button on the back of the microbit will restart the code.

.. code-block:: python

    from microbit import *
    import music

    Am_4 = [440, 494, 523, 587, 659, 698, 784, 880]
    timing = 400
    while True:
        for freq in Am_4:
            music.pitch(freq, duration=timing)
        if button_a.was_pressed():
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
                        if button_a.was_pressed():
                                break


            .. tab-item:: Q2

                Modify the code to play the pitches of the D major scale. See: http://www.piano-keyboard-guide.com/d-major-scale.html.

                .. code-block:: python

                    from microbit import *
                    import music

                    DM_freqs = [440, 494, 523, 587, 659, 698, 784, 880]
                    timing = 400
                    while True:
                        for freq in DM_freqs:
                            music.pitch(freq, duration=timing)
                        if button_a.was_pressed():
                            break



.. admonition:: Tasks

    #. Begin with the scale Am_4 = [440, 494, 523, 587, 659, 698, 784, 880]. Use list comprehension to create a new list, Am_5, in which the frequencies are multiplied by 2, but include the condition that the frequency is not 440. Scroll the octave number, without blocking the sound, when the octave list sounds start. See: https://pc-python.readthedocs.io/en/latest/python_advanced/list_comprehensions.html
    #. Begin with the scale Am_4= [440, 494, 523, 587, 659, 698, 784, 880]. Use list comprehension to create a new list, Am_5, excluding 440 and a new list, Am_3, in which the frequencies are divided by 2, excluding 880. Scroll the octave number, without blocking the sound, when the octave list sounds start.
    #. Begin with the scale Am_4= [440, 494, 523, 587, 659, 698, 784, 880]. Use list comprehension to create a new list, Am_54_rev, which is the reverse of Am_4, excluding 880. Show an up arrow when Am_4 is played and a down arrow for Am_54_rev.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Begin with the scale Am_4 = [440, 494, 523, 587, 659, 698, 784, 880]. Use list comprehension to create a new list, Am_5, in which the frequencies are multiplied by 2, but include the condition that the frequency is not 440. Scroll the octave number, without blocking the sound, when the octave list sounds start.

                .. code-block:: python

                    from microbit import *
                    import music

                    Am_4 = [440, 494, 523, 587, 659, 698, 784, 880]
                    Am_5 = [freq * 2 for freq in Am_4 if freq != 440]
                    print(Am_5)

                    timing = 400
                    while True:
                        display.scroll(4, wait=False)
                        for freq in Am_4:
                            music.pitch(freq, duration=timing)
                        display.scroll(5, wait=False)
                        for freq in Am_5:
                            music.pitch(freq, duration=timing)
                        if button_a.was_pressed():
                            break

            .. tab-item:: Q2

               Begin with the scale Am_4= [440, 494, 523, 587, 659, 698, 784, 880]. Use list comprehension to create a new list, Am_5, excluding 440 and a new list, Am_3, in which the frequencies are divided by 2, excluding 880. Scroll the octave number, without blocking the sound, when the octave list sounds start.

                .. code-block:: python

                    from microbit import *
                    import music


                    Am_4 = [440, 494, 523, 587, 659, 698, 784, 880]
                    Am_5 = [freq * 2 for freq in Am_4 if freq != 440]
                    Am_3 = [freq // 2 for freq in Am_4 if freq != 880]

                    timing = 400
                    while True:
                        display.scroll(3, wait=False)
                        for freq in Am_3:
                            music.pitch(freq, duration=timing)
                        display.scroll(4, wait=False)
                        for freq in Am_4:
                            music.pitch(freq, duration=timing)
                        display.scroll(5, wait=False)
                        for freq in Am_5:
                            music.pitch(freq, duration=timing)
                        if button_a.was_pressed():
                            break

            .. tab-item:: Q3

               Begin with the scale Am_4= [440, 494, 523, 587, 659, 698, 784, 880]. Use list comprehension to create a new list, Am_54_rev, which is the reverse of Am_4, excluding 880. Show an up arrow when Am_4 is played and a down arrow for Am_54_rev.

                .. code-block:: python

                    from microbit import *
                    import music

                    Am_4 = [440, 494, 523, 587, 659, 698, 784, 880]
                    Am_4_rev = [freq for freq in Am_4[::-1] if freq != 880]

                    timing = 400
                    while True:
                        display.show(Image.ARROW_N, wait=False)
                        for freq in Am_4:
                            music.pitch(freq, duration=timing)
                        display.show(Image.ARROW_S, wait=False)
                        for freq in Am_4_rev:
                            music.pitch(freq, duration=timing)
                        if button_a.was_pressed():
                            break

----

Accelerometer based pitches
-------------------------------

| The code below uses the accelerometer to choose the pitch and the note duration.
| The scale function is used to scale the tilting range to the length of the notes list and the length of the durations list.
| The pitches used are based on the E minor scale.

.. code-block:: python

    from microbit import *
    import music

    accelerometer.set_range(1)

    # A selection of E minor notes
    notes = [164.81, 185.00, 196.00, 220.00, 246.94,  # E3, F#3, G3, A3, B3
            329.63, 369.99, 392.00, 440.00, 493.88,  # E4, F#4, G4, A4, B4
            659.25, 739.99, 783.99, 880.00, 987.77,  # E5, F#5, G5, A5, B5
            1318.51, 1479.98, 1567.98, 1760.00, 1975.53]  # E6, F#6, G6, A6, B6

    # note lengths 4 ticks per beat or per 500ms
    durations = [125, 250, 500, 1000, 2000]

    durationlen = len(durations)
    notelen = len(notes)

    play_music = True
    while True:
        #use A to toggle music
        if button_a.was_pressed():
            play_music = not play_music
        if not play_music:
            continue
        #get accelerometer readings
        x_reading = abs(accelerometer.get_x())
        y_reading = abs(accelerometer.get_y())
        # use above 1023 incase some microbits give slightly higher readings
        scaled_x = scale(x_reading, from_=(-1200, 1200), to=(-notelen +1, notelen -1))
        scaled_y = scale(y_reading, from_=(-1200, 1200), to=(-durationlen +1, durationlen -1))
        #get a note based on tilt
        pitch = notes[scaled_x]
        duration = durations[scaled_y]
        music.pitch(int(pitch), duration)

----

.. admonition:: Exercise

    #. Use the accelerometer to control 8 pitches of a scale over just one octave.


