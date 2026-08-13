====================================================
LED Code Ordering
====================================================

Question 1
-------------------

| Put the lines in order to build an ongoing blinker loop that switches an LED on Pin 2 fully ON and OFF every second.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        pin2.write_digital(1)
        sleep(500)
        pin2.write_digital(0)
        sleep(500)

----

Question 2
-------------------

| A student connects a physical indicator light to Pin 1.
| Arrange the code lines to create a loop that checks Button B. If Button B is actively down, turn the indicator light fully ON. Otherwise, turn it fully OFF.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_b.is_pressed():
            pin1.write_digital(1)
        else:
            pin1.write_digital(0)

----

Question 3
-------------------------

| A student wants to flash a connected digital LED on Pin 0 a specific number of times.
| Arrange the lines to run a loop that pulses the LED ON for a duration that is a multiple of 300 milliseconds, based on a sequence of numbers. After each pulse, the LED should be turned OFF for 300 milliseconds.

.. ordering::
    :theme: light

    from microbit import *

    pulse_sequence = [1, 2, 3]
    for count in pulse_sequence:
        pin0.write_digital(1)
        sleep(300 * count)
        pin0.write_digital(0)
        sleep(300)

----

Question 4
------------------------------

| Put the code snippets in order so that when Button A is actively pressed down, it should write a half-brightness analog signal (512) to an LED on Pin 2. Otherwise, full brightness (1023) should be written to the LED. The loop should run every second.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            pin2.write_analog(512)
        else:
            pin2.write_analog(1023)
        sleep(1000)

----

Question 5
-------------------------

| Arrange the lines to loop through a list of brightness values to steadily increase the intensity of an LED on Pin 0.

.. ordering::
    :theme: light

    from microbit import *

    levels = [0, 256, 512, 768, 1023]
    while True:
        for value in levels:
            pin0.write_analog(value)
            sleep(200)




