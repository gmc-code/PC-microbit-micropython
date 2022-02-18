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

    #. Make the first sleep half a second.
    #. Make the second sleep half a second.
    #. Make one sleep 2 seconds and one sleep 250ms.
