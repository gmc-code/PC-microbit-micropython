==========================
Audio: SoundEffects **V2** 
==========================

Sound Effect Syntax
------------------------------------

.. py:class::
    audio.SoundEffect(freq_start=500, freq_end=2500, duration=500, vol_start=255, vol_end=0, waveform=audio.SoundEffect.WAVEFORM_SQUARE, fx=audio.SoundEffect.FX_NONE, shape=audio.SoundEffect.SHAPE_LOG)

     ``SoundEffect`` instance represents a sound effect. 

    :param freq_start: Start frequency in Hertz (Hz), range 0-9999, default: ``500``
    :param freq_end: End frequency in Hertz (Hz), , range 0-9999, default: ``2500``
    :param duration: Duration of the sound (ms), , range 0-9999, default: ``500``
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

| The parameter values can all be modified via attributes of the same name. 
| For example, first create an effect ``my_effect = SoundEffect(duration=1000)``,
and then change its attribute for duration: ``my_effect.duration = 500``.

----

Vary frequencies
---------------------

| The code below plays different sound effects by pressing the A or B button on the microbit. 
| The sound effect's frequency sweep goes from low to high when the A button is pressed, and from high to low when the B button is pressed.

----

| When the A button is pressed, the start frequency is increased in steps while the end frequency is kept the same.

.. code-block:: python
    
    from microbit import *
    import audio

    sound_effect = audio.SoundEffect()  # use defaults
    # SoundEffect(freq_start=500, freq_end=2500, duration=500, vol_start=255, vol_end=0, waveform=WAVEFORM_SQUARE, fx=FX_NONE, shape=SHAPE_LOG)
    while True:
        if button_a.is_pressed():
            sound_effect.freq_start = 880 - (100 * 4)
            sound_effect.freq_end = 880
            for freq_step in range(4):
                sound_effect.freq_start += 100
                audio.play(sound_effect, wait=True)                                           
                sleep(100)
        sleep(50)

----

.. admonition:: Tasks

    #. Modify the code above to so that when the B button is pressed, the start frequency is kept the same while the end frequency is increased in steps.
    #. Use both the A and B-button pressing code and replace all values with variables: ``base_freq``, ``step_size``, ``steps``.
    #. Modify the code above to use definitions with parameters. Name the def block, ``increase_freq``, for A-buuton pressing and  ``decrease_freq``, for B-buuton pressing.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above to so that when the B button is pressed, the start frequency is kept the same while the end frequency is increased in steps.

                .. code-block:: python
                    
                    from microbit import *
                    import audio

                    sound_effect = audio.SoundEffect()  # use defaults
                    # SoundEffect(freq_start=500, freq_end=2500, duration=500, vol_start=255, vol_end=0, waveform=WAVEFORM_SQUARE, fx=FX_NONE, shape=SHAPE_LOG)
                    base_freq = 880
                    step_size = 100
                    steps = 4
                    while True:
                        if button_b.is_pressed():
                            sound_effect.freq_start = 880
                            sound_effect.freq_end = 880 - (100 * 4)
                            for freq_step in range(4):
                                audio.play(sound_effect, wait=True)                                           
                                sound_effect.freq_end += 100
                                sleep(100)
                        sleep(50)
                    
            .. tab-item:: Q2

                Use both the A and B-button pressing code and replace all values with variables: ``base_freq``, ``step_size``, ``steps``.

                .. code-block:: python
                    
                    from microbit import *
                    import audio

                    sound_effect = audio.SoundEffect()  # use defaults
                    # SoundEffect(freq_start=500, freq_end=2500, duration=500, vol_start=255, vol_end=0, waveform=WAVEFORM_SQUARE, fx=FX_NONE, shape=SHAPE_LOG)
                    base_freq = 880
                    step_size = 100
                    steps = 4
                    while True:
                        if button_a.is_pressed():
                            sound_effect.freq_start = base_freq - (step_size * steps)
                            sound_effect.freq_end = base_freq
                            for freq_step in range(steps):
                                audio.play(sound_effect, wait=True)                                           
                                sound_effect.freq_start += step_size
                                sleep(100)
                        elif button_b.is_pressed():
                            sound_effect.freq_start = base_freq
                            sound_effect.freq_end = base_freq - (step_size * steps)
                            for freq_step in range(steps):
                                audio.play(sound_effect, wait=True)                                           
                                sound_effect.freq_end += step_size
                                sleep(100)
                        sleep(50)

            .. tab-item:: Q3

                Modify the code above to use definitions with parameters. Name the def block, ``increase_freq``, for A-buuton pressing and ``decrease_freq``, for B-buuton pressing.

                .. code-block:: python

                    from microbit import *
                    import audio


                    def increase_freq(sound_effect, base_freq, step_size, steps):
                        sound_effect.freq_start = base_freq - (step_size * steps)
                        sound_effect.freq_end = base_freq
                        for freq_step in range(steps):
                            audio.play(sound_effect, wait=True)
                            sound_effect.freq_start += step_size                                       
                            sleep(100)

                    def decrease_freq(sound_effect, base_freq, step_size, steps):
                        sound_effect.freq_start = base_freq
                        sound_effect.freq_end = base_freq - (step_size * steps)
                        for freq_step in range(steps):
                            audio.play(sound_effect, wait=True)
                            sound_effect.freq_end += step_size                                     
                            sleep(100)

                    sound_effect = audio.SoundEffect()  # use defaults
                    # SoundEffect(freq_start=500, freq_end=2500, duration=500, vol_start=255, vol_end=0, waveform=WAVEFORM_SQUARE, fx=FX_NONE, shape=SHAPE_LOG)
                    base_freq = 880
                    step_size = 100
                    steps = 4

                    while True:
                        if button_a.is_pressed():
                            increase_freq(sound_effect, base_freq, step_size, steps)
                        elif button_b.is_pressed():
                            decrease_freq(sound_effect, base_freq, step_size, steps)
                        sleep(50)

----  

Vary the waveform
--------------------

| The code below plays sounds based on the default sound effect.
| When the A button is pressed, each of the different waveforms is tried.
| Which waveforms sound similar?

.. code-block:: python
    
    from microbit import *
    import audio

    sound_effect = audio.SoundEffect()  # use defaults
    waveform_list = [audio.SoundEffect.WAVEFORM_SINE, audio.SoundEffect.WAVEFORM_SAWTOOTH,
                     audio.SoundEffect.WAVEFORM_TRIANGLE, audio.SoundEffect.WAVEFORM_SQUARE,
                     audio.SoundEffect.WAVEFORM_NOISE]

    while True:
        if button_a.is_pressed():
            for waveform_choice in waveform_list:
                sound_effect.waveform = waveform_choice
                audio.play(sound_effect, wait=True)                                           
                sleep(500)
        sleep(50)

----

microbit scale function
-------------------------

.. py:function:: scale(value, from_, to)

    Converts a value from a range to another range.

    :param value: A number to convert.
    :param from_: A tuple to define the range to convert from.
    :param to: A tuple to define the range to convert to.

    :returns: The ``value`` (float or int; int returned if both to vlaeus are integers) converted to the ``to`` range.

    e.g. scaled_value = scale(200, from_=(0,255), to=(0, 10))


----

.. admonition:: Tasks

    #. Modify the code above to use the x-tilt of the microbit to choose the waveform to use from the list. Use the scale function to scale the x accelerometer readings to integers form 0 to 4.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above use the x-tilt of the microbit to choose the waveform to use from the list. Use the scale function to scale the x accelerometer readings to integers form 0 to 4.

                .. code-block:: python
                    
                    from microbit import *
                    import audio

                    sound_effect = audio.SoundEffect()  # use defaults
                    waveform_list = [audio.SoundEffect.WAVEFORM_SINE, audio.SoundEffect.WAVEFORM_SAWTOOTH,
                                    audio.SoundEffect.WAVEFORM_TRIANGLE, audio.SoundEffect.WAVEFORM_SQUARE,
                                    audio.SoundEffect.WAVEFORM_NOISE]

                    while True:
                        if button_a.is_pressed():
                            xreading = abs(accelerometer.get_x())
                            waveform_index = scale(accelerometer.get_x(), from_=(-1023, 1023), to=(0, 4))
                            sound_effect.waveform = waveform_list[waveform_index]
                            audio.play(sound_effect, wait=True)                                           
                            sleep(500)
                        sleep(50)
    
----

Vary the fx
----------------

| The code below plays sounds based on the default sound effect.
| When the A button is pressed, each of the different add on effects is tried.

.. code-block:: python
    
    from microbit import *
    import audio

    sound_effect = audio.SoundEffect()  # use defaults
    fx_list =[audio.SoundEffect.FX_TREMOLO, audio.SoundEffect.FX_VIBRATO, 
                audio.SoundEffect.FX_WARBLE, audio.SoundEffect.FX_NONE]

    while True:
        if button_a.is_pressed():
            for fx_choice in fx_list:
                sound_effect.fx = fx_choice
                audio.play(sound_effect, wait=True)                                           
                sleep(500)
        sleep(50)

----

Copying sound effects
---------------------------

| Copying a sound effects can be useful when a second sound effect is to be based on another.

.. py:function:: copy()

    :returns: A copy of the SoundEffect.

----

| The code below specifies a sound effect, snd_effect1, start and end frequencies.
| snd_effect1 si copied to snd_effect2, which is then modified.
| A and B-buttons are used to play the 2 sound effects.

 .. code-block:: python
    
    from microbit import *
    import audio

    # Create a new Sound Effect and immediately play it
    snd_effect1 = audio.SoundEffect(freq_start=300, freq_end=1200)

    snd_effect2 = snd_effect1.copy()
    snd_effect2.freq_start = 2100
    snd_effect2.waveform=audio.SoundEffect.WAVEFORM_SAWTOOTH

    while True:
        if button_a.is_pressed():
            # the A-button silences the micro:bit
            audio.play(snd_effect1, wait=False)
            sleep(500)
        elif button_b.is_pressed():
            # B-button re-enables the speaker & plays an effect while showing an image
            audio.play(snd_effect2, wait=False)
            sleep(500)
        sleep(50)

----

Custom sound effects
--------------------------

| The code below plays the custom sound effects when the A-button is pressed.

 .. code-block:: python
    
    from microbit import *
    import audio


    laser = audio.SoundEffect(freq_start=1600, freq_end=1, duration=300, 
                            vol_start=255, vol_end=0, 
                            waveform=audio.SoundEffect.WAVEFORM_SQUARE, 
                            fx=audio.SoundEffect.FX_NONE, 
                            shape=audio.SoundEffect.SHAPE_CURVE)

    radio = audio.SoundEffect(freq_start=500, freq_end=499, duration=750, 
                            vol_start=255, vol_end=0, 
                            waveform=audio.SoundEffect.WAVEFORM_NOISE, 
                            fx=audio.SoundEffect.FX_NONE, 
                            shape=audio.SoundEffect.SHAPE_LINEAR)

    jump = audio.SoundEffect(freq_start=400, freq_end=600, duration=100, 
                            vol_start=255, vol_end=0, 
                            waveform=audio.SoundEffect.WAVEFORM_SQUARE, 
                            fx=audio.SoundEffect.FX_WARBLE, 
                            shape=audio.SoundEffect.SHAPE_LINEAR)

    water_drop = audio.SoundEffect(freq_start=200, freq_end=600, duration=150, 
                                vol_start=255, vol_end=0, 
                                waveform=audio.SoundEffect.WAVEFORM_SINE, 
                                fx=audio.SoundEffect.FX_NONE, 
                                shape=audio.SoundEffect.SHAPE_LINEAR)

    kick_drum = audio.SoundEffect(freq_start=200, freq_end=1, duration=100, 
                                vol_start=255, vol_end=0, 
                                waveform=audio.SoundEffect.WAVEFORM_SQUARE, 
                                fx=audio.SoundEffect.FX_NONE, 
                                shape=audio.SoundEffect.SHAPE_CURVE)

    tom = audio.SoundEffect(freq_start=300, freq_end=200, duration=75, 
                            vol_start=255, vol_end=0, 
                            waveform=audio.SoundEffect.WAVEFORM_TRIANGLE, 
                            fx=audio.SoundEffect.FX_NONE, 
                            shape=audio.SoundEffect.SHAPE_CURVE)

    snare = audio.SoundEffect(freq_start=523, freq_end=1, duration=100, 
                            vol_start=255, vol_end=0, 
                            waveform=audio.SoundEffect.WAVEFORM_NOISE, 
                            fx=audio.SoundEffect.FX_WARBLE, 
                            shape=audio.SoundEffect.SHAPE_LOG)

    hi_hat = audio.SoundEffect(freq_start=500, freq_end=1, duration=10, 
                            vol_start=255, vol_end=0, 
                            waveform=audio.SoundEffect.WAVEFORM_NOISE, 
                            fx=audio.SoundEffect.FX_NONE, 
                            shape=audio.SoundEffect.SHAPE_LINEAR)

    cowbell = audio.SoundEffect(freq_start=500, freq_end=500, duration=50, 
                                vol_start=255, vol_end=0, 
                                waveform=audio.SoundEffect.WAVEFORM_SINE, 
                                fx=audio.SoundEffect.FX_VIBRATO, 
                                shape=audio.SoundEffect.SHAPE_LINEAR)

    triangle = audio.SoundEffect(freq_start=54, freq_end=54, duration=500, 
                                vol_start=255, vol_end=0, 
                                waveform=audio.SoundEffect.WAVEFORM_NOISE, 
                                fx=audio.SoundEffect.FX_NONE, 
                                shape=audio.SoundEffect.SHAPE_LINEAR)

    sound_names = [laser, radio, jump, water_drop, kick_drum, tom, snare, hi_hat, cowbell, triangle]

    while True:
        if button_a.is_pressed():
            for snd in sound_names:
                audio.play(snd, wait=True)                                           
                sleep(500)
        sleep(50)
        
.. admonition:: Exercsie

    #. Put some of the custom sounds in a new order and play them on button pressing.

----

Transferring Sound Effects
----------------------------------------

| The ``repr()`` function can be used to create a string of Python code that can be stored or transferred
(you could transmit sounds via micro:bit radio!) and be executed with the ``eval()`` function.
| SoundEffect(500, 2500, 500, 255, 0, 3, 0, 18)


.. code-block:: python

    from microbit import *
    from audio import SoundEffect

    sound_code = repr(SoundEffect())  # SoundEffect(500, 2500, 500, 255, 0, 3, 0, 18)
    print(sound_code)
    eval("audio.play({})".format(sound_code))

