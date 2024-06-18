====================================================
Byte array images
====================================================


bytearray with integer list
-----------------------------------------

.. py:function:: Image(width=None, height=None, buffer=None)

    | Creates an image with width columns and height rows. 
    | The buffer can be a list of integers passed to bytearray as in bytearray(integer_list).

| The code below creates a brightness gradient using a list of brightness values passed to bytearray.

.. code-block:: python

    from microbit import *

    new_img = Image(5, 5, bytearray([1,1,1,1,1,3,3,3,3,3,5,5,5,5,5,7,7,7,7,7,9,9,9,9,9]))
    display.show(new_img)


| The advantage of using bytearray is that it allows integer lists to be used instead of strings.
| Integer lists are easier to manipulate.


| The code below uses bytearrays to design gradient custom images.

.. code-block:: python

    from microbit import *

    my_image_diag_grad = Image(5, 5, bytearray([
    1, 2, 3, 4, 5,
    2, 3, 4, 5, 6,
    3, 4, 5, 6, 7,
    4, 5, 6, 7, 8,
    5, 6, 7, 8, 9,
    ]))

    my_image_horz_grad = Image(5, 5, bytearray([
    1, 2, 3, 4, 5,
    1, 2, 3, 4, 5,
    1, 2, 3, 4, 5,
    1, 2, 3, 4, 5,
    1, 2, 3, 4, 5,
    ]))

    my_image_vert_grad = Image(5, 5, bytearray([
    1, 1, 1, 1, 1,
    2, 2, 2, 2, 2,
    3, 3, 3, 3, 3,
    4, 4, 4, 4, 4,
    5, 5, 5, 5, 5,
    ]))


    while True:
        display.show(my_image_horz_grad)
        sleep(500)
        display.show(my_image_vert_grad)
        sleep(600)
        display.show(my_image_diag_grad)
        sleep(700)
        display.clear()
        sleep(700)
        
----

Uniform images using List multiplication
-----------------------------------------

| Like strings, the * operator acting on a list, outputs a list with multiple copies of itself.
| e.g [1, 2, 3] * 2 returns [1, 2, 3, 1, 2, 3]

| [1] * 25 returns [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
| The code below creates a uniform image of brightness 1.

.. code-block:: python

    from microbit import *

    img = Image(5, 5, bytearray([1] * 25))
    display.show(img)

----

.. admonition:: Tasks

    #. Modify the code to produce an image of uniform brightness of 3.
    #. Modify the code to produce an image of uniform brightness of 7.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to produce an image of uniform brightness of 3.

                    .. code-block:: python

                        from microbit import *

                        img = Image(5, 5, bytearray([3] * 25))
                        display.show(img)

                .. tab-item:: Q2

                    Modify the code to produce an image of uniform brightness of 7.

                    .. code-block:: python

                        from microbit import *

                        img = Image(5, 5, bytearray([7] * 25))
                        display.show(img)

----

bytearray gradients using List multiplication
-------------------------------------------------

| A row of pixels can be replicated and used with bytearray.

| [1, 3, 5, 7, 9] * 5 returns [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9]
| The code below creates an image with a horizontal gradient of increasing brightness.

.. code-block:: python

    from microbit import *

    img = Image(5, 5, bytearray([1, 3, 5, 7, 9] * 5))
    display.show(img)

----

.. admonition:: Tasks

    #. Modify the code to produce a horizontal gradient of decreasing brightness.
    #. Modify the code to produce a horizontal gradient of decreasing then increasing brightness.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to produce a horizontal gradient of decreasing brightness.

                    .. code-block:: python

                        from microbit import *

                        img = Image(5, 5, bytearray([9, 7, 5, 3, 1] * 5))
                        display.show(img)

                .. tab-item:: Q2

                    Modify the code to produce a horizontal gradient of decreasing then increasing brightness.

                    .. code-block:: python

                        from microbit import *

                        img = Image(5, 5, bytearray([9, 6, 3, 6, 9] * 5))
                        display.show(img)
----

bytearray irregular patterns using List multiplication and concatenation
---------------------------------------------------------------------------

| A list of 25 integers can be built using * and + with lists.
| e.g [2, 4, 6, 8] * 6 + [2] returns [2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2, 4, 6, 8, 2]

.. sidebar::

    .. image:: images/alternating.png
        :scale: 50 %
        :align: center

| The code below creates an alternating pattern.

.. code-block:: python

    from microbit import *

    img = Image(5, 5, bytearray([1, 9] * 12 + [1]))
    display.show(img)

----

.. admonition:: Tasks

    #. Modify the code to produce an alternating pattern of brightness 9 and 4.
    #. Modify the code to produce a cyclic pattern of brightness 9 , 1 and 1.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to produce an alternating pattern of brightness 9 and 4.

                    .. code-block:: python

                        from microbit import *

                        img = Image(5, 5, bytearray([9, 4] * 12 + [9]))
                        display.show(img)

                .. tab-item:: Q2

                    Modify the code to produce a cyclic pattern of brightness 9 , 1 and 1.

                    .. code-block:: python

                        from microbit import *

                        img = Image(5, 5, bytearray([9, 1, 1] * 8 + [9]))
                        display.show(img)

----

Integer-list-producing definitions for bytearray
-----------------------------------------------------

| The tasks below require the creation of definitions to produce the list of values for the bytearray function. 
| The pixels brightness must be between 0 and 9, inclusive, and must be integers.
| Example code to limit the values and round to an integer is below.
| **x_val1** is the initial x value.
| **x** is the x position of a pixel (from 0 to 4)
| **x_step** is the step size for a gradient.
| **int(x_val1 + (x * x_step))** makes sure the calculation gives an integer.
| **max(0, x)** makes sure the value is at least 0.
| **min(9, x)** makes sure the value is no more than 9.

.. code-block:: python

    value = x_val1 + (x * x_step)
    # is improved to make sure integers between 0 and 9 are produced
    value = min(9, max(0, int(x_val1 + (x * x_step))))

| The definition, below, produces the integer list to be used for a horizontal gradient from 1 in the left to 9 in the right. [1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9, 1, 3, 5, 7, 9]
| It creates an empty list, **grid = []**.
| It then appends each new value to it, **grid.append(new_val)**.
| As the code loops through the x values, **for x in range(5)**, new values are calculated by adding steps: **new_val = x_val1 + (x * x_step)**.
| The image array is made using **gradient_x(1, 2)**, so that x starts at 1 and increases in steps of 2.

.. code-block:: python

    from microbit import *

    
    def gradient_x(x_val1, x_step):
        grid = []
        for y in range(5):
            for x in range(5):
                new_val = min(9, max(0, int(x_val1 + (x * x_step))))
                grid.append(new_val)
        return grid

    img_array = gradient_x(1, 2)
    img_horz_grad = Image(5, 5, bytearray(img_array))
    display.show(img_horz_grad)

----

.. admonition:: Tasks

    #. Use the definition for a horizontal gradient to create a gradient horizontally from 7 in the left to 3 in the right.
    #. Modify the code to create a vertical gradient from 1 in the top to 9 in the bottom using a definition to produce the gradient list: [1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9]
    #. Use the definition for a vertical gradient to create one from 9 in the top to 2 in the bottom. [9, 9, 9, 9, 9, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2], and display it.
    #. Write a definition to produce the list to be used for a diagonal gradient from 1 in the top left to 9 in the bottom right. [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9], and display it.

    
    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Use the definition for a horizontal gradient to create a gradient horizontally from 7 in the left to 3 in the right.

                .. code-block:: python
                    
                    from microbit import *


                    def gradient_x(x_val1, x_step):
                        grid = []
                        for y in range(5):
                            for x in range(5):
                                new_x = min(9, max(0, int(x_val1 + (x * x_step))))
                                grid.append(new_x)
                        return grid


                    img_array = gradient_x(7, -1)
                    img_horz_grad = Image(5, 5, bytearray(img_array))
                    display.show(img_horz_grad)

            .. tab-item:: Q2

                Modify the code to create a vertical gradient from 1 in the top to 9 in the bottom using a definition to produce the gradient list: [1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 5, 5, 5, 5, 5, 7, 7, 7, 7, 7, 9, 9, 9, 9, 9]

                .. code-block:: python
                    
                    from microbit import *


                    def gradient_y(y_val1, y_step):
                        grid = []
                        for y in range(5):
                            new_y = min(9, max(0, int(y_val1 + (y * y_step))))
                            for x in range(5):
                                grid.append(new_y)
                        return grid


                    img_array = gradient_y(1, 2)
                    img_vert_grad = Image(5, 5, bytearray(img_array))
                    display.show(img_vert_grad)

            .. tab-item:: Q3

                Use the definition for a vertical gradient to create one from 9 in the top to 2 in the bottom, [9, 9, 9, 9, 9, 7, 7, 7, 7, 7, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 2, 2, 2, 2, 2], and display it.

                .. code-block:: python
                    
                    from microbit import *


                    def gradient_y(y_val1, y_step):
                        grid = []
                        for y in range(5):
                            new_y = min(9, max(0, int(y_val1 + (y * y_step))))
                            for x in range(5):
                                grid.append(new_y)
                        return grid


                    img_array = gradient_y(9, -8 / 5)
                    img_vert_grad = Image(5, 5, bytearray(img_array))
                    display.show(img_vert_grad)


            .. tab-item:: Q4

                Write a definition to produce the list to be used for a diagonal gradient from 1 in the top left to 9 in the bottom right, [1, 2, 3, 4, 5, 2, 3, 4, 5, 6, 3, 4, 5, 6, 7, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9], and display it.

                .. code-block:: python
                    
                    from microbit import *


                    def gradient_xy(xy_val1, x_step, y_step):
                        grid = []
                        for y in range(5):
                            y_add = min(9, max(0, (y * y_step)))
                            for x in range(5):
                                x_add = min(9, max(0, (x * x_step)))
                                new_xy = min(9, max(0, int(xy_val1 + x_add + y_add)))
                                grid.append(new_xy)
                        return grid


                    img_array = gradient_xy(1, 1, 1)
                    img_vert_grad = Image(5, 5, bytearray(img_array))
                    display.show(img_vert_grad)

----

Random-integer-producing definitions for bytearray
-----------------------------------------------------

| The code below creates a 5 by 5 images with random brightness.

.. code-block:: python

    from microbit import *
    from random import randint


    def full_screen_fill_bytes(min_brightness=1, max_brightness=9):
        screen_bytes = []
        for y in range(0, 5):
            for x in range(0, 5):
                brightness = randint(min_brightness, max_brightness)
                screen_bytes.append(brightness)
        return screen_bytes


    while True:
        screen_bytes = full_screen_fill_bytes(1, 9)
        new_img = Image(5, 5, bytearray(screen_bytes))
        display.show(new_img)
        sleep(1000)

----

.. admonition:: Tasks

    #. Modify the code to add 2 nested for-loops for x values so that the left and right edges use the max_brightness value.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to add 2 nested for-loops for x values so that the left and right edges use the max_brightness value.

                .. code-block:: python
                    
                    from microbit import *
                    from random import randint


                    def full_screen_fill_bytes(min_brightness=1, max_brightness=9):
                        screen_bytes = []
                        for y in range(0, 5):
                            for x in range(0, 1):
                                brightness = max_brightness
                                screen_bytes.append(brightness)
                            for x in range(1, 4):
                                brightness = randint(min_brightness, max_brightness)
                                screen_bytes.append(brightness)
                            for x in range(4, 5):
                                brightness = max_brightness
                                screen_bytes.append(brightness)
                        return screen_bytes


                    while True:
                        screen_bytes = full_screen_fill_bytes(1, 9)
                        new_img = Image(5, 5, bytearray(screen_bytes))
                        display.show(new_img)
                        sleep(1000)   
        
----

List comprehension for bytearray images
--------------------------------------------

See: https://www.w3schools.com/python/python_lists_comprehension.asp

.. py:function:: new_list = [expression for item in iterable]

    | Create a list of the results of expressions that take each item in an iterable, such as a list, tuple or string.


| The code below creates a 5 by 5 image with increasing brightness.
| **[int(i/3 + 1) for i in range(25)]**  makes the list of integers: [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9].

.. code-block:: python

    from microbit import *


    brightness_array = [int(i/3 + 1) for i in range(25)]
    new_img = Image(5, 5, bytearray(brightness_array))
    display.show(new_img)


| The code below creates 5 by 5 images with random brightness.
| **[random.randint(0, 9) for _ in range(25)]**  makes a list of 25 random integers.
| **_** is used as a throw away variable since it is not used in the expression.

.. code-block:: python

    from microbit import *
    import random


    while True:
        brightness_array = [random.randint(0, 9) for _ in range(25)]
        new_img = Image(5, 5, bytearray(brightness_array))
        display.show(new_img)
        sleep(300)

----

.. admonition:: Tasks

    #. Modify the code to produce an image with pixels at a brightness determined by the formula: **int(((i % 3) + 1) * 3)**. This creates a cyclic pattern of 3.
    #. Modify the code to produce images made up of random brightnesses chosen from the list [1, 5, 9]. 


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to produce an image with pixels at a brightness determined by the formula: **int(((i % 3) + 1) * 3)**. This creates a cyclic pattern of 3.

                .. code-block:: python
                    
                    from microbit import *


                    brightness_array = [int(((i % 3) + 1) * 3) for i in range(25)]
                    new_img = Image(5, 5, bytearray(brightness_array))
                    display.show(new_img)

            .. tab-item:: Q2

                Modify the code to produce images made up of random brightnesses chosen from the list [1, 5, 9].

                .. code-block:: python
                    
                    from microbit import *
                    import random


                    while True:
                        brightness_array = [random.choice([1, 5, 9]) for _ in range(25)]
                        new_img = Image(5, 5, bytearray(brightness_array))
                        display.show(new_img)
                        sleep(500)

----

List comprehension with alternatives for bytearray images
----------------------------------------------------------

See: https://www.w3schools.com/python/python_lists_comprehension.asp

.. py:function:: new_list = [expression if condition else expression2 for item in iterable]

    | Create a list of expressions that take each item in an iterable, such as a list, tuple or string.

| The code below creates a 5 by 5 image with the brightness dependant on the position.
| **i % 2 == 0** is 0 for all even integers, i.

.. code-block:: python

    from microbit import *


    brightness_array = [9 if i % 2 == 0 else 0 for i in range(25)]
    new_img = Image(5, 5, bytearray(brightness_array))
    display.show(new_img)

----

.. admonition:: Tasks

    #. Modify the code set the brightness to 9 when i mod 1 is 1 instead of 0.
    #. Modify the code to use mod 3 instead of mod 2.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code set the brightness to 9 when i mod 1 is 1 instead of 0.

                .. code-block:: python
                    
                    from microbit import *

                    brightness_array = [9 if i % 2 == 1 else 0 for i in range(25)]
                    new_img = Image(5, 5, bytearray(brightness_array))
                    display.show(new_img)

            .. tab-item:: Q2

                Modify the code to use mod 3 instead of mod 2.

                .. code-block:: python
                    
                    from microbit import *

                    brightness_array = [9 if i % 3 == 0 else 0 for i in range(25)]
                    new_img = Image(5, 5, bytearray(brightness_array))
                    display.show(new_img)

