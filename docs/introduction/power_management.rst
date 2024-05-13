====================================================
Power Management **V2**
====================================================

The reset button can be used to manually control the power modes of the microbit.

----

Sleep
------

When powered by USB, press and hold power/reset for 5 seconds to enter sleep. The micro:bit power LED will dim from bright red to off. It will then flash on/off, showing you that it is still connected to the power source. Press power/reset to wake up. 

Removing the USB power cable and re-adding it will also wake the micro:bit.

----

Power off
----------

When powered by battery, press and hold power/reset for 5 seconds to power off the micro:bit. The micro:bit power LED will dim from bright red to off. It will then remain off until you press the power/reset to wake up. Disconnecting the USB and battery power supply will also power off the micro:bit.

Inserting a USB power lead will also wake the device.

----

Wake
-------------------

Pressing the power/reset again when in sleep/power-off mode will wake the micro:bit and your program will restart.

Removing the USB power cable and re-adding it will also wake the micro:bit.


----

.. admonition:: Warning

    | Mu v1.1.1 doesn't yet support the power module. Sep 2022.
    | Use the online micropython editor instead: https://python.microbit.org/v/3
    | Thonny v 4 can also be used.

----

Power module
--------------------------

| This module lets you manage the power modes of the microbit V2.
| See: https://microbit-micropython.readthedocs.io/en/v2-docs/power.html

----

Power down the microbit
--------------------------

There are two low power modes:

- **Off**: The power mode with the lowest power consumption, the only way to wake up the board is via the reset button, or by plugging the USB cable while on battery power. When the board wakes up it will restart and execute the programme from the beginning.

- **Deep Sleep**: Low power mode where the board can be woken up via multiple sources (pins, button presses, or a timer) and resume operation.

----

Power off
-----------------------

.. py:function:: power.off()

    | Power down the board to the lowest possible power mode.
    | This is the equivalent to pressing the reset button for a few seconds, to set the board to "Off mode".
    | The microbit, not on battery power, will only wake up if the reset button is pressed.
    | If on battery power, connecting a USB cable can wake it as well.
    | Waking up from this mode starts the programme from the beginning.

----

| The code below uses button-B pressing to power down the microbit.
| Press the reset button to wake it and restart the programme from the beginning.

.. code-block:: python

    from microbit import *
    import power


    display.scroll("starting up", delay=60)
    while True:
        if button_b.is_pressed():
            display.scroll("power off", delay=60)
            power.off()
        display.show(Image.HAPPY)
        sleep(200)

----

.. admonition:: Tasks

    #. Fix the code in 3 places so that it shows the image NO for 1 second before powering off if the B-button is pressed at any time.

        .. code-block:: python

            from microbit import *
            import power


            display.show(Image.YES)
            while True:
                if button_b.is_pressed():
                    display.show(Image.NO)
                    power.off()
                display.show(Image.HAPPY)
                sleep(1000)
                display.show("?")
                sleep(1000)

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Fix the code in 3 places so that it shows the image NO for 1 second before powering off if the B-button is pressed at any time.

                    .. code-block:: python

                        from microbit import *
                        import power


                        display.show(Image.YES)
                        while True:
                            if button_b.was_pressed():
                                display.show(Image.NO)
                                sleep(1000)
                                power.off()
                            display.show(Image.HAPPY)
                            sleep(1000)
                            display.show("?")
                            sleep(1000)

----

Deep Sleep
-----------------------


.. py:function:: power.deep_sleep(ms=None, wake_on=None, run_every=False)

    :param ms: A time in milliseconds to wait before it wakes up.
    :param wake_on: A single instance or a tuple of pins and/or buttons to wake up the board, e.g. ``deep_sleep(wake_on=button_a)`` or ``deep_sleep(wake_on=(pin0, pin2, button_b))``.
    :param run_every: Set to ``True`` to wake up with each ``microbit.run_every`` scheduled run.
    
    
    | Set the micro:bit into a low power mode where it can wake up and continue operation.
    | The programme state is preserved and when it wakes up it will resume operation where it left off.
    | Deep Sleep mode will consume more battery power than Off mode.
    | The wake up sources are configured via arguments.
    | If no wake up sources have been configured it will sleep until the reset button is pressed (which resets the board) or, on battery power, when the USB cable is inserted.
    | See: https://microbit-micropython.readthedocs.io/en/v2-docs/microbit.html


| The code below uses button-B pressing to go into a deep sleep.
| **wake_on=button_a** allows pressing button-A to wake it.
| **ms=30 * 60 * 1000** is a 30 minute deep sleep.
| **run_every=False** prevents run_every events from waking it.


.. code-block:: python

    from microbit import *
    import power

    display.scroll("starting up", delay=60)
    while True:
        if button_b.was_pressed():
            display.scroll("deep sleep", delay=60)
            sleep(300)
            power.deep_sleep(wake_on=button_a, ms=30 * 60 * 1000, run_every=False)
            display.scroll("waking", delay=60)
        display.show(Image.HAPPY)
        sleep(200)

----

Deep sleep wake via run_every
-------------------------------

| The code below uses button-A pressing to go into a deep sleep.
| **wake_on=None** prevents button pressing from waking it.
| **ms=30 * 1000** is a 30 second deep sleep.
| **run_every=True** allows run_every events to wake it.
| The decorator, **@run_every(s=10)**, causes wakeup_call() to run every 10 seconds.

.. code-block:: python
    
    from microbit import *
    import power

    @run_every(s=10)
    def wakeup_call():
        display.show(Image.ASLEEP)
        sleep(1000)
        
    display.show(Image.YES)
    while True:
        if button_b.was_pressed():
            display.show(Image.ARROW_S)
            sleep(300)
            power.deep_sleep(wake_on=None,ms=30 * 1000,run_every=True)
        display.show(Image.HAPPY)
        sleep(1000)


