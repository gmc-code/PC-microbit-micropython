====================================================
Move Motor LEDs
====================================================


| The Move Motor uses 4 ZIP LEDs (WS2812) on pin8.
| Each LED can produce a full spectrum of colours independent to all of the other LEDs on the bus. 
| Each ZIP LED has a Red, Green and Blue element within the LED, and each of these can achieve 256 levels of brightness.

NeoPixel module
-----------------

| The neopixel module allows use of WS2812 individually addressable RGB LEDs with the micro:bit. 
| First, import the neopixel library.

.. code-block:: python

    from microbit import *

----


    import neopixel

.. py:module:: neopixel



Setup LEDs
----------------------------------------

.. py:class:: NeoPixel(pin, n)

    | Initialise a strip of neopixel LEDs 
    | ``pin`` is the pin that they are connected by.
    | ``n`` is the number of LEDs


.. code-block:: python

    from microbit import *


    import neopixel


.. py:method:: clear()

        Clear all the pixels.


.. py:method:: show()

        Show the pixels. Must be called for any updates to become visible.

    | Each pixel is addressed by a position (starting from 0). 
    | Neopixels are given RGB (red, green, blue) values between 0-255 as a tuple. 
    | For example, ``(255,255,255)`` is white.


Operations
==========

Writing the colour doesn't update the display (use ``show()`` for that).

.. code-block:: python

    from microbit import *


    import neopixel

    np[0] = (255, 0, 128)  # first element
    np[-1] = (0, 255, 0)  # last element
    np.show()  # only now will the updated value be shown

To read the colour of a specific pixel just reference it.

.. code::

    print(np[0])

Using Neopixels
---------------------

| Interact with Neopixels as if they were a list of tuples. 
| Each tuple represents the RGB (red, green and blue) mix of colours for a specific pixel. 
| The RGB values can range between 0 to 255.

For example, initialise a strip of 8 neopixels on a strip connected to pin0
like this::

    import neopixel
    np = neopixel.NeoPixel(pin0, 8)

Set pixels by indexing them (like with a Python list). For instance, to
set the first pixel to full brightness red, you would use::

    np[0] = (255, 0, 0)

Or the final pixel to purple::

    np[-1] = (255, 0, 255)

Get the current colour value of a pixel by indexing it. For example, to print
the first pixel's RGB value use::

    print(np[0])

Finally, to push the new colour data to your Neopixel strip, use the .show()
function::

    np.show()

If nothing is happening, it's probably because you've forgotten this final
step..!

.. note::

    If you're not seeing anything change on your Neopixel strip, make sure
    you have ``show()`` at least somewhere otherwise your updates won't be
    shown.

Example
=======

    Repeatedly displays random colours onto the LED strip.
    This example requires a strip of 8 Neopixels (WS2812) connected to pin0.

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