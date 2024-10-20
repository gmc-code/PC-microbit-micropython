================================================================
Organising code with definitions for the Breadboard
================================================================

Code comparison
----------------------------------

| Write code that displays a message "A or B".
| When A is pressed, turn on the motor on pin 0 for 3 sec.
| When B is pressed, turn on the LED on pin 1 for 1 sec at full brightness,
| then 1 sec at half brightness.

.. list-table::
   :widths: 50 50
   :header-rows: 1
   :width: 100%

   * - code in sequence without definitions
     - code organised with definitions
   * - .. code-block:: python

           from microbit import *

           display.scroll('A or B')

           while True:
               if button_a.is_pressed():
                   # on pin 0
                   pin0.write_digital(1)
                   sleep(3000)
                   pin0.write_digital(0)
               elif button_b.is_pressed():
                   # on pin 1
                   pin1.write_digital(1)
                   sleep(1000)
                   pin1.write_analog(511)
                   sleep(1000)
                   pin1.write_digital(0)
               sleep(100)

     - .. code-block:: python

           from microbit import *

           def display_startup_message():
               display.scroll('A or B')

           def use_motor_A():
               # on pin 0
               pin0.write_digital(1)
               sleep(3000)
               pin0.write_digital(0)

           def use_LEDs_B():
               # on pin 1
               pin1.write_digital(1)
               sleep(1000)
               pin1.write_analog(511)
               sleep(1000)
               pin1.write_digital(0)

           display_startup_message()

           while True:
               if button_a.is_pressed():
                   use_motor_A()
               elif button_b.is_pressed():
                   use_LEDs_B()
               sleep(100)
