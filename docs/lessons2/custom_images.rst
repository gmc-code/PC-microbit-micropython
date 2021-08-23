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
| e.g. Image('11111:33333:55555:77777:99999')

| The code below shows a vertical brightness gradient from the top to the bottom.

.. code-block:: python

    from microbit import *


    display.show(Image('11111:33333:55555:77777:99999'))
    
| The code below shows a diagonal brightness gradient from the top left to the bottom right.

.. code-block:: python

    from microbit import *


    display.show(Image('12345:23456:34567:45678:56789'))

----

.. admonition:: Tasks

    #. Write code for a horizontal brightness gradient from the left to right.
    #. Write code for a vertical brightness gradient from the bottom to the top.
    #. Write code for a diagonal brightness gradient from the bottom left to the top right.   

----

Image strings: line by line
------------------------------

| The vertical gradient Image('11111:33333:55555:77777:99999') can be rewritten so that the 5 rows are lined up under each other like a 5 by 5 grid. Extra spaces can by used to line up each line.

.. code-block:: python

    from microbit import *

    vertical_gradient = Image('11111:'
                              '33333:'
                              '55555:'
                              '77777:'
                              '99999')
    display.show(vertical_gradient)


----

.. admonition:: Tasks

    #. Write code for a diagonal brightness gradient by lining up the 5 rows under each other.   

----

Pixel controls
---------------------

| Each pixel on the 5 by 5 grid can be controlled individually.
| The column numbers are 0 to 4 from left to right.
| The row numbers are 0 to 4 from top to bottom.

.. py:function:: display.set_pixel(x, y, value)

    Set the brightness of the LED at column x and row y to value, which has to be an integer between 0 and 9.


| The code below turns on the pixel in the top left.

.. code-block:: python

    from microbit import *


    display.set_pixel(0, 0, 9)

----

.. admonition:: Tasks

    #. Write code to turn on the pixel in column 3 row 4.
    #. Write code to turn on the pixel in the top right.
    #. Write code to turn on the pixel in the bottom right.
    #. Write code to turn on the pixel in the bottom left.
    #. Write code to turn on the 4 corner pixels.
    #. Write code to turn on the top 5 pixels.
    #. Write code to turn on the top 5 pixels at brightnesses of 1, 3, 5, 7, 9 from left to right.

----

Pixel rows and columns
------------------------

| For loops can be used to turn on all the pixels in a row or colum.

| The code below set the brightness to 2 for the first column.

.. code-block:: python

    from microbit import *

    x = 0
    for y in range(0, 5):
        display.set_pixel(x, y, 2)


| The code below set the brightness to 6 for the first row.

.. code-block:: python

    from microbit import *

    y = 0
    for x in range(0, 5):
        display.set_pixel(x, y, 6)

----

.. admonition:: Tasks

    #. Write code to turn on teh pixels in row 3.
    #. Write code to turn on the pixel in column 2.

----

Boat sinking animation
-----------------------------

| Several custom images can be stored in variables. e.g. boat1, boat2, boat3, boat4, boat5, boat6.
| Those variables can be put in a list. e.g. all_boats
| The list of custom images can be shown, making an animation.

.. code-block:: python

    from microbit import *

    boat1 = Image("05050:"
                "05050:"
                "05050:"
                "99999:"
                "09990")

    boat2 = Image("00000:"
                "05050:"
                "05050:"
                "05050:"
                "99999")

    boat3 = Image("00000:"
                "00000:"
                "05050:"
                "05050:"
                "05050")

    boat4 = Image("00000:"
                "00000:"
                "00000:"
                "05050:"
                "05050")

    boat5 = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "05050")

    boat6 = Image("00000:"
                "00000:"
                "00000:"
                "00000:"
                "00000")

    all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
    display.show(all_boats, delay=200)