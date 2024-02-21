====================================================
Practice tasks 1 Answers
====================================================

.. admonition:: Tasks

    1.  Write code to repetitively display 'WINNER' one character at a time, with 200ms between characters, and with a gap of a second before repeating.
    2.  Write code to repetitively scroll 'microbit' with a delay of 60ms, and with a gap of half a second before repeating.
    3.  Write code to repetitively display a heart and a giraffe with a gap of 250 millisec between them.
    4.  Write code to repetitively display 3 different shapes using a **list**, using default timing.
    5.  Write code to repetitively scroll (rapidly) the numbers from the **list** 2, 3, 5, 7, 11, 13, 17, 19 via a **for-loop**.
    6.  Write code to repetitively scroll the numbers 1 to 9 using a **for-loop** along with the **range** function.
    7.  Write code to repetitively scroll (quickly) each character in 'go team' using a **for-loop**, when the **A-button** is pressed.
    8.  Write code to repetitively scroll (rapidly) each sport in the list ``['swimming', 'rowing', 'canoeing']`` using a **for-loop**, when the **B-button** is pressed.
    9.  Write code in a ``while True`` loop to respond to button pressing such that when A is pressed each character in 'go team' is scrolled quickly using a **for-loop**, when B is pressed each sport in the **list** ``['swimming', 'rowing', 'canoeing']`` is scrolled quickly using a **for-loop**, and when no button is pressed the screen is **cleared**.
    10.  Write code in a ``while True`` loop to respond to button pressing such that when A is pressed the numbers 1,3,5,7,9 are scrolled quickly using the **range** function, when B is pressed the numbers 8,6,4,2,0 are scrolled quickly using the **range** function, and when no button is pressed the screen is **cleared**.
    11.  Write code to scroll **99 100 101 0 1 2** in three different ways: using a string, using a list and using 2 range functions. Use a 1 second gap between each way.




1.  Write code to repetitively display 'WinWINNERner' one character at a time, with 200ms between characters, and with a gap of a second before repeating.
2.  
.. code-block:: python

    from microbit import *

    while True:
        display.show('Winner', delay=200)
        sleep(1000)


----

2.  Write code to repetitively scroll 'microbit' with a delay of 60ms, and with a gap of half a second before repeating.

.. code-block:: python

    from microbit import *

    while True:
        display.scroll('microbit', delay=60)
        sleep(500)

----

3.  Write code to repetitively display a heart and a giraffe with a gap of 250 millisec between them.

.. code-block:: python

    from microbit import *

    while True:
        display.show(Image.HEART)
        sleep(250)
        display.show(Image.GIRAFFE)
        sleep(250)

----

4.  Write code to repetitively display 3 different shapes using a list, using default timing.

.. code-block:: python

    from microbit import *

    while True:
        display.show([Image.SQUARE, Image.DIAMOND, Image.TRIANGLE])

----

5.  Write code to repetitively scroll (rapidly) the numbers from the list 2, 3, 5, 7, 11, 13, 17, 19 via a for-loop.

.. code-block:: python

    from microbit import *

    num_list = [2, 3, 5, 7, 11, 13, 17, 19]
    while True:
        for num in num_list:
            display.scroll(num, delay=60)

----

6.  Write code to repetitively scroll the numbers 1 to 9 using a for-loop along with the range function.

.. code-block:: python

    from microbit import *

    while True:
        for num in range(1, 10):
            display.scroll(num, delay=50)

----

7.  Write code to repetitively scroll (quickly) each character in 'go team' using a for-loop, when the A-button is pressed.

.. code-block:: python

    from microbit import *

    string = 'go team'
    while True:
        if button_a.is_pressed():
            for char in string:
                display.scroll(char, delay=80)


----

8.  Write code to repetitively scroll (rapidly) each sport in the list ``['swimming', 'rowing', 'canoeing']`` using a for-loop, when the B-button is pressed.

.. code-block:: python

    from microbit import *

    sports_list = ['swimming', 'rowing', 'canoeing']
    while True:
        if button_b.is_pressed():
            for sport in sports_list:
                display.scroll(sport, delay=60)


----

9.  Write code in a ``while True`` loop to respond to button pressing such that when A is pressed each character in 'go team' is scrolled quickly using a for-loop, when B is pressed each sport in the list ``['swimming', 'rowing', 'canoeing']`` is scrolled rapidly using a for-loop, and when no button is pressed the screen is cleared.
    

.. code-block:: python

    from microbit import *

    string = 'go team'
    sports_list = ['swimming', 'rowing', 'canoeing']
    while True:
        if button_a.is_pressed():
            for char in string:
                display.scroll(char, delay=80)
        elif button_b.is_pressed():
            for sport in sports_list:
                display.scroll(sport, delay=60)
        else:
            display.clear()


----


10.  Write code in a ``while True`` loop to respond to button pressing such that when A is pressed the numbers 1,3,5,7,9 are scrolled quickly using the range function, when B is pressed the numbers 8,6,4,2,0 are scrolled quickly using the range function, and when no button is pressed the screen is cleared.
    

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            for num in range(1, 10, 2):
                display.scroll(num, delay=80)
        elif button_b.is_pressed():
            for num in range(8, -1, -2):
                display.scroll(num, delay=80)
        else:
            display.clear()

----

11.  Write code to scroll **99 100 101 0 1 2** in three different ways: using a string, using a list and using 2 range functions. Use a 1 second gap between each way.


.. code-block:: python

    from microbit import *

    num_string = "98 99 100 0 1 2"
    nums = [98, 99, 100, 0, 1, 2]

    while True:
        # using string
        display.scroll(num_string, delay=60)
        sleep(1000)
        # using a list
        for num in nums:
            display.scroll(num, delay=60)
        sleep(1000)
        # using range
        for num in range(98, 101):
            display.scroll(num, delay=60)
        for num in range(0, 3):
            display.scroll(num, delay=60)
        sleep(1000)

