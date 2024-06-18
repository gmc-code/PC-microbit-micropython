====================================================
Random pixels
====================================================


Random pixel and random brightness
-----------------------------------

| The following random functions can be used to create random pixels of random brightness.

----

Random pixel randint
-----------------------------------

.. py:function:: random.randint(a, b)

    Return a random integer from a to b, including both. 

| The code below displays a random pixel of random brightness every 50ms, then clears the display before showing the next one.

.. code-block:: python

    from microbit import *
    import random

    while True:
        random_brightness = random.randint(1, 9)
        random_x = random.randint(0, 4)
        random_y = random.randint(0, 4)
        display.set_pixel(random_x, random_y, random_brightness)
        sleep(50)
        display.clear()

----

.. admonition:: Tasks

    #. Modify the code to restrict the brightness to 1 to 5, and the pixels to the central 9 pixels.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to restrict the brightness to 1 to 5, and the pixels to the central 9 pixels.

                .. code-block:: python

                    from microbit import *
                    import random


                    while True:
                        random_brightness = random.randint(1, 5)
                        random_x = random.randint(1, 3)
                        random_y = random.randint(1, 3)
                        display.set_pixel(random_x, random_y, random_brightness)
                        sleep(50)
                        display.clear()

----

Tuple unpacking using an asterisk in a function call
-------------------------------------------------------

| Unpacking a tuple means splitting the tuple's elements into individual variables. 
| From the code above, the three lines of code that generate the random values can be moved into a function that returns the three random values in a tuple.
| The code below, uses the function, **rand_pix()**, to return a tuple of arguments for the **set_pixel** method.
| Tuple unpacking is used to unpack the tuple returned by the function, **rand_pix()**, for the **set_pixel** method.
| The returned tuple, **(random_x, random_y, random_brightness)**, is unpacked by **\*rand_pix()**, so that **random_x, random_y, random_brightness** are used as arguments.
| An asterisk * is used for unpacking positional arguments during the function call.

.. code-block:: python

    from microbit import *
    import random

    def rand_pix():
        random_brightness = random.randint(1, 9)
        random_x = random.randint(0, 4)
        random_y = random.randint(0, 4)
        return (random_x, random_y, random_brightness)

    while True:
        display.set_pixel(*rand_pix())
        sleep(50)
        display.clear()

----

.. admonition:: Tasks

    #. Modify the function, **rand_pix()**, to restrict the brightness to 4 to 7, and the pixels to the bottom 2 rows.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the function, **rand_pix()**, to restrict the brightness to 4 to 7, and the pixels to the bottom 2 rows.

                .. code-block:: python

                    from microbit import *
                    import random

                    def rand_pix():
                        random_brightness = random.randint(4, 7)
                        random_x = random.randint(0, 4)
                        random_y = random.randint(3, 4)
                        return (random_x, random_y, random_brightness)

                    while True:
                        display.set_pixel(*rand_pix())
                        sleep(50)
                        display.clear()

----

Tuple unpacking in multiple assignment
-----------------------------------------

| Instead of unpacking the returned tuple in the function call, multiple assignment is used in tuple unpacking.
| Tuple unpacking is used to unpack the returned tuple into 3 variables: 
| **random_x, random_y, random_brightness = rand_pix()**.
| These variables can then be passed into the set_pixel method: 
| **display.set_pixel(random_x, random_y, random_brightness)**.

.. code-block:: python

    from microbit import *
    import random

    def rand_pix():
        random_brightness = random.randint(1, 9)
        random_x = random.randint(0, 4)
        random_y = random.randint(0, 4)
        return (random_x, random_y, random_brightness)

    while True:
        random_x, random_y, random_brightness = rand_pix()
        display.set_pixel(random_x, random_y, random_brightness)
        sleep(50)
        display.clear()

----

.. admonition:: Tasks

    #. Modify the function, **rand_pix()**, to restrict the brightness to 3 to 6, and the pixels to the top 2 rows.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the function, **rand_pix()**, to restrict the brightness to 3 to 6, and the pixels to the top 2 rows.

                .. code-block:: python

                    from microbit import *
                    from microbit import *
                    import random

                    def rand_pix():
                        random_brightness = random.randint(3, 6)
                        random_x = random.randint(0, 4)
                        random_y = random.randint(0, 1)
                        return (random_x, random_y, random_brightness)

                    while True:
                        random_x, random_y, random_brightness = rand_pix()
                        display.set_pixel(random_x, random_y, random_brightness)
                        sleep(50)
                        display.clear()

----

Random pixel randrange(stop)
-----------------------------------

.. py:function:: random.randrange(stop)

    Return a randomly selected integer from zero and up to (but not including) **stop**.

| The code below uses randrange for the x and y values.
| **random.randrange(5)** returns values from 0 to 4.

.. code-block:: python

    from microbit import *
    import random

    def rand_pix():
        random_brightness = random.randint(1, 9)
        random_x = random.randrange(5)
        random_y = random.randrange(5)
        return (random_x, random_y, random_brightness)

    while True:
        random_x, random_y, random_brightness = rand_pix()
        display.set_pixel(random_x, random_y, random_brightness)
        sleep(50)
        display.clear()

----

.. admonition:: Tasks

    #. Modify the function, **rand_pix()**, to restrict the brightness to 3 to 6, and the pixels to the left 3 columns.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the function, **rand_pix()**, to restrict the brightness to 3 to 6, and the pixels to the left 3 columns.

                .. code-block:: python

                    from microbit import *
                    import random

                    def rand_pix():
                        random_brightness = random.randint(3, 6)
                        random_x = random.randrange(3)
                        random_y = random.randrange(5)
                        return (random_x, random_y, random_brightness)

                    while True:
                        display.set_pixel(*rand_pix())
                        sleep(50)
                        display.clear()


----

Random pixel randrange(start, stop)
--------------------------------------

.. py:function:: random.randrange(start, stop)

    Return a randomly selected integer from **start** and up to (but not including) **stop**.

| The code below uses randrange to restrict the x and y values to the inner square of 9 pixels.

.. code-block:: python

    from microbit import *
    import random

    def rand_pix():
        random_brightness = random.randint(1, 9)
        random_x = random.randrange(1, 4)
        random_y = random.randrange(1, 4)
        return (random_x, random_y, random_brightness)

    while True:
        random_x, random_y, random_brightness = rand_pix()
        display.set_pixel(random_x, random_y, random_brightness)
        sleep(50)
        display.clear()

----

.. admonition:: Tasks

    #. Modify the function, **rand_pix()**, to restrict the brightness to 1 to 3, and the pixels to the right 3 columns in the bottom 4 rows.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                    #. Modify the function, **rand_pix()**, to restrict the brightness to 1 to 3, and the pixels to the right 3 columns in the bottom 4 rows.

                .. code-block:: python

                    from microbit import *
                    import random

                    def rand_pix():
                        random_brightness = random.randint(1, 3)
                        random_x = random.randrange(2, 5)
                        random_y = random.randrange(1, 5)
                        return (random_x, random_y, random_brightness)

                    while True:
                        display.set_pixel(*rand_pix())
                        sleep(50)
                        display.clear()

----

Random pixel randrange(start, stop, step)
------------------------------------------

.. py:function:: random.randrange(start, stop, step)

    Return a randomly selected element from **start** and up to (but not including) **stop** in steps of **step**.

| The code below uses randrange to restrict the x and y values to rows and columns 0, 2, 4.
| The display is not cleared so that all the pixels that are set are shown.

.. code-block:: python

    from microbit import *
    import random

    def rand_pix():
        random_brightness = random.randint(1, 9)
        random_x = random.randrange(0, 5, 2)
        random_y = random.randrange(0, 5, 2)
        return (random_x, random_y, random_brightness)

    while True:
        random_x, random_y, random_brightness = rand_pix()
        display.set_pixel(random_x, random_y, random_brightness)
        sleep(50)
        display.clear()
----

.. admonition:: Tasks

    #. Modify the function, **rand_pix()**, to restrict the brightness to 1 to 3, and the pixels to columns 1 and 3 and the rows to 1 and 3.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                    #. Modify the function, **rand_pix()**, to restrict the brightness to 1 to 3, and the pixels to columns 1 and 3 and the rows to 1 and 3.
                .. code-block:: python

                    from microbit import *
                    import random

                    def rand_pix():
                        random_brightness = random.randint(1, 3)
                        random_x = random.randrange(1, 4, 2)
                        random_y = random.randrange(1, 4, 2)
                        return (random_x, random_y, random_brightness)

                    while True:
                        display.set_pixel(*rand_pix())
                        sleep(50)
                        display.clear()

----

Random pixel random.choice
---------------------------------

.. py:function:: random.choice(seq)

    Return a random element from the non-empty sequence ``seq`` such as a list or tuple.


| The code below uses **random.choice** to choose the x and y values from 1, 2 and 3.
| The brightness is chosen from values, 1, 5, and 9.
| The display is not cleared so that all the pixels that are set are shown.

.. code-block:: python

    from microbit import *
    import random

    while True:
        random_brightness = random.choice((1, 5, 9))
        random_x = random.choice((1, 2, 3))
        random_y = random.choice((1, 2, 3))
        display.set_pixel(random_x, random_y, random_brightness)
        sleep(50)

----

.. admonition:: Tasks

    #. Modify the code above to use a function, **rand_pix()**, to restrict the brightness to 1, 3 or 5, and the pixels to columns 0, 3, and 4 and the rows to 1 and 3.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                    #. Modify the code above to use a function, **rand_pix()**, to restrict the brightness to 1, 3 or 5, and the pixels to columns 0, 3, and 4 and the rows to 1 and 3.

                .. code-block:: python

                    from microbit import *
                    import random
                    
                    def rand_pix():
                        random_brightness = random.choice((1, 3, 5))
                        random_x = random.choice((0, 3, 4))
                        random_y = random.choice((1, 3))
                        return (random_x, random_y, random_brightness)

                    while True:
                        random_x, random_y, random_brightness = rand_pix()
                        display.set_pixel(random_x, random_y, random_brightness)
                        sleep(50)

----

Random Pixel rows and columns
--------------------------------

| The code below sets the brightness to 9 for a pixel in each row, with the column being random for each pixel.

.. code-block:: python

    from microbit import *
    import random

    def rand_x():
        return random.randint(0, 4)

    while True:
        for y in range(0, 5):
            display.set_pixel(rand_x(), y, 9)
        sleep(200)
        display.clear() 

----

.. admonition:: Tasks

    #. Write code to set the brightness to 9 for a pixel in each column, with the row being random for each pixel.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code to set the brightness to 9 for a pixel in each column, with the row being random for each pixel.
                
                .. code-block:: python

                    from microbit import *
                    import random

                    def rand_y():
                        return random.randint(0, 4)

                    while True:
                        for x in range(0, 5):
                            display.set_pixel(x, rand_y(), 9)
                        sleep(200)
                        display.clear() 

----

Random Pixels
--------------------------------

| The code below sets the brightness to 9 for 3 pixels in random rows and random columns.
| Note the use of the underscore, _, as a throw away variable, in **for _ in range(0, 3)**.
| A single underscore is used in place of a variable whose value is not going to be used in a loop.

.. code-block:: python

    from microbit import *
    import random

    def rand_val():
        return random.randint(0, 4)

    while True:
        for _ in range(3):
            display.set_pixel(rand_val(), rand_val(), 9)
        sleep(200)
        display.clear()

----

.. admonition:: Tasks

    #. Modify the code above to produce 10 random pixels at a time.
    #. Change the brightness to 5, and explore how many random pixels are needed so that only 1 to 3 pixels are left turned off. 

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above to produce 10 random pixels at a time.

                .. code-block:: python

                    from microbit import *
                    import random

                    def rand_val():
                        return random.randint(0, 4)

                    while True:
                        for _ in range(10):
                            display.set_pixel(rand_val(), rand_val(), 9)
                        sleep(200)
                        display.clear()

            .. tab-item:: Q2

                Change the brightness to 5, and explore how many random pixels are needed so that only 1 to 3 pixels are left turned off. 

                About 60 to 75 are needed since the same pixel may be generated more than once.

                .. code-block:: python

                    from microbit import *
                    import random

                    def rand_val():
                        return random.randint(0, 4)

                    while True:
                        for _ in range(75):
                            display.set_pixel(rand_val(), rand_val(), 9)
                        sleep(200)
                        display.clear()

----

Random Pixels choice Pixel rows and columns lists
----------------------------------------------------

| Lists can be used to restrict the possible x or y values.
| The function, **rand_val(vals)**, chooses one random value from the list passed to it.
| In the code below, there are a total of 9 pixels that can be used. 2 random pixels are shown at a time.

.. code-block:: python

    from microbit import *
    import random

    x_vals = [0, 2, 4]
    y_vals = [0, 2, 4]

    def rand_val(vals):
        return random.choice(vals)

    while True:
        for _ in range(2):
            display.set_pixel(rand_val(x_vals), rand_val(y_vals), 5)
        sleep(200)
        display.clear()


----

.. admonition:: Tasks

    #. Adjust the code to restrict the possible x and y values to the central 3 x 3 square, while showing 3 random pixels at a time.
    
    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Adjust the code to restrict the possible x and y values to the central 3 x 3 square, while showing 3 random pixels at a time.

                .. code-block:: python

                    from microbit import *
                    import random

                    x_vals = [1, 2 ,3]
                    y_vals = [1, 2 ,3]

                    def rand_val(vals):
                        return random.choice(vals)

                    while True:
                        for _ in range(3):
                            display.set_pixel(rand_val(x_vals), rand_val(y_w), 5)
                        sleep(200)
                        display.clear()

----

get_pixel and set_pixel
---------------------------

| ``display.get_pixel(x, y) == 0`` can be used to check if a pixel is on or off.

.. py:method:: get_pixel(x, y)

    Return the brightness of pixel at column ``x`` and row ``y`` as an
    integer between 0 and 9.


| The definition below checks each pixel to see if it is off and returns **True** if all are on.
| As soon as it finds a pixel that is off, it returns **False**.

.. code-block:: python

    from microbit import *
    
    def full_screen_on_check():
        for y in range(0, 5):
            for x in range(0, 5):
                if display.get_pixel(x, y) == 0:
                    return False
        return True


| The code below creates changing displays of random pixels.
| Start by just importing the **randint** function from the random module. 
| **full_screen_on_check()** checks to see when the display has been filled with 25 pixels.
| **fill_screen_with_counter** turns on random pixels with brightness between 5 and 9. It checks to see if the screen is filled, and returns the number of random pixels used in the process.
| The number of random pixels used to fill the screen is then scrolled.

.. code-block:: python

    from microbit import *
    from random import randint

    def full_screen_on_check():
        for y in range(0, 5):
            for x in range(0, 5):
                if display.get_pixel(x, y) == 0:
                    return False
        return True

    def fill_screen_with_counter():
        counter = 0
        while True:
            counter += 1
            x = randint(0, 4)
            y = randint(0, 4)
            brightness = randint(1, 4)
            display.set_pixel(x, y, brightness)
            if full_screen_on_check():
                return counter
            sleep(30)

    while True:
        new_fill_count = fill_screen_with_counter()
        display.scroll(new_fill_count)
        sleep(1000)


.. admonition:: Tasks

    #. Add code to display the min and max counts obtained in the code above.
    #. Improve the code in answer to task 1, by creating definitions to update the min and max counts, and to display the counts on button pressing. The main loop should look like this:
    #. Improve the code in answer to task 2, by adding a set to keep track of displayed pixels in the function, **fill_screen_with_counter()**. Number the pixels 0 to 4 in the top row, 5 to 9 in the next row. etc. Check to see if the length of the set is 25 to tell that the screen is full.

        .. code-block:: python

            counts = [None, None]

            while True:
                new_fill_count = fill_screen_with_counter()
                counts = update_counts(counts, new_fill_count)
                display_counts(counts, new_fill_count)
                sleep(1000)
                display.clear()

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Add code to display the min and max counts obtained in the code above.

                .. code-block:: python

                    from microbit import *
                    from random import randint

                    def full_screen_check():
                        for y in range(0, 5):
                            for x in range(0, 5):
                                if display.get_pixel(x, y) == 0:
                                    return False
                        return True

                    def fill_screen_with_counter():
                        counter = 0
                        while True:
                            counter += 1
                            x = randint(0, 4)
                            y = randint(0, 4)
                            brightness = randint(1, 4)
                            display.set_pixel(x, y, brightness)
                            if full_screen_check():
                                return counter
                            sleep(30)

                    min_fill_count = None
                    max_fill_count = None

                    while True:
                        new_fill_count = fill_screen_with_counter()
                        display.scroll(new_fill_count, delay=60)
                        if min_fill_count is not None:
                            min_fill_count = min(min_fill_count, new_fill_count)
                        else:
                            min_fill_count = new_fill_count
                        if max_fill_count is not None:
                            max_fill_count = max(max_fill_count, new_fill_count)
                        else:
                            max_fill_count = new_fill_count
                        display.scroll(min_fill_count, delay=60)
                        display.scroll(max_fill_count, delay=60)
                        sleep(1000)

            .. tab-item:: Q2

                Improve the code in answer to task 1, by creating definitions to update the min and max counts, and to display the counts on button pressing.

                .. code-block:: python

                    from microbit import *
                    from random import randint


                    def full_screen_check():
                        for y in range(0, 5):
                            for x in range(0, 5):
                                if display.get_pixel(x, y) == 0:
                                    return False
                        return True


                    def fill_screen_with_counter():
                        counter = 0
                        while True:
                            counter += 1
                            x = randint(0, 4)
                            y = randint(0, 4)
                            brightness = randint(1, 4)
                            display.set_pixel(x, y, brightness)
                            if full_screen_check():
                                return counter
                            sleep(10)


                    def update_counts(counts, count):
                        min_fill_count = counts[0]
                        if min_fill_count is not None:
                            min_fill_count = min(min_fill_count, count)
                        else:
                            min_fill_count = count
                        max_fill_count = counts[1]
                        if max_fill_count is not None:
                            max_fill_count = max(max_fill_count, count)
                        else:
                            max_fill_count = count
                        return (min_fill_count, max_fill_count)


                    def display_counts(counts, new_fill_count):
                        if button_a.was_pressed():
                            display.scroll(new_fill_count, delay=60)
                        if button_b.was_pressed():
                            display.scroll(counts[0], delay=60)
                            display.scroll(counts[1], delay=60)


                    counts = [None, None]

                    while True:
                        new_fill_count = fill_screen_with_counter()
                        counts = update_counts(counts, new_fill_count)
                        display_counts(counts, new_fill_count)
                        sleep(1000)
                        display.clear()

            .. tab-item:: Q3

                Improve the code in answer to task 2, by adding a set to keep track of displayed pixels in the function, **fill_screen_with_counter()**. Number the pixels 0 to 4 in the top row, 5 to 9 in the next row. etc. Check to see if the length of the set is 25 to tell that the screen is full.

                .. code-block:: python

                    from microbit import *
                    from random import randint
                    import utime


                    def full_screen_check():
                        for y in range(0, 5):
                            for x in range(0, 5):
                                if display.get_pixel(x, y) == 0:
                                    return False
                        return True


                    def fill_screen_with_counter():
                        counter = 0
                        screen_set = set()
                        while True:
                            counter += 1
                            x = randint(0, 4)
                            y = randint(0, 4)
                            brightness = randint(1, 4)
                            display.set_pixel(x, y, brightness)
                            screen_set.add(x + y*5)
                            if len(screen_set) == 25:
                                return counter
                            sleep(1)


                    def update_counts(counts, count):
                        min_fill_count = counts[0]
                        if min_fill_count is not None:
                            min_fill_count = min(min_fill_count, count)
                        else:
                            min_fill_count = count
                        max_fill_count = counts[1]
                        if max_fill_count is not None:
                            max_fill_count = max(max_fill_count, count)
                        else:
                            max_fill_count = count
                        return (min_fill_count, max_fill_count)


                    def display_counts(counts, new_fill_count):
                        if button_a.was_pressed():
                            display.scroll(new_fill_count, delay=60)
                        if button_b.was_pressed():
                            display.scroll(counts[0], delay=60)
                            display.scroll(counts[1], delay=60)


                    counts = [None, None]

                    while True:
                        new_fill_count = fill_screen_with_counter()
                        counts = update_counts(counts, new_fill_count)
                        display_counts(counts, new_fill_count)
                        sleep(1)
                        display.clear()


.. admonition:: Note

    #. Sets can be good to use when checking somethings since members of the set cannot be be repeated. Adding a member to a set that already exists has no affect.


