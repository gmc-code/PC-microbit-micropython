==========================
Audio
==========================

| See: `<https://microbit-micropython.readthedocs.io/en/stable/audio.html>`
| For control of the speaker and volume in V2 see:
| `<https://pc-microbit-micropython.readthedocs.io/en/latest/lessons2/music.html>`#v2-volume

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

**V2** Built-in sounds
------------------------

The built-in sounds can be called using ``audio.play(Sound.NAME)``.

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
| The A-button can be pressed to exit the for-loop then the while-loop using ``break``.
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
    #. Use the choice function to randomly pick a built-in sound from a sound list. See: `<https://www.w3schools.com/python/ref_random_choice.asp. Use button pressing to break out of the while-loop to stop playing sounds.

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

                    sound_list = [Sound.SAD, Sound.HAPPY, Sound.YAWN,]
                    for sound in sound_list:
                        audio.play(sound)
                        sleep(1000)

            .. tab-item:: Q2

                Use the choice function to randomly pick a built-in sound from a sound list. See: `<https://www.w3schools.com/python/ref_random_choice.asp. Use button pressing to break out of the while-loop to stop playing sounds.

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


