====================================================
Byte array images
====================================================


bytearray
-----------------------------------------

.. py:function:: Image(width=None, height=None, buffer=None)

    | Creates an image with width columns and height rows. 
    | Optionally buffer can be a list of integers passed passed to bytearray(integer_list)

| The code below creates a brightness gradient.

.. code-block:: python

    from microbit import *

    newimg = Image(5, 5, bytearray([1,1,1,1,1,3,3,3,3,3,5,5,5,5,5,7,7,7,7,7,9,9,9,9,9]))
    display.show(newimg)

----

| The tasks below require the creation of definitions to produce the list of values for the bytearray function. 
| The pixels brightness must be between 0 and 9, inclusive, and must be integers.
| Example code to limit the values and round to an integer is below.
| **x_val1** is the initial x value.
| **x** is the x position of a pixel (from 0 to 4)
| **xstep** is the step size for a gradient.
| **int(x_val1 + (x * xstep))** makes sure the calculation gives an integer.
| **max(0, x)** makes sure the value is at least 0.
| **min(9, x)** makes sure the value is no more than 9.

.. code-block:: python

    value = min(9, max(0, int(x_val1 + (x * xstep))))


.. admonition:: Tasks

    #. Write a definition to produce the list to be used for horizontal gradient from 1 in the left to 9 in the right. [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9]
    #. Modify the code to create a horizontal gradient from 1 in the left to 9 in the right using a definition to produce the gradient list.
    #. Use the definition for a horizontal gradient to create one from 7 in the left to 3 in the right.
    #. Write a definition to produce the list to be used for vertical gradient from 1 in the top to 9 in the bottom. [1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9]
    #. Modify the code to create a vertical gradient from 1 in the top to 9 in the bottom using a definition to produce the gradient list.
    #. Use the definition for a vertical gradient to create one from 9 in the top to 2 in the bottom. [9, 9, 9, 9, 9, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2]
    #. Write a definition to produce the list to be used for diagoanl gradient from 1 in the top left to 9 in the bottom right. [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9]
    #. Modify the code to create a diagonal gradient from 1 in top left to 9 in bottom right. 

    
    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write a definition to produce the list to be used for horizontal gradient from 1 in the left to 9 in the right. [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9]

                    .. code-block:: python

                        from microbit import *


                        def gradient_x(x_val1, xstep):
                            grid = []
                            for y in range(5):
                                for x in range(5):
                                    newx = min(9, max(0, int(x_val1 + (x * xstep))))
                                    grid.append(newx)
                            return grid

                        img_array = gradient_x(1, 9, 2)

                .. tab-item:: Q2

                    Modify the code to create a horizontal gradient from 1 in the left to 9 in the right using a definition to prodcue the gradient list.

                    .. code-block:: python
                        
                        from microbit import *


                        def gradient_x(x_val1, xstep):
                            grid = []
                            for y in range(5):
                                for x in range(5):
                                    newx = min(9, max(0, int(x_val1 + (x * xstep))))
                                    grid.append(newx)
                            return grid


                        img_array = gradient_x(1, 9, 2)
                        img_horzgrad = Image(5, 5, bytearray(img_array))
                        display.show(img_horzgrad)


                .. tab-item:: Q3

                    Use the definition for a horizontal gradient to create one from 7 in the left to 3 in the right.

                    .. code-block:: python
                        
                        from microbit import *


                        def gradient_x(x_val1, xstep):
                            grid = []
                            for y in range(5):
                                for x in range(5):
                                    newx = min(9, max(0, int(x_val1 + (x * xstep))))
                                    grid.append(newx)
                            return grid


                        img_array = gradient_x(7, -1)
                        img_horzgrad = Image(5, 5, bytearray(img_array))
                        display.show(img_horzgrad)

                .. tab-item:: Q4

                    Write a definition to produce the list to be used for vertical gradient from 1 in the top to 9 in the bottom. [1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9]

                    .. code-block:: python
                        
                        from microbit import *


                        def gradient_y(y_val1, ystep):
                            grid = []
                            for y in range(5):
                                newy = min(9, max(0, int(y_val1 + (y * ystep))))
                                for x in range(5):
                                    grid.append(newy)
                            return grid


                        img_array = gradient_y(1, 2)


                .. tab-item:: Q5

                    Modify the code to create a vertical gradient from 1 in the top to 9 in the bottom using a definition to produce the gradient list.

                    .. code-block:: python
                        
                        from microbit import *


                        def gradient_y(y_val1, ystep):
                            grid = []
                            for y in range(5):
                                newy = min(9, max(0, int(y_val1 + (y * ystep))))
                                for x in range(5):
                                    grid.append(newy)
                            return grid


                        img_array = gradient_y(1, 2)
                        img_vertgrad = Image(5, 5, bytearray(img_array))
                        display.show(img_vertgrad)

                .. tab-item:: Q6

                    Use the definition for a vertical gradient to create one from 9 in the top to 2 in the bottom. [9, 9, 9, 9, 9, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2]

                    .. code-block:: python
                        
                        from microbit import *


                        def gradient_y(y_val1, ystep):
                            grid = []
                            for y in range(5):
                                newy = min(9, max(0, int(y_val1 + (y * ystep))))
                                for x in range(5):
                                    grid.append(newy)
                            return grid


                        img_array = gradient_y(9, -8 / 5)
                        img_vertgrad = Image(5, 5, bytearray(img_array))
                        display.show(img_vertgrad)


                .. tab-item:: Q7

                    Write a definition to produce the list to be used for diagoanl gradient from 1 in the top left to 9 in the bottom right. [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9]

                    .. code-block:: python
                        
                        from microbit import *


                        def gradient_xy(xy_val1, xstep, ystep):
                            grid = []
                            for y in range(5):
                                yadd = min(9, max(0, (y * ystep)))
                                for x in range(5):
                                    xadd = min(9, max(0, (x * xstep)))
                                    newxy = min(9, max(0, int(xy_val1 + xadd + yadd)))
                                    grid.append(newxy)
                            return grid


                        img_array = gradient_xy(1, 1, 1)


                .. tab-item:: Q8

                    Modify the code to create a diagonal gradient from 1 in top left to 9 in bottom right. 

                    .. code-block:: python
                        
                        from microbit import *


                        def gradient_xy(xy_val1, xstep, ystep):
                            grid = []
                            for y in range(5):
                                yadd = min(9, max(0, (y * ystep)))
                                for x in range(5):
                                    xadd = min(9, max(0, (x * xstep)))
                                    newxy = min(9, max(0, int(xy_val1 + xadd + yadd)))
                                    grid.append(newxy)
                            return grid


                        img_array = gradient_xy(1, 1, 1)
                        img_vertgrad = Image(5, 5, bytearray(img_array))
                        display.show(img_vertgrad)



----

| The code below creates a 5 by 5 images with random brightness.

.. code-block:: python

    from microbit import *
    from random import randint


    def full_screen_fill_bytes(minbrightness=1, maxbrightness=9):
        screen_bytes = []
        for y in range(0, 5):
            for x in range(0, 5):
                brightness = randint(minbrightness, maxbrightness)
                screen_bytes.append(brightness)
        return screen_bytes


    while True:
        screen_bytes = full_screen_fill_bytes(0, 9)
        newimg = Image(5, 5, bytearray(screen_bytes))
        display.show(newimg)
        sleep(1000)

----

List comprehension for bytearray images
--------------------------------------------

See: https://www.w3schools.com/python/python_lists_comprehension.asp

.. py:function:: newlist = [expression for item in iterable]
                 newlist = [expression for item in iterable if condition == True]

    | Create a list of expressions that take each item in an iterable, such as a list, tuple or string.
