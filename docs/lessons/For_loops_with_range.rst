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

    #. Using the range function, write a for-loop that displays the numbers from 0 to 3.
    #. Using the range function, write a for-loop that displays the numbers from 0 up to but not including 5.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Using the range function, write a for-loop that displays the numbers from 0 to 3.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(4):
                            display.scroll(n, delay=80)
                        sleep(500)

            .. tab-item:: Q2

                Using the range function, write a for-loop that displays the numbers from 0 up to but not including 5.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(5):
                            display.scroll(n, delay=80)
                        sleep(500)

----

Adding to the range function variable
-----------------------------------------------------------------

| The code below uses the range function to get the numbers from 0 to 2 then adds 1 to each and scrolls 1 to 3.

.. code-block:: python

    from microbit import *

    while True:
        for n in range(3):
            display.scroll(n + 1, delay=80)
        sleep(500)


.. admonition:: Tasks

    #. Using the range function, write a for-loop that displays the numbers from 1 to 5.
    #. Using the range function, write a for-loop that displays the numbers from 2 to 5.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Using the range function, write a for-loop that displays the numbers from 1 to 5.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(5):
                            display.scroll(n + 1, delay=80)
                        sleep(500)

            .. tab-item:: Q2

                Using the range function, write a for-loop that displays the numbers from 2 to 5.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(4):
                            display.scroll(n + 2, delay=80)
                        sleep(500)

----

Subtracting from the range function variable
-----------------------------------------------------------------

| The code below uses the range function to get the numbers from 0 to 3 then subtracts 1 from each and scrolls -1 to 2.

.. code-block:: python

    from microbit import *

    while True:
        for n in range(4):
            display.scroll(n - 1, delay=80)
        sleep(500)


.. admonition:: Tasks

    #. Using the range function, write a for-loop that displays the numbers from -1 to 1.
    #. Using the range function, write a for-loop that displays the numbers from -2 to 2.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Using the range function, write a for-loop that displays the numbers from -1 to 1.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(3):
                            display.scroll(n - 1, delay=80)
                        sleep(500)

            .. tab-item:: Q2

                Using the range function, write a for-loop that displays the numbers from -2 to 2.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(5):
                            display.scroll(n - 2, delay=80)
                        sleep(500)

----

Multiplying the range function variable
-----------------------------------------------------------------

| The code below uses the range function to get the numbers from 0 to 2 then doubles each and scrolls 0 to 4.

.. code-block:: python

    from microbit import *

    while True:
        for n in range(3):
            display.scroll(n * 2, delay=80)
        sleep(500)


.. admonition:: Tasks

    #. Using the range function, write a for-loop that displays the numbers 0, 3, 6, 9.
    #. Using the range function, write a for-loop that displays the numbers 0, -1, -2, -3.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                 Using the range function, write a for-loop that displays the numbers 0, 3, 6, 9.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(4):
                            display.scroll(n * 3, delay=80)
                        sleep(500)

            .. tab-item:: Q2

                Using the range function, write a for-loop that displays the numbers 0, -1, -2, -3.

                .. code-block:: python

                    from microbit import *

                    while True:
                        for n in range(4):
                            display.scroll(n * -1*, delay=80)
                        sleep(500)

