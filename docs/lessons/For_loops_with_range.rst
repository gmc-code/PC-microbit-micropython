====================================================
For loops using the range function
====================================================

See: https://www.w3schools.com/python/python_for_loops.asp

| To loop through a set of code a specified number of times, use the range() function.
| The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

----

Range function starting at 0
----------------------------------------

.. py:function:: range(stop_value)

    Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends before the ``stop_value`` number. 

| range(3) returns the numbers 0, 1, 2. It starts at 0. It goes up by 1. It stops before 3, at 2.

| The code below will display the numbers from 0 to 2.

.. code-block:: python

    from microbit import *

    while True:
        for n in range(3):
            display.scroll(n, delay=80)
        sleep(500)

----

.. admonition:: Tasks

    #. Using the range function, write a for-loop that displays the numbers from 0 to 5. 
    #. Using the range function, write a for-loop that displays the numbers from 0 up to but not including 10.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Using the range function, write a for-loop that displays the numbers from 0 to 5.

                    .. code-block:: python

                        from microbit import *

                        while True:
                            for n in range(6):
                                display.scroll(n, delay=80)
                            sleep(500)

                .. tab-item:: Q2

                    Using the range function, write a for-loop that displays the numbers from 0 up to but not including 10.

                    .. code-block:: python

                        from microbit import *

                        while True:
                            for n in range(10):
                                display.scroll(n, delay=80)
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

----

Advanced: nested for loops with range function
-------------------------------------------------

| What does this code do?

.. code-block:: python
    
    from microbit import *

    while True:
        for start_num in range(4):
            for n in range(start_num, start_num + 5, 2):
                display.scroll(n, delay=40)




