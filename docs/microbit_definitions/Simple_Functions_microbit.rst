===================================
Simple Functions for the microbit
===================================

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


