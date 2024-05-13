============================
Functions for the microbit
============================

| See: https://www.w3schools.com/python/python_functions.asp


| Functions are blocks of code that can be used many times in a program. 
| They avoid code repetition.
| Functions can do something or return values.
| Functions are defined using the ``def`` keyword.
| To use the function, it is *called* using its name with parentheses.

----

Functions without parameters
---------------------------------

| The function below does something. It scrolls text.
| It is defined using the ``def`` keyword and has empty parentheses.
| The ``def`` line has a colon at the end and the code for the definition is indented.
| To use the function, it is *called* using its name with parentheses; ``show_welcome()``.

.. code-block:: python

    from microbit import *

    def show_welcome():
        display.scroll("Hello mb user!", delay=80)

    show_welcome()

----

.. admonition:: Tasks

    #. Write a function called ``scroll_name`` that scrolls your name.
    #. Write a function called ``countdown`` that counts down from 5 to 1, showing each number. 

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write a function called ``scroll_name`` that scrolls your name.

                    .. code-block:: python

                        from microbit import *

                        def scroll_name():
                            display.scroll("my name", delay=80)

                        scroll_name()

                .. tab-item:: Q2

                    Write a function called ``countdown`` that counts down from 5 to 1, showing each number.

                    .. code-block:: python

                        from microbit import *

                        def countdown():
                            for num in range(5, 0, -1):
                                display.show(num)
                                sleep(300)
                            display.clear()

                        countdown()
                            

----

Functions with parameters
-----------------------------

| Functions can be more flexible when they use `parameters`. 
| A parameter is the variable in the parentheses of the function which allows information to be passed to the function.
| An argument is the value in the parentheses that is sent to the function when it is called.
| In the code below, ``name`` is the parameter, and ``"beginner"`` and ``"user"`` are the arguments.
| Text joins are carried out with a ``+`` between the text strings.

.. code-block:: python

    from microbit import *

    def show_welcome(name):
        display.scroll("Hello " + name, delay=60)

    show_welcome("beginner")
    show_welcome("user")


----

Functions with default parameters
-----------------------------------------------

| Default values can be added to parameters. e.g. name="Novice"

| Text joins are carried out with a ``+`` between the text strings.
| ``str()`` is used to turn ``score``, which is a integer, into a string.

.. code-block:: python

    from microbit import *


    def player_info(name="Novice", score=0):
        display.scroll(name + " has a score of " + str(score), delay=80)


    player_info()
    player_info("Rookie", 100)


----

Order with named parameters
-----------------------------------------------

| When named parameters are used, their order is not important.

.. code-block:: python

    from microbit import *


    def player_info(name="Novice", score=0):
        display.scroll(name + "  a score of " + str(score), delay=80)


    player_info(name="Rookie", score=10)
    player_info(score=10, name="Rookie")

----

Parameter order: positional before default
-----------------------------------------------

| Non-default parameters have to come before default parameters.
| e.g in the code below, the **name** parameter (without a default value) must come before the **score** parameter (with a default value).

.. code-block:: python

    from microbit import *


    def player_info(name, score=0):
        display.scroll(name + " has a score of " + str(score), delay=80)


    player_info("novice")
    player_info("Rookie", 100)


----

.. admonition:: Tasks

    #. Write a function called ``player_info`` with 3 default parameters for their user_name, their number of game lives and their game health status and display an example using it.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write a function called ``player_info`` with 3 default parameters for their user_name, their number of game lives and their game health status and display an example using it.

                    .. code-block:: python

                        from microbit import *


                        def player_info(name="novice", game_lives=3, health=100):
                            display.scroll(name + "has" + str(game_lives) + " lives with health of " + str(health), delay=80)


                        player_info()
                        player_info("speedy", 2, 65)

----

Functions returning information
----------------------------------------

| Functions can be more powerful by `returning values`. 
| The return value is what the function passes back to the code that called it. 
| Below is an example of a function that takes one parameter, the number of inches, and returns the number of centimetres.

.. code-block:: python

    from microbit import *
    

    def convert_inches_to_centimetres(inches):
        return inches * 2.54


    length_cm = convert_inches_to_centimetres(8)
    display.scroll(length_cm)


| Below is an example of a function that takes two parameters, the length and width of a rectangle, and returns the area.

.. code-block:: python

    from microbit import *
    

    def area_of_rectangle(length, width):
        return length * width


    area = area_of_rectangle(9, 7)
    display.scroll(area)

| Below is an example of a function that takes two parameters and returns a string.
| Text joins are carried out with a ``+`` between the text strings.
| ``str()`` is used to turn ``age``, which is a integer, into a string.

.. code-block:: python

    from microbit import *


    def player_goals(name, goals):
        return name + " scored " + str(goals) + " goals."   

    display.scroll(player_goals("Cristiano Ronaldo", 824), delay=70)
    display.scroll(player_goals("Messi", 797), delay=70)
    display.scroll(player_goals("Pele", 762), delay=70)

----

.. admonition:: Tasks

    #. Define a function ``convert_cm_to_m(cm)`` that returns the result of converting a length in cm to metres.
    #. Define a function ``convert_m_to_cm(m)`` that returns the result of converting a length in metres to cm.
    #. Define a function ``area_square(length)`` that returns the area of a square.
    #. Write a function called ``random_greeting`` that returns a random greeting that is randomly chosen from a list of greetings: ``["Hi", "Hello", "G'day"]``. See: https://www.w3schools.com/python/ref_random_choice.asp

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Define a function ``convert_cm_to_m(cm)`` that returns the result of converting a length in cm to metres. 

                    .. code-block:: python

                        from microbit import *


                        def convert_cm_to_m(cm):
                            return cm / 100


                        length_cm = convert_cm_to_m(80)
                        display.scroll(length_cm)

                .. tab-item:: Q2

                    Define a function ``convert_m_to_cm(m)`` that returns the result of converting a length in metres to cm. 

                    .. code-block:: python

                        from microbit import *


                        def convert_m_to_cm(m):
                            return m * 100


                        length_m = convert_m_to_cm(1.82)
                        display.scroll(length_m)

                .. tab-item:: Q3

                    Define a function ``area_square(length)`` that returns the area of a square. 

                    .. code-block:: python

                        from microbit import *


                        def area_square(length):
                            return length * length


                        area = area_square(5)
                        display.scroll(area)

                .. tab-item:: Q4

                    Write a function called ``random_greeting`` that returns a random greeting that is randomly chosen from a list of greetings: ``["Hi", "Hello", "G'day"]``.

                    .. code-block:: python

                        from microbit import *
                        import random


                        def random_greeting(name):
                            greetings = ["Hi", "Hello", "G'day"]
                            greet = random.choice(greetings)
                            return greet + name


                        greeting = random_greeting("Jim")
                        display.scroll(greeting, delay=70)


----

Allowing for a variable number of arguments
---------------------------------------------

| ``*args`` allow a function to take any number of positional arguments (non keyword arguments).

| ``*nums`` allows a variable number of arguments to be passed in to be added in the ``multi_add`` function.
| In the function, ``nums`` is a tuple of the arguments.
| For ``multi_add(1, 3, 5, 7, 9)``, nums is the tuple ``(1, 3, 5, 7, 9)``.

.. code-block:: python

    from microbit import *


    def multi_add(*nums):
        sum = 0
        for num in nums:
            sum = sum + num
        return sum


    display.scroll(multi_add(1, 3, 5, 7, 9), delay=70)

----

.. admonition:: Tasks

    #. Define a function ``multi_product(*nums)`` that finds the product of the arguments.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Define a function ``multi_product(*nums)`` that finds the product of the first 4 primes.

                    .. code-block:: python

                        from microbit import *


                        def multi_product(*nums):
                            total = 1
                            for num in nums:
                                total = total * num
                            return total


                        display.scroll(multi_product(2, 3, 5, 7), delay=70)

