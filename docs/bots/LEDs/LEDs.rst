====================================================
LEDs
====================================================

| The MOVEMotor uses 4 ZIP LEDs (WS2812) on pin8.
| The neopixel module is used to drive these RGB LEDs.
| IN RGB, R stands for red, G stands for green, and B stands for blue.
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

Set up LEDs
-------------

.. py:method:: neopixel.NeoPixel(pin, n)

    | Initialise a strip of RGB LEDs 
    | ``pin`` is the pin that they are connected by.
    | ``n`` is the number of LEDs

| The code below sets up 4 LEDs connected to pin8 via: ``np = neopixel.NeoPixel(pin8, 4)``.
| The variable, np, is the neopixel object that is used to control the LEDs.

.. code-block:: python

    from microbit import *
    import neopixel


    np = neopixel.NeoPixel(pin8, 4)

----

Set LED colour and brightness
------------------------------

.. py:method:: np[n] = (red, green, blue)

    Set the red, green and blue brightness from 0 to 255 for a RGB LED at position n.

| Each LED is set by indexing it (like with a Python list, starting from 0). 
| e.g the LED in position 0 is ``np[0]``. 
| Neopixels are given RGB (red, green, blue) values between 0-255 as a tuple.
| A value of 0 is off, while 255 is full brightness. 
| When red, green and blue are all full brightness, ``(255, 255, 255)``, the colour is white.


| The code below sets the RGB values to (255, 255, 255) for the LED in position 0.

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

    #. Write code to set the last LEDS at position 1, 2 and 3 to yellow, cyan and magenta.

----

Show LEDs 
----------

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


Clear LEDs
------------

.. py:method:: clear()

        Clear all the LEDs so that they have no colours set and turns off the LEDs.

| The code below uses the variable ``buggy_lights`` for the neopixel settings.
| The front lights are at position 0 and 1. They are set to dull blue.
| The rear lights are at position 2 and 3. They are set to dull red.
| The lights are turned on for 2 seconds then turned off using ``clear()``.

.. code-block:: python

    from microbit import *
    import neopixel


    buggyLights = NeoPixel(pin8, 4)
    dull_blue = [20, 20, 25]
    dull_red = [25, 0, 0]
    buggyLights[0] = dull_blue
    buggyLights[1] = dull_blue
    buggyLights[2] = dull_red
    buggyLights[3] = dull_red
    buggyLights.show()
    sleep(2000)
    buggyLights.clear()

----

.. admonition:: Tasks

    | For quick RGB values for common colours, see https://www.rapidtables.com/web/color/RGB_Color.html

    #. | Modify the colours used in the code by changing the variable names and their values. | Use yellow and purple instead of red and blue.

----

LED values
-------------------

To read the colour of a specific pixel just reference it.


.. py:method:: np[n]

    Return the red, green and blue value for the RGB LED at position n.

| The code below sets the LED to a sandy brown colour. The ``for`` loop displays each value in the tuple ``(255, 0, 0)``.

.. code-block:: python

    from microbit import *
    import neopixel


    buggy_lights = neopixel.NeoPixel(pin8, 4)
    buggy_lights[0] = (255, 0, 0)
    for i in buggy_lights[0]:
        display.scroll(i)

----

Colour lists
-------------------

| A list of colours can be used to create a colourful display.
| 2 for loops are used, one nested inside the other.
| ``for c in colour_list:`` loops through the colours.
| ``for i in range(4):`` loops through each LED to set the colour for it.

.. code-block:: python

    from microbit import *
    import neopixel


    white = (255, 255, 255)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 128, 0)
    cyan = (0, 255, 255)
    blue = (0, 0, 255)
    magenta = (255, 0, 255)

    colour_list = [white, red, yellow, green, cyan, blue, magenta, ]

    buggy_lights = neopixel.NeoPixel(pin8, 4)
    for c in colour_list:
        for i in range(4):
            buggy_lights[i]=c
        buggy_lights.show()
        sleep(200)


----

.. admonition:: Tasks


    See https://www.indezine.com/products/powerpoint/learn/color/color-rgb.html

    #. Modify the code to use a shorter list of colours, with just the primary colours.
    #. Modify the code to use a shorter list of colours, with just the secondary colours.


----

Random brightness
-----------------

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

