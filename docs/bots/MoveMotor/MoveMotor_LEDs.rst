====================================================
MoveMotor LEDs
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

    #. Modify the code to turn on the front lights for 2 sec then turn on the rear lights for 2 sec.

----

LED values
-------------------

To read the colour of a specific RGB LED use its index position.


.. py:method:: np[n]

    Return the red, green and blue value for the RGB LED at position n.

| The code below sets the LED to red. The ``for`` loop displays each value in the tuple ``(255, 0, 0)``.

.. code-block:: python

    from microbit import *
    import neopixel


    buggy_lights = neopixel.NeoPixel(pin8, 4)
    buggy_lights[0] = (255, 0, 0)
    for rgb_value in buggy_lights[0]:
        display.scroll(rgb_value)

----

Colour lists
-------------------

| A list of colours can be used to create a colourful display.
| 2 for loops are used, one nested inside the other.
| ``for colour in colour_list:`` loops through the colours.
| ``for led_num in range(4):`` loops through each LED to set its colour.

.. code-block:: python

    from microbit import *
    import neopixel

    buggy_lights = neopixel.NeoPixel(pin8, 4)

    white = (255, 255, 255)
    red = (255, 0, 0)
    yellow = (255, 255, 0)
    green = (0, 128, 0)
    cyan = (0, 255, 255)
    blue = (0, 0, 255)
    magenta = (255, 0, 255)

    colour_list = [white, red, yellow, green, cyan, blue, magenta]

    for colour in colour_list:
        for led_num in range(4):
            buggy_lights[led_num]=colour
        buggy_lights.show()
        sleep(200)

----

Primary and secondary colours 
------------------------------

.. image:: images/primary_colours.png
    :scale: 50 %
    :align: left

.. image:: images/secondary_colours.png
    :scale: 50 %
    :align: center


.. admonition:: Tasks

    See https://www.indezine.com/products/powerpoint/learn/color/color-rgb.html

    #. Modify the code to use a shorter list of colours, with just the primary colours.
    #. Modify the code to use a shorter list of colours, with just the secondary colours.
