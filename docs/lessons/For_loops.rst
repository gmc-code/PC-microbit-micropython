====================================================
For loops
====================================================

For loops with strings
----------------------------------------

| ``for letter in my_string`` takes each character in the string ``my_string`` and puts it in the variable ``letter`` for display.

.. code-block:: python

    from microbit import *

    my_string = 'Hi Mb user'
    for letter in my_string:
        display.show(letter)
        sleep(200)

----

For loops with lists
----------------------------------------

| ``num in my_list`` takes each element in the list ``my_list`` and puts it in the variable ``num`` for use in the loop.

.. code-block:: python

    from microbit import *

    my_list = [2, 3, 5, 7]
    for num in my_list:
        display.show(num)
        sleep(300)
        num = num * 2
        display.scroll(num, delay = 50)

----

Nested For loops
----------------------------------------

| ``for col in my_col`` takes each element in the list ``my_col`` and puts it in the variable ``col`` for use in the loop.
| ``for row in my_row`` takes each element in the list ``my_row`` and puts it in the variable ``row`` for use in the loop.
| Each time the out loop, ``for col in my_col``, is run, the inner loop, ``for row in my_row``, completes all 4 loops since there are 4 elements in its list.
| The ested loops run a total of 3 * 4 or 12 times.

.. code-block:: python

    from microbit import *

    my_col = ["A", "B", "C"]
    my_row  = ['1', '2', '3', '4']

    for col in my_col:
        for row in my_row:
            display.scroll(col + row, delay=200)


----

| The nested loops below perform multiplication tables for 7 and 9.

.. code-block:: python

    from microbit import *

    nums_1 = [7, 9]
    nums_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for num_1 in nums_1:
        for num_2 in nums_2:
            display.scroll(num_1 * num_2, delay=100)


