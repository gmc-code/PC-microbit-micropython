==========================
power module
==========================

.. py:module:: power

This module lets you manage the power modes of the micro:bit V2.

There are two micro:bit board low power modes that can be requested from MicroPython:

- **Deep Sleep**: Low power mode. Woken up via multiple sources (pins, button presses, uart data, or a timer).
- **Off**: Lowest power consumption. Woken via the reset button, or by plugging the USB cable while
  on battery power, form which it will restart and execute the programme from the beginning.


+------------------+-----------------+--------------------+
| .. centered:: USB Powered (Interface always awake)      |
+------------------+-----------------+--------------------+
| Board Power Mode | Target MCU Mode | Interface MCU mode |
+==================+=================+====================+
| **Deep Sleep**   | 💤  Sleep       | ⏰ Awake           |
+------------------+-----------------+--------------------+
| **Off**          | 📴 Power Down   | ⏰ Awake           |
|                  |                 | (red LED blinking) |
+------------------+-----------------+--------------------+

+------------------+-----------------+--------------------+
| .. centered:: Battery Powered                           |
+------------------+-----------------+--------------------+
| Board Power Mode | Target MCU Mode | Interface MCU mode |
+==================+=================+====================+
| **Deep Sleep**   | 💤 Sleep        | 💤 Sleep           |
+------------------+-----------------+--------------------+
| **Off**          | 📴 Power Down   | 📴 Power Down      |
+------------------+-----------------+--------------------+


Functions
-----------

.. py:function:: off()

    Power down the board to the lowest possible power mode.

    This is the equivalent to pressing the reset button for a few seconds,
    to set the board in "Off mode".

    The micro:bit will only wake up if the reset button is pressed or,
    if on battery power, when a USB cable is connected.

    When the board wakes up the programme will start running from the beginning.


.. py:function:: deep_sleep(ms=None, wake_on=None, run_every=True)

    Set the micro:bit into a low power mode where it can wake up and continue
    operation.

    :param ms: A time in milliseconds to wait before it wakes up.
    :param wake_on: A single instance or a tuple of pins and/or buttons to
        wake up the board, e.g. ``deep_sleep(wake_on=button_a)`` or
        ``deep_sleep(wake_on=(pin0, pin2, button_b))``.
    :param run_every: A boolean to configure if the functions scheduled with
        ``microbit.run_every`` will continue to run while it sleeps.

    The programme state is preserved and when it wakes up it will resume
    operation where it left off.

    Deep Sleep mode will consume more battery power than Off mode.

    The wake up sources are configured via arguments.

    The board will always wake up when receiving UART data, when the reset
    button is pressed (which resets the board) or, in battery power,
    when the USB cable is inserted.

    When the ``run_every`` parameter is set to ``True`` (the default), any
    function scheduled with :py:meth:`microbit.run_every<microbit.run_every>`
    will momentarily wake up the board to run and when it finishes it will go
    back to sleep.


----

low power example
------------------------

.. code-block:: python

    from microbit import *
    """
    Shows a silly face on the display every 5 seconds.
    When button A is pressed it goes into Deep Sleep mode, and wakes 20 seconds later,
    or by pressing button A again.
    When button B is pressed it goes into to Off mode.
    """
    from microbit import *
    import power

    @run_every(s=5)
    def silly_face():
        display.show(Image.SILLY)
        sleep(400)

    while True:
        if button_b.is_pressed():
            display.scroll("Off")
            # In this mode the micro:bit can only wake up via the reset button
            power.off()
            # This line of code will never be executed, as waking up from this
            # mode starts the programme from the beginning
            display.show(Image.SURPRISED)
        elif button_a.is_pressed():
            display.show(Image.ASLEEP)
            sleep(300)
            # Go into Deep Sleep with multiple wake up sources
            power.deep_sleep(
                wake_on=button_a,
                ms=20*1000,        # In 20 seconds it wakes up anyway
                run_every=False,   # Stops run_every from waking up the board
            )
            # When the micro:bit wakes up will it continue running from here
            # Blink a few times to show you are waking up
            display.show([Image("99099:09090:99099:09990"), Image.ASLEEP] * 3, 250)
        display.show(Image.HAPPY)
        sleep(200)


data logging example
------------------------

.. code-block:: python

    from microbit import *
    import power
    import log

    # Log the temperature every 5 minutes
    @run_every(min=5)
    def log_temperature():
        log.add(temp=temperature())

    while True:
        # Display the temperature when button A is pressed
        if button_a.is_pressed():
            display.scroll(temperature())
        # To go sleep, wake up when button A is pressed, and ensure the
        # function scheduled with run_every still executes in the background
        power.deep_sleep(wake_on=button_a, run_every=True)


