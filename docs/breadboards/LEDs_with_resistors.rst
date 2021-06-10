==========================
LEDs_with_resistors
==========================

Connections
--------------------------

| The LEDs must be placed in line with a 47 ohm resistor.
| The 47 ohn resistor has Yellow, Violet, Black, Gold coloured bands.
| LEDS are normally connected to pin0, pin1, or pin2.
| All LEDS are also connected to the 0V pins.

----

Built-in Image lists
----------------------------------------

| When the list of images is more than a few, it is usual to put the list in a variable.
| The code below displays the built-in list of clock images.
| The built-in lists of images are called ``Image.ALL_CLOCKS`` and ``Image.ALL_ARROWS``:

.. image:: picture.jpeg
    :height: 100px
    :width: 200 px
    :scale: 50 %

    
.. code-block:: python

    from microbit import *

    display.show(Image.ALL_CLOCKS, loop=True, delay=100)

----

.. admonition:: Tasks

    #. Write code to display the images in the built-in image list: ``Image.ALL_ARROWS``.    

----




