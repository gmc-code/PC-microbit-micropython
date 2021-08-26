====================================================
MoveMotor LEDs
====================================================

| The MOVEMotor uses 4 ZIP LEDs (WS2812) on pin8.
| The neopixel module is used to drive these RGB LEDs.
| Each RGB LED can produce a full spectrum of colours independent to all of the other RGB LEDs. 
| Each ZIP LED has a Red, Green and Blue element within the LED, and each of these can have brightness set from 0 to 255.

NeoPixel module
-----------------

| The neopixel module allows use of multiple RGB LEDs connected to one pin so that each can have their own colour and brightness set.
| First, import the neopixel library with ``import neopixel``.

.. code-block:: python

    from microbit import *
    import neopixel

----

Setup LEDs
-------------

.. py:method:: neopixel.NeoPixel(pin, n)

    | Initialise a strip of RGB LEDs 
    | ``pin`` is the pin that they are connected by.
    | ``n`` is the number of LEDs

| The code below sets up 4 LEDs connected to pin8 via: ``np = neopixel.NeoPixel(pin8, 4)``.
| The variable, np, is then used to control the LEDs.

.. code-block:: python

    from microbit import *
    import neopixel


    np = neopixel.NeoPixel(pin8, 4)

----

Set LED colour and brightness
------------------------------

.. py:method:: np[n] = (red, green, blue)

    Set the red, green and blue brightness from 0 to 255 for RGB LED at position n.

| Each LED is set by indexing it (like with a Python list, starting from 0). 
| e.g the LED in position 0,  e.g. ``np[0]``. 
| Neopixels are given RGB (red, green, blue) values between 0-255 as a tuple.
| A value of 0 is off, while 255 is full brightness. 
| When red, green and blue are all full brightness, ``(255, 255, 255)``, the colour is white.


| The code below sets the colours to (255, 255, 255) for the LED in position 0.

.. code-block:: python

    from microbit import *
    import neopixel


    np = neopixel.NeoPixel(pin8, 4)
    np[0] = (255, 255, 255)

| The code below sets the colours of the 4 LEDs: np[0] is white, np[1] is red, np[2] is green and np[3] is blue, with all at full brightness.

.. code-block:: python

    from microbit import *
    import neopixel


    np = neopixel.NeoPixel(pin8, 4)
    np[0] = (255, 255, 255)
    np[1] = (255, 0, 0)
    np[2] = (0, 255, 0)    
    np[3] = (0, 0, 255)

----

.. admonition:: Tasks

    | For quick RGB values for common colours, see https://www.rapidtables.com/web/color/RGB_Color.html

    #. Write code to set the last three LEDS yellow, cyan and magenta.
    #. Pick 4 other colours from the website colours above and set the LEDs to those colours.

----

Show LED colour and brightness
--------------------------------

| Setting the colours for LEDs doesn't change the displayed colour of the LEDs until ``show()`` is used on the neopixel object that was set up. e.g. ``np.show()``

.. py:method:: show()

        Show the LEDs using their colour settings. This must be called for any updates to the LEDs to become visible.

| The code below displays the set colours for the neopixel LEDS using ``np.show()``

.. code-block:: python

    from microbit import *
    import neopixel


    np = neopixel.NeoPixel(pin8, 4)
    np[0] = (255, 255, 255)
    np.show()


Clearing Neopixels
-------------------

.. py:method:: clear()

        Clear all the LEDs.






Neopixels values
-------------------

To read the colour of a specific pixel just reference it.

.. code::

    print(np[0])


get
------------------------

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
| This example requires a strip of 4 Neopixels (WS2812) connected to pin8.

.. code-block:: python

    from microbit import *
    import neopixel
    from random import randint

    # Setup the Neopixel strip on pin8 with a length of 4 pixels
    np = neopixel.NeoPixel(pin8, 48)

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

