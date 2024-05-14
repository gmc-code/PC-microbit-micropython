====================================================
EXT: nested for-loops using the range function
====================================================

Set pixels
----------------

| Turning on and off pixels is explained at https://pc-microbit-micropython.readthedocs.io/en/latest/images/setting_pixels.html
| Read the above examples before reading further to see how they illustrate nested loops. 

----

Using pixels in nested for-loops
-----------------------------------

| In the code below, the outer loop iterates over x values from 0 to 4.
| For each x value, the inner loop iterates over y values from 0 to 4.
| So when x is 0, y goes from 0 to 4, turning on each pixel in the first column.
| This repeats for the other columns.

.. code-block:: python

    from microbit import *

    for x in range(5):
        for y in range(5):
            display.set_pixel(x, y, 9)
            sleep(100)

----


.. admonition:: Tasks

    #. Write code that turns on the pixels one row at a time from the top.
    #. Write code that turns on the pixels one row at a time from the bottom.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code that turns on the pixels one row at a time from the top.

                .. code-block:: python

                    from microbit import *

                    for y in range(5):
                        for x in range(5):
                            display.set_pixel(x, y, 9)
                            sleep(100)

            .. tab-item:: Q2

                Write code that turns on the pixels one row at a time from the bottom.

                .. code-block:: python

                    from microbit import *

                    for y in range(4,-1,-1):
                        for x in range(5):
                            display.set_pixel(x, y, 9)
                            sleep(100)

----

Advanced: nested for-loops with range function
-------------------------------------------------

| What does this code do?
| What are the values of start_num in the nested loop?

.. code-block:: python
    
    from microbit import *

    while True:
        for start_num in range(4):
            for n in range(start_num, start_num + 5, 2):
                display.scroll(n, delay=40)

