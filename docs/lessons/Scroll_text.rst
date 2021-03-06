====================================================
Scroll text
====================================================

.. py:module:: display

Display.scroll simple version
----------------------------------------

.. py:function:: scroll(value)

    | Scrolls ``value`` horizontally on the microbit LED display. 
    | ``value`` can be an integer or float (a decimal) or a string.

To scroll the string (in single quotes), 'Hi', across the display, use:

.. code-block:: python

    from microbit import *


    display.scroll('Hi')


Strings can be in double quotes like "Hello" :

.. code-block:: python

    from microbit import *


    display.scroll("Hello")


To scroll the integer, 5, across the display, use:

.. code-block:: python

    from microbit import *


    display.scroll(5)


To scroll the float, 3.14, across the display, use:

.. code-block:: python

    from microbit import *


    display.scroll(3.14)

------

.. admonition:: Tasks

    #. Write code to scroll your name.    
    #. Write code to scroll your age.
    #. Write code to scroll the chances of getting a tail on a coin throw.

----

Display.scroll with delay
----------------------------------------

.. py:function:: scroll(value, delay=150)

    | Scrolls ``value`` horizontally on the display. 
    | ``value`` can be an integer or float (a decimal) or a string.
    | The ``delay`` parameter controls how fast the text scrolls. 
    | The default delay is 150ms. When no delay is specified the default of 150ms is used.
    | The delay can be specified with the parameter name as in ``display.scroll('Hi', delay=150)``, or just as a number as the second argument as in ``display.scroll('Hi', 150)``.

To scroll the string, 'Hi', across the display quickly, use a short delay of about 50:

.. code-block:: python

    from microbit import *


    display.scroll('Hi', 50)

To scroll the float, 3.14159, across the display slowly, use a long delay of about 300:

.. code-block:: python

    from microbit import *


    display.scroll(3.14159, delay=300)

----

.. admonition:: Tasks

    #. Write code, using the delay parameter, to scroll info about the number of people in your family.    
    #. Write code, using the delay parameter, to scroll info about the number of rooms in your house.
    #. Write code, using the delay parameter, to scroll info about the your favourite phone app or electronic game.

----

while True loops
----------------------------------------

| Microbit code can be repeated using a ``while True:`` loop.
| This continues forever.
| The code to be repeated has to be indented with a tab character.
| Python uses indenting to group together the lines of code in a ``while`` loop.

.. code-block:: python

    from microbit import *


    while True:
        display.scroll('I like to watch', delay=60)
        display.scroll('AFL', delay=120)

----

.. admonition:: Tasks

    1. Modify the code below to display your favourite sport.

    .. code-block:: python

        from microbit import *


        while True:
            display.scroll('I like to play', delay=60)
            display.scroll('table tennis', delay=120)


    2. Modify the code below to display your name and age in years.

    .. code-block:: python

        from microbit import *


        while True:
            display.scroll('My name is', 60)
            display.scroll('?????', 120)
            display.scroll('I am', 60)
            display.scroll('??', 120)

----

Display.scroll using variables
----------------------------------------

| Instead of placing an integer, a float or a string directly in the brackets of ``display.scroll``, a variable can be used.
| This can make the code easier to read, since the variable value is separate from its use (here it is just being displayed).

.. code-block:: python

    from microbit import *


    strvalue = "abc"
    while True:
        display.scroll(strvalue)


.. code-block:: python

    from microbit import *


    intvalue = 123
    while True:
        display.scroll(intvalue)


.. code-block:: python

    from microbit import *


    floatvalue = 0.93
    while True:
        display.scroll(floatvalue)


| In the code below, 3 variables are used to hold a string, integer and float.
| These variables are then scrolled repeatedly in the ``while True:`` loop.
| This makes it easy to see and edit the values of the variables being used in the code.

.. code-block:: python

    from microbit import *


    player = 'Locket'
    goals = 1360
    goals_per_game = 4.84

    while True:
        display.scroll('Player=', 50)
        display.scroll(player, 50)
        display.scroll('Goals=', 50)
        display.scroll(goals, 150)
        display.scroll('Goals per game=', 50)
        display.scroll(goals_per_game, 300)


| For rules on variable names see: 
| https://pc-microbit-micropython.readthedocs.io/en/latest/python_basics/variables.html

----

.. admonition:: Tasks

    1. Modify the value of the variables below to display info for another great goal kicker.

        .. code-block:: python

            from microbit import *


            player = '????????'
            goals = ????
            goals_per_game = ?.??

            while True:
                display.scroll('Player=', 50)
                display.scroll(player, 50)
                display.scroll('Goals=', 50)
                display.scroll(goals, 150)
                display.scroll('Goals per game=', 50)
                display.scroll(goals_per_game, 300)

    2. Modify the code below to display info for a different batsman.

        .. code-block:: python

            from microbit import *


            batsman = 'Sobers'
            runs = 8032
            ave = 57.8

            while True:
                display.scroll('Batsman=', 50)
                display.scroll(batsman, 50)
                display.scroll('Runs=', 50)
                display.scroll(runs, 150)
                display.scroll('Ave=', 50)
                display.scroll(ave, 300)

----

Display.scroll full syntax
----------------------------------------

.. py:function:: scroll(value, delay=150, \*, wait=True, loop=False, monospace=False)

    | Scrolls ``value`` horizontally on the display.     
    | ``value`` can be an integer or float (a decimal) or a string.
    | The ``delay`` parameter controls how fast the text scrolls.
    | The default delay is 150ms. When no delay is specified the default of 150ms is used.

    The use of ``\*,`` in the syntax is to indicate that for those parameters after it, ``wait``, ``loop`` and ``monospace``, the arguments must be specified using their keyword.

    If ``wait`` is ``True``, this function will block until the animation is
    finished, otherwise the animation will happen in the background.

    If ``loop`` is ``True``, the animation will repeat forever.

    If ``monospace`` is ``True``, the characters will all take up 5 pixel-columns
    in width, otherwise there will be exactly 1 blank pixel-column between each
    character as they scroll.

----

.. admonition:: Tasks

    1. Experiment with the ``scroll`` named parameters by trying them out with True or False to see what effect they have.






