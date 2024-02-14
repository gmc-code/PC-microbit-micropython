====================================================
for-loops
====================================================

for-loops with strings
----------------------------------------

| Python can loop through each character in a string and do something with it.
| ``for character in welcome_string`` takes each character in the string ``Hello`` and puts it in the variable ``character``.

.. code-block:: python

    from microbit import *

    welcome_string = 'Hello'
    while True:
        for character in welcome_string:
            display.scroll(character)
            sleep(300)

| Using a for-loop allows other actions on each character or between each character in the string.

| The code below scrolls each character in the string ``Hello`` and puts another character between them.

.. code-block:: python

    from microbit import *

    welcome_string = 'Hello'
    gap_character = "-"
    while True:
        for character in welcome_string:
            display.scroll(character)
            display.show(gap_character)
            sleep(300)

----

.. admonition:: Tasks

    #. Write a for-loop to scroll each letter in 'ace' individually and show a "-" between them.
    #. Write a for-loop to scroll each digit in '123' individually and show a "*" between them. 
    #. Write a for-loop to scroll each letter in the word 'Hello' and show a happy face image after each letter.   
    #. Write a for-loop to scroll each letter in 'christmas' and show a XMAS image after each letter.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop to scroll each letter in 'ace' individually and show a "-" between them.

                .. code-block:: python

                    from microbit import *

                    string = 'ace'
                    gap_character = "-"
                    while True:
                        for character in string:
                            display.scroll(character)
                            display.show(gap_character)
                            sleep(300)

            .. tab-item:: Q2

                Write a for-loop to scroll each digit in '123' individually and show a "*" between them.

                .. code-block:: python

                    from microbit import *

                    string = '123'
                    gap_character = "*"
                    while True:
                        for character in string:
                            display.scroll(character)
                            display.show(gap_character)
                            sleep(300)

            .. tab-item:: Q3

                Write a for-loop to scroll each letter in the word 'Hello' and show a happy face image after each letter.  

                .. code-block:: python

                    from microbit import *

                    # A string with the word "Hello"
                    word = "Hello"

                    # Loop through each letter in the word
                    for letter in word:
                        # Scroll the letter on the display quickly
                        display.scroll(letter, delay=50)
                        # Show the HAPPY image for 300 ms
                        display.show(Image.HAPPY)
                        sleep(300)

            .. tab-item:: Q4

                Write a for-loop to scroll each letter in 'christmas' individually and show a XMAS image between them.

                .. code-block:: python

                    from microbit import *

                    # A string with the word "Christmas"
                    word = "Christmas"

                    # Loop through each letter in the word
                    for letter in word:
                        # Scroll the letter on the display quickly
                        display.scroll(letter, delay=50)
                        # Show the XMAS image for 300 ms
                        display.show(Image.XMAS)
                        sleep(300)

----

for-loops with lists
----------------------------------------

| Python can loop through each element in a list and do something with it.
| In the code below, each element in the list is displayed.

.. code-block:: python

    from microbit import *

    tennis_champs = ['Novak', 'Rafael', 'Roger']
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

    #. Write a for-loop to scroll each car in the list ``['Lotus', 'Shelby', 'Porsche']``.
    #. Write a for-loop to scroll each number in the list ``[1, 2, 3, 5, 8]``.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop to scroll each car in the list ``['Lotus', 'Shelby', 'Porsche']``.

                .. code-block:: python

                    from microbit import *

                    cars_list = ['Lotus', 'Shelby', 'Porsche']
                    while True:
                        for car in cars_list:
                            display.scroll(car)
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

Conditions within for-loops with lists
-----------------------------------------------

| What does this code do?
| ``test_num % num`` gets the remainder from division.
| Which numbers in the list are factors of 42?

.. code-block:: python

    from microbit import *

    primes = [2, 3, 5, 7]
    test_num = 42
    while True:
        for num in primes:
            if test_num % num == 0:
                display.scroll(num, delay=50)
        sleep(300)

----

.. admonition:: Tasks

    #. Write a for-loop to scroll the prime factors of 63 from a list of the first 4 primes.
    #. Write a for-loop to scroll the even numbers in the list of squares ``[1, 4, 9, 16, 25, 36]``.
    
    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop to scroll the prime factors of 63 from a list of the first 4 primes.

                .. code-block:: python

                    from microbit import *

                    primes = [2, 3, 5, 7]
                    test_num = 63
                    while True:
                        for num in primes:
                            if test_num % num == 0:
                                display.scroll(num, delay=50)
                        sleep(300)

            .. tab-item:: Q2

                Write a for-loop to scroll the even numbers in the list of squares ``[1, 4, 9, 16, 25, 36]``.

                .. code-block:: python

                    from microbit import *

                    num_list = [1, 4, 9, 16, 25, 36]
                    while True:
                        for num in num_list:
                            if num % 2 == 0:
                                display.scroll(num, delay=50)
                        sleep(300)

