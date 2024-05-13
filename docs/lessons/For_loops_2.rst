====================================================
EXT: for-loops
====================================================

Using if to test strings within for-loops
-----------------------------------------------

| What does this code do?
| ``name[0] in "AEIOU"`` returns True if the first character in the name string is in hte string of vowels.

| A string can be changed to upper case using ``.upper()``.
| e.g. ``anna.upper()`` returns "ANNA"

The code below scrolls the name in upper case only if the first letter is a vowel.

.. code-block:: python

    from microbit import *

    name = "Anna"
    while True:
        if name[0] in "AEIOU":
            display.scroll(name.upper(), delay=50)

----

.. admonition:: Tasks

    #. Write a for-loop to scroll names beginning with a vowel in ['Olivia', 'Emily', 'Chloe', 'Catherine', 'Anna', 'Gabriella', 'Hannah', 'Isabel', 'Julia']. Display the names in uppercase.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop to scroll names beginning with a vowel in ['Olivia', 'Emily', 'Chloe', 'Catherine', 'Anna', 'Gabriella', 'Hannah', 'Isabel', 'Julia']. Display the names in uppercase.

                .. code-block:: python

                    from microbit import *

                    name_list = ['Olivia', 'Emily', 'Chloe', 'Catherine', 'Anna', 'Gabriella', 'Hannah', 'Isabel', 'Julia']
                    while True:
                        for name in name_list:
                            if name[0] in "AEIOU":
                                display.scroll(name.upper(), delay=50)
                        sleep(300)


for-loops with mixed lists
----------------------------------------

| Mixed lists can be used with **display.show**.
| Strings, integers and floats, and Images can all be displayed with **display.show**.
| A short delay is used in **display.show** for when there are multiple characters in a string or number.
| A short sleep is used in the **for-loop** so that there is a noticeable gap between each list element no matter whether they are strings, numbers or images.
| A longer sleep is used after the **for-loop** before it repeats.

.. code-block:: python

    from microbit import *

    mixed_list = ['I', Image.HEART, 3.14]
    while True:
        for element in mixed_list:
            display.show(element, delay=200)
            sleep(700)
        sleep(1000)


----

.. admonition:: Tasks

    #. Create a mixed list to display the message to be asleep at 10 o'clock.
    #. Create a mixed list to display you're 3 favourite animals with their number order.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a mixed list to display the message to be asleep at 10 o'clock.

                .. code-block:: python

                    from microbit import *

                    mixed_list = [Image.ASLEEP, '@', Image.CLOCK10]
                    while True:
                        for element in mixed_list:
                            display.show(element, delay=200)
                            sleep(700)
                        sleep(1000)

            .. tab-item:: Q2

                Create a mixed list to display you're 3 favourite animals in number order.

                .. code-block:: python

                    from microbit import *

                    mixed_list = ["#1", Image.RABBIT, "#2", Image.DUCK, "#3", Image.TORTOISE]
                    while True:
                        for element in mixed_list:
                            display.show(element, delay=200)
                            sleep(700)
                        sleep(1000)

----

Nested for-loops
----------------------------------------

| A loop within another loop within is called a nested loop.
| The code below loops through each list and displays the result of joining each string.

.. code-block:: python

    from microbit import *

    col_letters = ['A', 'B', 'C']
    row_nums = ['1', '2', '3', '4']
    while True:
        for col in col_letters:
            for row in row_nums:
                display.scroll(col + row, delay=200)

| ``for col in col_letters`` takes each element in the list ``col_letters`` and puts it in the variable ``col`` for use in the loop.
| ``for row in row_nums`` takes each element in the list ``row_nums`` and puts it in the variable ``row`` for use in the loop.
| Each time the outer loop, ``for col in col_letters``, runs 3 times since there are 3 elements in ``['A', 'B', 'C']``.
| Each time the outer loop is run, the inner loop, ``for row in row_nums``, runs 4 times since there are 4 elements in ``['1', '2', '3', '4']``.
| The nested loops run a total of 3 * 4 or 12 times.
| The ``+`` in ``col + row`` does a text join. When ``col`` = 'A' and ``row`` = '1', ``col + row`` will result in ``'A1'``.

----

| The nested loops below perform multiplication tables for 7 and 9.
| The nested loops run a total of 2 * 9 or 18 times.

.. code-block:: python

    from microbit import *

    nums_1_list = [7, 9]
    nums_2_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        for num_1 in nums_1_list:
            for num_2 in nums_2_list:
                display.scroll(num_1 * num_2, delay=80)

----

.. admonition:: Tasks

    #. Write a nested for-loop that finds the sum of every different combination of one number from each of the two lists: ``[1, 2, 3]`` and ``[6, 5, 4]``.
    #. Write a nested for-loop that scrolls the 2 digit number formed from the joining of every different combination of one number from each of the two lists: ``[1, 2, 3]`` and ``[4, 5]``, keeping the digit from the first list first.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a nested for-loop that scrolls the sum of every different combination of one number from each of the two lists: ``[1, 2, 3]`` and ``[6, 5, 4]``.

                .. code-block:: python

                    from microbit import *

                    nums_1_list = [1, 2, 3]
                    nums_2_list = [6, 5, 4]
                    while True:
                        for num_1 in nums_1_list:
                            for num_2 in nums_2_list:
                                display.scroll(num_1 + num_2, delay=50)

            .. tab-item:: Q2

                Write a nested for-loop that scrolls the 2 digit number formed from the joining of every different combination of one number from each of the two lists: ``[1, 2, 3]`` and ``[4, 5]``, keeping the digit from the first list first.

                .. code-block:: python

                    from microbit import *

                    nums_1_list = [1, 2, 3]
                    nums_2_list = [4, 5]
                    while True:
                        for num_1 in nums_1_list:
                            for num_2 in nums_2_list:
                                display.scroll(str(num_1) + str(num_2), delay=50)


