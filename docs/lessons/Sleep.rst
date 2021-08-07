====================================================
Sleep
====================================================

.. py:module:: microbit


.. py:function:: show(value)

| The microbit can be paused using ``sleep``.

.. py:function:: sleep(n)

    Wait for n milliseconds. n can be an integer or a floating point number. One second is 1000 milliseconds.

| ``sleep(1000)`` will pause the execution for one second. 

.. code-block:: python

    from microbit import *


    sleep(1000)


----

.. admonition:: Questions

    #. Write a sleep for half a second.
    #. Write a sleep for two seconds. 
    #. Write a sleep for a tenth of a second. 
