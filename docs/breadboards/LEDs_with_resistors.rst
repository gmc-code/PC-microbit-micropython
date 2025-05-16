==========================
LEDs_with_resistors
==========================

| The examples below use sequence only. No definition blocks are used.
| For better organising code into def blocks see: https://pc-microbit-micropython.readthedocs.io/en/latest/breadboards/LEDs_with_resistors_2.html

----
Connections
--------------------------

| The LEDs must be placed in line with a 47 ohm resistor.
| The 47 ohm resistor has Yellow, Violet, Black, Gold coloured bands.
| LEDS are normally connected to pin0, pin1, or pin2.
| All LEDS are also connected to the 0V pins.

.. image:: images/47ohm.png
    :scale: 50 %

| Bend the resistor by holding it at the bend position so it is U-shaped.

.. image:: images/resistor_shape.png
    :scale: 50 %

| Place the resistor in the breadboard so that the legs go in about 5mm.

.. image:: images/resistor_on_breadboard_low.png
    :scale: 50 %

----

Model
----------------------------------------

#.  Place the resistors first.
#.  Place the LEDs with the **long lead** (leg) so that it is closest to the pin side of the circuit. In this model, the long lead is on the **left** side of the breadboard.
#.  Check that the red LED is connected to pin0, yellow to pin1, and green to pin2.
#.  Connect with the jumper wires.

.. image:: images/3LEDS_1_bb.png
    :scale: 50 %

.. image:: images/3LEDS_2_bb.png
    :scale: 50 %

.. image:: images/3LEDS_3_bb.png
    :scale: 50 %

.. image:: images/LEDS.jpg
    :scale: 30 %

----

Write digital
----------------------------------------

| To turn the LED on fully use ``pin0.write_digital(1)`` for the LED on pin0.
| To turn the LED off use ``pin0.write_digital(0)`` for the LED on pin0.
| For the other pins, just replace ``pin0`` with ``pin1`` or ``pin2``.

----

Turn on and off pin0
----------------------------------------

| Pressing A turns **on** the LED on pin0.
| Pressing B turns **off** the LED on pin0.

.. code-block:: python

    from microbit import *


    while True:
        if button_a.is_pressed():
            pin0.write_digital(1)
        elif button_b.is_pressed():
            pin0.write_digital(0)
        sleep(500)

----

Blink All
----------------------------------------

| Pressing A blinks all 3 LEDS in order, one after the other.
| Pressing B blinks all 3 LEDS together.

.. code-block:: python

    from microbit import *


    while True:
        if button_a.is_pressed():
            pin0.write_digital(1)
            sleep(1000)
            pin0.write_digital(0)
            pin1.write_digital(1)
            sleep(300)
            pin1.write_digital(0)
            pin2.write_digital(1)
            sleep(1000)
            pin2.write_digital(0)
        elif button_b.is_pressed():
            pin0.write_digital(1)
            pin1.write_digital(1)
            pin2.write_digital(1)
            sleep(1000)
            pin0.write_digital(0)
            pin1.write_digital(0)
            pin2.write_digital(0)
        sleep(500)

----

Blink using for i in range
----------------------------------------

| Repeated blinking can be done with a for-loop.
| The for-loop below runs 3 times.

.. code-block:: python

    from microbit import *


    while True:
        for i in range(3):
            pin0.write_digital(1)
            sleep(1000)
            pin0.write_digital(0)
            sleep(1000)
        sleep(3000)


----

.. admonition:: Tasks

    Remember that the red LED is on pin0, yellow on pin1, and green on pin2.

    #. Write code so that pressing A turns on the green LED only and pressing B turns on the yellow LED for 3 seconds then turns on the red LED only.
    #. Write code so that pressing A blinks red and yellow 3 times, while pressing B blinks yellow and green 3 times.
    #. Write code to turn on each of the LED's separately with button presses. e.g. button-A turns on red and turns the others off.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Write code so that pressing A turns on the green LED only and pressing B turns on the yellow LED for 3 seconds then turns on the red LED only.

                .. code-block:: python

                    from microbit import *


                    while True:
                        if button_a.is_pressed():
                            pin0.write_digital(0)
                            pin1.write_digital(0)
                            pin2.write_digital(1)
                        elif button_b.is_pressed():
                            pin0.write_digital(0)
                            pin1.write_digital(1)
                            pin2.write_digital(0)
                            sleep(3000)
                            pin0.write_digital(1)
                            pin1.write_digital(0)
                        sleep(500)

            .. tab-item:: Q2

                Write code so that pressing A blinks red and yellow 3 times, while pressing B blinks yellow and green 3 times.

                .. code-block:: python

                    from microbit import *


                    while True:
                        if button_a.is_pressed():
                            for i in range(3):
                                pin0.write_digital(1)
                                pin1.write_digital(1)
                                sleep(1000)
                                pin0.write_digital(0)
                                pin1.write_digital(0)
                                sleep(1000)
                        elif button_b.is_pressed():
                            for i in range(3):
                                pin1.write_digital(1)
                                pin2.write_digital(1)
                                sleep(1000)
                                pin1.write_digital(0)
                                pin2.write_digital(0)
                                sleep(1000)
                        sleep(500)

            .. tab-item:: Q3

                Write code to turn on each of the LED's separately with button presses. e.g. button-A turns on red and turns the others off.

                .. code-block:: python

                    from microbit import *


                    while True:
                        if button_a.is_pressed() and button_b.is_pressed():
                            pin0.write_digital(1)
                            pin1.write_digital(0)
                            pin2.write_digital(0)
                        elif button_a.is_pressed():
                            pin0.write_digital(0)
                            pin1.write_digital(1)
                            pin2.write_digital(0)
                        elif button_b.is_pressed():
                            pin0.write_digital(0)
                            pin1.write_digital(0)
                            pin2.write_digital(1)
                        sleep(500)

----

Write analog
----------------------------------------

| To turn the LED on fully use ``pin0.write_analog(1023)`` for the LED on pin0.
| To turn the LED off use ``pin0.write_analog(0)`` for the LED on pin0.
| ``write_analog`` can have values from 0 to 1023.
| ``write_analog`` can be used to dim the LED.

| Here is some sample code that cycles through a brightness list using ``write_analog`` on pin0.

.. code-block:: python

    from microbit import *

    brightness = [0, 205, 511, 716, 1023]
    sleep_time = 250
    while True:
        if button_a.is_pressed():
            # pulse_on
            for i in brightness:
                pin0.write_analog(i)
                sleep(sleep_time)
            pin0.write_analog(0)
        elif button_b.is_pressed():
            # pulse_off
            for i in brightness:
                pin0.write_analog(1023-i)
                sleep(sleep_time)
            pin0.write_analog(0)
        sleep(500)


| Here is some sample code which pulses the LED on and off.

.. code-block:: python

    from microbit import *


    while True:
        if button_a.is_pressed():
            # pulse_on
            sleep_time = 40
            step_size = 30
            for i in range(0, 1024, step_size):
                pin0.write_analog(i)
                sleep(sleep_time)
            pin0.write_analog(0)
        elif button_b.is_pressed():
            # pulse_off
            sleep_time = 40
            step_size = 30
            for i in range(1023, -1, -step_size):
                pin0.write_analog(i)
                sleep(sleep_time)
            pin0.write_analog(0)
        sleep(500)

----

.. admonition:: Tasks

    #. Modify the code to pulse on and off all 3 LEDs together.
    #. Write code to pulse all 3 LEDs but with an analog difference of about 340, so that when the red LED is at 1023 the yellow is at (1023 - 340) and the green LED is at (1023 - 340 -340).

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to pulse on and off all 3 LEDs together.

                .. code-block:: python

                    from microbit import *


                    while True:
                        if button_a.is_pressed():
                            # pulse_all_on
                            sleep_time = 40
                            step_size = 30
                            for i in range(0, 1024, step_size):
                                pin0.write_analog(i)
                                pin1.write_analog(i)
                                pin2.write_analog(i)
                                sleep(sleep_time)
                        elif button_b.is_pressed():
                            # pulse_all_off
                            sleep_time = 40
                            step_size = 30
                            for i in range(1023, -1, -step_size):
                                pin0.write_analog(i)
                                pin1.write_analog(i)
                                pin2.write_analog(i)
                                sleep(sleep_time)
                        sleep(500)

            .. tab-item:: Q2

                Write code to pulse all 3 LEDs but with an analog difference of about 340, so that when the red LED is at 1023 the yellow is at (1023 - 340) and the green LED is at (1023 - 340 -340).

                .. code-block:: python

                    from microbit import *


                    while True:
                        if button_a.is_pressed():
                            # pulse_all_diff_on
                            sleep_time = 50
                            step_size = 30
                            for i in range(0, 1704, step_size):
                                pin0.write_analog(min(1023, i))
                                pin1.write_analog(max(0, min(1023, i - 340)))
                                pin2.write_analog(max(0, min(1023, i - 680)))
                                sleep(sleep_time)
                        elif button_b.is_pressed():
                            # pulse_all_diff_off
                            sleep_time = 50
                            step_size = 30
                            for i in range(1704, -1, -step_size):
                                pin0.write_analog(min(1023, i))
                                pin1.write_analog(max(0, min(1023, i - 340)))
                                pin2.write_analog(max(0, min(1023, i - 680)))
                                sleep(sleep_time)
                            pin0.write_analog(0)
                        sleep(500)

 ----

.. admonition:: Exercises

    #. Investigate the use of the randrange function for creating random light displays. See: https://www.w3schools.com/python/ref_random_randrange.asp
    #. Investigate the use of the choice function for creating random light displays. Use ``pin_list = [pin0, pin1, pin2]`` to make a list of pins to choose from. See: https://www.w3schools.com/python/ref_random_choice.asp.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                .. code-block:: python

                    from microbit import *
                    import random


                    while True:
                        # random_colors
                        rand_val = random.randrange(0, 1024)
                        rand_pin = random.randrange(0, 3)
                        if rand_pin = 0:
                            pin0.write_analog(rand_val)
                        elif rand_pin = 1:
                            pin1.write_analog(rand_val)
                        elif rand_pin = 2:
                            pin2.write_analog(rand_val)
                        sleep(100)

            .. tab-item:: Q2

                .. code-block:: python

                    from microbit import *
                    import random

                    pin_list = [pin0, pin1, pin2]

                    while True:
                        # random_pin_brightness
                        rand_val = random.randrange(0, 1024)
                        rand_pin = random.choice(pin_list)
                        rand_pin.write_analog(rand_val)
                        sleep(100)




