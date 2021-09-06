====================================================
Maqueen info
====================================================

| See: https://wiki.dfrobot.com/micro_Maqueen_for_micro_bit_SKU_ROB0148-E
| See: https://edu.dfrobot.com/makelog-308323.html

| The DFRobot micro: Maqueen has 2 independent motors, 2 infrared line sensors for line tracking, distance sensors for obstacle avoidance, 4 ZIP Leds and a buzzer, all powered by 3 AAA batteries. 
| The servo outputs and infrared sensor on pin16 are not used here.


.. image:: images/Maqueen.png
    :scale: 50 %
    :align: center

| Dimensions 81mm x 85 mm x 44mm

Pins
---------

The pin numbers used to control different parts are below.

=======  ===========================
 Pin     Purpose
=======  ===========================
 pin0    Buzzer
 pin1    Ultrasonic Trigger
 pin2    Ultrasonic Echo
 pin8    Left Red LED
 pin12   Right Red LED
 pin13   Left Line Follow (IR)
 pin14   Right Line Follow (IR)
 pin15   4x LEDs
 pin16   InfraRed
 pin19   Motor (via I2C)
 pin20   Motor (via I2C)

=======  ===========================

Servo Connection is also by I2C
