====================================================
Practice tasks Answers
====================================================

.. admonition:: Tasks

    1.	Write code to repetitively display "Hello" one character at a time.
    2.	Write code to repetitively scroll "microbit".
    3.	Write code to repetitively display a heart and a giraffe.
    4.	Write code to repetitively display 3 different shapes using a list.
    5.	Write code to repetitively scroll the numbers 1 to 9 using a while loop.
    6.	Write code to repetitively scroll the numbers 5 to 0 using a while loop.
    7.	Write code to repetitively scroll the numbers from the list 2, 3, 5, 7, 11, 13, 17, 19 via a for loop.
    8.	Write code to repetitively scroll the numbers 1 to 9 using a for loop using the range function.



1.	Write code to repetitively display "Hello" one character at a time.

.. code-block:: python

    from microbit import *


    while True:
        display.show("Hello")

----

2.	Write code to repetitively scroll "microbit".

.. code-block:: python

    from microbit import *


    while True:
        display.scroll("microbit ")

----

3.	Write code to repetitively display a heart and a giraffe.

.. code-block:: python

    from microbit import *


    while True:
        display.show(Image.HEART)
        sleep(50)
        display.show(Image.GIRAFFE)
        sleep(50)

----

4.	Write code to repetitively display 3 different shapes using a list.

.. code-block:: python

    from microbit import *


    while True:
        display.show([Image.SQUARE, Image.DIAMOND, Image.TRIANGLE])

----

5.	Write code to repetitively scroll the numbers 1 to 9 using a while loop.

.. code-block:: python

    from microbit import *


    while True:
        i = 1
        while I < 10:
            display.scroll(i, delay=50)
            i += 1

----

6.	Write code to repetitively scroll the numbers 5 to 0 using a while loop.

.. code-block:: python

    from microbit import *


    while True:
        i = 5
        while I > -1
            display.scroll(i, delay=50)
            i -= 1

----

7.	Write code to repetitively scroll the numbers from the list 2, 3, 5, 7, 11, 13, 17, 19 via a for loop.

.. code-block:: python

    from microbit import *


    n = [2, 3, 5, 7, 11, 13, 17, 19]
    while True:
        for x in n:
            display.scroll(x, delay=50)

----

8.	Write code to repetitively scroll the numbers 1 to 9 using a for loop using the range function.

.. code-block:: python

    from microbit import *


    while True:
        for x in range(1,10):
            display.scroll(x, delay=50)



