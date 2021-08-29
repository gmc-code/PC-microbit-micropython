====================================================
MoveMotor line follower 4
====================================================

Add thick line following: follow_thick_line function
------------------------------------------------------

| Add code to follow a wide thick black track.
| Define ``follow_thick_line(drive_time=20)``
| Base this on the thin line following code.
| Modify the if and elif code to keep the buggy over the black track.
| When both line sensors are over white (``not(black_left) and not(black_right)``), the buggy spins to try to make just one sensor over black.
| When the left sensor is over black but the right is over white (``black_left and not(black_right)``), the buggy turns to the left to try to get the right line sensor back over black.
| When the right sensor is over black but the left is over white (``black_right and not(black_left)``), the buggy turns to the right to try to get the left line sensor back over black.
| When both line sensors are over black (``black_left and black_right``), the buggy the buggy goes forward.

.. code-block:: python

    def follow_thick_line(drive_time=20):
        left_sensor = line_sensor.line_sensor_read('left')
        right_sensor = line_sensor.line_sensor_read('right')
        black_left = left_sensor + CHANGETHRESHOLD < left_sensor_start
        black_right = right_sensor + CHANGETHRESHOLD < right_sensor_start
        if not(black_left) and not(black_right):
            display.show(' ')
            both_indicators()
            buggy.left_motor(-MAXTURN)
            buggy.right_motor(-MAXTURN)
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
            display.show(Image.ARROW_N)
            head_lights()
            buggy.left_motor(MAXSPEED)
            buggy.right_motor(MAXSPEED)
        sleep(drive_time)

----

Add thick line following: modify while True
------------------------------------------------------

| Add to the section of code where the constants are set, to include a boolean variable, ``thin_line_follow_flag``, which is True if the buggy follows a thin line or False if the buggy follows a thick line.
| Set ``thin_line_follow_flag = True`` to cause thin line following as the default.

.. code-block:: python

    thin_line_follow_flag = True


----

Add thick line following: modify the while True loop
------------------------------------------------------

| Add button pressing to change the line following mode.
| Use the A button to set the buggy to follow a thin line by setting ``thin_line_follow_flag`` to True.
| Use the B button to set the buggy to follow a thick line by setting ``thin_line_follow_flag`` to False.
| Add the if-else block to set teh line following mode based on ``thin_line_follow_flag``.

.. code-block:: python

    while True:
        if button_a.is_pressed() and not button_b.is_pressed():
            display.scroll('A', delay=100)
            thin_line_follow_flag = True
        elif button_b.is_pressed() and not button_a.is_pressed():
            display.scroll('B', delay=100)
            thin_line_follow_flag = False
        if thin_line_follow_flag:
            follow_thin_line(MOTORTIME)
        else:
            follow_thick_line(MOTORTIME)

----

Version 4 Line following code in full
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

    thin_line_follow_flag = True
    CHANGETHRESHOLD = 40
    MAXSPEED = 1
    MINTURN = -1
    MAXTURN = 1
    MOTORTIME = 20
    SPINTIME = 800
    # Set up the Neopixels on pin8 with a length of 4 pixels
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

    def follow_thin_line(drive_time=20):
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
        sleep(drive_time)
        
    def follow_thick_line(drive_time=20):
        left_sensor = line_sensor.line_sensor_read('left')
        right_sensor = line_sensor.line_sensor_read('right')
        black_left = left_sensor + CHANGETHRESHOLD < left_sensor_start
        black_right = right_sensor + CHANGETHRESHOLD < right_sensor_start
        if not(black_left) and not(black_right):
            display.show(' ')
            both_indicators()
            buggy.left_motor(-MAXTURN)
            buggy.right_motor(-MAXTURN)
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
            display.show(Image.ARROW_N)
            head_lights()
            buggy.left_motor(MAXSPEED)
            buggy.right_motor(MAXSPEED)
        sleep(drive_time)

    def spin_from_obstacle(spin_time=800):
        display.show(' ')
        both_indicators()
        buggy.left_motor(MAXTURN)
        buggy.right_motor(-MAXTURN)
        sleep(spin_time)
        
    def start_buggy():
        left_sensor = line_sensor.line_sensor_read('left')
        right_sensor = line_sensor.line_sensor_read('right')
        display.scroll('L' + str(left_sensor), delay=60)
        display.scroll('R' + str(right_sensor), delay=60)
        head_lights()
        police_siren()
        both_indicators()

    start_buggy()
    while True:
        if button_a.is_pressed() and not button_b.is_pressed():
            display.scroll('A', delay=100)
            thin_line_follow_flag = True
        elif button_b.is_pressed() and not button_a.is_pressed():
            display.scroll('B', delay=100)
            thin_line_follow_flag = False
        if thin_line_follow_flag:
            follow_thin_line(MOTORTIME)
        else:
            follow_thick_line(MOTORTIME)
        # check for obstacle and spin and go back
        if distance_sensor.distance() < 10:
            spin_from_obstacle(SPINTIME)
        buggy.stop()
        sleep(10)



----

.. admonition:: Tasks

    #. Set up a thin line track and a thick line track and switch the buggy from one track to the other using button pressing.
    #. Use the track templates to create identically shaped thin and thick tracks and time the buggy on each to find out which track it is better at following.



