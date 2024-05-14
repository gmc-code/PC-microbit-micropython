====================================================
Image arithmetic
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


Fill
-----------------------------


.. py:method:: fill(value)

    | Set the brightness of all the pixels in the image to the **value**, between 0 and 9.
    | The fill method applies the fill in-place to the image.
    | Don't use with built-in images since they are read-only and cannot be altered.

| The code below sets all the pixels to a brightness of 6.

.. code-block:: python

    from microbit import *

    img = Image()
    img.fill(6)
    display.show(img)

----

.. admonition:: Tasks

    #. Create a blank image and fill it with brightness of 9.
    #. Create a blank image and use a for-loop to set its brightness from 1 to 9 in less than 2 seconds using the fill method.
    #. Create an animation using the fill method in which the brightness of all the pixels goes form 0 to 9 and back to 0 in less than 2 seconds.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Create a blank image and fill it with brightness of 9.

                    .. code-block:: python

                        from microbit import *

                        img = Image()
                        img.fill(6)
                        display.show(img)

                .. tab-item:: Q2

                    Create a blank image and use a for-loop to set its brightness from 1 to 9 in less than 2 seconds using the fill method.

                    .. code-block:: python

                        from microbit import *

                        img = Image()

                        for i in range(1, 10):
                            img.fill(i)
                            display.show(img)
                            sleep(200)

                .. tab-item:: Q2

                    Create an animation using the fill method in which the brightness of all the pixels goes form 0 to 9 and back to 0 in less than 2 seconds.

                    .. code-block:: python

                        from microbit import *

                        img = Image()

                        for i in range(0, 10):
                            img.fill(i)
                            display.show(img)
                            sleep(100)
                        for i in range(9, -1, -1):
                            img.fill(i)
                            display.show(img)
                            sleep(100)

----

Invert
-----------------------------

.. py:function:: invert()

    | Return a new image by inverting the brightness of the pixels in the source image.


.. code-block:: python

    from microbit import *
    
    img1 = Image()
    img1_inverted = img1.invert()
    display.show(img1_inverted)


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
                        inv_square = square.invert()
                        while True:
                            display.show(square)
                            sleep(500)
                            display.show(inv_square)
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
    img_sad_happy = img_sad + img_happy

    while True:
        display.show(img_sad)
        sleep(500)
        display.show(img_happy)
        sleep(500)
        display.show(img_sad_happy)
        sleep(500)

----

.. admonition:: Tasks

    #. Modify the code to create the addition of the images from 3 and 5.
    #. Modify the code to create the addition of the images "m" and an inverted "m".
    #. Modify the code to create the addition of the sad and asleep images.

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
                        img_m_and_m_inv = img_m + img_m_inv

                        while True:
                            if button_a.is_pressed():
                                display.show(img_m)
                            elif button_b.is_pressed():
                                display.show(img_m_inv)
                            else:
                                display.show(img_m_and_m_inv)
                            sleep(500)

                .. tab-item:: Q3

                    Modify the code to create the addition of the sad and asleep images.

                    .. code-block:: python

                        from microbit import *


                        img1 = Image.SAD
                        img2 = Image.ASLEEP
                        img12 = img1 + img2

                        while True:
                            display.show(img1)
                            sleep(800)
                            display.show(img2)
                            sleep(800)
                            display.show(img12)
                            sleep(800)

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
                        img_sad_less_happy = img_sad - img_happy

                        while True:
                            display.show(img_sad)
                            sleep(500)
                            display.show(img_happy)
                            sleep(500)
                            display.show(img_sad_less_happy)
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
    #. Using the pulsing code above as a starting point, add extra code so that it is possible to set the number of pulses per second and use that to calculate the sleep_time.

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

Pulsing HEART
---------------

| In the code below, image **img9** has pixels of brightness 9.
| An image, **img1**, with brightness 1, is first created from that, then other brightnesses are obtained in for-loops so that the image is pulsed.
| The sleep_time variable makes it convenient to adjust the pulsing rate.

.. code-block:: python

    from microbit import *

    img9 = Image.HEART
    img1 = img9 / 9
    sleep_time = 50
    while True:
        for i in range(10):
            img = img1 * i
            display.show(img)
            sleep(sleep_time)
        for i in range(9, -1, -1):
            img = img1 * i
            display.show(img)
            sleep(sleep_time)

----

.. admonition:: Tasks

    #. Using the pulsing code above as a starting point, add extra code so that it is possible to set use the number of pulses per second to calculate the sleep_time. Set the pulse rate to 100 pulses per minute.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Using the pulsing code above as a starting point, add extra code so that it is possible to use the number of pulses per second to calculate the sleep_time.

                    .. code-block:: python

                        from microbit import *
                        
                        img9 = Image.HEART
                        img1 = img9 / 9
                        pulses_per_min = 100
                        sleep_time = int(3000 / pulses_per_min)
                        while True:
                            for i in range(10):
                                img = img1 * i
                                display.show(img)
                                sleep(sleep_time)
                            for i in range(9, -1, -1):
                                img = img1 * i
                                display.show(img)
                                sleep(sleep_time)

----


List comprehension for a series of images
--------------------------------------------

See: https://www.w3schools.com/python/python_lists_comprehension.asp

.. function:: new_list = [expression for item in iterable]

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


| Another way to do this is by multiplication of a base image with all pixels at a brightness of 1.

.. code-block:: python

    from microbit import *
    
    img0 = Image()
    img0.fill(1)
    square_9to0_list = [img0 * i for i in range(9, -1, -1)]

    while True:
        if button_a.is_pressed():
            display.show(square_9to0_list, delay=100, wait=False)
        elif button_b.is_pressed():
            display.show(square_9to0_list, delay=300, wait=False)

----

.. admonition:: Tasks

    #. Modify the code to create a simple square brightness animation from 0 to 9 at different speeds set by the delay value.
    #. Modify the code to create a series of images of a sad face with brightness of 9, 7, 5, 3, 1 using list comprehension.
    #. Modify the code to create a series of images of a sad face with brightness of 1, 3, 5, 7, 9 using list comprehension.
    
    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to create a simple square brightness animation from 0 to 9 at different speeds set by the delay value.

                    .. code-block:: python

                        from microbit import *

                        square_0to9_list = [Image().invert()*(i/9) for i in range(0, 10, 1)]

                        while True:
                            if button_a.is_pressed():
                                display.show(square_0to9_list, delay=100, wait=False)
                            elif button_b.is_pressed():
                                display.show(square_0to9_list, delay=300, wait=False)

                .. tab-item:: Q2

                    Modify the code to create a series of images of a sad face with brightness of 9, 7, 5, 3, 1 using list comprehension.

                    .. code-block:: python

                        from microbit import *

                        sad_9to0_list = [Image.SAD * (i/9) for i in range(9, -1, -2)]

                        while True:
                            if button_a.is_pressed():
                                display.show(sad_9to0_list, delay=100, wait=False)
                            elif button_b.is_pressed():
                                display.show(sad_9to0_list, delay=300, wait=False)

                .. tab-item:: Q3

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

Pulsing Images
---------------

| The code below pulses any image with a given delay between each brightness.
| The image is used to make 20 images with brightness values that go from 0 to 9 and back down to 0.
| The input image needs to have pixel brightnesses of 9, although pixels of 5 or above will work.
| The custom syntax is below:

.. function:: pulse_image(img, pulse_delay=100)

    | **img** can be a built-in such as **Image.HEART** or a custom image such as **Image("90909:" * 5)** or **Image(5, 5, bytearray([9] * 25))**.
    | Pulse_delay defaults to 100 ms. It is the time between each image.

| Pulse_image uses the image_brightness function to produce an image with the given brightness.
| Pixels in the original image with a brightness of 5 or more are included; other pixels will be off. 

.. code-block:: python

    from microbit import *


    def image_brightness(img, brightness):
        res = img / 9 * brightness
        return res


    def pulse_image(img, pulse_delay=100):
        img_list1 = [image_brightness(img, i) for i in range(0, 10, 1)]
        img_list2 = [image_brightness(img, i) for i in range(9, -1, -1)]
        display.show(img_list1 + img_list2, delay=pulse_delay, wait=True) 


    while True:
        pulse_image(Image.HEART, 50)

----

.. admonition:: Tasks

    #. Modify the code above to pulse a series of animal images.
    #. Modify the code to pulse a series of faces.
    #. Add a for-loop to pulse each face 3 times before changing to the next face.
    #. Replace the image_brightness function with **image_brightness_with_inverted** to create a combined image that has the inverted image of complimentary brightness. e.g. original image of brightness 2 added to inverted image of brightness 7. Rename pulse_image to **pulse_image_inverted** to include the new **image_brightness_with_inverted**.
    
    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code above to pulse a series of animal images.

                    .. code-block:: python

                        from microbit import *


                        def image_brightness(img, brightness):
                            res = img / 9 * brightness
                            return res


                        def pulse_image(img, pulse_delay=100):
                            img_list1 = [image_brightness(img, i) for i in range(0, 10, 1)]
                            img_list2 = [image_brightness(img, i) for i in range(9, -1, -1)]
                            display.show(img_list1 + img_list2, delay=pulse_delay, wait=True) 


                        animal_images = [
                                            Image.RABBIT,
                                            Image.COW,
                                            Image.DUCK,
                                            Image.TORTOISE,
                                            Image.BUTTERFLY,
                                            Image.GIRAFFE,
                                            Image.SNAKE,
                                        ]
                                        
                            
                        while True:
                            for img in animal_images:
                                pulse_image(img, 50)


                .. tab-item:: Q2

                    Modify the code to pulse a series of faces.

                    .. code-block:: python

                        from microbit import *


                        def image_brightness(img, brightness):
                            res = img / 9 * brightness
                            return res


                        def pulse_image(img, pulse_delay=100):
                            img_list1 = [image_brightness(img, i) for i in range(0, 10, 1)]
                            img_list2 = [image_brightness(img, i) for i in range(9, -1, -1)]
                            display.show(img_list1 + img_list2, delay=pulse_delay, wait=True) 


                        images = [Image.HAPPY, Image.SMILE, Image.SAD, Image.CONFUSED,
                            Image.ANGRY, Image.ASLEEP, Image.SURPRISED, Image.SILLY,
                            Image.FABULOUS, Image.MEH]    
                            
                        while True:
                            for img in images:
                                pulse_image(img, 50)

                .. tab-item:: Q3

                    Add a for-loop to quickly pulse each face 3 times before changing to the next face.

                    .. code-block:: python

                        from microbit import *

                        def image_brightness(img, brightness):
                            res = img / 9 * brightness
                            return res


                        def pulse_image(img, pulse_delay=100):
                            img_list1 = [image_brightness(img, i) for i in range(0, 10, 1)]
                            img_list2 = [image_brightness(img, i) for i in range(9, -1, -1)]
                            display.show(img_list1 + img_list2, delay=pulse_delay, wait=True) 


                        images = [Image.HAPPY, Image.SMILE, Image.SAD, Image.CONFUSED,
                            Image.ANGRY, Image.ASLEEP, Image.SURPRISED, Image.SILLY,
                            Image.FABULOUS, Image.MEH]    
                            
                        while True:
                            for img in images:
                                for _ in range(3):
                                    pulse_image(img, 40)

                .. tab-item:: Q4

                    Replace the image_brightness function with **image_brightness_with_inverted** to create a combined image that has the inverted image of complimentary brightness. e.g. original image of brightness 2 added to inverted image of brightness 7. Rename pulse_image to **pulse_image_inverted** to include the new **image_brightness_with_inverted**.

                    .. code-block:: python

                        from microbit import *

                        def image_brightness_with_inverted(img, brightness):
                            res = img / 9 * brightness
                            res_inv = img.invert() / 9 * (9 - brightness)
                            return res + res_inv


                        def pulse_image_inverted(img, pulse_delay=100):
                            img_list1 = [image_brightness_with_inverted(img, i) for i in range(0, 10, 1)]
                            img_list2 = [image_brightness_with_inverted(img, i) for i in range(9, -1, -1)]
                            display.show(img_list1 + img_list2, delay=pulse_delay, wait=True) 


                        images = [Image.HAPPY, Image.SMILE, Image.SAD, Image.CONFUSED,
                            Image.ANGRY, Image.ASLEEP, Image.SURPRISED, Image.SILLY,
                            Image.FABULOUS, Image.MEH]    
                            
                        while True:
                            for img in images:
                                for _ in range(3):
                                    pulse_image_inverted(img, 40)

