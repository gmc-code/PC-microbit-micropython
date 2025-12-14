==========================
uarray
==========================

.. py:module:: uarray

| MicroPython contains an ``uarray`` module based upon the ``array`` module in the
Python standard library.
| See: `<https://docs.python.org/3.9/library/array.html>`#module-array
| See: `<https://www.dummies.com/article/technology/programming-web-design/c/determining-types-of-numbers-in-c-199399/

| An array is an object type which can compactly contain integers or floating point numbers. Arrays are sequence types and behave like lists, except that the type of objects stored in them is constrained. The type is specified at object creation time by using a type code, which is a single character.

----

arrays
----------------------

.. function:: uarray.array(typecode)
              uarray.array(typecode, iterable)

    Return an array of type **typecode**.
    Initial contents can be specified by **iterable**. If it is not provided, an empty array is created.
    Supported format codes: b, B, h, H, i, I, l, L, q, Q, f, d
    Use i for integers.

| The typecode specifies the type of elements stored in the array:
| b — Signed 8-bit integer (int8_t)
| B — Unsigned 8-bit integer (uint8_t)
| h — Signed 16-bit integer (int16_t)
| H — Unsigned 16-bit integer (uint16_t)
| i — Signed 32-bit integer (int32_t) (Recommended for general integers)
| I — Unsigned 32-bit integer (uint32_t)
| l — Signed 32-bit integer (Same as i, but used in some variations)
| L — Unsigned 32-bit integer (Same as I)
| q — Signed 64-bit integer (int64_t)
| Q — Unsigned 64-bit integer (uint64_t)
| f — Floating-point (single precision, 32-bit)
| d — Floating-point (double precision, 64-bit)

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

----

Average temperatures using an array
---------------------------------------

.. code-block:: python

    from microbit import *
    import uarray

    # Create an array to store 10 temperature readings, setting all to current temp initially
    temp0 = temperature()
    temperature_readings = uarray.array('i', [temp0] * 10)

    while True:
        # Shift all readings to the left
        for i in range(len(temperature_readings) - 1):
            temperature_readings[i] = temperature_readings[i + 1]

        # Add the latest temperature reading to the end of the array
        temperature_readings[-1] = temperature()

        # Calculate the average temperature
        avg_temp = sum(temperature_readings) // len(temperature_readings)

        # Display the average temperature
        display.scroll(str(avg_temp) + "C")

        sleep(1000)

----

Breadboard LED brightness via array
-----------------------------------------

.. code-block:: python

    from microbit import *
    import uarray

    # Define brightness levels
    brightness_levels = uarray.array('i', [0, 128, 255])

    while True:
        for brightness in brightness_levels:
            pin0.write_analog(brightness)
            sleep(1000)


----

Max light levels
-----------------------------------------

| This example uses an array to store light level readings and displays the maximum light level detected.

.. code-block:: python

    from microbit import *
    import uarray

    # Create an array to store light level readings
    light_levels = uarray.array('i', [0] * 10)

    while True:
        # Shift all readings to the left
        for i in range(len(light_levels) - 1):
            light_levels[i] = light_levels[i + 1]

        # Add the latest light level reading to the end of the array
        light_levels[-1] = display.read_light_level()

        # Find the maximum light level
        max_light = max(light_levels)

        # Display the maximum light level
        display.scroll(str(max_light))

        sleep(1000)

