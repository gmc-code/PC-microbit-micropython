====================================================
Custom images
====================================================

Image strings
----------------

| The basic syntax for showing an image is:

.. py:function:: show(image)

    | Display an image.


| The image can be a string made up of a 25 integers where each integer is the brightness from 0 to 9, where 0 if off and 9 is full brightness.
| The 25 values are broken up into 5 lines of 5 with a colon between them.
| e.g. ``Image('01234:56789:09090:98765:43210')``

.. sidebar::

    .. image:: images/square.png
        :scale: 50 %
        :align: center


----

Potentiometer and rows
------------------------------

| For loops can be used to turn on pixels based on values in lists.
| Each row will have the same patern of pixels.
| Each column will have the same patern of pixels.
| A variable, ``xlist``, can store the columns numbers.
| A variable, ``ylist``, can store the row numbers.
| The code below produces an image of a six on a die.

.. code-block:: python

    from microbit import *

    xlist = [0, 4]
    ylist = [0, 1, 2, 3, 4]
    for x in xlist:
        for y in ylist:
            display.set_pixel(x, y, 9)

----

Invert
-----------------------------

| Several custom images can be stored in variables. e.g. boat1, boat2, boat3, boat4, boat5, boat6.
|
.. code-block:: python

    from microbit import *
    

    # Create the "flash" animation frames. Can you work out how it's done?
    flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

    while True:
        if button_a.was_pressed():
            display.show(flash, delay=100, wait=False)
        if button_b.was_pressed():
            display.show(flash, delay=300, wait=False)