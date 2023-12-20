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




