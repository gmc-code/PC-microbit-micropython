====================================================
Custom images advanced
====================================================

See: https://microbit-micropython.readthedocs.io/en/v2-docs/image.html

Image()
-----------------------------

| The basic syntax for showing creating an Image object is:

.. py:function:: Image()

    | Returns an empty image object, with each pixel of brightness 0.
    | **Image()** is equivalent to:
    | Image(
        '00000:'
        '00000:'
        '00000:'
        '00000:'
        '00000:'
        )

----

Invert
-----------------------------

.. py:function:: Image().invert()

    | Return a new image by inverting the brightness of the pixels in the source image.


| **Image().invert()** is equivalent to:

.. code-block:: python

    Image(
        '99999:'
        '99999:'
        '99999:'
        '99999:'
        '99999:'
        )

| When inverted, a pixel of brightness 0 becomes 9, 1 becomes 8, 2 becomes 7,....8 becomes 1, 9 becomes 0.   

| An image may be stored in a variable then inverted.
| In the code below, the image is inverted, and so:
| **Image('11111:33333:55555:77777:99999')** is inverted to:
| **Image('88888:66666:44444:22222:00000:')**

.. code-block:: python

    from microbit import *
    
    img1 = Image('11111:33333:55555:77777:99999')
    img1_inverted = img1.invert()


.. sidebar::

    .. image:: images/HAPPY.png
        :scale: 50 %
        :align: center

    .. image:: images/happy_inverted.png
        :scale: 50 %
        :align: right

| A built-in image can be stored in a variable, then inverted.
| The inverted HAPPY face is shown.

.. code-block:: python

    from microbit import *
    
    img1 = Image.HAPPY
    img1_inverted = img1.invert()
    display.show(img1_inverted)

----

.. admonition:: Tasks

    #. Invert the square: ``Image('99999:90009:90009:90009:99999')``. Display the square and its inversion in a while loop.
    #. Invert the gradient: ``Image('11111:33333:55555:77777:99999')``. Display the gradient and its inversion in a while loop.
    #. Invert Image.SAD. Display the sad face and its inversion in a while loop.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Invert the square: ``Image('99999:90009:90009:90009:99999')``. Display the square and its inversion in a while loop.

                    .. code-block:: python

                        from microbit import *


                        square = Image('99999:90009:90009:90009:99999')
                        invsquare = square.invert()
                        while True:
                            display.show(square)
                            sleep(500)
                            display.show(invsquare)
                            sleep(500)

                .. tab-item:: Q2

                    Invert the gradient: ``Image('11111:33333:55555:77777:99999')``. Display the gradient and its inversion in a while loop.

                    .. code-block:: python

                        from microbit import *


                        img1 = Image('11111:33333:55555:77777:99999')
                        img1_inverted = img1.invert()
                        while True:
                            display.show(img1)
                            sleep(500)
                            display.show(img1_inverted)
                            sleep(500)

                .. tab-item:: Q3

                    Invert Image.SAD. Display the sad face and its inversion in a while loop.

                    .. code-block:: python

                        from microbit import *


                        img1 = Image.SAD
                        img1_inverted = img1.invert()
                        while True:
                            display.show(img1)
                            sleep(500)
                            display.show(img1_inverted)
                            sleep(500)

----

Image of a single string character
-----------------------------------------

.. py:function:: Image(character)

    | Returns an image object that represents the character. The characters must be in quotes.

| ``img_m = Image("m")`` stores the image in a variable which is then shown via: ``display.show(img_m)``

.. code-block:: python

    from microbit import *

    img_m = Image("m")

    while True:
        if button_a.is_pressed():
            display.show(img_m)
        sleep(200)

----


.. admonition:: Tasks

    #. Modify the code to create an images of 3.
    #. Modify the code to create images of "m" and an inverted "m".

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to create images of 3 and 5.

                    .. code-block:: python

                        from microbit import *

                        img_3 = Image("3")

                        while True:
                            if button_a.is_pressed():
                                display.show(img_3)
                            sleep(200)

                .. tab-item:: Q2
                    
                    Modify the code to create images of "m" and an inverted "m".

                    .. code-block:: python

                        from microbit import *

                        img_m = Image("m")
                        img_invm = img_m.invert()

                        while True:
                            if button_a.is_pressed():
                                display.show(img_m)
                            elif button_b.is_pressed():
                                display.show(img_invm)
                            sleep(200)

----

Adding Image pixels
-----------------------------------------

.. py:function:: image1 + image2

    | Create a new image by adding the brightness values from the two images for each pixel.

| The code below adds the images made from an "m" and a "w".

.. code-block:: python

    from microbit import *

    img_m = Image("m")
    img_w = Image("w")
    img_mw = img_m + img_w

    while True:
        if button_a.is_pressed():
            display.show(img_m)
        elif button_b.is_pressed():
            display.show(img_w)
        else:
            display.show(img_mw)
        sleep(500)


.. sidebar::

    .. image:: images/SAD.png
        :scale: 50 %
        :align: center

    ~~~~~~~~~~~~~~~~~

    .. image:: images/HAPPY.png
        :scale: 50 %
        :align: center

    ~~~~~~~~~~~~~~~~~

    .. image:: images/SAD_HAPPY.png
        :scale: 50 %
        :align: center


| The code below adds the SAD image and the HAPPY image.

.. code-block:: python

    from microbit import *


    img1 = Image.SAD
    img2 = Image.HAPPY
    while True:
        display.show(img1)
        sleep(500)
        display.show(img2)
        sleep(500)
        display.show(img1 + img2)
        sleep(500)


----


.. admonition:: Tasks

    #. Modify the code to create the addition of the images from 3 and 5.
    #. Modify the code to create the addition of the images "m" and an inverted "m".

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to create the addition of the images from 3 and 5.

                    .. code-block:: python

                        from microbit import *

                        img_3 = Image("3")
                        img_5 = Image("5")
                        img_35 = img_3 + img_5

                        while True:
                            if button_a.is_pressed():
                                display.show(img_3)
                            elif button_b.is_pressed():
                                display.show(img_5)
                            else:
                                display.show(img_35)
                            sleep(500)

                .. tab-item:: Q2

                    Modify the code to create the addition of the images "m" and an inverted "m".

                    .. code-block:: python

                        from microbit import *

                        img_m = Image("m")
                        img_invm = img_m.invert()
                        img_m_invm = img_m + img_invm

                        while True:
                            if button_a.is_pressed():
                                display.show(img_m)
                            elif button_b.is_pressed():
                                display.show(img_invm)
                            else:
                                display.show(img_m_invm)
                            sleep(500)

----

Subtracting Image pixels
-----------------------------------------

.. py:function:: image1 - image2

    | Create a new image by subtracting the brightness values of one image from another for each pixel.


.. code-block:: python

    from microbit import *

    img_m = Image("m")
    img_w = Image("w")
    img_m_sub_w = img_m - img_w

    while True:
        if button_a.is_pressed():
            display.show(img_m)
        elif button_b.is_pressed():
            display.show(img_w)
        else:
            display.show(img_m_sub_w)
        sleep(500)

----


.. admonition:: Tasks

    #. Modify the code to create a new image by subtracting the image "m" from an inverted blank image.
    #. Modify the code to create a new image by subtracting the image HAPPY from the image SAD.


    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to create a new image by subtracting the image "m" from an inverted blank image.

                    .. code-block:: python

                        from microbit import *


                        img_all = Image().invert()
                        img_m = Image("m")
                        img_all_sub_m = img_all - img_m

                        while True:
                            if button_a.is_pressed():
                                display.show(img_m)
                            elif button_b.is_pressed():
                                display.show(img_all)
                            else:
                                display.show(img_all_sub_m)
                            sleep(500)

                .. tab-item:: Q2

                    Modify the code to create a new image by subtracting the image HAPPY from the image SAD.

                    .. code-block:: python

                        from microbit import *


                        img1 = Image.SAD
                        img2 = Image.HAPPY
                        while True:
                            display.show(img1)
                            sleep(500)
                            display.show(img2)
                            sleep(500)
                            display.show(img1 - img2)
                            sleep(500)


----

Multiplying and dividing Image pixels
-----------------------------------------

.. py:function:: image * n

    | Create a new image by multiplying the brightness of each pixel by n.
    | Make sure the resulting Image object has integer values.

.. py:function:: image / n

    | Create a new image by dividing the brightness of each pixel by n.
    | Make sure the resulting Image object has integer values.

| In the code below, image **img_m9** have pixels of brightness 9.
| An image with brightness 1 is first created from that, then other brightnesses can be easily set.

.. code-block:: python

    from microbit import *

    img_m9 = Image("m")
    img_m1 = img_m9 / 9 
    img_m6 = img_m1 * 6

    while True:
        if button_a.is_pressed():
            display.show(img_m9)
        elif button_b.is_pressed():
            display.show(img_m6)
        else:
            display.show(img_m1)
        sleep(500)

----

.. admonition:: Tasks

    #. Modify the code to create the images of a "w" with brightness of 9, 1 and 4.
    #. Modify the code to create the addition of the images "m" at brightness 6 and "w" at brightness 3.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to create the images of a "w" with brightness of 9, 1 and 4.

                    .. code-block:: python

                        from microbit import *

                        img_w9 = Image("w")
                        img_w1 = img_w9 / 9 
                        img_w4 = img_w1 * 4

                        while True:
                            if button_a.is_pressed():
                                display.show(img_w9)
                            elif button_b.is_pressed():
                                display.show(img_w4)
                            else:
                                display.show(img_w1)
                            sleep(500)

                .. tab-item:: Q2

                    Modify the code to create the addition of the images "m" at brightness 6 and "w" at brightness 3.

                    .. code-block:: python

                        from microbit import *

                        img_m9 = Image("m")
                        img_m1 = img_m9  / 9 
                        img_m6 = img_m1 * 6
                        img_w9 = Image("w")
                        img_w1 = img_w9  / 9 
                        img_w3 = img_w1 * 3
                        img_comp = img_m6 + img_w3

                        while True:
                            if button_a.is_pressed():
                                display.show(img_m6)
                            elif button_b.is_pressed():
                                display.show(img_w3)
                            else:
                                display.show(img_comp)
                            sleep(500)

----

List comprehension for a series of images
--------------------------------------------

See: https://www.w3schools.com/python/python_lists_comprehension.asp

.. py:function:: image_list = [Image().invert()*(i/9) for i in range(9, -1, -1)]

    | Create a series of 5 by 5 images with brightness decreasing from 9 to 0 in steps of 1.

----

| The code below creates a simple square brightness animation from 9 to 0 at different speeds set by the delay value.

.. code-block:: python

    from microbit import *
    
    square_9to0_list = [Image().invert()*(i/9) for i in range(9, -1, -1)]

    while True:
        if button_a.is_pressed():
            display.show(square_9to0_list, delay=100, wait=False)
        elif button_b.is_pressed():
            display.show(square_9to0_list, delay=300, wait=False)

----

.. admonition:: Tasks

    #. Modify the code to create a series of images of a sad face with brightness of 9, 7, 5, 3, 1 using list comprehension.
    #. Modify the code to create a series of images of a sad face with brightness of 1, 3, 5, 7, 9 using list comprehension.
    
    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to create a series of images of a sad face with brightness of 9, 7, 5, 3, 1 using list comprehension.

                    .. code-block:: python

                        from microbit import *

                        sad_9to0_list = [Image.SAD * (i/9) for i in range(9, -1, -2)]

                        while True:
                            if button_a.is_pressed():
                                display.show(sad_9to0_list, delay=100, wait=False)
                            elif button_b.is_pressed():
                                display.show(sad_9to0_list, delay=300, wait=False)

                .. tab-item:: Q2

                    Modify the code to create a series of images of a sad face with brightness of 1, 3, 5, 7, 9 using list comprehension.

                    .. code-block:: python

                        from microbit import *

                        sad_0to9_list = [Image.SAD * (i/9) for i in range(0, 10, 2)]

                        while True:
                            if button_a.is_pressed():
                                display.show(sad_0to9_list, delay=100, wait=False)
                            elif button_b.is_pressed():
                                display.show(sad_0to9_list, delay=300, wait=False)

----

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
| Example ode to limit the values and round to an integer is below.
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

get_pixel and set_pixel
---------------------------


| The code below creates changing displays of random pixels. It checks to see when the display has been filled with 25 pixels and displays the number of attempts of creating random pixels.

.. code-block:: python

    from microbit import *
    from random import randint

    def full_screen_check():
        for y in range(0, 5):
            for x in range(0, 5):
                if display.get_pixel(x, y) == 0:
                    return False
        return True

    def fill_screen_with_counter():
        counter = 0
        while True:
            counter += 1
            x = randint(0, 4)
            y = randint(0, 4)
            brightness = randint(5,9)
            display.set_pixel(x, y, brightness)
            if full_screen_check():
                display.scroll(counter)
                return counter
            sleep(30)

    while True:
        fill_screen_with_counter()
        sleep(1000)



