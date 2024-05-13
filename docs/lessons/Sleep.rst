====================================================
Sleep
====================================================


| The microbit can be paused using ``sleep``.

.. py:function:: sleep(n)

    | Wait for n milliseconds. 
    | n can be an integer or a decimal (floating point number). 
    | 1000 milliseconds is one second.

| ``sleep(1000)`` will pause the program for one second. 

.. code-block:: python

    from microbit import *

    sleep(1000)

| Sleeps are often used after displaying text and images to have a pause before other actions.
| A 1000ms sleep has been placed after each scrolled text below.

.. code-block:: python

    from microbit import *

    while True:
        display.scroll('I like', delay=60)
        sleep(1000)
        display.scroll('school', delay=120)
        sleep(1000)
      
----

.. admonition:: Questions

    Use the example code above for the questions below.

    #. Make the first sleep half a second.
    #. Make the second sleep a quarter of a second.
    #. Make the first sleep 2 seconds and the second sleep 200ms.
    
    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Make the first sleep half a second.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll('I like', delay=60)
                        sleep(500)
                        display.scroll('school', delay=120)
                        sleep(1000)


            .. tab-item:: Q2

                Make the second sleep a quarter of a second.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll('I like', delay=60)
                        sleep(1000)
                        display.scroll('school', delay=120)
                        sleep(250)

            .. tab-item:: Q3

                Make the first sleep 2 seconds and the second sleep 200ms.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll('I like', delay=60)
                        sleep(2000)
                        display.scroll('school', delay=120)
                        sleep(200)
