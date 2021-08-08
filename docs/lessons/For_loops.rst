====================================================
For loops
====================================================

For loops with strings
----------------------------------------

| Python can loop through each character in a string and do something with it.
| ``for letter in welcome_string`` takes each character in the string ``welcome_string`` and puts it in the variable ``letter``.

.. code-block:: python

    from microbit import *


    welcome_string = 'Hi Mb user'
    while True:
        for letter in welcome_string:
            display.show(letter)
            sleep(300)
----

.. admonition:: Tasks

    #. Write a for loop to show each letter in 'winner'.    
    #. Write a for loop to show each character in '2021'.    

----

For loops with lists
----------------------------------------

| Python can loop through each element in a list and do something with it.
| In the code below, each element in the list is displayed.

.. code-block:: python

    from microbit import *


    tennis_champs = ['Novak', 'Roger', 'Rafael']
    while True:
        for tennis_star in tennis_champs:
            display.scroll(tennis_star, delay=80)
            sleep(300)


| In the code below, each number in the list is displayed.

.. code-block:: python

    from microbit import *


    primes = [2, 3, 5, 7]
    while True:
        for num in primes:
            display.show(num)
            sleep(300)


----

.. admonition:: Tasks

    #. Write a for loop to scroll each name in the list ``['Ariarne', 'Cate', 'Emma', 'Kaylee']``.
    #. Write a for loop to show each number in the list ``[1, 1, 2, 3, 5, 8]``.

----

Nested For loops
----------------------------------------

| A loop with another loop within is called a nested loop.
| ``for col in my_col`` takes each element in the list ``my_col`` and puts it in the variable ``col`` for use in the loop.
| ``for row in my_row`` takes each element in the list ``my_row`` and puts it in the variable ``row`` for use in the loop.
| Each time the outer loop, ``for col in my_col``, is run, the inner loop, ``for row in my_row``, completes all 4 loops since there are 4 elements in its list.
| The nested loops run a total of 3 * 4 or 12 times.
| The ``+`` in ``col + row`` does a text join. When ``col`` = "A" and ``row`` = '1', ``col + row`` will result in ``"A1"``.

.. code-block:: python

    from microbit import *


    while True:
        my_col = ["A", "B", "C"]
        my_row  = ['1', '2', '3', '4']

        for col in my_col:
            for row in my_row:
                display.scroll(col + row, delay=200)


----

| The nested loops below perform multiplication tables for 7 and 9.

.. code-block:: python

    from microbit import *


    while True:
        nums_1 = [7, 9]
        nums_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        for num_1 in nums_1:
            for num_2 in nums_2:
                display.scroll(num_1 * num_2, delay=100)



----

.. admonition:: Tasks

    #. Write a for loop that shows the result from multiplying each number in the list, ``[3, 5, 7]`` by 5.    
    #. Write a for loop that finds the sum of two numbers from the two lists: ``[2, 4, 6]`` and ``[3, 5,7]``.

