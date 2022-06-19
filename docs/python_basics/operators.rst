==========================
Operators
==========================

Arithmetic operators
-----------------------

Arithmetic operators are used with numbers to perform common mathematical operations.

.. list-table::
    :widths: 20 60 20
    :header-rows: 1

    *   - **Operator** 
        - **Description**  
        - **Example**
    *   - \+
        - Addition    
        - x + y
    *   - \-
        - Subtraction    
        - x - y
    *   - \*    
        - Multiplication    
        - x * y
    *   - /    
        - Division    
        - x / y
    *   - %    
        - Modulus    
        - x % y
    *   - \**    
        - Exponentiation    
        - x ** y
    *   - //    
        - Floor division    
        - x // y


| Modulus gives the remainder from a division.
| Floor division rounds down the result from a division to the nearest integer.
| Exponentiation raises to a power.

.. code-block:: python

    a=9
    b=2

    print('a =', a, ',', 'b =', b)
    # a = 9 , b = 2

    print('Addition : a + b =', a + b)
    # Addition : a + b = 11

    print('Subtraction : a - b =', a - b)
    # Subtraction : a - b = 7

    print('Multiplication : a * b =', a * b)
    # Multiplication : a * b = 18

    print('Division (float) : a / b =', a / b)
    # Division (float) : a / b = 4.5

    print('Division (floor) : a // b =', a // b)
    # Division (floor) : a // b = 4

    print('Modulus (remainder) : a % b =', a % b)
    # Modulus (remainder) : a % b = 1

    print('Exponent (power) : a ** b =', a ** b)
    # Exponent (power) : a ** b = 81


| Basic arithmetic operators: ``+,-,*,/`` are used in the same way as a calculator. 
| Below is an example using arithmetic operators for the temperature read by the micro:bit in Celsius to Fahrenheit::

.. code-block:: python

    from microbit import *

    celsiusTemp = temperature()
    fahrenheitTemp = celsiusTemp * 9 / 5 + 32  


Operator ``%``, called ``mod`` is used to calculate the remainder when one value is divided by another. For example: maybe you'd like to know whether a number is odd or even, you could try dividing it by 2, if it's even, then there will be no remainder.

.. code-block:: python

    number = 3
    if number % 2 == 1:
        print("The number is odd")
    else:
        print("The number is even")

If the remainder is equal to ``1`` then this program will print ``The number is odd``, otherwise it will print ``The number is even``. 
You might write this program in a different way. People think about problems in different ways and no two programs are likely to be the same. 


Strings
--------

Strings (``str`` type in Python) are sequences of characters, with a length limited only by the memory of your machine. A useful fact to note is  that they can be concatenated using a ``+`` symbol.

.. code-block:: python

    name = "Hayley"
    message = "Well done " + name + ". You are victorious!"

This will concatenate the items on the right hand side of ``=`` and put the result in the variable called ``message``.

To join numbers and strings together, you must first convert the number to a string using the ``str()`` function if you want to do that.

.. code-block:: python

    temperature = 4
    if temperature < 6:
        display.scroll(str(temperature) + " is cold")


Booleans
---------
| A Boolean value is a value that is either ``True`` or ``False``, also represented by `1` and `0`. 
| In Python, there is a number of operations that allow you to manipulate boolean expressions.  

Comparison
--------------

Comparison operations are useful to test variable values in conditional statements or loops. Here are some examples of 
comparisons written in English::

    score is greater than 100
    name equals "Harry"
    x acceleration is not equal to 0

Rewriting the comparisons above in Python would be.

.. code-block:: python

    score > 100
    name ==  "Harry"
    acceleration  != 0

Python comparison operators:

.. tabularcolumns:: |L|l|

+--------------------------------+----------------------------------------+
| **Comparison Operator**        | **Meaning**                            |
+================================+========================================+
| ==                             | Equal to                               |
+--------------------------------+----------------------------------------+
| <, <=                          | Less than, less than or equal to       |
+--------------------------------+----------------------------------------+
| >, >=                          | Greater than, greater than or equal to |
+--------------------------------+----------------------------------------+
| !=                             | not equal to                           |
+--------------------------------+----------------------------------------+



Logical operations
-------------------------

Logical operators test the truth value of their operands.

+--------------+---------------------------------+-------------------+
| **Operator** |  **Evaluates to ``True`` if:**  | **Example**       |
+==============+=================================+===================+
| and          |  Both operands are true         | ``True and True`` |
+--------------+---------------------------------+-------------------+
| or           |  At least one operand is true   | ``True or False`` |
+--------------+---------------------------------+-------------------+
| not          |  Operand is false               | ``not False``     |
+--------------+---------------------------------+-------------------+
    

Membership operations
---------------------------

Membership operators are useful to determine presence of an element in a sequence.

+--------------+----------------------------------------------------------+--------------------------+
| **Operator** | **Evaluates to ``True`` if:**                            | **Example**              | 
+==============+==========================================================+==========================+
|   in         | A variable value is in the specified sequence            | ``x in [1, 2, 3, 4]``    |
+--------------+----------------------------------------------------------+--------------------------+
| not in       | Does not find a variable value in the specified sequence | ``x not in [1, 2, 3, 4]``|
+--------------+----------------------------------------------------+-----+--------------------------+

Using Boolean operations
----------------------------

You may have already used some examples that do this. In this example, the micro:bit will 
show an arrow changing in direction according to acceleration.


.. code-block:: python

    from microbit import *
    
    while True:
        x_bearing = accelerometer.get_x()

        if (x_bearing <= 100) and (x_acceleration >= 50):
        display.show(Image.ARROW_N)

        elif x_bearing > 100:
            display.show(Image.ARROW_E) 
    
        elif  x_bearing < 50:
            display.show(Image.ARROW_W) 

        else:
            display.show(Image.ARROW_S)     
