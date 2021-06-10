==========================
Variables
==========================

| A variable is a name used to refer to a memory location where a value is stored. 
| It can be thought of as a box that stores data. 
| In Python, the same variable can be reused to store values of any type.
| e.g In ``rectangle_length = 2.3``, the variable names is ``rectangle_length``, the type is ``float`` (decimal) and the value is ``2.3``.
| e.g In ``user_name = GMC``, the variable names is ``user_name``, the type is ``str`` (string) and the value is ``GMC``.

Rules for Python variable names:
	• A variable name must start with a letter or the underscore character
	• A variable name cannot start with a number
	• A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
	• Variable names are case-sensitive (``age``, ``Age`` and ``AGE`` are three different variables)

----

Python conventions
--------------------------

| It is helpful to use meaningful variable names that indicate what the variable is. e.g. ``height`` instead of ``x`` for the height of an object.

Snake case
---------------

| Snake case is used for variables and functions.
| Snake case uses underscores between words. e.g. player_count, player_1_score, player_2_score

ALL_CAPS
---------------

| ALL_CAPS are used for constants, such as ``PI = 3.14``, ``GRAVITY = 9.8``, ``MILE_TO_METRES = 1609``.

CapWords
---------------

| CapWords, such as ``AnimalFeatures``, are used for Class names in python.

camelCase
---------------

| camelCase variables, such as ``playerScore``, are not recommended in python.

KebabCase
---------------

| KebabCase variables, such as ``player-score``, are not recommended in python.

----

Sample code
--------------------------

| In the code below, a counter variable is increased by one every time the A button is pressed. 
| Snake case with underscores is used in the name of the variable, ``a_count``.
| The variable must be assigned a value so it an be used.
| Assigning an initial value to a variable is called initializing the variable.

.. code-block:: python

    from microbit import *

    a_count = 0

    while True:
        if button_a.is_pressed():
            a_count = a_count + 1
            display.scroll(a_count, delay=80)

----

| In the code below, the distance in miles from 1 to 10 is converted to metres.
| ALL_CAPS are used for the constant: ``MILES_TO_METRES``
| The function name uses snake case: ``convert_miles_to_metres``.
| The function parameter uses snake case: ``distance_miles``.
| The variables use snake case: ``dist_miles`` and ``dist_metres``.

.. code-block:: python

    from microbit import *

    MILES_TO_METRES = 1609

    def convert_miles_to_metres(distance_miles):
        return distance_miles * MILES_TO_METRES

    while True:
        for dist_miles in range(1, 11):
            dist_metres = convert_miles_to_metres(dist_miles)
            display.scroll(dist_miles, delay=80)
            display.scroll('=', delay=80)
            display.scroll(dist_metres, delay=80)
        sleep(500)

----

Tasks
--------------------------

.. admonition:: Questions

    #. Convert ``AGE`` to snake case.
    #. Convert ``MyName`` to snake case.
    #. Convert ``My-FirstName-LastName`` to snake case.
    #. Convert ``rectangleArea`` to snake case.
    #. Convert ``cm_in_an_inch = 2.14`` to ALL_CAPS.
    #. Convert ``lbs_in_a_kg = 2.2`` to ALL_CAPS.
    #. A program asks for a person's age and stores it. What would be a good variable name to use: ``x``, ``variable1``, ``AGE``, ``age``, ``Years_Old``?
    #. A program uses a person's first name and last name. What would be a good variable name to use for their last name: ``x``, ``variable1``, ``SURNAME``, ``last_name``, ``Name``?
    #. A program calculates the area of a rectangle. What would be two good variable names to use for the length and width of the rectangle: ``x``, ``y``, ``LENGTH``, ``length``, ``Width``, ``width``?


