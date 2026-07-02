====================================================
EXT: For loops using the range function
====================================================


Looping Through a List of Values using element index from range function
------------------------------------------------------------------------------

.. py:function:: for i in range(len(value_list))

    Iterates through all elements in ``value_list``, using `i` as the index.

| e.g. ``value_list = ["D", "O", "G"]`` stores predefined values.
| e.g. ``for i in range(len(value_list))`` loops over the list using index positions.

| The code below will display each number in `value_list`, scrolling them one by one.

.. code-block:: python

    from microbit import *

    value_list = ["D", "O", "G"]

    while True:
        for i in range(len(value_list)):
            display.scroll(i, delay=50)
            display.scroll(value_list[i], delay=80)
        sleep(500)

| The code below moves left to right on the display and turns on a pixel using the y values.

.. code-block:: python

    from microbit import *

    y_list = [1, 4, 2, 3, 0]  # max of 5 values, with each from 0 to 4

    while True:
        for x in range(len(y_list)):
            y = y_list[x]
            display.clear()  # Clear previous pixel
            display.set_pixel(x, y, 9)  # Set pixel brightness to max
            sleep(500)

----

.. admonition:: Tasks

    #. Modify the "DOG" example above to work for "STAR".
    #. Modify the pixel example to work for [2, 3, 2].

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the "DOG" example above to work for "STAR".

                .. code-block:: python

                    from microbit import *

                    value_list = ["S", "T", "A", "R"]

                    while True:
                        for i in range(len(value_list)):
                            display.scroll(i, delay=50)
                            display.scroll(value_list[i], delay=80)
                        sleep(500)

            .. tab-item:: Q2

                Modify the pixel example to work for [2, 3, 2, 1].

                .. code-block:: python

                    from microbit import *

                    y_list = [2, 3, 2, 1]  # max of 5 values, with each from 0 to 4

                    while True:
                        for x in range(len(y_list)):
                            y = y_list[x]
                            display.clear()  # Clear previous pixel
                            display.set_pixel(x, y, 9)  # Set pixel brightness to max
                            sleep(500)

----

Range function with start and stop values
--------------------------------------------

.. py:function:: range(start_value, stop_value)

    Returns a sequence of numbers, starting at the ``start_value`` number, and increments by 1 (by default), and ends before the ``stop_value`` number.

| range(2, 6) returns the numbers 2, 3, 4, 5. It starts at 2. It goes up by 1. It stops before 6, at 5.
| range(2, 6) can be read as 'range of 2 up to but not including 6'.

| The code below will display the numbers 2, 3, 4, 5.

.. code-block:: python

    from microbit import *

    while True:
        for n in range(2, 6):
            display.scroll(n, delay=80)
        sleep(500)

----

.. admonition:: Tasks

    #. Using the range function, write a for-loop that displays the numbers 3, 4, 5, 6, 7.
    #. Using the range function, write a for-loop that displays the numbers from 4 up to but not including 9.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Using the range function, write a for-loop that displays the numbers 3, 4, 5, 6, 7.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(3, 8):
                            display.scroll(n, delay=80)
                        sleep(500)

            .. tab-item:: Q2

                Using the range function, write a for-loop that displays the numbers from 4 up to but not including 9.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(4, 9):
                            display.scroll(n, delay=80)
                        sleep(500)

----

Range function with a step size
--------------------------------------------

.. py:function:: range(start_value, stop_value, step_size)

    Returns a sequence of numbers, starting at the ``start_value`` number, incremented by ``step_size``, and ending before the ``stop_value`` number.

| range(1, 6, 2) returns the numbers 1, 3, 5. It starts at 1. It goes up by 2. It stops before 6, at 5.
| range(1, 6, 2) can be read as 'range of 1 up to but not including 6 in steps of 2'.

| The code below will display the numbers 1, 3, 5.

.. code-block:: python

    from microbit import *

    while True:
        for n in range(1, 6, 2):
            display.scroll(n, delay=50)
        sleep(500)

----

.. admonition:: Tasks

    #. Using the range function, write a for-loop that displays the numbers 2, 4, 6, 8.
    #. Using the range function, write a for-loop that displays the numbers 3, 7, 11, 15.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Using the range function, write a for-loop that displays the numbers 2, 4, 6, 8.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(2, 9, 2):
                            display.scroll(n, delay=50)
                        sleep(500)

            .. tab-item:: Q2

                Using the range function, write a for-loop that displays the numbers 3, 7, 11, 15.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(3, 16, 4):
                            display.scroll(n, delay=50)
                        sleep(500)

----

Using range to count down with a negative step size
----------------------------------------------------


| range(10, 0, -1) counts down from 10 to 1.

.. code-block:: python

    from microbit import *

    while True:
        for n in range(10, 0, -1):
            display.scroll(n, delay=80)
        sleep(500)


----

.. admonition:: Tasks

    #. Using the range function, write a for-loop that displays the numbers 9, 7, 5, 3.
    #. Using the range function, write a for-loop that displays the numbers 8, 5, 2.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Using the range function, write a for-loop that displays the numbers 9, 7, 5, 3.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(9, 2, -2):
                            display.scroll(n, delay=80)
                        sleep(500)

            .. tab-item:: Q2

                Using the range function, write a for-loop that displays the numbers 8, 5, 2.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(8, 1, -3):
                            display.scroll(n, delay=80)
                        sleep(500)





