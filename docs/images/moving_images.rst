====================================================
Moving images
====================================================

.. py:class:: Image

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

----

Shifting combined
--------------------------------

| An image can be shifted up or down and left or right to create movement patterns.

| The custom syntax below combines shifting in the x and y directions:

.. function:: shift_x_y(img, x, y, sleeptime=80)

    | **img** can be a built in such as **Image.HEART** or a custom image such as **Image("90909:" * 5)** or **Image(5, 5, bytearray([9] * 25))**.
    | x is an integer
    | **sleeptime** defaults to 80 ms. It is the sleep time after showing the shifted image.

| The code below shifts a butterfly image clockwise in 4 moves. 


.. code-block:: python

    from microbit import *

    def shift_x_y(img, x, y, sleeptime=80):
        shift_img = img.shift_right(x)
        shift_img = shift_img.shift_down(y)
        display.show(shift_img)
        sleep(sleeptime)
            

    img = Image.BUTTERFLY
    sleeptime = 200
    while True:
        display.show(img)
        sleep(sleeptime)
        shift_x_y(img, 1, 0, sleeptime)
        shift_x_y(img, 1, 1, sleeptime)
        shift_x_y(img, 0, 1, sleeptime)

----

.. admonition:: Tasks

    #.  Alter the arguments to move the butterfly anticlockwise.
    #.  Create a definition, **shift_img_directions(img, directions, sleeptime=80)**,  that takes a list of tuples, **directions**,  for the shifts and applies them to move the butterfly anticlockwise.
    #.  Use the definition, **shift_img_directions(img, directions, sleeptime=80)**, to move the butterfly clockwise.
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

                        def shift_x_y(img, x, y, sleeptime=80):
                            shift_img = img.shift_right(x)
                            shift_img = shift_img.shift_down(y)
                            display.show(shift_img)
                            sleep(sleeptime)
                                

                        img = Image.BUTTERFLY   
                        sleeptime = 200
                        while True:
                            display.show(img)
                            sleep(sleeptime)
                            shift_x_y(img, 0, 1, sleeptime)
                            shift_x_y(img, 1, 1, sleeptime)
                            shift_x_y(img, 1, 0, sleeptime)

                .. tab-item:: Q2

                    Create a definition, **shift_img_directions(img, directions, sleeptime=80)**,  that takes a list of tuples, **directions**,  for the shifts and applies them to move the butterfly anticlockwise.

                    .. code-block:: python

                        from microbit import *

                        def shift_x_y(img, x, y, sleeptime=80):
                            shift_img = img.shift_right(x)
                            shift_img = shift_img.shift_down(y)
                            display.show(shift_img)
                            sleep(sleeptime)
                                
                            
                        def shift_img_directions(img, directions, sleeptime=80):
                            for x,y in directions:
                                shift_x_y(img, x, y, sleeptime)


                        img = Image.BUTTERFLY
                        sleeptime = 200
                        while True:
                            anticlockwise_directions =  [(0, 0), (0, 1), (1, 1), (1, 0)]
                            shift_img_directions(img, anticlockwise_directions, sleeptime)

                .. tab-item:: Q3

                    Use the definition, **shift_img_directions(img, directions, sleeptime=80)**, to move the butterfly clockwise.

                    .. code-block:: python

                        from microbit import *

                        def shift_x_y(img, x, y, sleeptime=80):
                            shift_img = img.shift_right(x)
                            shift_img = shift_img.shift_down(y)
                            display.show(shift_img)
                            sleep(sleeptime)
                                
                            
                        def shift_img_directions(img, directions, sleeptime=80):
                            for x,y in directions:
                                shift_x_y(img, x, y, sleeptime)


                        img = Image.BUTTERFLY
                        sleeptime = 200
                        while True:
                            clockwise_directions =  [(0, 0), (1, 0), (1, 1), (0, 1) ]
                            shift_img_directions(img, clockwise_directions, sleeptime)

                .. tab-item:: Q4

                    Predict what the following directions might do: **directions =  [(0, 0), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, 0)]**

                    They move the image clockwise in a 2 by 2 square rnaging from (-1, -1) to (1, 1).
                    
----

Cropping images
--------------------------------

| An image can be cropped.

.. py:method:: crop(x, y, w, h)

    | Return a new image by cropping the picture from x, y with width w, height h.
    | The new image is positioned at 0, 0 in the top left.

.. code-block:: python

    from microbit import *

    display.show(Image('00300:'
                    '03630:'
                    '36963:'
                    '03630:'
                    '00300'))


----

Other methods
---------------------

| Try out the other methods.

.. py:method:: width()

    Return the number of columns in the image.

.. py:method:: height()

    Return the numbers of rows in the image.


.. py:method:: copy()

    Return an exact copy of the image.


.. py:method:: blit(src, x, y, w, h, xdest=0, ydest=0)

    Copy the rectangle defined by **x**, **y**, **w**, **h** from the image **src** into
    this image at **xdest**, **ydest**.
    Areas in the source rectangle, but outside the source image are treated as having a value of 0.

    **shift_left()**, **shift_right()**, **shift_up()**, **shift_down()** and **crop()**
    can are all implemented by using **blit()**.
    For example, img.crop(x, y, w, h) can be implemented as::

        def crop(self, x, y, w, h):
            res = Image(w, h)
            res.blit(self, x, y, w, h)
            return res



