====================================================
For loops
====================================================

For loops with strings
----------------------------------------

| The code below loops through each character in a string and does something with it.
| ``for welcome_character in welcome_string`` takes each character in the string ``welcome_string`` and puts it in the variable ``welcome_character``.

.. code-block:: python

    from microbit import *

    welcome_string = 'Hello'
    while True:
        for welcome_character in welcome_string:
            display.scroll(welcome_character)
        sleep(300)
        
----

.. admonition:: Tasks

    #. Write a for-loop to scroll each letter in 'winner' individually.
    #. Write a for-loop to scroll each digit in '2023' individually.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop to scroll each letter in 'winner' individually.

                .. code-block:: python

                    from microbit import *

                    string = 'winner'
                    while True:
                        for character in string:
                            display.scroll(character)
                        sleep(300)

            .. tab-item:: Q2

                Write a for-loop to scroll each digit in '1966' individually.

                .. code-block:: python

                    from microbit import *

                    string = '1966'
                    while True:
                        for character in string:
                            display.scroll(character)
                        sleep(300)

----

Add actions to a for-loop
----------------------------------------

| Apart from simply scrolling the character in a string, as in the examples above, other actions can be added to the for-loop.
| The code below adds an underscore, '_', between each character.'

.. code-block:: python

    from microbit import *

    welcome_string = 'Hello'
    while True:
        for welcome_character in welcome_string:
            display.scroll(welcome_character)
            display.scroll('_')
        sleep(300)



.. admonition:: Tasks

    #. Write a for-loop to scroll each letter in 'ace' individually with an '*' between them.
    #. Write a for-loop to scroll each digit in '8850' individually with a '-' between them.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop to scroll each letter in 'ace' individually with an '*' between them.

                .. code-block:: python

                    from microbit import *

                    string = 'ace'
                    while True:
                        for character in string:
                            display.scroll(character)
                            display.scroll('*')
                        sleep(300)

            .. tab-item:: Q2

                Write a for-loop to scroll each digit in '8850' individually with a '-' between them.

                .. code-block:: python

                    from microbit import *

                    string = '2023'
                    while True:
                        for character in string:
                            display.scroll(character)
                            display.scroll('-')
                        sleep(300)

----

For loops with lists
----------------------------------------

| Python can loop through each element in a list and do something with it.
| In the code below, each element in the list is displayed.

.. code-block:: python

    from microbit import *

    wise_men = ['Melchior', 'Caspar', 'Balthazar']
    while True:
        for wise_man in wise_men:
            display.scroll(wise_man, delay=80)
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

    #. Write a for-loop to scroll each name in the list ``['Bugs', 'Daffy', 'Marvin']``.
    #. Write a for-loop to scroll each number in the list ``[1, 2, 3, 5, 8]``.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop to scroll each name in the list ``['Bugs', 'Daffy', 'Marvin']``.

                .. code-block:: python

                    from microbit import *

                    names_list = ['Bugs', 'Daffy', 'Marvin']
                    while True:
                        for name in names_list:
                            display.scroll(name)
                        sleep(300)

            .. tab-item:: Q2

                Write a for-loop to scroll each number in the list ``[1, 2, 3, 5, 8]``.

                .. code-block:: python

                    from microbit import *

                    num_list = [1, 2, 3, 5, 8]
                    while True:
                        for num in num_list:
                            display.scroll(num)
                        sleep(300)


----

Nested For loops
----------------------------------------

| A loop within another loop within is called a nested loop.
| The code below loops through each list and displays the result of joining each string.

.. code-block:: python

    from microbit import *

    col_letters = ['A', 'B', 'C']
    row_nums  = ['1', '2', '3', '4']
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

| The nested loops below perform multiplication tables for 5 and 6.
| The nested loops run a total of 2 * 9 or 18 times.

.. code-block:: python

    from microbit import *

    nums_1_list = [5, 6]
    nums_2_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    while True:
        for num_1 in nums_1_list:
            for num_2 in nums_2_list:
                display.scroll(num_1 * num_2, delay=80)

----

.. admonition:: Tasks

    #. Write a for-loop that shows the result from multiplying each number in the list, ``[3, 5, 7]`` by 5, using a variable for each part of the multiplication.
    #. Write a nested for-loop that finds the sum of every different combination of two numbers from the two lists: ``[2, 4, 6]`` and ``[3, 5, 7]``.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop that shows the result from **multiplying** each number in the list, ``[3, 5, 7]`` by 5, using a variable for each part of the multiplication.

                .. code-block:: python

                    from microbit import *

                    nums_1_list = [3, 5, 7]
                    num_2 = 5
                    while True:
                        for num_1 in nums_1_list:
                            display.scroll(num_1 * num_2, delay=80)

            .. tab-item:: Q2

                Write a nested for-loop that finds the **sum** of every different combination of two numbers from the two lists: ``[2, 4, 6]`` and ``[3, 5, 7]``.

                .. code-block:: python

                    from microbit import *

                    nums_1_list = [2, 4, 6]
                    nums_2_list = [3, 5, 7]
                    while True:
                        for num_1 in nums_1_list:
                            for num_2 in nums_2_list:
                                display.scroll(num_1 + num_2, delay=80)


----

For loops with mixed lists
----------------------------------------

| Mixed lists can be used with **display.show**.
| Strings, integers and floats, and Images can all be displayed with **display.show**.
| A short delay is used in **display.show** for when there are multiple characters in a string or number.
| A short sleep is used in the **for-loop** so that there is a noticeable gap between each list element no matter whether they are strings, numbers or images.
| A longer sleep is used after the **for-loop** before it repeats.

| What does this code mean?

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

                    mixed_list = ['#1', Image.RABBIT, '#2', Image.DUCK, '#3', Image.TORTOISE]
                    while True:
                        for element in mixed_list:
                            display.show(element, delay=200)
                            sleep(700)
                        sleep(1000)
                        