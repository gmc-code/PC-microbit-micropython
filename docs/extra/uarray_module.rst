==========================
uarray
==========================

.. py:module:: uarray

| MicroPython contains an ``uarray`` module based upon the ``array`` module in the
Python standard library. 
| See: https://docs.micropython.org/en/latest/library/array.html
| See: https://docs.python.org/3.11/library/array.html#module-array
| See: https://www.dummies.com/article/technology/programming-web-design/c/determining-types-of-numbers-in-c-199399/

| An array is an object type which can compactly contain integers or floating point numbers. Arrays are sequence types and behave like lists, except that the type of objects stored in them is constrained. The type is specified at object creation time by using a type code, which is a single character.    

----

arrays
----------------------

.. function:: uarray.array(typecode)
              uarray.array(typecode, iterable)

    Return an array of type **typecode**.
    Initial contents can be specified by **iterable**. If it is not provided, an empty array is created.
    Supported format codes: b, B, h, H, i, I, l, L, q, Q, f, d


Integer array
-------------------

| The code below creates an array of integers using a typecode of "i".

.. code-block:: python

    from microbit import *
    import uarray

    while True:
        array_val = uarray.array("i", [1, 2, 3])
        for i in array_val:
            display.scroll(i, delay=60)

| This can also be doen using indexing.

.. code-block:: python

    from microbit import *
    import uarray

    while True:
        array_val = uarray.array("i", [1, 2, 3])
        for i in range(len(array_val)):
            display.scroll(array_val[i], delay=60)

----

Append
---------------

.. function:: append(val)

    Append new element val to the end of array, growing it.

| The code below appends an int to an array of ints.

.. code-block:: python

    from microbit import *
    import uarray

    array_val = uarray.array('i', [1, 2, 3])
    array_val.append(4)
    while True:
        for i in array_val:
            display.scroll(i, delay=60)

| The code below appends a float to an array of floats.
| The int, 4, is automatically converted to a float, 4.0.

.. code-block:: python

    from microbit import *
    import uarray

    array_val = uarray.array('f', [1.9, 2.0, 3])
    array_val.append(4)
    while True:
        for i in array_val:
            display.scroll(i, delay=60)

----

Extend
---------------

.. function:: extend(iterable)

    Append new elements as contained in iterable to the end of array, growing it.
    The typecode has to be the same for both arrays.

.. code-block:: python

    from microbit import *
    import uarray

    array_val = uarray.array('i', [1, 2, 3])
    array2_val = uarray.array('i', [5, 7, 9])
    array_val.extend(array2_val)
    while True:
        for i in array_val:
            display.scroll(i, delay=60)


----

Decimals
---------------

| The code below creates an array of floats (decimals) using a typecode of "d".

.. code-block:: python

    from microbit import *
    import uarray

    array1_val = uarray.array('d', [1.0, 2.0, 3.14])
    array2_val = uarray.array('d', [5, 7, 9])
    array1_val.extend(array2_val)
    while True:
        for i in array1_val:
            display.scroll(i, delay=60)
