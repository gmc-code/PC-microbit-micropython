====================================================
While_loops
====================================================

| See: https://www.w3schools.com/python/python_while_loops.asp
| While loop run a set of statements as long as a condition is true.
| The statements within the loop are indented.

While true
----------------------------------------

| ``while True:`` loops run forever.

.. code-block:: python

    from microbit import *

    while True:
        display.scroll('I am a microbit', delay=80)

----

Counters
----------------------------------------

| While loops have a condition that is tested each time the loop runs.
| The condition must be True for the loop to run.
| If the condition is False, the loop is exited.
| A counter can be used in the while loop condition.
| The counter is set before the while loop.
| The counter is incremented in a while loop. 

----

Counting up
----------------------------------------

| In the example below, ``i`` is the counter.
| ``i`` starts off at 0 and is increased by 1 in the while loop line: ``i += 1``.
| The while runs while ``i`` increases from 0 to 9, but then exits when ``i`` is 10.

.. code-block:: python

    from microbit import *

    i = 0
    while i < 10:
        display.scroll(i, delay=50)
        i += 1

----

Counting down
----------------------------------------

| ``i`` starts off at 5 and is decreased by 1 in the while loop line: ``i -= 1``.
| The test uses a ``>`` sign when counting down.
| The loop below stops when is no longer greater than 1, i.e. when it is 1.

.. code-block:: python

    from microbit import *
    i = 5
    while i > 1:
        display.scroll(i, delay=50)
        i -= 1

----

Step size
----------------------------------------

| The code below counts up from 0 to 10 in steps of 2. 
| ``i += 2`` sets a step size of 2.

.. code-block:: python

    from microbit import *

    i = 0
    while i < 11:
        display.scroll(i, delay=50)
        i += 2

----

.. admonition:: Tasks

    #. Write a while loop that counts up from 0 to 5.    
    #. Write a while loop that counts up from 0 to 9 in steps of 3.
    #. Write a while loop that counts down from 9 to 0.    
    #. Write a while loop that counts up from 9 to 9 in steps of 3.

