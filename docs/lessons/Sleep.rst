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

----

.. admonition:: Questions

    #. Write a sleep for half a second.
    #. Write a sleep for two seconds. 
    #. Write a sleep for a tenth of a second. 
