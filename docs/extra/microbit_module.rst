==========================
microbit module
==========================

.. py:module:: microbit


| The ``microbit`` module gives access to all the hardware that is built-in on the microbit.
| See: https://microbit-micropython.readthedocs.io/en/stable/microbit.html
| Some useful methods from the microbit module are below.

sleep
-------------

.. py:function:: sleep(n)

    Wait for ``n`` milliseconds. One second is 1000 milliseconds, so
    ``microbit.sleep(1000)`` will pause the execution for one second.

    :param n: An integer or floating point number indicating the number of
        milliseconds to wait.

temperature
-------------

.. py:function:: temperature()

    :returns: An integer with the temperature of the micro:bit in degrees
        Celcius.

panic
-------------

.. py:function:: panic(n)

    Enter a panic mode that stops all execution, scrolls an error code in
    the micro:bit display and requires restart. Used when debugging to stop code at a point.

    :param n: An arbitrary integer between 0 and 255 to indicate an error code.


reset
-------------

.. py:function:: reset()

    Restart the board.


running_time
-------------

.. py:function:: running_time()

    :returns: The number of milliseconds since the board was switched on or
        restarted.

scale
-------------

.. py:function:: scale(value, from_, to)

    Converts a value from a range to another range.

    :param value: A number to convert.
    :param from_: A tuple to define the range to convert from.
    :param to: A tuple to define the range to convert to.

    :returns: The ``value`` converted to the ``to`` range.

    For example, to convert 30 degrees from Celsius to Fahrenheit::

        temp_fahrenheit = scale(30, from_=(0.0, 100.0), to=(32.0, 212.0))

    This can be useful to convert values between inputs and outputs,
    for example an accelerometer x value to a speaker volume.

    If one of the numbers in the ``to`` parameter is a floating point
    (i.e a decimal number like ``10.0``), this function will return a
    floating point number.
    If they are both integers (i.e ``10``), it will return an integer::

        returns_int = scale(accelerometer.get_x(), from_=(-2000, 2000), to=(0, 255))

    Negative scaling is also supported, for example
    ``scale(25, from_=(0, 100), to=(0, -200))`` will return ``-50``.


