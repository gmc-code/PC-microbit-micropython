==========================
uarray
==========================

.. py:module:: uarray

| MicroPython contains an ``uarray`` module based upon the ``array`` module in the
Python standard library. 
| See: https://docs.python.org/3.9/library/array.html#module-array
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

| The code below creates an array of integers.

.. code-block:: python

    from microbit import *
    import uarray

    while True:
        array_val = uarray.array("i", [1, 2, 3])
        for i in array_val:
            display.scroll(i)

----

.. function:: append(val)

    Append new element val to the end of array, growing it.

.. code-block:: python

    from microbit import *
    import uarray

    array_val = uarray.array('i', [1, 2, 3])
    array_val.append(4)
    while True:
        for i in array_val:
            display.scroll(i)

----

.. function:: extend(iterable)

    Append new elements as contained in iterable to the end of array, growing it.

.. code-block:: python

    from microbit import *
    import uarray

    array_val = uarray.array('i', [1, 2, 3])
    array2_val = uarray.array('i', [5, 7, 9])
    array_val.extend(array2_val)
    while True:
        for i in array_val:
            display.scroll(i)
