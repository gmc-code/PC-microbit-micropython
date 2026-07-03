====================================================
LED Code Ordering
====================================================

Question 1
-------------------

| Put the lines in order to build an ongoing blinker loop that switches an LED on Pin 2 fully ON and OFF every half-second.

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

| A student wants to flash a connected digital  LED on Pin 0 a specific number of times.
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

| Rearrange the lines to create an alternating toggle system on Pin 0 and Pin 1.
| The loop should run four times, toggling the two pins between ON and OFF every 400 milliseconds.
| The first toggle should be Pin 0 ON, Pin 1 OFF, the second toggle should be Pin 0 OFF, Pin 1 ON, the third toggle should be Pin 0 ON, Pin 1 OFF, and the fourth toggle should be Pin 0 OFF, Pin 1 ON.
| steps % 2 == 0 means that the step is even, and steps % 2 == 1 means that the step is odd.

.. ordering::
    :theme: light

    from microbit import *

    for steps in range(4):
        if steps % 2 == 0:
            pin0.write_digital(1)
            pin1.write_digital(0)
        else:
            pin0.write_digital(0)
            pin1.write_digital(1)
        sleep(400)

----

Question 5
------------------------------

| Put the code snippets in order so that when Button A is actively pressed down, it should write a half-brightness analog signal (512) to an LED on Pin 2. Otherwise, full brightness (1023) should be written to the LED. The loop should run every 250 milliseconds.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            pin2.write_analog(512)
        else:
            pin2.write_analog(1023)
        sleep(250)

----

Question 6
-------------------------

| Arrange the lines to loop through a sequence tuple of brightness values to steadily increase the intensity of an LED on Pin 0.

.. ordering::
    :theme: light

    from microbit import *

    levels = [0, 256, 512, 768, 1023]
    while True:
        for value in levels:
            pin0.write_analog(value)
            sleep(200)

----

Question 7
------------------------------

| Arrange the code segments to create a multi-LED delayed wave sequence.
| As the loop index increases, Pin 0 updates instantly, while Pin 1 safely reads a delayed step behind by validating that the item index has reached 1 or higher.

.. ordering::
    :theme: light

    from microbit import *

    brightness_list = [0, 512, 1023, 1023]
    while True:
        for i in range(4):
            pin0.write_analog(brightness_list[i])
            if i >= 1:
                pin1.write_analog(brightness_list[i - 1])
            sleep(250)


