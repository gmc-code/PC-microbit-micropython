====================================================
Practice tasks 2 Answers
====================================================

.. admonition:: Tasks

    1.  Write code to repetitively scroll the numbers 1 to 9 using a while loop.
    2.  Write code to repetitively scroll the numbers 5 to 0 using a while loop.




1.  Write code to repetitively scroll the numbers 1 to 9 using a while loop.

.. code-block:: python

    from microbit import *

    while True:
        num = 1
        while num < 10:
            display.scroll(num, delay=50)
            num += 1

----

2.  Write code to repetitively scroll the numbers 5 to 0 using a while loop.

.. code-block:: python

    from microbit import *

    while True:
        num = 5
        while num > -1
            display.scroll(num, delay=50)
            num -= 1
