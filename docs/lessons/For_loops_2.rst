====================================================
EXT: for-loops
====================================================

Spacing characters
----------------------------

.. code-block:: python

    from microbit import *

    welcome_string = 'Hello'
    string_length = len(welcome_string)
    spacing_character = "_"
    while True:
        for i in range(string_length):
            display.scroll(welcome_string[i])
            if i < string_length - 1:
                display.scroll(spacing_character)
        sleep(300)


Code shifts
-----------------------------------------

| Characters can be converted to ASCII numbers. and back.

| e.g `h` is converted to ascii_num `104`, then ascii_num `102` is converted to `f`. 
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

    #. Write a for-loop that converts the code word "ald" to the secret word "dog".

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a for-loop that converts the code word "ald" to the secret word "dog".

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
| ``test_num % num`` gets the remainder from division.
| ``if test_num % num == 0`` checks whether the remainder is zero or not.

| The code below finds the prime factors of 15.

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

| ``month[0:3]`` is a string slice in which characters 0 to 2 are returned.
| The code below gets the first three letters of each month.

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

| What does this code do?
| ``name[0] in "AEIOU"`` returns **True** if character 0 in the name string is in the string of vowels.
| ``name[0] not in "AEIOU"`` returns **True** if character 0 in the name string is **not** in the string of vowels.

| A string can be changed to upper case using ``.upper()``.
| e.g. ``anna.upper()`` returns "ANNA"

The code below scrolls the name in upper case only if the name starts with a vowel.

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

| A list can be sorted alphabetically using the ``sorted()`` function.
| e.g. ``sorted_name_list = sorted(name_list)`` stores the sorted list in a new list, sorted_name_list.

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




