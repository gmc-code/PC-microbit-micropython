====================================================
Show text
====================================================

.. py:module:: display

Display.show simple version
----------------------------------------

.. py:function:: show(value)

    | Display letters/digits of a string, float or integer, in sequence.
    | Each letter, digit is shown with 400 milliseconds between them.


To show the string, "Hi", one character at a time on the display, use:

.. code-block:: python

    from microbit import *


    display.show('Hi')


To show the integer, 16, one digit at a time on the display, use:

.. code-block:: python

    from microbit import *


    display.show(16)


To show the float, 3.14, one digit at a time on the display, use:

.. code-block:: python

    from microbit import *


    display.show(3.14)

----

.. admonition:: Tasks

    #. Write code to show your house color.    
    #. Write code to show your height in cm.
    #. Write code to show the chances of getting a 6 on a die throw.

----

Display.clear
----------------------------------------

.. py:function:: clear()

    | Clear the display.


| After ``display.show`` is used, the last digit or character will be left displayed.
| Use ``display.clear()`` to remove the last digit or character from the display.

.. code-block:: python

    from microbit import *


    display.show(3.14)
    display.clear()

----

Display.show with delay
----------------------------------------

.. py:function:: show(value, delay=400)

    | Display letters/digits of a string, float or integer, in sequence.
    | Each letter, digit is shown with ``delay`` milliseconds between them.
    | The delay can be specified with the parameter name as in ``display.show('Hi', delay=400)``, or just as a number as in ``display.show('Hi', 400)``.

To show the string, "Hi", with a short delay of 200ms:

.. code-block:: python

    from microbit import *


    display.show('Hi', 200)
    display.clear()

To show the float, 3.14159, across the display slowly use a long delay of about 300:

.. code-block:: python

    from microbit import *


    display.show(3.14159, delay=300)
    display.clear()

----

.. admonition:: Tasks

    #. Write code, using a delay, to show info about the number of children in your family.    
    #. Write code, using a delay, to show a countdown from 5 to 0.

----

Sleep
----------------------------------------
.. py:function:: sleep(n)

    | Wait for n milliseconds. One second is 1000 milliseconds.
    | ``n`` can be an integer or a floating point number.

| ``sleep(1000)`` will pause the microbit for one second. 
| ``sleep(500)`` will pause the microbit for half a second. 
| ``sleep(100)`` will pause the microbit for 0.1 sec. 

----

while True loops
----------------------------------------

| Microbit code can be repeated using a ``while True:`` loop.
| This continues forever.
| The code to be repeated has to be indented with a tab character.
| Python uses indenting to group the lines of code together in a ``while`` loop.

.. code-block:: python

    from microbit import *


    while True:
        display.show('I like the ', delay=60)
        display.show('NBA', delay=120)
        display.clear()
        sleep(500)

----

.. admonition:: Tasks

    1. Modify the code below to display your favourite activity.

    .. code-block:: python

        from microbit import *


        while True:
            display.show('I like to', delay=60)
            display.show('ride my bike', delay=120)
            display.clear()
            sleep(500)

    1. Modify the code below to display your name and age in years.

    .. code-block:: python

        from microbit import *


        while True:
            display.show('My name is', 60)
            display.show('?????', 120)
            display.show('I am', 60)
            display.show('??', 120)
            display.clear()
            sleep(500)

----

Display.show using variables
----------------------------------------

| In the code below, 3 variables are used to hold a string, integer and float.
| These variables are then showed repetedly in the ``while True:`` loop.
| This makes it easy to see and edit the values of the variables being used in the code.

.. code-block:: python

    from microbit import *


    player = 'Dunstall'
    goals = 1254
    goals_per_game = 4.66

    while True:
        display.show('Player', 200)
        display.show(player, 400)
        display.show('Goals', 200)
        display.show(goals, 400)
        display.show('Goals per game', 200)
        display.show(goals_per_game, 800)
        display.clear()
        sleep(500)

----

.. admonition:: Tasks

    1. Modify the value of the variables below to display info for another great goal kicker.

        .. code-block:: python

            from microbit import *


            player = '????????'
            goals = ????
            goals_per_game = ?.??

            while True:
                display.show('Player=', 50)
                display.show(player, 100)
                display.show('Goals=', 50)
                display.show(goals, 150)
                display.show('Goals per game=', 50)
                display.show(goals_per_game, 300)
                display.clear()
                sleep(500)

    2. Modify the code below to display info for another bowler.

        .. code-block:: python

            from microbit import *


            bowler = 'Sobers'
            wickets = 235
            ave = 34.0

            while True:
                display.show('Bowler=', 50)
                display.show(bowler, 100)
                display.show('Wickets=', 50)
                display.show(wickets, 150)
                display.show('Ave=', 50)
                display.show(ave, 300)
                display.clear()
                sleep(500)

----

Display.show full syntax
----------------------------------------

.. py:function:: show(value, delay=400, \*, wait=True, loop=False, clear=False)

    Display letters/digits of a string, float,  in sequence.
    Each letter, digit or image is shown with ``delay`` milliseconds between them.

    The use of ``\*,`` in the syntax is to indicate that for those parameters after it, ``wait``, ``loop`` and ``clear``, the arguments must be specified using their keyword.

    If ``wait`` is ``True``, this function will block until the animation is
    finished, otherwise the animation will happen in the background.

    If ``loop`` is ``True``, the animation will repeat forever.

    If ``clear`` is ``True``, the display will be cleared after it has finished.

    Note that the ``wait``, ``loop`` and ``clear`` arguments must be specified
    using their keyword.


