====================================================
Practice tasks 2 Answers
====================================================

.. admonition:: Tasks

    1.  Write code to repetitively scroll (quickly) each character in 'go team' using a for-loop, when the A-button is pressed.
    2.  Write code to repetitively scroll (quickly) each sport in the list ``['swimming', 'rowing', 'canoeing']`` using a for-loop, when the B-button is pressed.
    3.  Write code in a ``while True`` loop to respond to button pressing such that when A is pressed each character in 'go team' is scrolled quickly using a for-loop, when B is pressed each sport in the list ``['swimming', 'rowing', 'canoeing']`` is scrolled quickly using a for-loop, and when no button is pressed the screen is cleared.
    4.  Write code in a ``while True`` loop to respond to button pressing such that when A is pressed the numbers 0, 1, 2 are scrolled quickly using the range function, when B is pressed the numbers 0, 1, 2, 3, 4 are scrolled quickly using the range function, and when no button is pressed the screen is cleared.


1.  Write code to repetitively scroll (quickly) each character in 'go team' using a for-loop, when the A-button is pressed.

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            for char in 'go team':
                display.scroll(char, delay=80)


----

2.  Write code to repetitively scroll (quickly) each sport in the list ``['swimming', 'rowing', 'canoeing']`` using a for-loop, when the B-button is pressed.

.. code-block:: python

    from microbit import *

    while True:
        if button_b.is_pressed():
            for sport in ['swimming', 'rowing', 'canoeing']:
                display.scroll(sport, delay=80)


----

3.  Write code in a ``while True`` loop to respond to button pressing such that when A is pressed each character in 'go team' is scrolled quickly using a for-loop, when B is pressed each sport in the list ``['swimming', 'rowing', 'canoeing']`` is scrolled quickly using a for-loop, and when no button is pressed the screen is cleared.


.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            for char in 'go team':
                display.scroll(char, delay=80)
        elif button_b.is_pressed():
            for sport in ['swimming', 'rowing', 'canoeing']:
                display.scroll(sport, delay=80)
        else:
            display.clear()


----

4.  Write code in a ``while True`` loop to respond to button pressing such that when A is pressed the numbers 0, 1, 2 are scrolled quickly using the range function, when B is pressed the numbers 0, 1, 2, 3, 4 are scrolled quickly using the range function, and when no button is pressed the screen is cleared.


.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            for num in range(3):
                display.scroll(num, delay=80)
        elif button_b.is_pressed():
            for num in range(5):
                display.scroll(num, delay=80)
        else:
            display.clear()


