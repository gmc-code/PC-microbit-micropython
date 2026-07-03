====================================================
For loops with range Code Ordering
====================================================

Question 1
----------

| A student is coding an automated greenhouse plant watering system.
| Rearrange the lines below to create a loop that runs exactly 3 times to show an indicator image on the micro:bit display panel for each watering cycle.

.. ordering::
    :theme: light

    from microbit import *

    for pump_pulse in range(3):
        display.show(Image.HAPPY)
        sleep(1000)

----

Question 2
----------

| Put the code snippets in order to build a lighthouse safety beacon.
| The program must flash an alert symbol ("X") a total of 4 times.

.. ordering::
    :theme: light

    from microbit import *

    for flash_count in range(4):
        display.show("X")
        sleep(200)
        display.clear()
        sleep(200)

----

Question 3
----------

| Arrange the lines of code to create a rocket launch systems checker.
| The loop should step a counter variable through its default sequence starting from 0, stopping automatically just before it hits 5, to scroll each checkpoint number.

.. ordering::
    :theme: light

    from microbit import *

    for check_id in range(5):
        display.scroll(check_id)
        sleep(200)

----

Question 4
----------

| A student wants to flash a digital binary metronome signal.
| Order the lines below to create a loop that steps a variable through the numbers 0 and 1 only, showing each digit on the screen.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        for beat in range(2):
            display.show(beat)
            sleep(500)

----

Question 5
----------

| Rearrange the code segments below to create a simple step-multiplier calculator for a fitness tracker.
| The loop should run 3 times (generating values 0, 1, and 2), multiply each value by 10, and scroll the calculated results.

.. ordering::
    :theme: light

    from microbit import *

    for step_factor in range(3):
        total_steps = step_factor * 10
        display.scroll(total_steps)
        sleep(1000)



