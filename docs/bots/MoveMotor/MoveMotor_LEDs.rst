====================================================
MoveMotor LEDs
====================================================

| The MOVEMotor uses 4 ZIP LEDs (WS2812) on pin8.
| The neopixel module is used to drive these RGB LEDs.
| Each LED can produce a full spectrum of colours independent to all of the other LEDs. 
| Each ZIP LED has a Red, Green and Blue element within the LED, and each of these can have brightness from 0 to 255.

NeoPixel module
-----------------

| The neopixel module allows use of multiple RGB LEDs connected to one pin so that each can have their own colour and brightness set.
| First, import the neopixel library with ``import neopixel``.

.. code-block:: python

    from microbit import *
    import neopixel


Setup LEDs
----------------------------------------

.. py:method:: neopixel.NeoPixel(pin, n)

    | Initialise a strip of RGB LEDs 
    | ``pin`` is the pin that they are connected by.
    | ``n`` is the number of LEDs

| The code below sets up 4 LEDs connected to pin0 via: ``np = neopixel.NeoPixel(pin0, 4)``.
| The variable, np, is then used to control the LEDs.

.. code-block:: python

    from microbit import *


    import neopixel
    np = neopixel.NeoPixel(pin0, 4)


| Each LED is addressed by a position (starting from 0). 
| Neopixels are given RGB (red, green, blue) values between 0-255 as a tuple. 
| For example, ``(255,255,255)`` is white.


.. py:method:: clear()

        Clear all the LEDs.


.. py:method:: show()

        Show the LEDs using their colour settings. This must be called for any updates to teh LEDs to become visible.



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
---------

| Repeatedly displays random colours onto the LED strip.
| This example requires a strip of 4 Neopixels (WS2812) connected to pin0.

.. code-block:: python

    from microbit import *
    import neopixel
    from random import randint

    # Setup the Neopixel strip on pin0 with a length of 4 pixels
    np = neopixel.NeoPixel(pin0, 48)

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

----

| Repeatedly display random colours on the 4 LEDs connected to pin8.

.. code-block:: python

    from microbit import *
    import neopixel
    import random


    # Setup the Neopixel strip on pin8 with a length of 4 pixels
    NUM_PIXELS = 4
    LED_PIN = pin8
    np = neopixel.NeoPixel(LED_PIN, NUM_PIXELS)

    def front_lights():
        # LED 0 and 1; red, green and blue value between 0 and 255
        np[0] = (0, 255, 0)
        np[1] = (0, 255, 0)
        # Display the current pixel data on the Neopixel strip
        np.show()

    def rear_lights():
        # LED 2 and 3; red, green and blue value between 0 and 255
        np[2] = (255, 0, 0)
        np[3] = (255, 0, 0)
        # Display the current pixel data on the Neopixel strip
        np.show()

    def same_random_pixels():
        # Iterate over each LED in the strip
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        for pixel_id in range(NUM_PIXELS):
            # Assign the current LED a random red, green and blue value between 0 and 60
            np[pixel_id] = (red, green, blue)
        # Display the current pixel data on the Neopixel strip
        np.show()


    front_lights()
    rear_lights()

    while True:
        sleep(400)
        same_random_pixels()

