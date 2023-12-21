==========================
Audio: SoundEffects **V2** 
==========================

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/audio.html
| For control of the speaker and volume in V2 see: 
| https://pc-microbit-micropython.readthedocs.io/en/latest/lessons2/music.html#v2-volume

----

main controls
---------------

.. py:function:: play(source, wait=True, pin=pin0)

    | Play the source of the sound.
    | ``source`` can be a built-in sound or a sound effect, or an iterable of sound effects, created via the audio.SoundEffect() class, or an iterable of AudioFrame elements.
    | If **wait** is ``True``, this function will block until the source has been completely played.
    | **pin** is on optional argument to specify the output pin with default of ``pin0``. Use ``pin=None`` to make no sound.


.. py:function:: is_playing()

    Returns ``True`` if audio is playing, otherwise returns ``False``.

.. py:function:: stop()

    Stops all audio playback.

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

----

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