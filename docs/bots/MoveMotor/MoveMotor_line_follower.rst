====================================================
MoveMotor line follower
====================================================

Track templates
----------------------------------------

| The track templates have various track segments that can be cut out to make a line following track.

Thin line track
~~~~~~~~~~~~~~~~~~~~~

| For a track with a thin line download the word file :download:`linefollowtiles -thin.docx <files/linefollowtiles -thin.docx>`.
| The buggy can be placed with the **thin** line up the middle of it so that the line sensors are over **white** paper either side of the black line. When a line sensor comes over the black line, that side needs to turn away from the line before it crosses it.

Thick track
~~~~~~~~~~~~~~~~~~~~~

| For a track with a thick line download the word file :download:`linefollowtiles -thick.docx <files/linefollowtiles -thick.docx>`.
| The buggy can be placed over the **thick** track so that the line sensors are over **black** paper. When a line sensor comes over the white surrounding paper, that side needs to turn away from the track edge back into the black area.


Set up buggy and sensors
----------------------------------------

| Import the MOVEmotor module and setup the buggy and line sensor.
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
| Set a ``CHANGETHRESHOLD`` constant to be the minimum change in the line sensor reading when the colour below it is no longer full white. A value of 40 works seems to work well.
| The buggy should only move slowly so that it doesn't go too far over the black line. Hence the speed settings must be very low.
| Set a ``MAXSPEED`` constant to be the speed for the motors when going straight forward.
| Set a ``MAXTURN`` constant to be the speed for the outside motor on a turn which needs to be greater than the speed of the inside motor.
| Set a ``MINTURN`` constant to be the speed for inside motor on a turn. This is best if it is negative so it goes backwards.

.. code-block:: python

    CHANGETHRESHOLD = 40
    MAXSPEED = 1
    MAXTURN = 1
    MINTURN = -1

----

Define follow_thin_line
----------------------------------------

| Define ``follow_thin_line()`` so that the buggy keeps a thin black line between both line sensors.
| Get the line sensor readings.
| Set ``black_left`` to True if the left sensor is over part of the black line.
| ``black_left``, which is equal to ``left_sensor + CHANGETHRESHOLD < left_sensorStart``, will be True if the left sensor reading has dropped by more than 40 compared to the original reading when it was flashed the code.
| Set ``black_right`` to True if the right sensor is over part of the black line.
| When both line sensors are over white, the buggy goes forward.
| When the left sensor is over black, the buggy turns to the left to try to get the left line sensor back over white.
| When the right sensor is over black, the buggy turns to the right to try to get the right line sensor back over white.
| When both line sensors are over black, the buggy spins to try to make just one sensor over black.


.. code-block:: python

    def follow_thin_line():
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

----

while True loop
----------------------------------------

| The while True loop first stops both motors then does the line following for 20ms.

.. code-block:: python

    while True:
        buggy.stop()
        sleep(10)
        follow_thin_line()
        sleep(20)

----

Code for thin line following
----------------------------------------

| Define ``follow_thin_line()`` so that teh buggy keeps a thin black line between both line sensors.

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

    def follow_thin_line():
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

    while True:
        buggy.stop()
        sleep(10)
        follow_thin_line()
        sleep(20)


----

Line following code in full
----------------------------------------

| The code below will follow both the thin line track that goes between the line sensors or the thick line track that both sensors sit over.

.. code-block:: python

    from microbit import *
    import music
    from neopixel import NeoPixel as leds
    import MOVEMotor


    buggy = MOVEMotor.MOVEMotorMotors()
    buggy.stop()
    line_sensor = MOVEMotor.MOVEMotorLineSensors()
    line_sensor.line_sensor_calibrate()
    left_sensor_start = line_sensor.line_sensor_read('left')
    right_sensor_start = line_sensor.line_sensor_read('right')
    distance_sensor = MOVEMotor.MOVEMotorDistanceSensors()

    calflag = True
    thin_line_follow_flag = True
    CHANGETHRESHOLD = 40
    MAXSPEED = 1
    MINTURN = -1
    MAXTURN = 1
    # Setup the Neopixels on pin8 with a length of 4 pixels
    NUM_PIXELS = 4
    LED_PIN = pin8
    buggy_lights = leds(LED_PIN, NUM_PIXELS)
    DULL_WHITE = (20, 20, 20)
    DULL_YELLOW = (35, 25, 0)
    DULL_RED = (20, 0, 0)

    def rear_lights():
        buggy_lights[2] = DULL_RED
        buggy_lights[3] = DULL_RED

    def front_lights(left, right):
        buggy_lights[0] = left
        buggy_lights[1] = right
        rear_lights()
        buggy_lights.show()

    def head_lights():
        front_lights(DULL_WHITE, DULL_WHITE)

    def left_indicator():
        front_lights(DULL_YELLOW, DULL_WHITE)

    def right_indicator():
        front_lights(DULL_WHITE, DULL_YELLOW)

    def both_indicators():
        front_lights(DULL_YELLOW, DULL_YELLOW)

    def police_siren():
        for i in range(3):
            for freq in range(1500, 1760, 16):
                music.pitch(freq, 30, wait=False)
                sleep(20)
            for freq in range(1760, 1500, -16):
                music.pitch(freq, 30, wait=False)
                sleep(20)

    def follow_thin_line():
        left_sensor = line_sensor.line_sensor_read('left')
        right_sensor = line_sensor.line_sensor_read('right')
        black_left = left_sensor + CHANGETHRESHOLD < left_sensor_start
        black_right = right_sensor + CHANGETHRESHOLD < right_sensor_start
        if not(black_left) and not(black_right):
            display.show(Image.ARROW_N)
            head_lights()
            buggy.left_motor(MAXSPEED)
            buggy.right_motor(MAXSPEED)
        elif black_left and not(black_right):
            display.show(Image.ARROW_W)
            left_indicator()
            buggy.left_motor(MINTURN)
            buggy.right_motor(MAXTURN)
        elif black_right and not(black_left):
            display.show(Image.ARROW_E)
            right_indicator()
            buggy.left_motor(MAXTURN)
            buggy.right_motor(MINTURN)
        else:
            display.show(' ')
            both_indicators()
            buggy.left_motor(MAXTURN)
            buggy.right_motor(-MAXTURN)

    def follow_thick_line():
        left_sensor = line_sensor.line_sensor_read('left')
        right_sensor = line_sensor.line_sensor_read('right')
        black_left = left_sensor + CHANGETHRESHOLD < left_sensor_start
        black_right = right_sensor + CHANGETHRESHOLD < right_sensor_start
        if not(black_left) and not(black_right):
            display.show(' ')
            both_indicators()
            buggy.left_motor(MAXTURN)
            buggy.right_motor(-MAXTURN)
        elif black_left and not(black_right):
            display.show(Image.ARROW_E)
            left_indicator()
            buggy.left_motor(MINTURN)
            buggy.right_motor(MAXTURN)
        elif black_right and not(black_left):
            display.show(Image.ARROW_W)
            right_indicator()
            buggy.left_motor(MAXTURN)
            buggy.right_motor(MINTURN)
        else:
            display.show(Image.ARROW_N)
            head_lights()
            buggy.left_motor(MAXSPEED)
            buggy.right_motor(MAXSPEED)

    def spin_from_obstacle():
        display.show(' ')
        both_indicators()
        buggy.left_motor(MAXTURN)
        buggy.right_motor(-MAXTURN)


    while True:
        sleep(20)
        buggy.stop_left()
        buggy.stop_right()
        sleep(10)
        if calflag:
            left_sensor = line_sensor.line_sensor_read('left')
            right_sensor = line_sensor.line_sensor_read('right')
            display.scroll('L' + str(left_sensor), delay=60)
            display.scroll('R' + str(right_sensor), delay=60)
            head_lights()
            police_siren()
            both_indicators()
            calflag = False
        else:
            if button_a.is_pressed() and not button_b.is_pressed():
                display.scroll('A', delay=100)
                thin_line_follow_flag = True
            elif button_b.is_pressed() and not button_a.is_pressed():
                display.scroll('B', delay=100)
                thin_line_follow_flag = False
            if thin_line_follow_flag:
                follow_thin_line()
            else:
                follow_thick_line()
            # check for obstacle and spin and go back
            if distance_sensor.distance() < 10:
                spin_from_obstacle()
                sleep(800)




----

.. admonition:: Tasks

    #. Write code to read the right line sensor and display its value.
    #. Write code to read both the left and the right line sensor and display their values with 'L' before the left reading and 'R' before the right reading.

