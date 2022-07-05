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


| The code below shows a large bright square.

.. code-block:: python

    from microbit import *

    display.show(Image('99999:90009:90009:90009:99999'))

----

| The code below shows a vertical brightness gradient of dull to bright from the top to the bottom.

.. code-block:: python

    from microbit import *

    display.show(Image('11111:33333:55555:77777:99999'))
    
| The code below shows a diagonal brightness gradient (dull to bright) from the top left to the bottom right.

.. code-block:: python

    from microbit import *

    display.show(Image('12345:23456:34567:45678:56789'))

----

.. admonition:: Tasks

    #. Write code for a large square of brightness 2.
    #. Write code for a vertical brightness gradient of bright to dull from the top down to the bottom.
    #. Write code for a horizontal brightness gradient of dull to bright from the left to right.
    #. Write code for a diagonal brightness gradient of dull to bright from the bottom left to the top right.   

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write code for a large square of brightness 2.

                    .. code-block:: python

                        from microbit import *

                        display.show(Image('22222:20002:20002:20002:22222'))

                .. tab-item:: Q2

                    Write code for a vertical brightness gradient of bright to dull from the top down to the bottom.

                    .. code-block:: python

                        from microbit import *

                        display.show(Image('99999:77777:55555:33333:11111'))

                .. tab-item:: Q3

                    Write code for a horizontal brightness gradient of dull to bright from the left to right.

                    .. code-block:: python

                        from microbit import *

                        display.show(Image('13579:13579:13579:13579:13579'))

                .. tab-item:: Q4

                    Write code for a diagonal brightness gradient of dull to bright from the bottom left to the top right. 

                    .. code-block:: python

                        from microbit import *

                        display.show(Image('56789:45678:34567:23456:12345'))
                    

----

Image strings: line by line
------------------------------

| The large square Image('99999:90009:90009:90009:99999') can be rewritten so that the 5 rows are lined up under each other like a 5 by 5 grid. Extra spaces can by used to line up each line.

.. code-block:: python

    from microbit import *

    large_square = Image('99999:'
                         '90009:'
                         '90009:'
                         '90009:'
                         '99999')
    display.show(large_square)


----

.. admonition:: Tasks

    #. Write code for a large square of brightness 3 by lining up the 5 rows of the image under each other.
    #. Write code for a small square of brightness 9 by lining up the 5 rows of the image under each other.
    #. Write code for 2 symmetrically spaced central horizontal lines of brightness 5 by lining up the 5 rows of the image under each other. 
    #. Write code for 2 symmetrically spaced central vertical lines of brightness 5 by lining up the 5 rows of the image under each other.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write code for a large square of brightness 3 by lining up the 5 rows of the image under each other.

                    .. code-block:: python

                        from microbit import *

                        large_square = Image('33333:'
                                             '30003:'
                                             '30003:'
                                             '30003:'
                                             '33333')
                        display.show(large_square)

                .. tab-item:: Q2

                    Write code for a small square of brightness 9 by lining up the 5 rows of the image under each other.

                    .. code-block:: python

                        from microbit import *

                        small_square = Image('00000:'
                                             '09990:'
                                             '09090:'
                                             '09990:'
                                             '00000')
                        display.show(small_square)


                .. tab-item:: Q3

                    Write code for 2 symmetrically spaced central horizontal lines of brightness 5 by lining up the 5 rows of the image under each other.

                    .. code-block:: python

                        from microbit import *

                        hor_lines = Image('00000:'
                                          '55555:'
                                          '00000:'
                                          '55555:'
                                          '00000')
                        display.show(hor_lines)

                .. tab-item:: Q4

                    Write code for 2 symmetrically spaced central vertical lines of brightness 5 by lining up the 5 rows of the image under each other.

                    .. code-block:: python

                        from microbit import *

                        vert_lines = Image('05050:'
                                           '05050:'
                                           '05050:'
                                           '05050:'
                                           '05050')
                        display.show(vert_lines)

----

Pixel controls
---------------------

.. image:: images/microbit_numbering.png
    :scale: 100 %
    :align: center

.. image:: images/microbit-led-coords.png
    :scale: 60 %
    :align: center

| Each pixel on the 5 by 5 grid can be controlled individually.
| The column numbers are 0 to 4 from left to right.
| The row numbers are 0 to 4 from top to bottom.

.. py:function:: display.set_pixel(x, y, value)

    Set the brightness of the LED at column x and row y to value, which has to be an integer between 0 and 9.

| The code below turns on the pixel in the top left with full brightness.

.. code-block:: python

    from microbit import *

    display.set_pixel(0, 0, 9)

----

.. admonition:: Tasks

    #. Write code to turn on the pixel, 3 columns across and 4 rows down.
    #. Write code to turn on the pixel, 4 columns across and 2 rows down.
    #. Write code to turn on the pixel in the top right.
    #. Write code to turn on the pixel in the bottom right.
    #. Write code to turn on the pixel in the bottom left.
    #. Write code to turn on the 4 corner pixels.
    #. Write code to turn on the top 5 pixels.
    #. Write code to turn on the top 5 pixels at brightnesses of 1, 3, 5, 7, 9 from left to right.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write code to turn on the pixel, 3 columns across and 4 rows down.

                    .. code-block:: python

                        from microbit import *

                        display.set_pixel(2, 3, 9)

               .. tab-item:: Q2

                    Write code to turn on the pixel, 4 columns across and 2 rows down.

                    .. code-block:: python

                        from microbit import *

                        display.set_pixel(3, 1, 9)

                .. tab-item:: Q3

                    Write code to turn on the pixel in the top right.

                    .. code-block:: python

                        from microbit import *

                        display.set_pixel(4, 0, 9)

                .. tab-item:: Q4

                    Write code to turn on the pixel in the bottom right.

                    .. code-block:: python

                        from microbit import *
                        
                        display.set_pixel(4, 4, 9)

                .. tab-item:: Q5

                    Write code to turn on the pixel in the bottom left.

                    .. code-block:: python

                        from microbit import *

                        display.set_pixel(0, 4, 9)

                .. tab-item:: Q6

                    Write code to turn on the 4 corner pixels.

                    .. code-block:: python

                        from microbit import *

                        display.set_pixel(0, 0, 9)
                        display.set_pixel(0, 4, 9)
                        display.set_pixel(4, 0, 9)
                        display.set_pixel(4, 4, 9)

                .. tab-item:: Q7

                    Write code to turn on the top 5 pixels.

                    .. code-block:: python

                        from microbit import *

                        display.set_pixel(0, 0, 9)
                        display.set_pixel(1, 0, 9)
                        display.set_pixel(2, 0, 9)
                        display.set_pixel(3, 0, 9)
                        display.set_pixel(4, 0, 9)

                .. tab-item:: Q8

                    Write code to turn on the top 5 pixels at brightnesses of 1, 3, 5, 7, 9 from left to right.

                    .. code-block:: python

                        from microbit import *

                        display.set_pixel(0, 0, 1)
                        display.set_pixel(1, 0, 3)
                        display.set_pixel(2, 0, 5)
                        display.set_pixel(3, 0, 7)
                        display.set_pixel(4, 0, 9)

----

Pixel rows and columns
------------------------

| For loops can be used to turn on all the pixels in a row or colum.

| The code below sets the brightness to 2 for the first column, column 0.

.. code-block:: python

    from microbit import *

    x = 0
    for y in range(0, 5):
        display.set_pixel(x, y, 2)

| The code below sets the brightness to 6 for the first row, row 0.

.. code-block:: python

    from microbit import *

    y = 0
    for x in range(0, 5):
        display.set_pixel(x, y, 6)

----

.. admonition:: Tasks

    #. Write code to turn on the pixels in row 3, starting at row 0.
    #. Write code to turn on the pixels in column 2, starting at column 0.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write code to turn on the pixels in row 3, starting at row 0.

                    .. code-block:: python

                        from microbit import *

                        x = 3
                        for y in range(0, 5):
                            display.set_pixel(x, y, 9)

                .. tab-item:: Q2

                    Write code to turn on the pixels in column 2, starting at column 0.

                    .. code-block:: python

                        from microbit import *

                        y = 2
                        for x in range(0, 5):
                            display.set_pixel(x, y, 9)

----

Pixel rows and columns lists
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
    ylist = [0, 2, 4]
    for x in xlist:
        for y in ylist:
            display.set_pixel(x, y, 9)

----

.. admonition:: Tasks

    #. Adjust the code above to turn on columns 1 to 3 and rows 0 and 4.
    #. Adjust the code above to turn on columns 0 and 4 and rows 1 to 3.
    #. Combine the two answers to produce a square shape without the corners.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Adjust the code above to turn on columns 1 to 3 and rows 0 and 4.

                    .. code-block:: python

                        from microbit import *

                        xlist = [1, 2, 3]
                        ylist = [0, 4]
                        for x in xlist:
                            for y in ylist:
                                display.set_pixel(x, y, 9)

                .. tab-item:: Q2

                    Adjust the code above to turn on columns 0 and 4 and rows 1 to 3.

                    .. code-block:: python

                        from microbit import *

                        xlist = [0, 4]
                        ylist = [1, 2, 3]
                        for x in xlist:
                            for y in ylist:
                                display.set_pixel(x, y, 9)

               .. tab-item:: Q3

                    Combine the two answers to produce a square shape without the corners.

                    .. code-block:: python

                        from microbit import *

                        xlist = [1, 2, 3]
                        ylist = [0, 4]
                        for x in xlist:
                            for y in ylist:
                                display.set_pixel(x, y, 9)
                                
                        xlist = [0, 4]
                        ylist = [1, 2, 3]
                        for x in xlist:
                            for y in ylist:
                                display.set_pixel(x, y, 9)

----

Boat sinking animation
-----------------------------

| Several custom images can be stored in variables. e.g. boat1, boat2, boat3, boat4, boat5, boat6.
| Those variables can be put in a list. e.g. sinking_boats
| Since ``display.show`` can use a list of images, the list of custom images can be shown in sequence, making an animation.

.. code-block:: python

    from microbit import *

    boat1 = Image('05050:'
                  '05050:'
                  '05050:'
                  '99999:'
                  '09990')

    boat2 = Image('00000:'
                  '05050:'
                  '05050:'
                  '05050:'
                  '99999')

    boat3 = Image('00000:'
                  '00000:'
                  '05050:'
                  '05050:'
                  '05050')

    boat4 = Image('00000:'
                  '00000:'
                  '00000:'
                  '05050:'
                  '05050')

    boat5 = Image('00000:'
                  '00000:'
                  '00000:'
                  '00000:'
                  '05050')

    boat6 = Image('00000:'
                  '00000:'
                  '00000:'
                  '00000:'
                  '00000')

    sinking_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
    while True:
        display.show(sinking_boats, delay=500)

----

.. admonition:: Tasks

    #. Write a list variable, ``rising_boats``, that lists the boats in reverse order and animates a rising boat. Rather than manually listing the order, use ``list(reversed(**imageslist**))``.  (See the built-in images lesson for an explanation.)
    #. Combine the 2 animations to show a boat sinking and rising over and over again.


    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write a list variable, ``rising_boats``, that lists the boats in reverse order and animates a rising boat. Rather than manually listing the order, use ``list(reversed(**imageslist**))``. 

                    .. code-block:: python

                        from microbit import *

                        boat1 = Image("05050:" "05050:" "05050:" "99999:" "09990")
                        boat2 = Image("00000:" "05050:" "05050:" "05050:" "99999")
                        boat3 = Image("00000:" "00000:" "05050:" "05050:" "05050")
                        boat4 = Image("00000:" "00000:" "00000:" "05050:" "05050")
                        boat5 = Image("00000:" "00000:" "00000:" "00000:" "05050")
                        boat6 = Image("00000:" "00000:" "00000:" "00000:" "00000")

                        sinking_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
                        rising_boats = list(reversed(sinking_boats))

                        while True:
                            display.show(rising_boats, delay=500)


                .. tab-item:: Q2

                    Combine the 2 animations to show a boat sinking and rising over and over again.

                    .. code-block:: python

                        from microbit import *

                        boat1 = Image("05050:" "05050:" "05050:" "99999:" "09990")
                        boat2 = Image("00000:" "05050:" "05050:" "05050:" "99999")
                        boat3 = Image("00000:" "00000:" "05050:" "05050:" "05050")
                        boat4 = Image("00000:" "00000:" "00000:" "05050:" "05050")
                        boat5 = Image("00000:" "00000:" "00000:" "00000:" "05050")
                        boat6 = Image("00000:" "00000:" "00000:" "00000:" "00000")

                        sinking_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
                        rising_boats = list(reversed(sinking_boats))

                        while True:
                            display.show(sinking_boats, delay=500)
                            display.show(rising_boats, delay=500)

