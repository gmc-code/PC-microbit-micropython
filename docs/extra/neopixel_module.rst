==========================
neopixel module
==========================

.. py:module:: neopixel

The ``neopixel`` module lets you use NeoPixel (WS2812) individually addressable
RGB and RGBW LED strips with the microbit.

See: https://microbit-micropython.readthedocs.io/en/v2-docs/neopixel.html

----

Import module
-----------------

.. code-block:: python

    import neopixel


Initialise neopixels
-----------------------

.. py:class:: NeoPixel(pin, n, bpp=3)

    Initialise a new strip of ``n`` number of neopixel LEDs controlled via pin
    ``pin``.

    :param pin: The pin to which the NeoPixel strip is connected.
    :param n: The number of NeoPixel LEDs in the strip.
    :param bpp: The number of bytes per pixel. Default is ``3`` for RGB and GRB, and ``4`` for RGBW.

.. code-block:: python

    import neopixel

    np = neopixel.NeoPixel(pin0, 8)


set neopixel colours
----------------------------

| Each pixel is addressed by a position (starting from 0).
| Neopixels are given RGB (red, green, blue) values between 0-255 as a tuple.
| For example, in RGB, ``(255,255,255)`` is white.
| For RGBW, (red, green, blue, white), ``(255,255,255,0)`` or ``(0,0,0,255)`` is white.

Writing the colour doesn't update the display (use ``show()`` for that).

.. code-block:: python

    np[0] = (255, 0, 0)  # first pixel red
    np[-1] = (0, 255, 0)  # last pixel yellow
    np.show()  # display updated values

Show
------------

.. py:method:: show()

    Show the pixels. Must be called for any updates to become visible.

Get colour
-----------------

Get the colour of a specific pixel just reference it.

.. code::

    print(np[0])

Fill **V2**
------------

.. py:method:: fill(colour)

    Colour all pixels a given value.
    e.g. `fill((0,0,255))`

Clear
------------

.. py:method:: clear()

    Clear all the pixels.


Random pixel colours
------------------------

.. code-block:: python

    """
        Repeatedly displays random colours on the LED Neopixel strip on pin0 with a length of 8 pixels
    """
    from microbit import *
    import neopixel
    from random import randint

    # Setup the Neopixel strip on pin0 with a length of 8 pixels
    np = neopixel.NeoPixel(pin0, 8)

    while True:
        #Iterate over each LED in the strip

        for pixel_id in range(0, len(np)):
            red = randint(0, 60)
            green = randint(0, 60)
            blue = randint(0, 60)

            # Assign the current LED a random red, green and blue value between 0 and 60
            np[pixel_id] = (red, green, blue)

            # Display the current pixel data on the Neopixel strip
            np.show()
            sleep(100)


