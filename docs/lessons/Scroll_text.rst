====================================================
Scroll text
====================================================

.. py:module:: display

Display.scroll simple version
----------------------------------------

.. py:function:: scroll(value)

    | Scrolls ``value`` horizontally on the microbit LED display.
    | ``value`` can be an integer or float (a decimal) or a string (text in quotes).

To scroll the string (in single quotes), '``Hi``', across the display, use ``display.scroll('Hi')``:

.. code-block:: python

    from microbit import *

    while True:
        display.scroll('Hi')


To scroll the string (in double quotes), "``Hello``", across the display, use ``display.scroll("Hello")``:

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Hello")


To scroll the integer, ``5``, across the display, use ``display.scroll(5)``:

.. code-block:: python

    from microbit import *

    while True:
        display.scroll(5)


To scroll the float, ``3.14``, across the display, use ``display.scroll(3.14)``:

.. code-block:: python

    from microbit import *

    while True:
        display.scroll(3.14)

------

.. admonition:: Tasks

    #. Write code to scroll your name.
    #. Write code to scroll your age.
    #. Write code to scroll the number of teams in the AFL.
    #. Write code to scroll the chances of getting a tail on a coin throw.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to scroll your name.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("Tim")

            .. tab-item:: Q2

                Write code to scroll your age.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll(12)


            .. tab-item:: Q3

                Write code to scroll the number of teams in the AFL.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll(18)


            .. tab-item:: Q4

                Write code to scroll the chances of getting a tail on a coin throw.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll(0.5)

----

Display.scroll with delay
----------------------------------------

.. py:function:: scroll(value, delay=150)

    | Scrolls ``value`` horizontally on the display.
    | ``value`` can be an integer or float (a decimal) or a string.
    | The ``delay`` parameter controls how fast the text scrolls.
    | The default delay is 150ms. When no delay is specified the default of 150ms is used.
    | The delay can be specified with the parameter name as in ``display.scroll('Hi', delay=150)``, or just as a number as the second argument as in ``display.scroll('Hi', 150)``.

To scroll the string, 'Hi', across the display rapidly, use a short delay of 50ms:

.. code-block:: python

    from microbit import *

    while True:
        display.scroll('Hi', 50)


To scroll the float, 3.14159, across the display slowly, use a long delay of 300ms:

.. code-block:: python

    from microbit import *

    while True:
        display.scroll(3.14159, delay=300)


To scroll a date as text, "Dec 25", across the display quickly, use a short delay of 100ms:

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Dec 25", delay=100)

----

.. admonition:: Tasks

    #. Write code, using a short delay, to scroll info about the number of people in your family.
    #. Write code, using a short delay, to scroll info about the number of rooms in your house.
    #. Write code, using a short delay, to scroll info about your birth year.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code, using a short delay, to scroll info about the number of people in your family.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("5 in family", delay=100)

            .. tab-item:: Q2

                Write code, using a short delay, to scroll info about the number of rooms in your house.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("12 rooms", delay=100)

            .. tab-item:: Q3

                Write code, using a short delay, to scroll info about your birth year.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll("Born 1987", delay=100)

----

scroll at different speeds
----------------------------------------

| The code below uses a shorter delay for the initial text then a longer delay for the main information.

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

    str_value = 'abc'
    while True:
        display.scroll(str_value)


.. code-block:: python

    from microbit import *

    int_value = 123
    while True:
        display.scroll(int_value)


.. code-block:: python

    from microbit import *

    float_value = 0.93
    while True:
        display.scroll(float_value)


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
        display.scroll(player, 80)
        display.scroll('Goals=', 50)
        display.scroll(goals, 150)
        display.scroll('Goals per game=', 50)
        display.scroll(goals_per_game, 300)


| For rules on variable names see:
| `<https://pc-microbit-micropython.readthedocs.io/en/latest/python_basics/variables.html>`

----

.. admonition:: Tasks

    1. Modify the value of the variables below to display info for another great goal kicker.

        .. code-block:: python

            from microbit import *

            player = 'Pele'
            goals = 775
            goals_per_game = 0.92

            while True:
                display.scroll('Player=', 50)
                display.scroll(player, 100)
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
                display.scroll(batsman, 100)
                display.scroll('Runs=', 50)
                display.scroll(runs, 150)
                display.scroll('Ave=', 50)
                display.scroll(ave, 300)

    3. Modify the code below to display info for another great NBA player.

        .. code-block:: python

            from microbit import *

            player = 'Kobe Bryant'
            points = 33643
            ave = 25.0

            while True:
                display.scroll('player=', 50)
                display.scroll(player, 100)
                display.scroll('Points=', 50)
                display.scroll(points, 150)
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

    The use of ``\*,`` in the syntax is to indicate that for those parameters after it, ``wait``, ``loop`` and ``monospace``, the arguments must be specified using their keyword. e.g ``wait=True`` is needed; not simply ``True``.

    If ``wait`` is ``True``, this function will block until the animation is
    finished, otherwise the animation will happen in the background.

    If ``loop`` is ``True``, the animation will repeat forever.

    If ``monospace`` is ``True``, the characters will all take up 5 pixel-columns
    in width, otherwise there will be exactly 1 blank pixel-column between each
    character as they scroll.

----

.. admonition:: Tasks

    1. Experiment with the ``scroll`` named parameters by trying them out with True or False to see what effect they have.

