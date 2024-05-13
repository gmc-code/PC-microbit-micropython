==========================
Audio
==========================

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/audio.html
| For control of the speaker and volume in V2 see: 
| https://pc-microbit-micropython.readthedocs.io/en/latest/lessons2/music.html#v2-volume

----

Audio Library
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
    | ``source`` can be a **built-in sound** or a **sound effect**, or an iterable of sound effects, created via the audio.SoundEffect() class, or an iterable of **AudioFrame** elements.
    | If **wait** is ``True``, this function will block until the source has been completely played.
    | **pin** is on optional argument to specify the output pin with default of ``pin0``. Use ``pin=None`` to make no sound.


.. py:function:: is_playing()

    Returns ``True`` if audio is playing, otherwise returns ``False``.

.. py:function:: stop()

    Stops all audio playback. This would be useful if ``wait=False`` such that the sound playing is non blocking. 
