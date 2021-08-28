====================================================
MoveMotor line follower 2
====================================================

Adding obstacle detection: set up the distance sensor
-------------------------------------------------------

| Add code to use the distance sensor so that, if something blocks the track, the buggy will turn around and go back the other way.

| Set up the buggy's distance sensor.

.. code-block:: python

    distance_sensor = MOVEMotor.MOVEMotorDistanceSensors()

----

Add obstacle detection: spin function
----------------------------------------

| If the distance sensor detects an object with 10 cm the buggy needs to spin around on the track.
| Define ``spin_from_obstacle(spin_time=800)`` so that the buggy spins on the spot. As the left motor goes forward, the right motor reverses.
| Use a default parameter, ``spin_time=800``, which will set the sleep so that the buggy turns about 180 degrees (when the motor speed is the default of 1).


.. code-block:: python

    def spin_from_obstacle(spin_time=800):
        buggy.left_motor(MAXTURN)
        buggy.right_motor(-MAXTURN)
        sleep(spin_time)

----

Add obstacle detection: spin time constant
---------------------------------------------

| Add the ``SPINTIME`` constant to the code with the other constants.
| This will be passed to the ``spin_from_obstacle`` function to set the spin time.

.. code-block:: python

    SPINTIME = 800

----

Add obstacle detection: add to the while True loop
---------------------------------------------------

| Add code to the while True loop to detect any objects within 10cm and spin the buggy if so.

.. code-block:: python

    # check for obstacle and spin and go back
    if distance_sensor.distance() < 10:
        spin_from_obstacle(SPINTIME)

----

Version 2 Code for thin line following with obstacle detection
-------------------------------------------------------------------

.. code-block:: python

    from microbit import *
    import MOVEMotor


    buggy = MOVEMotor.MOVEMotorMotors()
    buggy.stop()
    line_sensor = MOVEMotor.MOVEMotorLineSensors()
    line_sensor.line_sensor_calibrate()
    left_sensor_start = line_sensor.line_sensor_read('left')
    right_sensor_start = line_sensor.line_sensor_read('right')
    distance_sensor = MOVEMotor.MOVEMotorDistanceSensors()

    CHANGETHRESHOLD = 40
    MAXSPEED = 1
    MINTURN = -1
    MAXTURN = 1
    MOTORTIME = 20
    SPINTIME = 800

    def follow_thin_line(drive_time=20):
        left_sensor = line_sensor.line_sensor_read('left')
        right_sensor = line_sensor.line_sensor_read('right')
        black_left = left_sensor + CHANGETHRESHOLD < left_sensor_start
        black_right = right_sensor + CHANGETHRESHOLD < right_sensor_start
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

    def spin_from_obstacle(spin_time=800):
        buggy.left_motor(MAXTURN)
        buggy.right_motor(-MAXTURN)
        sleep(spin_time)

    while True:
        follow_thin_line(MOTORTIME)
        # check for obstacle and spin and go back
        if distance_sensor.distance() < 10:
            spin_from_obstacle(SPINTIME)
        buggy.stop()
        sleep(10)

----

.. admonition:: Tasks

    #. Try adding some obstacles on the track or just to the side of the track to see how well the buggy detects them. 
    #. Try adjusting the SPINTIME constant to see if a better outcomes can be obtained when turning the the buggy away from obstacles. Use the A button to increase SPINTIME by 100 and the B button to decrease SPINTIME by 50.



