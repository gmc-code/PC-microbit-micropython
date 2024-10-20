===================================
Functions without parameters
===================================

| See: https://www.w3schools.com/python/python_functions.asp


| Functions are blocks of code that can be used many times in a program. 
| They avoid code repetition.
| Functions can **do something** or **return values**.
| Functions are defined using the ``def`` keyword.
| To use the function, it is *called* using its name with parentheses.

----

Functions that do something
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


Functions that return a value
---------------------------------

| The function below returns a value.
| It returns True when the microbit is tilted to the right enough, otherwise it returns False.


.. code-block:: python

    from microbit import *

    def is_right_tilt():
        if accelerometer.get_x() > 300:
            return True
        else:
            return False

    while True:
        display.scroll(is_right_tilt())
        sleep(500)


----

.. admonition:: Tasks

    #. Write a function called ``is_left_tilt`` that returns True or False.
    #. Write a function called ``is_cold`` that returns True when the temperature is below 20 Celsius, otherwise False.
    #. Write a function called ``get_fahrenheit`` that returns the temperature in degress Fahrenheit.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write a function called ``is_left_tilt`` that returns True or False.

                .. code-block:: python

                    from microbit import *

                    def is_left_tilt():
                        if accelerometer.get_x() < -300:
                            return True
                        else:
                            return False

                    while True:
                        display.scroll(is_left_tilt())
                        sleep(500)


            .. tab-item:: Q2

                Write a function called ``is_cold`` that returns True when the temperature is below 20 Celsius, otherwise False.

                .. code-block:: python

                    from microbit import *

                    def is_cold():
                        if temperature() < 20:
                            return True
                        else:
                            return False

                    while True:
                        display.scroll(is_cold())
                        sleep(500)


            .. tab-item:: Q3

                Write a function called ``get_fahrenheit`` that returns the temperature in degress Fahrenheit.

                .. code-block:: python

                    from microbit import *

                    def get_fahrenheit():
                        celsius = temperature()
                        fahrenheit = (celsius * 1.8) + 32
                        return fahrenheit

                    while True:
                        display.scroll(get_fahrenheit())
                        sleep(500)

