==========================
urandom
==========================

.. py:module:: urandom

| MicroPython contains an ``urandom`` module based upon the ``random`` module in the Python standard library.
| This module generates random numbers.

----

Functions for integers
----------------------

.. function:: urandom.randint(a, b)

    Return an integer in the range from a to b, including b.

| The code below scrolls a random number from 0 to 7, including 7.

.. code-block:: python

    from microbit import *
    import urandom

    while True:
        display.scroll(urandom.randint(0, 7), delay=80)
        sleep(200)

.. note::

   Be careful with **randint**, since it doesn't follow the usual rule in python where the stop value is not included. **(0, 7)** normally means from 0 up to **but not including** 7. Whereas, for **randint**, **(0, 7)** means from 0 up to **and including** 7.

----

.. function:: urandom.randrange(stop)
              randrange(start, stop)
              randrange(start, stop, step)

    The first form returns an integer from 0 up to but not including the stop integer.
    The second form returns an integer from the start integer up to but not including the stop integer.
    The third form returns an integer from the start integer up to but not including the stop integer, in steps of **step**.  For instance, calling ``randrange(1, 10, 2)`` will
    return odd numbers from 1 to 9.

----

.. function:: urandom.getrandbits(n)

    Return an integer with *n* urandom bits where n is from 0 to 32.
    When n = 1, values are 0 or 1.
    When n = 2, values are 0, 1, 2 or 3.
    When n = 3, values are from 0 to 7.
    The maximum value is found using (n**2 -1). eg. n**3 - 1 = 7
    This may be useful for specifying random numebrs based on powers of 2.

| The code below scrolls a random number from 0 to 7.

.. code-block:: python

    from microbit import *
    import urandom

    while True:
        display.scroll(urandom.getrandbits(3), delay=80)
        sleep(200)

----

Functions for floats
--------------------

.. function:: urandom.random()

    Return a random floating point number from 0.0 up to but not including 1.0 with 7 decimal places.

| The code below scrolls a random float from 0.0 up to but not including 1.0.

.. code-block:: python

    from microbit import *
    import urandom

    while True:
        display.scroll(urandom.random(), delay=80)
        sleep(200)

| The code below scrolls a random float from 0.0 up to but not including 1.0 rounded to 2 decimal places using the round function.

.. code-block:: python

    from microbit import *
    import urandom

    while True:
        display.scroll(round(urandom.random(), 2), delay=80)
        sleep(200)

----

.. function:: urandom.uniform(a, b)

    Return a random floating point number between a and b inclusive of both.
    b can be lower of higher than a. The order doesn't matter.
    urandom.uniform(1, 3) is the same as urandom.uniform(3, 1)

| The code below scrolls a random float from 0 to 3, then a float from 4 to 6.

.. code-block:: python

    from microbit import *
    import urandom

    while True:
        display.scroll(round(urandom.uniform(1, 3), 2), delay=80)
        sleep(200)
        display.scroll(round(urandom.uniform(6, 4), 2), delay=80)
        sleep(200)

.. note::

   Be careful with **uniform**, since it doesn't follow the usual rule in python where the stop value is not included. **(1, 3)** normally means from 1 up to **but not including** 3. Whereas, for **uniform**, **(1, 3)** means from 1 up to **and including** 3.

----

choice
---------------

.. function:: urandom.choice(sequence)

    Returns one item at random from a *sequence* (tuple, list or
    any object that supports the subscript operation).

| The code below makes random choices from a string, a tuple and a list.

.. code-block:: python

    from microbit import *
    import urandom

    str_val = "python"
    tuple_val = (1, 2, 3)
    list_val = ["red", "green", "yellow", "blue"]
    while True:
        display.scroll(urandom.choice(str_val), delay=80)
        sleep(200)
        display.scroll(urandom.choice(tuple_val), delay=80)
        sleep(200)
        display.scroll(urandom.choice(list_val), delay=80)
        sleep(200)

----

seed
---------------

.. function:: urandom.seed(n=None)

    Initialise the urandom number generator module with the seed *n* which should
    be an integer.  When no argument (or ``None``) is passed in, it will initialise the generator with a hardware generated random number.


.. code-block:: python

    from microbit import *
    import urandom

    urandom.seed()
