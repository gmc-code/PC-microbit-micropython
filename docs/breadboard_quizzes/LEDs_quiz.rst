====================================================
LEDs Quiz
====================================================

Section 1: Multiple Choice
==========================

Question 1
----------

.. multichoice::

    Why is a 47 ohm resistor required for each LED in the circuit?
    [ ] To make the LED shine at maximum brightness | Incorrect. Resistors reduce current flow rather than increasing brightness.
    [x] To limit current and prevent damage to the LED | Correct! The resistor prevents too much electricity from damaging the LED.
    [ ] To change the color of the light emitted by the LED | Incorrect. Resistors control current flow, not light color.

----

Question 2
----------

.. multichoice::

    Which command turns an LED completely ON using digital control?
    [x] write_digital(1) | Correct! Passing 1 turns the digital output HIGH (ON).
    [ ] write_digital(0) | Incorrect. `write_digital(0)` turns the LED OFF.
    [ ] write_digital(1023) | Incorrect. `1023` is used with `write_analog()`, not `write_digital()`.

----

Question 3
----------

.. multichoice::

    Which command turns an LED completely OFF using digital control?
    [] write_digital(1) | Incorrect! Passing 1 turns the digital output HIGH (ON).
    [x] write_digital(0) | Correct. `write_digital(0)` turns the LED OFF.
    [ ] write_digital(1023) | Incorrect. `1023` is used with `write_analog()`, not `write_digital()`.

----

Question 4
----------

.. multichoice::

    What brightness level does `pin0.write_analog(512)` set on the LED?
    [ ] Very dim | Incorrect. `256` represents a very dim setting.
    [x] Half brightness | Correct! `512` is half of the maximum analog value (`1023`).
    [ ] Full brightness | Incorrect. `1023` represents full brightness.

----

Question 5
----------

.. multichoice::

    When connecting an LED to the breadboard, which way should the long leg point?
    [x] Towards the micro:bit pins | Correct! The long leg (anode) connects towards the micro:bit control pin.
    [ ] Towards the ground rail | Incorrect. The long leg connects towards the micro:bit control pin.
    [ ] Orientation does not matter for LEDs | Incorrect. LEDs are diodes and only allow current to flow in one direction.

----

Section 2: Cloze
=====================================

Question 6
----------

| Complete the code to turn on the Yellow LED connected to pin1 using digital control.

.. cloze::

    from microbit import *

    while True:
        @@ pin1 | pin0 | pin2 @@.@@ write_digital(1) | write_digital(0) | write_analog(1) @@

----

Question 7
----------

| Complete the code to make the Red LED blink ON and OFF.

.. cloze::

    from microbit import *

    while True:
        pin0.write_digital(1)
        sleep(500)
        pin0.write_digital(@@ 0 | 1 | 1023 @@)
        sleep(500)

----

Question 8
----------

| Complete the code to set the Green LED (pin2) to about three-quarter brightness.

.. cloze::

    from microbit import *

    while True:
        pin2.@@ write_analog(768) | write_analog(256) | write_digital(768) @@

----

Question 9
----------

| Complete the loop to cycle through each brightness value in the list.

.. cloze::

    from microbit import *

    brightness_list = [0, 256, 512, 768, 1023]

    while True:
        for level @@ in | from | inside @@ brightness_list:
            pin0.write_analog(@@ level | brightness_list | 1023 @@)
            sleep(250)

----

Question 10
-----------

| Complete the code to blink all three LEDs together when Button B is pressed.

.. cloze::

    from microbit import *

    while True:
        if button_b.@@ is_pressed() | was_pressed() | gets_pressed() @@:
            pin0.write_digital(1)
            pin1.write_digital(1)
            pin2.write_digital(1)
            sleep(500)
            pin0.write_digital(0)
            pin1.write_digital(0)
            pin2.write_digital(0)

----

Section 3: Code Ordering
========================

Question 11
-----------

| Order the lines to turn ON the Red LED when Button A is pressed, and OFF when not pressed.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            pin0.write_digital(1)
        else:
            pin0.write_digital(0)
        sleep(500)

----

Question 12
-----------

| Order the lines to blink the Red LED 3 times using a for-loop.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        for i in range(3):
            pin0.write_digital(1)
            sleep(500)
            pin0.write_digital(0)
            sleep(500)
        sleep(3000)

----

Question 13
-----------

| Put the code segments in order to sequentially blink Red, Yellow, then Green LEDs one at a time.

.. ordering::
    :theme: light
    :no-padding:

    from microbit import *

    while True:
        pin0.write_digital(1)
        sleep(500)
        pin0.write_digital(0)
        pin1.write_digital(1)
        sleep(500)
        pin1.write_digital(0)
        pin2.write_digital(1)
        sleep(500)
        pin2.write_digital(0)

----

Question 14
-----------

| Order the code to make the Red LED gradually become brighter using a list of values.

.. ordering::
    :theme: light

    from microbit import *

    brightness_list = [0, 256, 512, 768, 1023]

    while True:
        for val in brightness_list:
            pin0.write_analog(val)
            sleep(250)

----

Question 15
-----------

| Put the code in order to dim the Red LED from full brightness to OFF using a list.

.. ordering::
    :theme: light

    from microbit import *

    brightness_list = [1023, 768, 512, 256, 0]

    while True:
        for val in brightness_list:
            pin0.write_analog(val)
            sleep(250)

