====================================================
Power Management **V2**
====================================================


.. py:module:: power

| This module lets you manage the power modes of the microbit V2.
| See: https://microbit-micropython.readthedocs.io/en/v2-docs/power.html

There are two low power modes:

- **Deep Sleep**: Low power mode where the board can be woken up via multiple sources (pins, button presses, or a timer) and resume operation.
- **Off**: The power mode with the lowest power consumption, the only way to wake up the board is via the reset button, or by plugging the USB cable while on battery power. When the board wakes up it will restart and execute your programme from the beginning.

----

Power down the board
-----------------------

.. py:function:: off()

    | Power down the board to the lowest possible power mode.
    | This is the equivalent to pressing the reset button for a few second, to set the board to "Off mode".
    | The microbit will only wake up if the reset button is pressed or, if on battery power, when a USB cable is connected.
    | When the board wakes up it will start from a reset state, so the programme will start running from the beginning.

.. py:function:: deep_sleep(ms=None, wake_on=None, run_every=False)

    | Set the micro:bit into a low power mode where it can wake up and continue operation.
    | The programme state is preserved and when it wakes up it will resume operation where it left off.
    | Deep Sleep mode will consume more battery power than Off mode.
    | The wake up sources are configured via arguments.
    | If no wake up sources have been configured it will sleep until the reset button is pressed (which resets the board) or, in battery power when the USB cable is inserted.

    :param ms: A time in milliseconds to wait before it wakes up.
    :param wake_on: A single instance or a tuple of pins and/or buttons to wake up the board, e.g. ``deep_sleep(wake_on=button_a)`` or ``deep_sleep(wake_on=(pin0, pin2, button_b))``.
    :param run_every: Set to ``True`` to wake up with each ``microbit.run_every`` scheduled run.
    See: https://microbit-micropython.readthedocs.io/en/v2-docs/microbit.html

