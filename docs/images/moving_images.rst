====================================================
Moving images
====================================================

| The following methods are described below: shift_left, shift_right, shift_up, shift_down, crop and blit.


Shift left and right
--------------------------------

| An image can be shifted left or right. 
| Parts of the image moved off screen are lost.
| So, if making animations, it is best to reuse the original image rather than reuse moved images.

.. py:method:: shift_left(n)

    Return a new image by shifting the image left by **n** columns.


.. py:method:: shift_right(n)

    Return a new image by shifting the image right by **n** columns.


| The code below shifts the small image of a dice, with a five on it, to the right 1 step, back, to the left 1 step and back.

.. code-block:: python

    from microbit import *

    img1 = Image("00000:09090:00900:09090:00000")

    display.show(img1)
    sleep(500)
    img = img1.shift_right(1)
    display.show(img)
    sleep(500)
    display.show(img1)
    sleep(500)
    img = img1.shift_left(1)
    display.show(img)
    sleep(500)
    display.show(img1)

----

.. admonition:: Tasks

    #.  Use a **for-loop** with the list: [-4, -3, -2, -1, 0, 1, 2, 3, 4] to shift the dice image to the right from off screen on the left to off screen on the right in 9 steps.
    #.  Use a **for-loop** with the range function to do the same shifts to shift the dice image to the right from off screen on the left to off screen on the right in 9 steps.
    #.  Use a **for-loop** with the list: [-4, -2, 0, 2, 4] to shift the dice image to the left from off screen on the right to off screen on the left in 5 steps.
    #.  Use a **for-loop** with the range function to do the same shifts to shift the dice image to the left from off screen on the right to off screen on the left in 5 steps.
    #.  Use a **for-loop** with the list: [0, 1, 2, 3, 4, -4, -3, -2, -1, 0] to shift the dice image to the right from a central position and back from off screen on the left in 10 steps.
    #.  Use a **for-loop** with the list: [0, 2, 4, -4, -2, 0] shift the dice image to the left from a central position and back from off screen on the right in 6 steps.
    #.  Create a definition, **h_shift_img_directions(img, directions, sleep_time=80)**,  that takes a list of shifts, **directions**,  for the shifts and applies them to move the dice image sideways, using [-4, -3, -2, -1, 0, 1, 2, 3, 4] as the argument for directions.


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Use a **for-loop** with the list: [-4, -3, -2, -1, 0, 1, 2, 3, 4] to shift the dice image to the right from off screen on the left to off screen on the right in 9 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in [-4, -3, -2, -1, 0, 1, 2, 3, 4]:
                        img = img1.shift_right(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q2

                Use a **for-loop** with the range function to do the same shifts to shift the dice image to the right from off screen on the left to off screen on the right in 9 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in range(-4, 5, 1):
                        img = img1.shift_right(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q3

                Use a **for-loop** with the list: [-4, -2, 0, 2, 4] to shift the dice image to the left from off screen on the right to off screen on the left in 5 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in [-4, -2, 0, 2, 4]:
                        img = img1.shift_left(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q4

                Use a **for-loop** with the range function to do the same shifts to shift the dice image to the left from off screen on the right to off screen on the left in 5 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in range(-4, 5, 2):
                        img = img1.shift_left(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q5

                Use a **for-loop** with the list: [0, 1, 2, 3, 4, -4, -3, -2, -1, 0] to shift the dice image to the right from a central position and back from off screen on the left in 10 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in [0, 1, 2, 3, 4, -4, -3, -2, -1, 0]:
                        img = img1.shift_right(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q6

                Use a **for-loop** with the list: [0, 2, 4, -4, -2, 0] shift the dice image to the left from a central position and back from off screen on the right in 6 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in [0, 2, 4, -4, -2, 0]:
                        img = img1.shift_left(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q7

                Create a definition, **h_shift_img_directions(img, directions, sleep_time=80)**,  that takes a list of shifts, **directions**,  for the shifts and applies them to move the dice image sideways, using [-4, -3, -2, -1, 0, 1, 2, 3, 4] as the argument for directions.

                .. code-block:: python

                    from microbit import *


                    def h_shift_img_directions(img, directions, sleep_time=80):
                        for x in directions:
                            shift_img = img.shift_right(x)
                            display.show(shift_img)
                            sleep(sleep_time)


                    img = Image("00000:09090:00900:09090:00000")
                    sleep_time = 200
                    h_directions = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
                    while True:
                        h_shift_img_directions(img, h_directions, sleep_time)


----

Shift up and down
--------------------------------

| An image can be shifted up or down.


.. py:method:: shift_up(n)

    Return a new image by shifting the image up by **n** rows.
        
.. py:method:: shift_down(n)

    Return a new image by shifting the image down by **n** rows.


| The code below shifts the small image of a dice, with a five on it, up 1 step, back, down 1 step and back.

.. code-block:: python

    from microbit import *

    img1 = Image("00000:09090:00900:09090:00000")

    display.show(img1)
    sleep(500)
    img = img1.shift_up(1)
    display.show(img)
    sleep(500)
    display.show(img1)
    sleep(500)
    img = img1.shift_down(1)
    display.show(img)
    sleep(500)
    display.show(img1)

----

.. admonition:: Tasks

    #.  Use a **for-loop** with the list: [-4, -3, -2, -1, 0, 1, 2, 3, 4] to shift the dice image up from off screen on the bottom to off screen on the top in 9 steps.
    #.  Use a **for-loop** with the range function to do the same shifts to shift the dice image up from off screen on the bottom to off screen on the top in 9 steps.
    #.  Use a **for-loop** with the list: [-4, -2, 0, 2, 4] to shift the dice image to the bottom from off screen on the top to off screen on the bottom in 5 steps.
    #.  Use a **for-loop** with the range function to do the same shifts to shift the dice image to the bottom from off screen on the top to off screen on the bottom in 5 steps.
    #.  Use a **for-loop** with the list: [0, 1, 2, 3, 4, -4, -3, -2, -1, 0] to shift the dice image up from a central position and back from off screen on the bottom in 10 steps.
    #.  Use a **for-loop** with the list: [0, 2, 4, -4, -2, 0] shift the dice image to the bottom from a central position and back from off screen on the top in 6 steps.
    #.  Create a definition, **v_shift_img_directions(img, directions, sleep_time=80)**,  that takes a list of shifts, **directions**,  for the shifts and applies them to move the dice image sideways, using [0, 1, 2, 3, 4, -4, -3, -2, -1, 0] as the argument for directions.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Use a **for-loop** with the list: [-4, -3, -2, -1, 0, 1, 2, 3, 4] to shift the dice image up from off screen on the bottom to off screen on the top in 9 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in [-4, -3, -2, -1, 0, 1, 2, 3, 4]:
                        img = img1.shift_up(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q2

                Use a **for-loop** with the range function to do the same shifts to shift the dice image up from off screen on the bottom to off screen on the top in 9 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in range(-4, 5, 1):
                        img = img1.shift_up(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q3

                Use a **for-loop** with the list: [-4, -2, 0, 2, 4] to shift the dice image to the bottom from off screen on the top to off screen on the bottom in 5 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in [-4, -2, 0, 2, 4]:
                        img = img1.shift_down(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q4

                Use a **for-loop** with the range function to do the same shifts to shift the dice image to the bottom from off screen on the top to off screen on the bottom in 5 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in range(-4, 5, 2):
                        img = img1.shift_down(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q5

                Use a **for-loop** with the list: [0, 1, 2, 3, 4, -4, -3, -2, -1, 0] to shift the dice image up from a central position and back from off screen on the bottom in 10 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in [0, 1, 2, 3, 4, -4, -3, -2, -1, 0]:
                        img = img1.shift_up(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q6

                Use a **for-loop** with the list: [0, 2, 4, -4, -2, 0] shift the dice image to the bottom from a central position and back from off screen on the top in 6 steps.

                .. code-block:: python

                    from microbit import *

                    img1 = Image("00000:09090:00900:09090:00000")

                    for i in [0, 2, 4, -4, -2, 0]:
                        img = img1.shift_down(i)
                        display.show(img)
                        sleep(500)

            .. tab-item:: Q7

                Create a definition, **v_shift_img_directions(img, directions, sleep_time=80)**,  that takes a list of shifts, **directions**,  for the shifts and applies them to move the dice image sideways, using [0, 1, 2, 3, 4, -4, -3, -2, -1, 0] as the argument for directions.

                .. code-block:: python

                    from microbit import *


                    def v_shift_img_directions(img, directions, sleep_time=80):
                        for y in directions:
                            shift_img = img.shift_down(y)
                            display.show(shift_img)
                            sleep(sleep_time)


                    img = Image("00000:09090:00900:09090:00000")
                    sleep_time = 200
                    v_directions = [0, 1, 2, 3, 4, -4, -3, -2, -1, 0]
                    while True:
                        v_shift_img_directions(img, v_directions, sleep_time)


----

Shifting vertically and horizontally
-----------------------------------------

| An image can be shifted in a vertical sequence and in a horizontal sequence to create movement patterns.


.. admonition:: Tasks

    #.  Use both **h_shift_img_directions(img, directions, sleep_time=80)** and **v_shift_img_directions(img, directions, sleep_time=80)**, to make a cross shaped movement pattern for Image("00000:09090:00900:09090:00000").

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Use both **h_shift_img_directions(img, directions, sleep_time=80)** and **v_shift_img_directions(img, directions, sleep_time=80)**, to make a cross shaped movement pattern for Image("00000:09090:00900:09090:00000").

                .. code-block:: python

                    from microbit import *


                    def v_shift_img_directions(img, directions, sleep_time=80):
                        for y in directions:
                            shift_img = img.shift_down(y)
                            display.show(shift_img)
                            sleep(sleep_time)

                    def h_shift_img_directions(img, directions, sleep_time=80):
                        for x in directions:
                            shift_img = img.shift_right(x)
                            display.show(shift_img)
                            sleep(sleep_time)

                    img = Image("00000:09090:00900:09090:00000")
                    sleep_time = 80
                    directions = [0, 1, 2, 3, 4, -4, -3, -2, -1, 0]
                    while True:
                        h_shift_img_directions(img, directions, sleep_time)
                        v_shift_img_directions(img, directions, sleep_time)


----

Shifting combined
--------------------------------

| An image can be shifted up or down and left or right to create movement patterns.

| The custom syntax below combines shifting in the x and y directions:

.. function:: shift_x_y(img, x, y, sleep_time=80)

    | **img** can be a built-in such as **Image.HEART** or a custom image such as **Image("90909:" * 5)** or **Image(5, 5, bytearray([9] * 25))**.
    | x is an integer
    | **sleep_time** defaults to 80 ms. It is the sleep time after showing the shifted image.

| The code below shifts a butterfly image clockwise in 4 moves. 


.. code-block:: python

    from microbit import *

    def shift_x_y(img, x, y, sleep_time=80):
        shift_img = img.shift_right(x)
        shift_img = shift_img.shift_down(y)
        display.show(shift_img)
        sleep(sleep_time)
            

    img = Image.BUTTERFLY
    sleep_time = 200
    while True:
        display.show(img)
        sleep(sleep_time)
        shift_x_y(img, 1, 0, sleep_time)
        shift_x_y(img, 1, 1, sleep_time)
        shift_x_y(img, 0, 1, sleep_time)

----

.. admonition:: Tasks

    #.  Alter the arguments to move the butterfly anticlockwise.
    #.  Create a definition, **shift_img_directions(img, directions, sleep_time=80)**,  that takes a list of tuples, **directions**,  for the shifts and applies them to move the butterfly anticlockwise.
    #.  Use the definition, **shift_img_directions(img, directions, sleep_time=80)**, to move the butterfly clockwise.
    #.  Predict what the following directions might do: **directions =  [(0, 0), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, 0)]**

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Alter the arguments to move the butterfly anticlockwise.

                .. code-block:: python

                    from microbit import *

                    def shift_x_y(img, x, y, sleep_time=80):
                        shift_img = img.shift_right(x)
                        shift_img = shift_img.shift_down(y)
                        display.show(shift_img)
                        sleep(sleep_time)
                            

                    img = Image.BUTTERFLY   
                    sleep_time = 200
                    while True:
                        display.show(img)
                        sleep(sleep_time)
                        shift_x_y(img, 0, 1, sleep_time)
                        shift_x_y(img, 1, 1, sleep_time)
                        shift_x_y(img, 1, 0, sleep_time)

            .. tab-item:: Q2

                Create a definition, **shift_img_directions(img, directions, sleep_time=80)**,  that takes a list of tuples, **directions**,  for the shifts and applies them to move the butterfly anticlockwise.

                .. code-block:: python

                    from microbit import *

                    def shift_x_y(img, x, y, sleep_time=80):
                        shift_img = img.shift_right(x)
                        shift_img = shift_img.shift_down(y)
                        display.show(shift_img)
                        sleep(sleep_time)
                            
                        
                    def shift_img_directions(img, directions, sleep_time=80):
                        for x,y in directions:
                            shift_x_y(img, x, y, sleep_time)


                    img = Image.BUTTERFLY
                    sleep_time = 200
                    while True:
                        anticlockwise_directions =  [(0, 0), (0, 1), (1, 1), (1, 0)]
                        shift_img_directions(img, anticlockwise_directions, sleep_time)

            .. tab-item:: Q3

                Use the definition, **shift_img_directions(img, directions, sleep_time=80)**, to move the butterfly clockwise.

                .. code-block:: python

                    from microbit import *

                    def shift_x_y(img, x, y, sleep_time=80):
                        shift_img = img.shift_right(x)
                        shift_img = shift_img.shift_down(y)
                        display.show(shift_img)
                        sleep(sleep_time)
                            
                        
                    def shift_img_directions(img, directions, sleep_time=80):
                        for x,y in directions:
                            shift_x_y(img, x, y, sleep_time)


                    img = Image.BUTTERFLY
                    sleep_time = 200
                    while True:
                        clockwise_directions =  [(0, 0), (1, 0), (1, 1), (0, 1) ]
                        shift_img_directions(img, clockwise_directions, sleep_time)

            .. tab-item:: Q4

                Predict what the following directions might do: **directions =  [(0, 0), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, 0)]**

                They move the image clockwise in a 2 by 2 square ranging from (-1, -1) to (1, 1).

----

Cropping images
--------------------------------

| An image can be cropped into a new image.

.. py:method:: crop(x, y, w, h)

    | Return a new image by cropping the image from x, y with width w, height h.
    | The new image is positioned at 0, 0 in the top left.

.. code-block:: python

    from microbit import *

    img = Image("00300:03630:36963:03630:00300")
    img_crop = img.crop(2, 2, 3, 3)

    while True:
        display.show(img)
        sleep(500)
        display.show(img_crop)
        sleep(500)

| Cropping usually needs shifting combined with it.
| The blit method is more useful for this.

----

Cropping images and repositioning with blit
------------------------------------------------------

| An image can be cropped and positioned in another image with the blit method.

.. py:method:: blit(src, x, y, w, h, xdest=0, ydest=0)

    | Copy the rectangle defined by **x**, **y**, **w**, **h** from an image **src** into
    the image at **xdest**, **ydest**.
    | Areas in the source rectangle, but outside the source image are given a value of 0.


| The code below crops a source image, source_img, from pixel x, y for a width, w, and height, h, and places it a pixel i, j in the a new blank 5 by 5 image which is returned.

.. code-block:: python

    from microbit import *
        
    def crop_to(source_img, x, y, w, h, i, j):
        res = Image(5, 5)
        res.blit(source_img, x, y, w, h, i, j)
        return res

| The code below gives an example of cropping the centre part of **Image.SQUARE_SMALL** and repositioning it in new images along the top of the image.
| The original image and the 3 new images are shown.

.. code-block:: python

    from microbit import *
    

    def crop_to(source_img, x, y, w, h, i, j):
        res = Image(5, 5)
        res.blit(source_img, x, y, w, h, i, j)
        return res


    img = Image.SQUARE_SMALL
    img_00 = crop_to(img, 1, 1, 3, 3, 0, 0)    
    img_10 = crop_to(img, 1, 1, 3, 3, 1, 0)
    img_20 = crop_to(img, 1, 1, 3, 3, 2, 0)

    while True:
        display.show(img)
        sleep(500)
        display.show(img_00)
        sleep(500)
        display.show(img_10)
        sleep(500)
        display.show(img_20)
        sleep(500)

----

.. admonition:: Tasks

    #.  Rewrite the code above to achieve the same result, but by using a for-loop, **for x in [0, 1, 2]**, to create the 3 cropped images above and display them.
    #.  Modify the code further to use nested for-loops by adding **for y in [0, 1, 2]** to display the cropped image in 9 positions.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Rewrite the code above to achieve the same result, but by using a for-loop, **for x in [0, 1, 2]**, to create the 3 cropped images above and display them.

                .. code-block:: python

                    from microbit import *


                    def crop_to(source_img, x, y, w, h, i, j):
                        res = Image(5, 5)
                        res.blit(source_img, x, y, w, h, i, j)
                        return res


                    img = Image.SQUARE_SMALL

                    while True:
                        display.show(img)
                        sleep(500)
                        for x in [0, 1, 2]:
                            img_x = crop_to(img, 1, 1, 3, 3, x, 0)
                            display.show(img_x)
                            sleep(200)

            .. tab-item:: Q2

                Modify the code further to use nested for-loops by adding **for y in [0, 1, 2]** to display the cropped image in 9 positions.

                .. code-block:: python

                    from microbit import *


                    def crop_to(source_img, x, y, w, h, i, j):
                        res = Image(5, 5)
                        res.blit(source_img, x, y, w, h, i, j)
                        return res


                    img = Image.SQUARE_SMALL

                    while True:
                        display.show(img)
                        sleep(500)
                        for y in [0, 1, 2]:
                            for x in [0, 1, 2]:
                                img_xy = crop_to(img, 1, 1, 3, 3, x, y)
                                display.show(img_xy)
                                sleep(200)

----

Repositioning a 3by3 image via accelerometer
------------------------------------------------------

| An 3 by 3 image can be moved around on screen using tilting.
| The 3 by 3 image can be the central part of a 5 by 5 image.
| The definition, **place_3by3**, takes a source image, uses its central 9 pixels and repositions them at position x, y in the returned image.
| The definition, **get_3by3_pos**, takes a starting position, x, y, and adjusts the the x, y values using the accelerometer. The x and y values are restricted to 0 to 2 so that a 3by3 image can always be seen fully on the display.

.. code-block:: python

    from microbit import *
        
    def place_3by3(source_img, x, y):
        res = Image(5, 5)
        res.blit(source_img, 1, 1, 3, 3, x, y)
        return res


    def get_3by3_pos(x, y):
        dx = accelerometer.get_x()
        dy = accelerometer.get_y()
        sensitivity = 200
        if dx > sensitivity:
            x += 1
        if dx < -sensitivity:
            x -= 1
        if dy > sensitivity:
            y += 1
        if dy < -sensitivity:
            y -= 1
        # keep on grid
        x = max(0, min(x, 2))
        y = max(0, min(y, 2))
        return x, y

----

.. admonition:: Tasks

    #.  Complete the code required to move a number 5 dice around the screen using the functions above.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Complete the code required to move a number 5 dice around the screen using the functions above.

                .. code-block:: python

                    from microbit import *


                    def place_3by3(source_img, x, y):
                        res = Image(5, 5)
                        res.blit(source_img, 1, 1, 3, 3, x, y)
                        return res


                    def get_3by3_pos(x, y):
                        dx = accelerometer.get_x()
                        dy = accelerometer.get_y()
                        sensitivity = 200
                        if dx > sensitivity:
                            x += 1
                        if dx < -sensitivity:
                            x -= 1
                        if dy > sensitivity:
                            y += 1
                        if dy < -sensitivity:
                            y -= 1
                        # keep on grid
                        x = max(0, min(x, 2))
                        y = max(0, min(y, 2))
                        return x, y


                    img1 = Image("00000:09090:00900:09090:00000")
                    x, y = 2, 2

                    while True:
                        x, y = get_3by3_pos(x, y)
                        img = place_3by3(img1, x, y)
                        display.show(img)
                        sleep(200)


----

Filling images and repositioning with blit
------------------------------------------------------

| A rectangle image can be filled and positioned in an another image with blit.

| The code below fills a rectangle of width, w, and height, h, and given brightness, and places it at pixel x, y in the a new blank 5 by 5 image which is then returned.

.. code-block:: python

    from microbit import *
        
    def blit_fill_rect(w, h, brightness, x, y):
        src = Image(w, h)
        src.fill(brightness)
        res = Image(5, 5)
        res.blit(src, 0, 0, 5, 5, x, y)
        return res

| The code below gives an example of creating rectangles that overlap.

.. code-block:: python

    from microbit import *


    def blit_fill_rect(w, h, brightness, x, y):
        src = Image(w, h)
        src.fill(brightness)
        res = Image(5, 5)
        res.blit(src, 0, 0, 5, 5, x, y)
        return res


    rect1 = blit_fill_rect(3, 4, 5, 0, 0)
    rect2 = blit_fill_rect(4, 3, 4, 1, 2)
    rects = rect1 + rect2

    display.show(rects)

----

.. admonition:: Tasks

    #.  Write code to place 4, 2 by 2 squares, of brightness 5, in each corner.
    #.  Write code to place 4, 2 by 2 squares, of brightness 5, in each corner using nested for-loops for the x and y values, adding them to the display with a 500ms delay.
    #.  Write a function, **rect_overlaps(count=2)**, to return a composite image of a given number of rectangles (default 2) of random size and position, of brightness 9. Restrict the width and height to 2 to 4. Restrict the top left to (0,0) to (3,3). Display a new composite image every 200ms.
    

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to place 4, 2 by 2 squares, of brightness 5, in each corner. 

                .. code-block:: python

                    from microbit import *


                    def blit_fill_rect(w, h, brightness, x, y):
                        src = Image(w, h)
                        src.fill(brightness)
                        res = Image(5, 5)
                        res.blit(src, 0, 0, 5, 5, x, y)
                        return res


                    rect1 = blit_fill_rect(2, 2, 5, 0, 0)
                    rect2 = blit_fill_rect(2, 2, 5, 3, 0)
                    rect3 = blit_fill_rect(2, 2, 5, 0, 3)
                    rect4 = blit_fill_rect(2, 2, 5, 3, 3)
                    rects = rect1 + rect2 + rect3 + rect4

                    display.show(my_image_overlap)

            .. tab-item:: Q2

                Write code to place 4, 2 by 2 squares, of brightness 5, in each corner. 

                .. code-block:: python

                    from microbit import *


                    def blit_fill_rect(w, h, brightness, x, y):
                        src = Image(w, h)
                        src.fill(brightness)
                        res = Image(5, 5)
                        res.blit(src, 0, 0, 5, 5, x, y)
                        return res


                    my_image_overlap = Image()
                    for x in [0, 3]:
                        for y in [0, 3]:
                            rect = blit_fill_rect(2, 2, 5, x, y)
                            my_image_overlap = my_image_overlap + rect
                            display.show(my_image_overlap)
                            sleep(500)

            .. tab-item:: Q3

                Write a function, **rect_overlaps(count=2)**, to return a composite image of a given number of rectangles (default 2) of random size and position, of brightness 9. Restrict the width and height to 2 to 4. Restrict the top left to (0,0) to (3,3). Display a new composite image every 200ms.

                .. code-block:: python

                    from microbit import *
                    import random


                    def blit_fill_rect(w, h, brightness, x, y):
                        src = Image(w, h)
                        src.fill(brightness)
                        res = Image(5, 5)
                        res.blit(src, 0, 0, 5, 5, x, y)
                        return res


                    def rect_overlaps(count=2):
                        rect_overlap = Image()
                        for _ in range(3):
                            w = random.randint(2, 4)
                            h = random.randint(2, 4)
                            brightness = 9  # random.randint(3, 6)
                            x = random.randint(0, 3)
                            y = random.randint(0, 3)
                            rect = blit_fill_rect(w, h, brightness, x, y)
                            rect_overlap = rect_overlap + rect
                        return rect_overlap


                    while True:
                        display.show(rect_overlaps(count=2))
                        sleep(200)

