====================================================
Moving images
====================================================

Shift left and right
--------------------------------

| An image can be shifted left or right.

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

Other methods
---------------------

| Try out the other methods.

.. py:method:: width()

    Return the number of columns in the image.

.. py:method:: height()

    Return the numbers of rows in the image.

.. py:method:: crop(x, y, w, h)

    Return a new image by cropping the picture to a width of ``w`` and a height of ``h``, starting with the pixel at column ``x`` and row ``y``.

.. py:method:: copy()

    Return an exact copy of the image.

.. py:method:: invert()

    Return a new image by inverting the brightness of the pixels in the
    source image.

.. py:method:: fill(value)

    Set the brightness of all the pixels in the image to the
    ``value``, which has to be between 0 (dark) and 9 (bright).

    This method will raise an exception when called on any of the built-in
    read-only images, like ``Image.HEART``.

.. py:method:: blit(src, x, y, w, h, xdest=0, ydest=0)

    Copy the rectangle defined by ``x``, ``y``, ``w``, ``h`` from the image ``src`` into
    this image at ``xdest``, ``ydest``.
    Areas in the source rectangle, but outside the source image are treated as having a value of 0.

    ``shift_left()``, ``shift_right()``, ``shift_up()``, ``shift_down()`` and ``crop()``
    can are all implemented by using ``blit()``.
    For example, img.crop(x, y, w, h) can be implemented as::

        def crop(self, x, y, w, h):
            res = Image(w, h)
            res.blit(self, x, y, w, h)
            return res
