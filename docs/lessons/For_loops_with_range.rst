====================================================
For loops using the range function
====================================================

See: https://www.w3schools.com/python/python_for_loops.asp

| To loop through a set of code a specified number of times, use the range() function.
| The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

Range function starting at 0
----------------------------------------

.. py:function:: range(stopvalue)

    Returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends before the ``stopvalue`` number. 

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

    #. Write a for loop that displays the numbers from 0 to 5. 
    #. Write a for loop that displays the numbers from 0 up to but not including 10. 

----

Range function with start and stop values
--------------------------------------------

.. py:function:: range(startvalue, stopvalue)

    Returns a sequence of numbers, starting from the ``startvalue`` number, and increments by 1 (by default), and ends before the ``stopvalue`` number. 

| range(2, 6) returns the numbers 2,3,4,5. It starts at 1. It goes up by 1. It stops before 6, at 5.

| The code below will display the numbers from 1 to 4.

.. code-block:: python

    from microbit import *


    while True:
        for n in range(1, 5):
            display.scroll(n, delay=80)
        sleep(500)

----

.. admonition:: Tasks

    #. Write a for loop that displays the numbers from 0 to 5. 
    #. Write a for loop that displays the numbers from 0 up to but not including 10. 

----

Range function with a step size
--------------------------------------------

.. py:function:: range(startvalue, stopvalue, stepsize)

    Returns a sequence of numbers, starting from the ``startvalue`` number, and increments by ``stepsize``, and ends before the ``stopvalue`` number. 

| range(1, 6, 2) returns the numbers 1,3,5. It starts at 1. It goes up by 2. It stops before 6, at 5.

| The code below will display the numbers 1, 3, 5, 7, 9.

.. code-block:: python

    from microbit import *


    while True:
        for n in range(1, 10, 2):
            display.scroll(n, delay=50)
        sleep(500)

----

.. admonition:: Tasks

    #. Write a for loop that displays the numbers from 0 to 5. 
    #. Write a for loop that displays the numbers from 0 up to but not including 10. 

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

    #. Write a for loop that counts up from 0 to 5.    
    #. Write a for loop that counts up from 0 to 9 in steps of 3.
    #. Write a for loop that counts down from 9 to 0.    
    #. Write a for loop that counts up from 9 to 0 in steps of 3. 



