
====================================================
Motor Code Ordering
====================================================

Question 1
-------------------------

| Put the snippets in order to build an automated pulsing pump cycle.
| The program should run the motor connected to Pin 1 for a short burst of half a second, turn it completely OFF, and wait for 1 second before repeating.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        pin1.write_digital(1)
        sleep(500)
        pin1.write_digital(0)
        sleep(1000)

----

Question 2
-------------------

| Arrange the code lines to create a manual safety override switch for a motor connected to Pin 2.
| If Button A is actively pressed down, send a continuous digital high signal to run the motor. Otherwise, keep it stopped.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            pin2.write_digital(1)
        else:
            pin2.write_digital(0)
        sleep(250)

----

Question 3
-------------------------

| A student wants to trigger a sequence of 3 rapid motor bursts using a fixed loop tracking list.
| Order the lines below to run a `for` loop that cycles through a list of 3 items and turns the motor on Pin 0 fully ON for a duration that is a multiple of 300 milliseconds, based on the current item in the list. After each burst, the motor should be turned OFF for 400 milliseconds.


.. ordering::
    :theme: light

    from microbit import *

    burst_markers = [1, 3, 5]
    for burst_multiplier in burst_markers:
        pin0.write_digital(1)
        sleep(300 * burst_multiplier)
        pin0.write_digital(0)
        sleep(400)

----

Question 4
-------------------------

| Put the lines in order to build an ongoing cycle that pulses the transistor-driven motor on Pin 0 at a low speed completely ON for one second, and then turns it to half speed for one second.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        pin0.write_analog(300)
        sleep(1000)
        pin0.write_analog(512)
        sleep(1000)

----

Question 5
-------------------

| Arrange the code lines to use Button A to turn the motor on Pin 0 to a safe startup power level of 320. Otherwise, turn the motor off completely.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            pin0.write_analog(320)
        else:
            pin0.write_analog(0)

----

Question 6
-------------------

| Arrange the code lines to use Button A to turn the motor on Pin 0 to a safe startup power level of 320, and Button B to turn the motor to a higher power level of 512. Otherwise, turn the motor off completely.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            pin0.write_analog(320)
        elif button_b.is_pressed():
            pin0.write_analog(512)
        else:
            pin0.write_analog(0)


