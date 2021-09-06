====================================================
MoveMotor line follower 1
====================================================

Set up buggy and sensors
----------------------------------------

| Import the MOVEmotor module and set up the buggy and line sensor.
| Make sure that the buggy is over a consistent white surface so that when the line sensors are calibrated, the left and right line sensors have similar readings.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    buggy = MOVEMotor.MOVEMotorMotors()
    buggy.stop()
    line_sensor = MOVEMotor.MOVEMotorLineSensors()
    line_sensor.line_sensor_calibrate()

----

Set speed constants
----------------------------------------

| Create some constants so that the values can be changed in one place when testing the performance of the buggy.
| Set a ``CHANGETHRESHOLD`` constant to be the minimum change in the line sensor reading when the colour below it is no longer fully white. A value of 40 works seems to work well.
| The buggy should only move slowly so that it doesn't go too far over the black line. Hence the speed settings must be very low. Speeds of 1 work best for the tracks provided.
| Set a ``MAXSPEED`` constant to be the speed for the motors when going straight forward.
| Set a ``MAXTURN`` constant to be the speed for the outside motor on a turn which needs to be greater than the speed of the inside motor.
| Set a ``MINTURN`` constant to be the speed for inside motor on a turn. This is best if it is negative so it goes backward.
| Set a ``MOTORTIME`` constant to be 20 ms for the motors to run before stopping and checking the line sensors again.

.. code-block:: python

    CHANGETHRESHOLD = 40
    MAXSPEED = 1
    MAXTURN = 1
    MINTURN = -1
    MOTORTIME = 20

----

Define follow_thin_line
----------------------------------------

| Define ``follow_thin_line(drive_time=20)`` so that the buggy keeps a thin black line between both line sensors.
| Use a default parameter, ``drive_time=20``, which controls the sleep time during which the motors keep running.
| Get the line sensor readings.
| Set ``black_left`` to True if the left sensor is over part of the black line.
| ``black_left``, which is equal to ``left_sensor + CHANGETHRESHOLD < left_sensorStart``, will be True if the left sensor reading has dropped by more than 40 compared to the original reading when the microbit started.
| Set ``black_right`` to True if the right sensor is over part of the black line.
| ``black_right``, which is equal to ``right_sensor + CHANGETHRESHOLD < right_sensorStart``, will be True if the right sensor reading has dropped by more than 40 compared to the original reading when the microbit started.
| When both line sensors are over white (``not(black_left) and not(black_right)``), the buggy goes forward.
| When the left sensor is over black (``black_left and not(black_right)``), the buggy turns to the left to try to get the left line sensor back over white.
| When the right sensor is over black (``black_right and not(black_left)``), the buggy turns to the right to try to get the right line sensor back over white.
| When both line sensors are over black (``black_left and black_right``), the buggy spins to try to make just one sensor over black.


.. code-block:: python

    def follow_thin_line(drive_time=20):
        left_sensor = line_sensor.line_sensor_read('left')
        right_sensor = line_sensor.line_sensor_read('right')
        black_left = left_sensor + CHANGETHRESHOLD < left_sensorStart
        black_right = right_sensor + CHANGETHRESHOLD < right_sensorStart
        if not(black_left) and not(black_right):
            buggy.left_motor(MAXSPEED)
            buggy.right_motor(MAXSPEED)
        elif black_left and not(black_right):
            buggy.left_motor(MINTURN)
            buggy.right_motor(MAXTURN)
        elif black_right and not(black_left):
            buggy.left_motor(MAXTURN)
            buggy.right_motor(MINTURN)
        else:
            buggy.left_motor(MAXTURN)
            buggy.right_motor(-MAXTURN)
        sleep(drive_time)

----

while True loop
----------------------------------------

| The while True loop does the line following for MOTORTIME ms then stops both motors and then pauses for a short sleep of 10 ms.

.. code-block:: python

    while True:
        follow_thin_line(MOTORTIME)
        buggy.stop()
        sleep(10)

----

Version 1 Code for thin line following
----------------------------------------

| Below is the basic code for thin line following.

.. code-block:: python

    from microbit import *
    import MOVEMotor


    buggy = MOVEMotor.MOVEMotorMotors()
    buggy.stop()
    line_sensor = MOVEMotor.MOVEMotorLineSensors()
    line_sensor.line_sensor_calibrate()
    left_sensorStart = line_sensor.line_sensor_read('left')
    right_sensorStart = line_sensor.line_sensor_read('right')

    CHANGETHRESHOLD = 40
    MAXSPEED = 1
    MINTURN = -1
    MAXTURN = 1
    MOTORTIME = 20

    def follow_thin_line(drive_time=20):
        left_sensor = line_sensor.line_sensor_read('left')
        right_sensor = line_sensor.line_sensor_read('right')
        black_left = left_sensor + CHANGETHRESHOLD < left_sensorStart
        black_right = right_sensor + CHANGETHRESHOLD < right_sensorStart
        if not(black_left) and not(black_right):
            buggy.left_motor(MAXSPEED)
            buggy.right_motor(MAXSPEED)
        elif black_left and not(black_right):
            buggy.left_motor(MINTURN)
            buggy.right_motor(MAXTURN)
        elif black_right and not(black_left):
            buggy.left_motor(MAXTURN)
            buggy.right_motor(MINTURN)
        else:
            buggy.left_motor(MAXTURN)
            buggy.right_motor(-MAXTURN)
        sleep(drive_time)

    while True:
        follow_thin_line(MOTORTIME)
        buggy.stop()
        sleep(10)


----

.. admonition:: Tasks

    #. Try adjusting the constants to see if the performance of the buggy can be improved. Can a faster motor speed be used and still keep the buggy on the track around corners?
    #. Try adjusting the MOTORTIME to see if the performance of the buggy can be improved. Use the A button to increase MOTORTIME by 10 and the B button to decrease MOTORTIME by 5.
    #. Try adjusting the MAXSPEED to see if the performance of the buggy can be improved. Use the A button to increase MAXSPEED by 1 and the B button to decrease MAXSPEED by 0.5.


