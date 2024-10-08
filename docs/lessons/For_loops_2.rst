====================================================
EXT: for-loops
====================================================

Spacing characters
----------------------------

| The code below scrolls each character in "a*c*e", but does so by starting with 'ace' and "*" and uses them in a for-loop.
| It uses indexing to get each character in the string 'ace' which is stored in the variable card_name. e.g. card_name[0] gets 'a'.
| It uses an if statement to check whether the loop is up to the last character so that it only adds '*' if it is not the last character.

.. code-block:: python

    from microbit import *

    card_name = 'ace'
    string_length = len(card_name)
    spacing_character = "*"
    while True:
        for i in range(string_length):
            display.scroll(card_name[i])
            if i < string_length - 1:
                display.scroll(spacing_character)
        sleep(300)


.. admonition:: Tasks

    #. Write a for-loop to scroll each letter in 'bot' individually with a '|' between them.
    #. Write a for-loop to scroll each digit in '8850' individually with a '+' between them.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop to scroll each letter in 'bot' individually with an '|' between them.

                .. code-block:: python

                    from microbit import *

                    string = 'bot'
                    spacing_character = "|"
                    while True:
                        for character in string:
                            display.scroll(character)
                            display.scroll(spacing_character)
                        sleep(300)

            .. tab-item:: Q2

                Write a for-loop to scroll each digit in '8850' individually with a '+' between them.

                .. code-block:: python

                    from microbit import *

                    string = '2023'
                    spacing_character = "+"
                    while True:
                        for character in string:
                            display.scroll(character)
                            display.scroll(spacing_character)
                        sleep(300)

----

Code shifts
-----------------------------------------

| ASCII stands for American Standard Code for Information Interchange. 
| ASCII is a character encoding standard used in electronic communication to represent text. Each character (like letters, numbers, and symbols) is assigned a unique numeric value.
| Characters can be converted to ASCII numbers, and back.

.. py:function:: ord(character)

    | returns the ASCII value for character.
    | e.g ``display.scroll(ord('a'))`` scrolls 97.

.. py:function:: chr(number)

    | returns the character for the ASCII number.
    | e.g ``display.scroll(chr(97))`` scrolls 'a'.

| The code below converts the character to its ASCII number, decreases the ASCII number by 2, then converts the modified ASCII number back to a character.
| e.g `h` is converted to ascii_num `104`, `104` is changed to `102`, then ascii_num `102` is converted to `f`. 
| `'h'` (ASCII 104) becomes `'f'` (ASCII 102)
| `'q'` (ASCII 113) becomes `'o'` (ASCII 111)
| `'z'` (ASCII 122) becomes `'x'` (ASCII 120)

| ``ord(character)`` converts the character to its ASCII number.
| ``ascii_num -= 2`` decreases the ASCII number by 2.
| ``chr(ascii_num)`` converts the modified ASCII number back to a character.

.. code-block:: python

    from microbit import *

    code_string = 'hqz'

    while True:
        for character in code_string:
            ascii_num = ord(character)
            ascii_num -=2
            new_char = chr(ascii_num)
            display.scroll(new_char, delay=50)
        sleep(300)


.. admonition:: Tasks

    #. Write a for-loop that converts the code word "ald", then scrolls the converted secret word "dog".

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop that converts the code word "ald", then scrolls the converted secret word "dog".

                .. code-block:: python

                    from microbit import *

                    code_string = 'ald'

                    while True:
                        for character in code_string:
                            ascii_num = ord(character)
                            ascii_num +-=3
                            new_char = chr(ascii_num)
                            display.scroll(new_char, delay=50)
                        sleep(300)

----

Prime factors
----------------

| The modulo operator % returns the remainder of a division operation.

.. py:attribute:: dividend % divisor

    | returns the remainder when `dividend` is divided by `divisor`.
    | e.g 14 % 3 returns 2, because 14 divided by 3 is 4 with a remainder of 2.

| e.g. ``5 % 2`` returns the remainder 1.
| ``test_num % num`` returns the remainder from division.
| ``if test_num % num == 0`` checks whether the remainder is zero or not.

| The code below scrolls the prime factors of 15, by only scrolling the divisor when the remainder is 0.

.. code-block:: python

    from microbit import *

    primes = [2, 3, 5]
    test_num = 15
    while True:
        for num in primes:
            if test_num % num == 0:
                display.scroll(num, delay=50)
        sleep(300)

----

.. admonition:: Tasks

    #. Modify the code above to find the prime factors of 42.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above to find the prime factors of 42.

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

Abbreviations
--------------------------------------

.. py:attribute:: string[start:stop]

    | returns character `start` up to but not including character `stop` of the string.
    | ``'January'[0:3]`` returns characters 0 to 2 which is 'Jan'.

| The code below gets the first three letters of each month by using the slice ``month[0:3]``.

.. code-block:: python

    from microbit import *

    months = ['January', 'February', 'March']
    while True:
        for month in months:
            short_month = month[0:3]
            display.scroll(short_month, delay=80)
        sleep(300)

.. admonition:: Tasks

    #. Modify the code above to scroll the first 3 letters of the days: "Monday", "Tuesday", "Wednesday".

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above to scroll the first 3 letters of the days: "Monday", "Tuesday", "Wednesday".

                .. code-block:: python

                    from microbit import *

                    days = ["Monday", "Tuesday", "Wednesday"]
                    while True:
                        for day in days:
                            short_day = day[0:3]
                            display.scroll(short_day, delay=80)
                        sleep(300)


----

Vowels
-----------------------------------------------

| The keyword, ``in``, can be used to test whether a character is in a string.

.. py:attribute:: element in collection

    | returns `True` if `element` is found in `collection`, otherwise `False`.
    | ``"A" in "AEIOU"`` returns True.

.. py:attribute:: element not in collection

    | returns `True` if `element` is not found in `collection`, otherwise `False`.
    | ``"B" not in "AEIOU"`` returns True.


| What does this code do?
| ``name[0] in "AEIOU"`` returns **True** if character 0 in the name string is in the string of vowels.
| ``name[0] not in "AEIOU"`` returns **True** if character 0 in the name string is **not** in the string of vowels.


.. py:function:: string.upper()

    | returns a new string with all characters converted to uppercase.
    | ``"hello world".upper()`` returns "HELLO WORLD".
    | e.g. ``anna.upper()`` returns "ANNA"

| The code below scrolls the name in upper case only if the name starts with a vowel.

.. code-block:: python

    from microbit import *

    name_list = ['Alexia', 'Bethany', 'Chloe']
    while True:
        for name in name_list:
            if name[0] in "AEIOU":
                display.scroll(name.upper(), delay=50)
        sleep(300)

The code below scrolls the name in upper case only if the name **does not** start with a vowel.

.. code-block:: python

    from microbit import *

    name_list = ['Alexia', 'Bethany', 'Chloe']
    while True:
        for name in name_list:
            if name[0] not in "AEIOU":
                display.scroll(name.upper(), delay=50)
        sleep(300)


.. py:function:: sorted_list = sorted(original_list)

    | returns a new list with the elements of `original_list` sorted in ascending order by default.
    | sorted_name_list = sorted(["Charlie", "Alice", "Bob"])  returns the list sorted_name_list which is ["Alice", "Bob", "Charlie"].

The code below sorts the list first then scrolls the name in uppercase.

.. code-block:: python

    from microbit import *

    name_list = ['Zoe', 'Yasmin', 'Xena']
    sorted_name_list = sorted(name_list)

    while True:
        for name in sorted_name_list:
            display.scroll(name.upper(), delay=50)
        sleep(300)


----

.. admonition:: Tasks

    #. Write a for-loop to scroll names beginning with a vowel in ['Gabriella', 'Julia', 'Isabel', 'Hannah', 'Emily', 'Fiona', 'Chloe', 'Daisy', 'Anna', 'Bella']. Display the names in uppercase. Display the names in alphabetical order.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop to scroll names beginning with a vowel in ['Gabriella', 'Julia', 'Isabel', 'Hannah', 'Emily', 'Fiona', 'Chloe', 'Daisy', 'Anna', 'Bella']. Display the names in uppercase. Display the names in alphabetical order.

                .. code-block:: python

                    from microbit import *

                    name_list = ['Gabriella', 'Julia', 'Isabel', 'Hannah', 'Emily', 'Fiona', 'Chloe', 'Daisy', 'Anna', 'Bella']

                    sorted_name_list = sorted(name_list)

                    while True:
                        for name in sorted_name_list:
                            if name[0] in "AEIOU":
                                display.scroll(name.upper(), delay=50)
                        sleep(300)




