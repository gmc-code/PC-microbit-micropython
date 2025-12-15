====================================================
For loops
====================================================

For loops with strings
----------------------------------------

.. py:function:: for char in str:

    | the string is looped through with each character in the string, ``str``, being placed in the ``char`` variable for use in the for loop block code.


| The code below loops through each character in a string and does something with it.
| ``for welcome_character in welcome_string`` takes each character in the string ``welcome_string`` and puts it in the variable ``welcome_character``.
| ``display.scroll(welcome_character)`` then scrolls the character.

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
    spacing_character = "_"
    while True:
        for welcome_character in welcome_string:
            display.scroll(welcome_character)
            display.scroll(spacing_character)
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
                    spacing_character = "*"
                    while True:
                        for character in string:
                            display.scroll(character)
                            display.scroll(spacing_character)
                        sleep(300)

            .. tab-item:: Q2

                Write a for-loop to scroll each digit in '8850' individually with a '-' between them.

                .. code-block:: python

                    from microbit import *

                    string = '2023'
                    spacing_character = "-"
                    while True:
                        for character in string:
                            display.scroll(character)
                            display.scroll(spacing_character)
                        sleep(300)

| The disadvantage of this approach is that the spacing character is also added to the end, after the last character.
| e.g "a*c*e*"
| See the `Spacing characters under EXT: for-loops <https://pc-microbit-micropython.readthedocs.io/en/latest/lessons/For_loops_2.html>`_#spacing-characters>`_ for ideas to get "a*c*e" instead of "a*c*e*".

----

For loops with lists
----------------------------------------

.. py:function:: for item in lst:

    | The list is looped through with each element in the list, ``lst``, being placed in the ``item`` variable for use in the for loop block code.


| Python can loop through each element in a list and do something with it.
| In the code below, each element in the list is displayed.
| The sleep is placed after the for-loop to create a short delay before looping through the list again.

.. code-block:: python

    from microbit import *

    wise_men = ['Melchior', 'Caspar', 'Balthazar']
    while True:
        for wise_man in wise_men:
            display.scroll(wise_man, delay=80)
        sleep(300)


| In the code below, each number in the list is displayed via a for-loop.
| The sleep is placed within the for-loop to create a short delay before the next number is shown.

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

    #. Write a for-loop that scrolls all the letter pairings from the 2 lists: ["A", "B", "C"] and ["X", "Y", "Z"] taking one letter from each with the first letter always beng form the first list given.
    #. Write a nested for-loop that tuns on and off pixels at points (x,y) using the lists:   ``x_positions = [0, 1, 2, 3, 4]`` and ``y_positions = [4, 3, 2, 1, 0]``. Use ``display.set_pixel(x, y, 9)`` to turn on the pixel and ``display.set_pixel(x, y, 0)`` to turn it off after a short sleep.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop that scrolls all the letter pairings from the 2 lists: ["A", "B", "C"] and ["X", "Y", "Z"] taking one letter from each with the first letter always beng form the first list given.

                .. code-block:: python

                    from microbit import *

                    letters_1 = ["A", "B", "C"]
                    letters_2 = ["X", "Y", "Z"]

                    while True:
                        for letter1 in letters_1:
                            for letter2 in letters_2:
                                display.scroll(letter1 + letter2, delay=100)

            .. tab-item:: Q2

                Write a nested for-loop that tuns on and off pixels at points (x,y) using the lists:   ``x_positions = [0, 1, 2, 3, 4]`` and ``y_positions = [4, 3, 2, 1, 0]``. Use ``display.set_pixel(x, y, 9)`` to turn on the pixel and ``display.set_pixel(x, y, 0)`` to turn it off after a short sleep.

                .. code-block:: python

                    from microbit import *

                    x_positions = [0, 1, 2, 3, 4]
                    y_positions = [4, 3, 2, 1, 0]

                    while True:
                        for x in x_positions:
                            for y in y_positions:
                                display.set_pixel(x, y, 9)
                                sleep(200)
                                display.set_pixel(x, y, 0)



| For examples of using nested for-loops specific to the microbit display see the `Setting Pixels page under Images <https://pc-microbit-micropython.readthedocs.io/en/latest/images/setting_pixels.html>`_#pixel-rows-and-columns-lists>`_.

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


EXT: storing values in a list
---------------------------------

|

.. admonition:: Exercises

    #. Here is some fun code that displays a heart image as a series of 3 pixels. Change it form 3 to 5 pixels.
    #. Here is some fun code that displays a heart image as a series of shown pixels. Change the pop parameter to pop the last item via -1 to clear the image in reverse.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Here is some fun code that displays a heart image as a series of 3 pixels. Change it form 3 to 5 pixels.

                .. code-block:: python

                    from microbit import *

                    heart = [
                        [0, 1, 1, 1, 0],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [0, 1, 1, 1, 0],
                        [0, 0, 1, 0, 0]
                    ]

                    lit_pixels = []  # Keep track of three active pixels

                    while True:
                        for y in range(5):
                            for x in range(5):
                                if heart[y][x]:  # Only process active parts of the heart shape
                                    display.set_pixel(x, y, 9)
                                    lit_pixels.append((x, y))  # Store pixel coordinates

                                    # If more than 3 pixels are lit, remove the oldest one
                                    if len(lit_pixels) > 3:
                                        old_x, old_y = lit_pixels.pop(0)
                                        display.set_pixel(old_x, old_y, 0)

                                    sleep(100)

                        sleep(500)
                        display.clear()
                        sleep(500)

            .. tab-item:: Q2

                Here is some fun code that displays a heart image as a series of shown pixels. Change the pop parameter to pop the last item via -1 to clear the image in reverse.

                .. code-block:: python

                    from microbit import *

                    heart = [
                        [0, 1, 1, 1, 0],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [0, 1, 1, 1, 0],
                        [0, 0, 1, 0, 0]
                    ]

                    lit_pixels = []  # Keep track of active pixels

                    while True:
                        # Light up pixels one by one
                        for y in range(5):
                            for x in range(5):
                                if heart[y][x]:  # Only process active parts of the heart shape
                                    display.set_pixel(x, y, 9)
                                    lit_pixels.append((x, y))  # Store pixel coordinates
                                    sleep(100)

                        # Fade out pixels one by one instead of clearing all at once
                        while lit_pixels:
                            old_x, old_y = lit_pixels.pop(0)
                            display.set_pixel(old_x, old_y, 0)
                            sleep(100)

                        sleep(500)

            .. tab-item:: Q3

                Here is some fun code that displays a heart image as a series of shown pixels, then clears it by choosing random pixels from the stored list of pixels. Modify it to dim the pixels instead of turning them off.

                .. code-block:: python

                    from microbit import *
                    import random  # Import random module

                    heart = [
                        [0, 1, 1, 1, 0],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [0, 1, 1, 1, 0],
                        [0, 0, 1, 0, 0]
                    ]

                    lit_pixels = []  # Keep track of active pixels

                    while True:
                        # Light up pixels one by one
                        for y in range(5):
                            for x in range(5):
                                if heart[y][x]:  # Only process active parts of the heart shape
                                    display.set_pixel(x, y, 9)
                                    lit_pixels.append((x, y))  # Store pixel coordinates
                                    sleep(100)

                        # Remove pixels randomly instead of sequentially
                        while lit_pixels:
                            random_index = random.randint(0, len(lit_pixels) - 1)  # Get a random pixel index
                            old_x, old_y = lit_pixels.pop(random_index)  # Remove a random pixel
                            display.set_pixel(old_x, old_y, 0)
                            sleep(50)

                        sleep(500)
