==========================
Functions
==========================

| See: https://www.w3schools.com/python/python_functions.asp


| Functions are blocks of code that can be used many times in a program. 
| They avoid code repetition.
| Functions can do something or return values.
| Functions are defined using the ``def`` keyword.
| To use the function, it is *called* using its name with parentheses.

----

Functions without parameters
---------------------------------

| The function below does something. It displays text.
| It is defined using the ``def`` keyword and has empty parentheses.
| The ``def`` line has a colon at the end and the code for the definition is indented.
| To use the function, it is *called* using its name with parentheses; ``show_welcome()``.

.. code-block:: python

    from microbit import *


    def show_welcome():
        display.scroll("Hello Microbit user!", delay=80)


    show_welcome()

----

.. admonition:: Note

    Without the return statement, the function will return ``None``.

----

.. admonition:: Tasks

    #. Write a function called ``animate_3`` that displays 3 shapes quickly. 
    #. Write a function called ``countdown`` that counts down from 9 to 0, showing the number every half a second. 

----

Functions with parameters
-----------------------------

| Functions can be more powerful by using `parameters`. 
| A parameter is the variable in the parentheses of the function which allows information to be passed to the function.
| An argument is the value in the parentheses that is sent to the function when it is called.
| In the code below, ``name`` is the parameter, and ``"GMC"`` and ``"user"`` are the arguments.

.. code-block:: python

    from microbit import *


    def show_welcome(name):
        display.scroll("Hello " + name, delay=80)


    show_welcome("GMC")
    show_welcome("user")


Functions with default parameters
-----------------------------------------------

| In the code below, ``pin`` and ``repcount`` and ``sleepms`` are the parameters.
| Each has been given a default value that will be used if one is not specified in the arguments when the function is called.
| e.g ``blink_LED()`` will use pin=pin0, repcount=3, sleepms=100.
| e.g ``blink_LED(pin=pin1)`` will use pin=pin1, repcount=3, sleepms=100.
| e.g ``blink_LED(repcount=5)`` will use pin=pin0, repcount=5, sleepms=100.
| e.g ``blink_LED(repcount=10, sleepms=20)`` will use pin=pin0, repcount=10, sleepms=20.

.. code-block:: python

    from microbit import *


    def blink_LED(pin=pin0, repcount=3, sleepms=100):
        for i in range(repcount):
            pin.write_digital(1)
            sleep(sleepms)
            pin.write_digital(0)
            sleep(sleepms)


    while True:
        if button_a.is_pressed():
            blink_LED(pin=pin1, repcount=2, sleepms=200)
        else:
            blink_LED(pin=pin2, repcount=10, sleepms=20)
        sleep(1000)


----

.. admonition:: Tasks

    #. Write a function called ``countdown`` with 1 parameter for an integer to count down from, to zero, showing the number every half a second. 
    #. Write a function called ``animate_3`` with 3 parameters for 3 shapes to display quickly. 

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
    display.scroll(length_cm, delay=80)


| Below is an example of a function that takes two parameters, the length and width or a rectangle, and returns the area.

.. code-block:: python

    from microbit import *


    def area_of_rectangle(length, width):
        return length * width


    area = area_of_rectangle(9, 7)
    display.scroll(area, delay=80)


| Below is an example of a function that takes two parameters and returns a welcome message using the name and age of a person.
| Text joins are carried out with a ``+`` between the text strings.
| ``str()`` is used to turn ``age``, which is a number, into a string.

.. code-block:: python

    from microbit import *

w
    def name_age_greeting(name, age):
        return "Hello " + name + ", you are " + str(age) + " years old."   


    display.scroll(name_age_greeting("Peter", 21))
    display.scroll(name_age_greeting("Paul", 24))
    display.scroll(name_age_greeting("Mary", 19))

----

.. admonition:: Tasks

    #. Define a function ``convert_cm_to_m(cm)`` that converts a length in cm to metres.
    #. Define a function ``convert_m_to_cm(m)`` that converts a length in metres to cm.
    #. Define a function ``area_square(length)`` that calculates the area of a square.
    #. Write a function called ``countdown`` that returns a list of numbers starting at a specified number and ending at 0.
    #. Write a function called ``random_greeting`` that scrolls a random greeting that is randomly chosen from a list of greetings:.: ``["Hi", "Hello", "G'day"]``. See: https://microbit-micropython.readthedocs.io/en/latest/tutorials/random.html
    