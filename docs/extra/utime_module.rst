==========================
utime
==========================

.. py:module:: utime

| MicroPython contains an ``utime`` module based upon the ``time`` module in the Python standard library.
| This module is used to measure time intervals and create delays.

----

sleep
-------------------

| The standard microbit library has its own sleep method (in milli-secs).
| ``utime.sleep`` may be convenient for micro sleeps or sleeps in seconds.

.. py:function:: utime.sleep(seconds)

    Sleep for the given number of seconds. ``seconds`` is an int or float.

| The code below has a sleep of 2 seconds between scrolling text.

.. code-block:: python

    from microbit import *
    import utime

    while True:
        display.scroll(".")
        utime.sleep(2)

.. py:function:: utime.sleep_ms(ms)

    Delay for given number of milliseconds. ``ms`` is a positive int or 0.

| The dot moves along the top row every 200 milliseconds.

.. code-block:: python

    from microbit import *
    import utime

    while True:
        for x in range(5):
            display.clear()
            display.set_pixel(x, 0, 9)
            utime.sleep_ms(200)



.. py:function:: utime.sleep_us(us)

    Delay for given number of microseconds. ``us`` is a positive int or 0.

| Pin 0 is switched on for 500 microseconds at a time, which makes a buzzing sound on a speaker or headphones connected to pin 0.

.. code-block:: python

    from microbit import *
    import utime

    for i in range(1000):
        pin0.write_digital(1)
        utime.sleep_us(500)
        pin0.write_digital(0)
        utime.sleep_us(500)



----

ticks
-------------------

.. py:function:: utime.ticks_ms()

    Returns an increasing millisecond counter with an arbitrary reference point,
    that wraps around after some value.
    This counter is useful for measuring time intervals and implementing delays.

| A reaction timer. Press button A as soon as the heart appears.

.. code-block:: python

    from microbit import *
    import utime
    import random

    while True:
        display.clear()
        sleep(random.randint(1000, 4000))
        display.show(Image.HEART)
        start = utime.ticks_ms()
        while not button_a.is_pressed():
            utime.sleep_ms(1)
        reaction = utime.ticks_diff(utime.ticks_ms(), start)
        display.scroll(str(reaction) + "ms", delay=80)



.. py:function:: utime.ticks_us()

    Returns an increasing microsecond counter with an arbitrary reference point,
    that wraps around after some value.

| The code times how long a loop of 1000 additions takes, in microseconds.

.. code-block:: python

    from microbit import *
    import utime

    start = utime.ticks_us()
    total = 0
    for i in range(1000):
        total += i
    duration = utime.ticks_diff(utime.ticks_us(), start)
    display.scroll(str(duration) + "us", delay=80)



----

ticks_add
-------------------

.. py:function:: utime.ticks_add(ticks, delta)

    Offset ticks value by a given number, which can be either positive or
    negative. Given a ticks value, this function allows to calculate a ticks
    value, delta ticks before or after it.


| To find out wrap value use the code below which compares it with usys.maxsize.
| Typically it is half of the max integer that the microbit can handle.

.. code-block:: python

    from microbit import *
    import utime
    import usys

    # Find out TICKS_MAX used e.g. 1073741823
    val = utime.ticks_add(0, -1)
    # print(val)
    display.scroll(str(val), delay=80)
    max_sys = usys.maxsize
    # print(max_sys/val)
    display.scroll(str(max_sys/val), delay=80)

----

ticks_diff
-------------------

.. py:function:: utime.ticks_diff(ticks1, ticks2)

    Measure ticks difference between values returned from
    :func:`utime.ticks_ms()` or :func:`utime.ticks_us()` functions, as a signed value
    which may wrap around.

    The argument order is the same as for subtraction operator,
    ``ticks_diff(ticks1, ticks2)`` has the same meaning as ``ticks1 - ticks2``.

| A stopwatch. Button A starts it and button B stops it and shows the time in seconds.

.. code-block:: python

    from microbit import *
    import utime

    start = None
    while True:
        if button_a.was_pressed():
            start = utime.ticks_ms()
            display.show(Image.ARROW_E)
        if button_b.was_pressed() and start is not None:
            elapsed = utime.ticks_diff(utime.ticks_ms(), start)
            display.scroll(round(elapsed / 1000, 1), delay=80)
            start = None
        sleep(10)




TIMED_OUT
----------------------

| The code waits up to 2 seconds for pin2 to go high, then stops waiting.

.. code-block:: python

    from microbit import *
    import utime

    display.scroll(pin2.read_digital())
    start = utime.ticks_ms()
    while pin2.read_digital() == 0:
        if utime.ticks_diff(utime.ticks_ms(), start) > 2000:
            display.scroll("TIMED_OUT")
            break

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
        display.show(str(remaining_time // 1000))

        # Sleep for a short period to update the display
        utime.sleep_ms(200)

    # Display a smiley face when the countdown is complete
    display.show(Image.HAPPY)
