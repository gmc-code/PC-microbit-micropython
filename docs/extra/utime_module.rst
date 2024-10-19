==========================
utime
==========================

.. py:module:: utime

| MicroPython contains an ``utime`` module based upon the ``time`` module in the Python standard library.
| This module gets measure time intervals and create delays.

----

sleep
-------------------

| The standard microbit library has its own sleep method (in milli-secs).
| ``utime.sleep`` may be convenient for micro sleeps or sleeps in seconds.

.. method:: utime.sleep(seconds)

    Sleep for the given number of seconds. ``seconds`` is an int or float.

.. method:: utime.sleep_ms(ms)

    Delay for given number of milliseconds. ``milliseconds`` is a positive int or 0.

.. method:: utime.sleep_us(us)

    Delay for given number of microseconds. ``microseconds`` is a positive int or 0.

| The code below has a sleep of 2 seconds between scrolling text.

.. code-block:: python

    from microbit import *
    import utime

    while True:
        display.scroll(".")
        utime.sleep(2)

----

ticks
-------------------

.. method:: utime.ticks_ms()

    Returns an increasing millisecond counter with an arbitrary reference point,
    that wraps around after some value.
    This counter is useful for measuring time intervals and implementing delays.

.. method:: utime.ticks_us()

    Returns an increasing microsecond counter with an arbitrary reference point,
    that wraps around after some value.

----

ticks_add
-------------------

.. method:: utime.ticks_add(ticks, delta)

    Offset ticks value by a given number, which can be either positive or
    negative. Given a ticks value, this function allows to calculate a ticks
    value, delta ticks before or after it.


| To find out wrap value use the code below which compares it with usys.maxsize.
| Typically it is half of the max integer that the microbit can handle.

.. code-block:: python

    from microbit import *
    import utime
    import usys

    # Find out TICKS_MAX used .e.g 1073741823
    print(utime.ticks_add(0, -1))
    val = utime.ticks_add(0, -1)
    print(val)
    max_sys = usys.maxsize
    print(max_sys/val)

----

ticks_diff
-------------------

.. method:: utime.ticks_diff(ticks1, ticks2)

    Measure ticks difference between values returned from
    :func:`utime.ticks_ms()` or :func:`ticks_us()` functions, as a signed value
    which may wrap around.

    The argument order is the same as for subtraction operator,
    ``ticks_diff(ticks1, ticks2)`` has the same meaning as ``ticks1 - ticks2``.


TIMED_OUT
----------------------

.. code-block:: python

    from microbit import *
    import utime

    display.scroll(pin2.read_digital())
    start = utime.ticks_ms()
    while pin2.read_digital() == 0:
        if utime.ticks_diff(utime.ticks_ms(), start) > 2000:
            display.scroll("TIMED_OUT")

Deadline
-----------------

.. code-block:: python

    from microbit import *
    import utime

    timer = 3000
    deadline = utime.ticks_add(utime.ticks_ms(), timer)
    while utime.ticks_diff(deadline, utime.ticks_ms()) > 0:
        utime.sleep_ms(200)
    display.show(Image.SKULL)

countdown timer
-----------------------

.. code-block:: python

    from microbit import *
    import utime

    # Set the countdown timer to 10 seconds (10000 milliseconds)
    countdown_time = 10000
    deadline = utime.ticks_add(utime.ticks_ms(), countdown_time)

    while utime.ticks_diff(deadline, utime.ticks_ms()) > 0:
        # Calculate the remaining time
        remaining_time = utime.ticks_diff(deadline, utime.ticks_ms())

        # Convert remaining time to seconds by integer division and display it
        display.show(str(remaining_time // 1000), delay=200))

        # Sleep for a short period to update the display
        utime.sleep_ms(200)

    # Display a smiley face when the countdown is complete
    display.show(Image.HAPPY)
