====================================================
Potentiometer Code Ordering
====================================================

Question 1
----------------------

| Put the snippets in order to read the dial position on Pin 2 and immediately output the raw data sequence onto the scrolling LED screen.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        pot_val = pin2.read_analog()
        display.scroll(pot_val, delay=80)
        sleep(20)

----

Question 2
-----------------

| A student hooks up an external LED component to Pin 0 alongside their dial on Pin 2.
| Order the blocks below to feed the incoming analog dial values straight out to control the LED brightness level.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        pot_val = pin2.read_analog()
        pin0.write_analog(pot_val)
        sleep(40)

----

Question 3
-----------------

| Put the code snippets in order to build a dual-fading light system.
| As Pin 0 gets brighter when the dial turns up, Pin 1 must safely dim down by subtracting the dial position from the maximum value.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        pot_val = pin2.read_analog()
        pin0.write_analog(pot_val)
        pin1.write_analog(1023 - pot_val)
        sleep(40)

----

Question 4
-------------------

| Put the instructions in the correct order to create a low-threshold safety sensor switch.
| If the dial value on Pin 2 drops strictly below 500, a warning indicator light on Pin 0 must switch to fully ON.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        pot_val = pin2.read_analog()
        if pot_val < 500:
            pin0.write_digital(1)
        else:
            pin0.write_digital(0)

----

Question 5
-----------------

| Order the lines below to build a high-threshold logic split circuit with an embedded status icon tracker.
| When the dial crosses 500 or more, turn on Pin 1 and display a built-in happy face icon to show authorization.

.. ordering::
    :theme: light
    :no-padding:

    from microbit import *

    while True:
        pot_val = pin2.read_analog()
        if pot_val >= 500:
            pin0.write_digital(0)
            pin1.write_digital(1)
            display.show(Image.HAPPY)
        else:
            pin0.write_digital(1)
            pin1.write_digital(0)
            display.clear()
        sleep(40)

----

Question 6
------------------------------

| Rearrange the code segments to create a multi-level signal routing system.
| Handle low dial signals on Pin 0, middle dial signals on Pin 1, and high dial signals on Pin 8 sequentially.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        pot_val = pin2.read_analog()
        if pot_val < 300:
            pin0.write_digital(1)
        elif pot_val < 600:
            pin1.write_digital(1)
        else:
            pin8.write_digital(1)

----

Question 7
------------------------------

| Rearrange the code segments to create a multi-level signal routing system.
| Usse 3 zone switches to handle low dial signals on Pin 0, middle dial signals on Pin 1, and high dial signals on Pin 8 sequentially while ensuring that only one zone is active at a time.

.. ordering::
    :theme: light:
    :no-padding:

    from microbit import *

    while True:
        pot_val = pin2.read_analog()
        if pot_val < 300:
            # Zone 1 Active Only
            pin0.write_digital(1)
            pin1.write_digital(0)
            pin8.write_digital(0)
        elif pot_val < 600:
            # Zone 2 Active Only
            pin0.write_digital(0)
            pin1.write_digital(1)
            pin8.write_digital(0)
        else:
            # Zone 3 Active Only
            pin0.write_digital(0)
            pin1.write_digital(0)
            pin8.write_digital(1)
        sleep(20)


