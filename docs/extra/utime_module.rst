====================================================
utime
====================================================

.. py:module:: utime

Use the ``utime`` module to get measure time intervals and create delays.

----

sleep
-------------------

.. method:: utime.sleep(seconds)

    Sleep for the given number of seconds. ``seconds`` is an int or float.

.. method:: utime.sleep_ms(ms)

    Delay for given number of milliseconds. ``milliseconds`` is a positive int or 0.

.. method:: utime.sleep_us(us)

    Delay for given number of microseconds. ``microseconds`` is a positive int or 0.

----

ticks
-------------------

.. method:: utime.ticks_ms()

    Returns an increasing millisecond counter with an arbitrary reference point, 
    that wraps around after some value.


.. method:: utime.ticks_us()

    Returns an increasing microsecond counter with an arbitrary reference point, 
    that wraps around after some value.

| To find out wrap value use:

    .. code-block:: python

        from microbit import *
        import utime

        # Find out TICKS_MAX used by this port
        print(utime.ticks_add(0, -1))

----

ticks_add
-------------------

.. method:: utime.ticks_add(ticks, delta)

    Offset ticks value by a given number, which can be either positive or 
    negative. Given a ticks value, this function allows to calculate a ticks 
    value, delta ticks before or after it.

| Find out TICKS_MAX for the wrapping.

.. code-block:: python

        from microbit import *
        import utime

        # Find out TICKS_MAX
        tick_max = utime.ticks_add(0, -1)
        print(tick_max)
        
| Example:

.. code-block:: python

    from microbit import *
    import utime

    timer = 3000
    deadline = utime.ticks_add(utime.ticks_ms(), timer)
    while utime.ticks_diff(deadline, utime.ticks_ms()) > 0:
        utime.sleep_ms(200)
    display.show(Image.SKULL)

----

ticks_diff
-------------------

.. method:: utime.ticks_diff(ticks1, ticks2)

    Measure ticks difference between values returned from 
    :func:`utime.ticks_ms()` or :func:`ticks_us()` functions, as a signed value
    which may wrap around.

    The argument order is the same as for subtraction operator, 
    ``ticks_diff(ticks1, ticks2)`` has the same meaning as ``ticks1 - ticks2``.

    :func:`utime.ticks_diff()` is designed to accommodate various usage 
    patterns, among them:

    Polling with timeout. In this case, the order of events is known, and you
    will deal only with positive results of :func:`utime.ticks_diff()`:

    .. code-block:: python

        # Wait for GPIO pin to be asserted, but at most 500us
        start = utime.ticks_us()
        while pin.value() == 0:
            if utime.ticks_diff(utime.ticks_us(), start) > 500:
                raise TimeoutError


    Scheduling events. In this case, :func:`utime.ticks_diff()` result may be
    negative if an event is overdue:


    .. code-block:: python

        # This code snippet is not optimized
        now = time.ticks_ms()
        scheduled_time = task.scheduled_time()
        if ticks_diff(scheduled_time, now) > 0:
            print("Too early, let's nap")
            sleep_ms(ticks_diff(scheduled_time, now))
            task.run()
        elif ticks_diff(scheduled_time, now) == 0:
            print("Right at time!")
            task.run()
        elif ticks_diff(scheduled_time, now) < 0:
            print("Oops, running late, tell task to run faster!")
            task.run(run_faster=true)



