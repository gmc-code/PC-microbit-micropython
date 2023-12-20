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
    | ``source`` can be a built-in sound or a sound effect, or an iterable of sound effects, created via the audio.SoundEffect() class, or an iterable of AudioFrame elements.
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

Sound Effects **V2**
------------------------------------

.. py:class::
    SoundEffect(freq_start=500, freq_end=2500, duration=500, vol_start=255, vol_end=0, waveform=WAVEFORM_SQUARE, fx=FX_NONE, shape=SHAPE_LOG)

    An ``SoundEffect`` instance represents a sound effect, composed by a set of
    parameters configured via the constructor or attributes.

    All the parameters are optional, with default values as shown above, and
    they can all be modified via attributes of the same name. For example, we
    can first create an effect ``my_effect = SoundEffect(duration=1000)``,
    and then change its attributes ``my_effect.duration = 500``.

    :param freq_start: Start frequency in Hertz (Hz), default: ``500``
    :param freq_end: End frequency in Hertz (Hz), default: ``2500``
    :param duration: Duration of the sound (ms), default: ``500``
    :param vol_start: Start volume value, range 0-255, default: ``255``
    :param vol_end: End volume value, range 0-255, default: ``0``
    :param waveform: Type of waveform shape, one of these values:
        ``WAVEFORM_SINE``, ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``,
        ``WAVEFORM_SQUARE``, ``WAVEFORM_NOISE`` (randomly generated noise).
        Default: ``WAVEFORM_SQUARE``
    :param fx: Effect to add on the sound, one of the following values:
        ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, or ``FX_NONE``.
        Default: ``FX_NONE``
    :param shape: The type of the interpolation curve between the start and end
        frequencies, different wave shapes have different rates of change
        in frequency. One of the following values: ``SHAPE_LINEAR``,
        ``SHAPE_CURVE``, ``SHAPE_LOG``. Default: ``SHAPE_LOG``

    .. py:function:: copy()

        :returns: A copy of the SoundEffect.

    .. py:attribute:: freq_start

        Start frequency in Hertz (Hz), a number between ``0`` and ``9999``.

    .. py:attribute:: freq_end

        End frequency in Hertz (Hz), a number between ``0`` and ``9999```.

    .. py:attribute:: duration

        Duration of the sound in milliseconds, a number between ``0`` and
        ``9999``.

    .. py:attribute:: vol_start

        Start volume value, a number between ``0`` and ``255``.

    .. py:attribute:: vol_end

        End volume value, a number between ``0`` and ``255``.

    .. py:attribute:: waveform

        Type of waveform shape, one of these values: ``WAVEFORM_SINE``,
        ``WAVEFORM_SAWTOOTH``, ``WAVEFORM_TRIANGLE``, ``WAVEFORM_SQUARE``,
        ``WAVEFORM_NOISE`` (randomly generated noise).

    .. py:attribute:: fx

        Effect to add on the sound, one of the following values:
        ``FX_TREMOLO``, ``FX_VIBRATO``, ``FX_WARBLE``, or ``None``.

    .. py:attribute:: shape

        The type of interpolation curve between the start and end
        frequencies, different wave shapes have different rates of change
        in frequency. One of the following values: ``SHAPE_LINEAR``,
        ``SHAPE_CURVE``, ``SHAPE_LOG``.

The arguments used to create any Sound Effect,
can be inspected by looking at each of the SoundEffect instance attributes,
or by converting the instance into a string (which can be done via ``str()``
function, or by using a function that does the conversion automatically like
``print()``).

For example, with the :doc:`REPL </devguide/repl>` you can inspect the
default SoundEffects::

    >>> print(audio.SoundEffect())
    SoundEffect(freq_start=500, freq_end=2500, duration=500, vol_start=255, vol_end=0, waveform=WAVE_SQUARE, fx=FX_NONE, shape=SHAPE_LOG)

This format is "human readable", which means it is easy for us to read,
and it looks very similar to the code needed to create that SoundEffect,
but it's not quite right. The ``repr()`` function can be used to create a
string of Python code that can be stored or transferred
(you could transmit sounds via micro:bit radio!) and be executed with the
``eval()`` function::

    >>> from audio import SoundEffect
    >>> sound_code = repr(SoundEffect())
    >>> print(sound_code)
    SoundEffect(500, 2500, 500, 255, 0, 3, 0, 18)
    >>> eval("audio.play({})".format(sound_code))

Sound Effects Example
---------------------

 .. code-block:: python
    
    from microbit import *


    # Play the default Sound Effect
    audio.play(audio.SoundEffect())

    # Create a new Sound Effect and immediately play it
    audio.play(audio.SoundEffect(
        freq_start=400,
        freq_end=2000,
        duration=500,
        vol_start=100,
        vol_end=255,
        waveform=audio.SoundEffect.WAVEFORM_TRIANGLE,
        fx=audio.SoundEffect.FX_VIBRATO,
        shape=audio.SoundEffect.SHAPE_LOG
    ))

    # Play a Sound Effect instance, modify an attribute, and play it again
    my_effect = audio.SoundEffect(
        freq_start=400,
        freq_end=2000,
    )
    audio.play(my_effect)
    my_effect.duration = 1000
    audio.play(my_effect)

    # You can also create a new effect based on an existing one, and modify
    # any of its characteristics via arguments
    my_modified_effect = my_effect.copy()
    my_modified_effect.waveform = audio.SoundEffect.WAVEFORM_NOISE
    audio.play(my_modified_effect)

    # Use sensor data to modify and play an existing Sound Effect instance
    my_effect.duration = 600
    while True:
        # int() might be temporarily needed: https://github.com/microbit-foundation/micropython-microbit-v2/issues/121
        my_effect.freq_start = int(scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 9999)))
        my_effect.freq_end = int(scale(accelerometer.get_y(), from_=(-2000, 2000), to=(0, 9999)))
        audio.play(my_effect)

        if button_a.is_pressed():
            # Button A silences the micro:bit
            speaker.off()
            display.show(Image("09090:00000:00900:09990:00900"))
            sleep(500)
        elif button_b.is_pressed():
            # Button B re-enables the speaker & plays an effect while showing an image
            speaker.on()
            audio.play(audio.SoundEffect(), wait=False)
            display.show(Image.MUSIC_QUAVER)
            sleep(500)

        sleep(150)

----

**AudioFrame**
------------------

| An AudioFrame object is a list of 32 samples each of which is an unsigned byte (whole number between 0 and 255).
| It takes just over 4 ms to play a single frame.
| ``audio.play`` requires an iterable (a list or generator) of **AudioFrame** instances, each 32 samples at 7812.5 Hz, and uses linear interpolation to output a PWM signal at 32.5 kHz, which gives tolerable sound quality.
| Use ``frame = audio.AudioFrame()`` to create the audioframe object. 
| Use ``frame[i] = ...`` to fill all 32 samples as i changes from 0 to 31.
| The sawtooth values below go down by 8 each sample: [252,244,236,...,20,12,4].

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
| The function, ``repeated_frame``, uses a generator (yield keyword) to create an iterable object. This means it generates each repetition on-the-fly each time you iterate over it, which is more memory-efficient than creating a large list or other collection. This is especially useful if count is a large number.

.. code-block:: python
        
    def repeated_frame(frame, count):
        # use a generator to reduce memory usage
        for i in range(count):
            yield frame

| Final code that plays a sawtooth audioframe for about 2 seconds:

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

    repeat_count = 100
    sawtooth_frame = get_sawtooth_frame()

    while True:
        if button_a.is_pressed():
            play_rep_frame("saw", sawtooth_frame, repeat_count)
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