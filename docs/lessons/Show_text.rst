====================================================
Show text
====================================================

.. py:module:: display

display.show simple version
----------------------------------------

.. py:function:: show(value)

    | Display letters/digits of a string, float or integer, in sequence.
    | Each letter, character or digit is shown with 400 milliseconds between them.


To show the string, '``Hi``', one character at a time on the display, use ``display.show('Hi')``:

.. code-block:: python

    from microbit import *

    while True:
        display.show('Hi')


To show the integer, ``16``, one digit at a time on the display, use ``display.show(16)``:

.. code-block:: python

    from microbit import *

    while True:
        display.show(16)


To show the float, ``3.14``, one digit at a time on the display, use ``display.show(3.14)``:

.. code-block:: python

    from microbit import *

    while True:
        display.show(3.14)

----

.. admonition:: Tasks

    #. Write code to show your school house color. 
    #. Write code to show your height in cm.
    #. Write code to show the chances of getting a 6 on a die throw.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to show your school house color.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("Hughes")

            .. tab-item:: Q2

                Write code to show your height in cm.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(182)

            .. tab-item:: Q3

                Write code to show the chances of getting a 6 on a die throw.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(0.16)

----

Display.clear
----------------------------------------

.. py:function:: clear()

    | Clear the display.


| After ``display.show`` is used, the last digit or character will be left displayed.
| Use ``display.clear()`` to remove the last digit or character from the display.
| Use a sleep after the clear so that the display remains blank for a short time.

.. code-block:: python

    from microbit import *

    while True:
        display.show(3.14)
        display.clear()
        sleep(2000)

----

.. admonition:: Tasks

    #. Write code to show 123, then clear the screen for 1 sec.
    #. Write code to show "ABC", then clear the screen for half a sec.


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to show 123, then clear the screen for 1 sec.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(123)
                        display.clear()
                        sleep(1000)

            .. tab-item:: Q2

                Write code to show "ABC", then clear the screen for half a sec.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("ABC")
                        display.clear()
                        sleep(500)
                        
----


display.show with clear
----------------------------------------

.. py:function:: show(value, clear=False)

    | Display letters/digits of a string, float, in sequence. 
    | If ``clear`` is ``True``, the display will be cleared after it has finished. Its default value is False, in which case, the last character is left displayed.


| After ``display.show`` is used, the last digit or character will be left displayed.
| Use ``clear=True`` to remove the last digit or character from the display.
| Use a sleep afterwards so that the display remains blank for a short time.
| e.g. ``display.show('Hi', clear=True)``

.. code-block:: python

    from microbit import *

    while True:
        display.show(3.14, clear=True)
        sleep(500)

----

.. admonition:: Tasks

    #. Write code to show 123, with the last character being removed, then sleep for 1 sec.
    #. Write code to show "ABC", with the last character being removed, then sleep for half a sec.


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to show 123, with the last character being removed, then sleep for 1 sec.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(123, clear=True)
                        sleep(1000)

            .. tab-item:: Q2

                Write code to show "ABC", with the last character being removed, then sleep for half a sec.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show("ABC", clear=True)
                        sleep(500)

----

display.show with delay
----------------------------------------

.. py:function:: show(value, delay=400)

    | Display letters, characters, and digits of a string, float or integer, in sequence.
    | Each letter, character or digit is shown with ``delay`` milliseconds between them.
    | The default delay is 400ms. When no delay is specified the default of 400ms is used.
    | The delay can be specified with the parameter name as in ``display.show('Hi', delay=400)``, or just as a number as in ``display.show('Hi', 400)``.

To show the string, '``Hi``', with a short delay of 200ms, use ``display.show('Hi', 200)``:

.. code-block:: python

    from microbit import *

    while True:
        display.show('Hi', 200)
        display.clear()
        sleep(2000)

To show the float, ``3.14159``, across the display slowly use a medium delay of 300ms via ``display.show(3.14159, delay=300)``:

.. code-block:: python

    from microbit import *

    while True:
        display.show(3.14159, delay=300)
        display.clear()
        sleep(2000)

----

.. admonition:: Tasks

    #. Write code, using a short delay of 200ms, to show 99.94, then clear the screen for 1 sec.
    #. Write code, using a short delay of 150ms, to show 5.64, then clear the screen for half a sec.


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code, using a short delay of 200ms, to show 99.94, then clear the screen for 1 sec.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(99.94, delay=200)
                        display.clear()
                        sleep(1000)

            .. tab-item:: Q2

                Write code, using a short delay of 150ms, to show 5.64, then clear the screen for half a sec.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.show(5.64, delay=150)
                        display.clear()
                        sleep(500)


----

Show at different speeds
----------------------------------------

| The code below uses a shorter delay for the initial text then a longer delay for the main information.

.. code-block:: python

    from microbit import *

    while True:
        display.show('I like the ', delay=200)
        display.show('NBA', delay=400)
        display.clear()
        sleep(2000)

----

.. admonition:: Tasks

    1. Modify the code below to display your favourite activity.

    .. code-block:: python

        from microbit import *

        while True:
            display.show('I like to', delay=200)
            display.show('ride my bike', delay=400)
            display.clear()
            sleep(2000)

    2. Modify the code below to display your name and age in years.

    .. code-block:: python

        from microbit import *

        while True:
            display.show('My name is', 200)
            display.show('?????', 400)
            display.show('I am', 200)
            display.show('??', 400)
            display.clear()
            sleep(2000)

----

display.show using variables
----------------------------------------

| In the code below, 3 variables are used to hold a string, integer and float.
| These variables are then showed repeatedly in the ``while True:`` loop.
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
        display.show(goals, 500)
        display.show('Goals per game', 200)
        display.show(goals_per_game, 600)
        display.clear()
        sleep(2000)

----

.. admonition:: Tasks

    1. Modify the value of the variables below to display info for another great goal kicker.

        .. code-block:: python

            from microbit import *

            player = 'Romario'
            goals = 780
            goals_per_game = 0.78

            while True:
                display.show('Player=', 200)
                display.show(player, 300)
                display.show('Goals=', 200)
                display.show(goals, 400)
                display.show('Goals per game=', 200)
                display.show(goals_per_game, 500)
                display.clear()
                sleep(2000)

    2. Modify the code below to display info for another great bowler.

        .. code-block:: python

            from microbit import *

            bowler = 'Muralitharan'
            wickets = 800
            ave = 22.7

            while True:
                display.show('Bowler=', 200)
                display.show(bowler, 300)
                display.show('Wickets=', 200)
                display.show(wickets, 400)
                display.show('Ave=', 200)
                display.show(ave, 500)
                display.clear()
                sleep(2000)

    3. Modify the code below to display info for another prolific NBA scorer.

        .. code-block:: python

            from microbit import *

            player = 'Kareem Abdul-Jabbar'
            points = 38387
            ave = 24.6

            while True:
                display.show('player=', 200)
                display.show(player, 300)
                display.show('Points=', 200)
                display.show(points, 400)
                display.show('Ave=', 200)
                display.show(ave, 500)

----

Show full syntax
----------------------------------------

.. py:function:: show(value, delay=400, \*, wait=True, loop=False, clear=False)

    | Display letters/digits of a string, float, in sequence. 
    | Each letter, digit or image is shown with ``delay`` milliseconds between them. 
    | The default delay is 400ms. When no delay is specified the default of 400ms is used.

    The use of ``\*,`` in the syntax is to indicate that for those parameters after it, ``wait``, ``loop`` and ``clear``, the arguments must be specified using their keyword.

    If ``wait`` is ``True``, this function will block until the animation is
    finished, otherwise the animation will happen in the background.

    If ``loop`` is ``True``, the animation will repeat forever.

    If ``clear`` is ``True``, the display will be cleared after it has finished.

----

.. admonition:: Tasks

    1. Experiment with the ``show`` named parameters by trying them out with True or False to see what effect they have.

----

.. admonition:: Tip

    | **display.show** has a ``wait`` parameter that can be set to ``False`` so that displaying information on the microbit display doesn't hold up other actions like driving motors on a bot. 
    | e.g. ``display.show(motor_speed, wait=False)``


