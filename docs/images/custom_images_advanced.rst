====================================================
Custom images advanced
====================================================

See: https://microbit-micropython.readthedocs.io/en/v2-docs/image.html

Image()
-----------------------------

| The basic syntax for showing creating an Image object is:

.. py:function:: Image()

    | Returns an image object, with each pixel of brightness 0.
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

.. sidebar::

    .. image:: images/vertical_gradient.png
        :scale: 50 %
        :align: left
    
    .. image:: images/vertical_gradient_inverted.png
        :scale: 50 %
        :align: right

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
        :align: left
    
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


                        img_sad = Image.SAD
                        img_sad_inverted = img_sad.invert()
                        while True:
                            display.show(img_sad)
                            sleep(500)
                            display.show(img_sad_inverted)
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

    #. Modify the code to create an image of 3.
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
                        img_m_inv = img_m.invert()

                        while True:
                            if button_a.is_pressed():
                                display.show(img_m)
                            elif button_b.is_pressed():
                                display.show(img_m_inv)
                            sleep(200)

----

Adding Image pixels
-----------------------------------------

.. py:function:: image1 + image2

    | Create a new image by adding the brightness values from the two images for each pixel.

    .. image:: images/mw.png
        :scale: 50 %
        :align: right

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
        :align: left

    .. image:: images/HAPPY.png
        :scale: 50 %
        :align: right

    .. image:: images/SAD_HAPPY.png
        :scale: 50 %
        :align: center

| The code below adds the SAD image and the HAPPY image.

.. code-block:: python

    from microbit import *


    img_sad = Image.SAD
    img_happy = Image.HAPPY
    img_sadhappy = img_sad + img_happy

    while True:
        display.show(img_sad)
        sleep(500)
        display.show(img_happy)
        sleep(500)
        display.show(img_sadhappy)
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
                        img_m_inv = img_m.invert()
                        img_mminv = img_m + img_m_inv

                        while True:
                            if button_a.is_pressed():
                                display.show(img_m)
                            elif button_b.is_pressed():
                                display.show(img_m_inv)
                            else:
                                display.show(img_mminv)
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


                        img_sad = Image.SAD
                        img_happy = Image.HAPPY
                        img_sadlesshappy = img_sad - img_happy

                        while True:
                            display.show(img_sad)
                            sleep(500)
                            display.show(img_happy)
                            sleep(500)
                            display.show(img_sadlesshappy)
                            sleep(500)


----

Multiplying and dividing Image pixels
-----------------------------------------

.. py:function:: image * n

    | Create a new image by multiplying the brightness of each pixel by n.
    | It makes sure the resulting Image object has integer values.
    | Values for each pixel cannot go over 9.

.. py:function:: image / n

    | Create a new image by dividing the brightness of each pixel by n.
    | It makes sure the resulting Image object has integer values.
    | Values for each pixel are rounded; 0.4 down to 0, 0.5 up to 1.

| In the code below, image **img_m9** has pixels of brightness 9.
| An image, **img_m1**, with brightness 1, is first created from that, then other brightnesses can be easily obtained by multiplication.

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
                        img_m6_w3 = img_m6 + img_w3

                        while True:
                            if button_a.is_pressed():
                                display.show(img_m6)
                            elif button_b.is_pressed():
                                display.show(img_w3)
                            else:
                                display.show(img_m6_w3)
                            sleep(500)

----


List comprehension for a series of images
--------------------------------------------

See: https://www.w3schools.com/python/python_lists_comprehension.asp

.. py:function:: newlist = [expression for item in iterable]

    | Create a list of expressions that take each item in an iterable, such as a list, tuple or string.

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

