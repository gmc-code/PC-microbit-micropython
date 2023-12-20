==========================
Audio
==========================

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/audio.html
| For control of the speaker and volume in V2 see: 
| https://pc-microbit-micropython.readthedocs.io/en/latest/lessons2/music.html#v2-volume

----

Library
----------------------------------------

.. py:module:: audio

| This module allows you play sounds with the microbit.
| Put ``import audio`` at the top under ``from microbit import *``.
| By default, sound output will be via the edge connector on pin 0 and the built-in speaker in V2.

.. code-block:: python

    from microbit import *
    import audio

----

main controls
---------------

.. py:function:: play(source, wait=True, pin=pin0)

    | Play the source of the sound.
    | ``source`` can be a built-in sound or an iterable of AudioFrame elements.
    | If **wait** is ``True``, this function will block until the source has been completely played.
    | **pin** is on optional argument to specify the output pin with default of ``pin0``. Use ``pin=None`` to make no sound.


.. py:function:: is_playing()

    | Returns ``True`` if audio is playing, otherwise returns ``False``.

.. py:function:: stop()

    Stops all audio playback.

----

**V2** Expressive sounds 
--------------------------

| The built-in expressive sounds can be called using ``audio.play(Sound. ...)``.
| e.g. ``audio.play(Sound.GIGGLE)``

* ``Sound.GIGGLE``
* ``Sound.HAPPY``
* ``Sound.HELLO``
* ``Sound.MYSTERIOUS``
* ``Sound.SAD``
* ``Sound.SLIDE``
* ``Sound.SOARING``
* ``Sound.SPRING``
* ``Sound.TWINKLE``
* ``Sound.YAWN``


.. code-block:: python

    from microbit import *
    import audio

    audio.play(Sound.GIGGLE)


| The code below uses a for-loop to loop through each Sound in the ``sound_list`` and play it.

.. code-block:: python

    from microbit import *
    import audio

    sound_list = [Sound.GIGGLE, Sound.TWINKLE]
    for sound in sound_list:
        audio.play(sound)

----

All Built in sounds
----------------------------------------

| The code below plays all the built-in sounds.
| The A button can be pressed to exit the for-loop then the while loop using ``break``.
| Pressing the reset button on the back of the microbit will restart the code.

.. code-block:: python

    from microbit import *
    import audio

    built_in_sounds = [
        Sound.GIGGLE,
        Sound.HAPPY,
        Sound.HELLO,
        Sound.MYSTERIOUS,
        Sound.SAD,
        Sound.SLIDE,
        Sound.SOARING,
        Sound.SPRING,
        Sound.TWINKLE,
        Sound.YAWN,
    ]
 
    while True:
        for sound in built_in_sounds:
            audio.play(sound)
            sleep(1000)
            if button_a.is_pressed():
                break
        if button_a.is_pressed():
            break

----

.. admonition:: Tasks

    #. Play any 3 built-in sounds using a list, separating them with a 1 second pause.
    #. Use the choice function to randomly pick a built-in sound from a sound list. See: https://www.w3schools.com/python/ref_random_choice.asp. Use button pressing to break out of the while loop to stop playing sounds.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play any 3 built-in sounds using a list, separating them with a 1 second pause.

                .. code-block:: python

                    from microbit import *
                    import audio

                    sound_list = [Sound.SAD, Sound.HAPPY, Sound.YAWN]
                    for sound in sound_list:
                        audio.play(sound)
                        sleep(1000)

            .. tab-item:: Q2

                Use the choice function to randomly pick a built-in sound from a sound list. See: https://www.w3schools.com/python/ref_random_choice.asp. Use button pressing to break out of the while loop to stop playing sounds.

                .. code-block:: python

                    from microbit import *
                    import audio
                    from random import choice as rand_choice

                    sound_list = [Sound.SAD, Sound.HAPPY, Sound.YAWN]

                    while True:
                        audio.play(rand_choice(sound_list))
                        sleep(1000)
                        if button_a.is_pressed():
                            break

----

**AudioFrame**
------------------

| An AudioFrame object is a list of 32 samples each of which is an unsigned byte (whole number between 0 and 255).
| It takes just over 4 ms to play a single frame.
| ``audio.play`` requires an iterable (a list or generator) of **AudioFrame** instances, each 32 samples at 7812.5 Hz, and uses linear interpolation to output a PWM signal at 32.5 kHz, which gives tolerable sound quality.
| Use ``frame = audio.AudioFrame()`` to create the audioframe object. 
| Use ``frame[i] = ...`` to fill all 32 samples as i changes from 0 to 31.
| The sawtooth values below go down by 8 each sample: [252,244,236,228,220,212,204,196,188,180,172,164,156,148,140,132,124,116,108,100,92,84,76,68,60,52,44,36,28,20,12,4].

| Since an audio frame only goes for 4ms, it needs to be repeated 250 times to last for 1 second.
| If it is repeated in a list, as in ``repeated_frame1`` below, the size is limited to about 8000 iterations (about 20seconds).

.. code-block:: python
        
    def repeated_frame1(frame, count):
        # will hit a memory problem after about 8000 repeats
        wave = []
        for i in range(count):
            wave.append(frame)
        return wave

| Generators are used in this case to avoid memory issues.
| Use ``yield`` in the for-loop to create a generator that releases each repeat of the ``frame`` as it is needed in the calling code.

.. code-block:: python
        
    def repeated_frame(frame, count):
        # use a generator to reduce memory usage
        for i in range(count):
            yield frame

| Final code that plays a sawtooth audioframe for about 2 seconds:

.. code-block:: python
        
    from microbit import *
    import audio


    def get_sawtooth_frame():
        frame = audio.AudioFrame()
        # len = 32
        for i in range(len(frame)):
            frame[i] = int(252 - i * 8)
        return frame

    def repeated_frame(frame, count):
        # use a generator to reduce memory usage
        for i in range(count):
            yield frame

    def play_wave(name, wave, cycles):
        display.scroll(name + " wave", wait=False, delay=80)
        audio.play(wave, wait=False)
        for i in range(cycles):
            if button_b.is_pressed():
                display.scroll("")
                audio.stop()
                break
            sleep(4)


    cycles = 500
    sawtooth_frame = get_sawtooth_frame()
    sawtooth_wave = repeated_frame(sawtooth_frame, cycles)

    while True:
        if button_a.is_pressed():
            play_wave("Sawtooth", sawtooth_wave, cycles)
        sleep(100)


----

Common AudioFrame structures
-----------------------------------

| Sawtooth, square and triangle audioframes are constructed and played below.

.. code-block:: python
        
    from microbit import *
    import audio


    def play_rep_frame(name, frame, count):
        wave = repeated_frame(frame, count)
        while audio.is_playing():
            sleep(4)
            audio.stop()
        display.scroll(name, wait=False, delay=60)
        audio.play(wave, wait=False)
        
    def repeated_frame(frame, count):
        # use a generator to reduce memory usage
        for i in range(count):
            yield frame

    def get_sawtooth_frame():
        frame = audio.AudioFrame()
        # len = 32
        for i in range(len(frame)):
            frame[i] = int(252 - i * 8)
        return frame


    def get_sawtooth2_frame():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            if i < len(frame) // 2:
                frame[i] = int(252 - i * 16)
            else:
                frame[i] = int(252 - (i - 16) * 16)
        return frame

    def get_square_frame():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            if i < len(frame) // 2:
                frame[i] = 252
            else:
                frame[i] = 0
        return frame
        
    def get_square2_frame():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            if i < len(frame) // 4:
                frame[i] = 252
            elif i < len(frame) * 2 // 4:
                frame[i] = 0
            elif i < len(frame) * 3 // 4:
                frame[i] = 252
            else:
                frame[i] = 0
        return frame

    def get_triangle_frame():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            if i < len(frame) // 2:
                frame[i] = i * 8
            else:
                frame[i] = 252 - (i - 16) * 8
        return frame
        
    def get_triangle2_frame():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            if i < len(frame) // 4:
                frame[i] = i * 16
            elif i < len(frame) * 2 // 4:
                frame[i] = 252 - (i - 8) * 16
            elif i < len(frame) * 3 // 4:
                frame[i] = (i - 16) * 16
            else:
                frame[i] = 252 - (i - 24) * 16
        return frame

    repeat_count = 100
    sawtooth_frame = get_sawtooth_frame()
    sawtooth2_frame = get_sawtooth2_frame()
    square_frame = get_square_frame()
    square2_frame = get_square2_frame()
    triangle_frame = get_triangle_frame()
    triangle2_frame = get_triangle2_frame()

    while True:
        if pin_logo.is_touched():
            play_rep_frame("saw", sawtooth_frame, repeat_count)
            sleep(repeat_count * 5)
            play_rep_frame("saw2", sawtooth2_frame, repeat_count)
        elif button_a.is_pressed():
            play_rep_frame("sqr", square_frame, repeat_count)
            sleep(repeat_count * 5)
            play_rep_frame("sqr2", square2_frame, repeat_count)
        elif button_b.is_pressed():
            play_rep_frame("tri", triangle_frame, repeat_count)
            sleep(repeat_count * 5)
            play_rep_frame("tri2", triangle2_frame, repeat_count)
        sleep(100)