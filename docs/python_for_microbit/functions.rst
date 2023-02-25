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

| The function below does something. It prints text.
| It is defined using the ``def`` keyword and has empty parentheses.
| The ``def`` line has a colon at the end and the code for the definition is indented.
| To use the function, it is *called* using its name with parentheses; ``show_welcome()``.

.. code-block:: python

    def show_welcome():
        print("Hello python user!")

    show_welcome()


----

.. admonition:: Note

    Without the return statement, the function will return ``None``.

----

.. admonition:: Tasks

    #. Write a function called ``print_name`` that prints your name.
    #. Write a function called ``countdown`` that counts down from 5 to 1, printing each number. 

----

Functions with parameters
-----------------------------

| Functions can be more powerful by using `parameters`. 
| A parameter is the variable in the parentheses of the function which allows information to be passed to the function.
| An argument is the value in the parentheses that is sent to the function when it is called.
| In the code below, ``name`` is the parameter, and ``"beginner"`` and ``"user"`` are the arguments.

.. code-block:: python

    def show_welcome(name):
        print("Hello " + name)

    show_welcome("beginner")
    show_welcome("user")

----

Functions with default parameters
-----------------------------------------------

| 

.. code-block:: python


    def employee_info(name="N. U. Guy", salary=20000):
        print(f"{name} earns ${salary} per year")


    employee_info()
    employee_info(name="Nu Guy", salary=25000)
    employee_info("B. Ginner", 30000)

----

.. admonition:: Tasks

    #. Write a function called ``player_info`` with 3 default parameters for their user_name, their number of game lives and their game health status and print an example using it.

----

Functions returning information
----------------------------------------

| Functions can be more powerful by `returning values`. 
| The return value is what the function passes back to the code that called it. 
| Below is an example of a function that takes one parameter, the number of inches, and returns the number of centimetres.

.. code-block:: python

    def convert_inches_to_centimetres(inches):
        return inches * 2.54

    length_cm = convert_inches_to_centimetres(8)
    print(length_cm)


| Below is an example of a function that takes two parameters, the length and width of a rectangle, and returns the area.

.. code-block:: python

     def area_of_rectangle(length, width):
        return length * width

    area = area_of_rectangle(9, 7)
    print(area)

| Below is an example of a function that takes two parameters and returns a welcome message using the name and age of a person.
| Text joins are carried out with a ``+`` between the text strings.
| ``str()`` is used to turn ``age``, which is a integer, into a string.

.. code-block:: python

    def name_age_greeting(name, age):
        return "Hello " + name + ", you are " + str(age) + " years old."   

    print(name_age_greeting("Peter", 21))
    print(name_age_greeting("Paul", 24))
    print(name_age_greeting("Mary", 19))

----

.. admonition:: Tasks

    #. Define a function ``convert_cm_to_m(cm)`` that returns the result of converting a length in cm to metres.
    #. Define a function ``convert_m_to_cm(m)`` that returns the result of converting a length in metres to cm.
    #. Define a function ``area_square(length)`` that returns the area of a square.
    #. Write a function called ``random_greeting`` that returns a random greeting that is randomly chosen from a list of greetings: ``["Hi", "Hello", "G'day"]``. See: https://www.w3schools.com/python/ref_random_choice.asp


----

``*args``
----------------------------------------

| ``*args`` allow a function to take any number of positional arguments (non keyword arguments).

| ``*num`` allows a variable number of arguments to be passed in to be added in the ``multi_add`` function.
| In the function, ``num`` is a tuple of the arguments.
| For ``multi_add(2,5)``, num is the tuple`` (2, 5)``.
| For ``multi_add(1, 3, 5, 7, 9)``, num is the tuple ``(1, 3, 5, 7, 9)``.

.. code-block:: python

    def multi_add(*num):
        sum = 0
        for n in num:
            sum = sum + n
        return sum

    print(multi_add(2, 5))
    print(multi_add(1, 3, 5, 7, 9))