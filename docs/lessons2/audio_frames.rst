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

See: https://support.microbit.org/support/solutions/articles/19000125318-playing-audio-on-the-micro-bit


AudioFrames
---------------

.. py:class::
    AudioFrame

    An ``AudioFrame`` object is a list of 32 samples each of which is a whole number between 0 and 255 (unsigned byte).

    It takes just over 4 ms to play a single frame.

    .. py:function:: copyfrom(other)

        Overwrite the data in this ``AudioFrame`` with the data from another
        ``AudioFrame`` instance.

        :param other: ``AudioFrame`` instance from which to copy the data.


----

Advanced Technical Details
-----------------------------------

.. note::
    You don't need to understand this section to use the ``audio`` module.
    It is just here in case you wanted to know how it works.

The ``audio`` module can consume an iterable (sequence, like list or tuple, or
generator) of ``AudioFrame`` instances, each 32 samples at 7812.5 Hz, and uses
linear interpolation to output a PWM signal at 32.5 kHz, which gives tolerable
sound quality.

The function ``play`` fully copies all data from each ``AudioFrame`` before it
calls ``next()`` for the next frame, so a sound source can use the same
``AudioFrame`` repeatedly.

The ``audio`` module has an internal 64 sample buffer from which it reads
samples. When reading reaches the start or the mid-point of the buffer, it
triggers a callback to fetch the next ``AudioFrame`` which is then copied into
the buffer. This means that a sound source has under 4ms to compute the next
``AudioFrame``, and for reliable operation needs to take less 2ms (which is
32000 cycles, so should be plenty).

----

Advanced Example
-----------------

.. code-block:: python

    from microbit import *
    import audio
    import math


    def repeated_frame(frame, count):
        for i n range(count):
            yield frame


    # Press button-A to skip to next wave.
    def show_wave(name, frame, duration=1500):
        display.scroll(name + " wave", wait=False,delay=100)
        audio.play(repeated_frame(frame, duration),wait=False)
        for i in range(75):
            sleep(100)
            if button_a.is_pressed():
                display.clear()
                audio.stop()
                break


    frame = audio.AudioFrame()

    for i in range(len(frame)):
        frame[i] = int(math.sin(math.pi*i/16)*124+128.5)
    show_wave("Sine", frame)

    triangle = audio.AudioFrame()

    QUARTER = len(triangle)//4
    for i in range(QUARTER):
        triangle[i] = i*15
        triangle[i+QUARTER] = 248-i*15
        triangle[i+QUARTER*2] = 128-i*15
        triangle[i+QUARTER*3] = i*15+8
    show_wave("Triangle", triangle)

    square = audio.AudioFrame()

    HALF = len(square)//2
    for i in range(HALF):
        square[i] = 8
        square[i+HALF] = 248
    show_wave("Square", square)
    sleep(1000)

    for i in range(len(frame)):
        frame[i] = 252-i*8
    show_wave("Sawtooth", frame)

    del frame

    #Generate a waveform that goes from triangle to square wave, reasonably smoothly.
    frames = [ None ] * 32
    for i in range(32):
        frames[i] = frame = audio.AudioFrame()
        for j in range(len(triangle)):
            frame[j] = (triangle[j]*(32-i) + square[j]*i)>>5


    def repeated_frames(frames, count):
        for frame in frames:
            for i in range(count):
                yield frame


    display.scroll("Ascending wave", wait=False)
    audio.play(repeated_frames(frames, 60))

----
