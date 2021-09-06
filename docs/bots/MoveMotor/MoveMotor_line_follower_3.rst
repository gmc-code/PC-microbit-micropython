====================================================
MoveMotor line follower 3
====================================================

Adding lights and sound: import modules
-------------------------------------------------------

| Use the LEDs and buzzer.

| Import the music module to use the buzzer.
| Import the neopixel module so it can be referred to simply as ``leds``.

.. code-block:: python

    import music
    from neopixel import NeoPixel as leds

----

Adding lights and sound: set up lights
-------------------------------------------------------

| Set up the Neopixels on pin8 with a length of 4 pixels using the neopixel syntax.
| The constants, LED_PIN and NUM_PIXELS, are used to help remember the neopixel syntax. 
| It would be just as easy to use ``buggy_lights = leds(pin8, 4)``.
| Add constants for the LED colours to use. These have the RGB values for the colours. The ones chosen are subtle. They avoid using the full brightness values up to 255.

.. code-block:: python


    LED_PIN = pin8
    NUM_PIXELS = 4
    buggy_lights = leds(LED_PIN, NUM_PIXELS)
    DULL_WHITE = (20, 20, 20)
    DULL_YELLOW = (35, 25, 0)
    DULL_RED = (20, 0, 0)

----

Adding lights and sound: lights functions
-------------------------------------------------------

| Define ``rear_lights()`` so that it sets the rear lights (index 2 and 3) to red.
| Define ``front_lights(left, right)`` so that it keeps the reuses the rear lights and sets the front left and right lights (index 0 and 1) to the colours passed in place of the ``left`` and ``right`` parameters.
    def left_indicator(): 
| Define ``head_lights()``, ``left_indicator()``, ``right_indicator()``, ``both_indicators()``, so that they use ``front_lights(left, right)`` and specify the front lights to use for each.

.. code-block:: python

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

----

Adding lights and sound: police siren function
-------------------------------------------------------

| Set up the ``police_siren()`` function so that it makes a siren for a short time.
| Use the ``music.pitch`` method playing the siren sounds.

.. py:method::  music.pitch(frequency, duration=-1, pin=microbit.pin0, wait=True)

    | Plays a pitch at the integer frequency given for the specified number of milliseconds.
    | If the frequency is set to 440 and the duration to 1000 then a standard concert A note is played for one second.
    | Note that only one pitch can be played on one pin at any one time.
    | If wait is set to True, this function is blocking.
    | If duration is negative the pitch is played continuously until either the blocking call is interrupted or, in the case of a background call, a new frequency is set or stop is called (see below).

| Use the ``music.pitch`` method in a for-loop in which pith frequency goes up in steps before going down in a second for-loop and then repeated.

.. code-block:: python

    def police_siren():
        for i in range(3):
            for freq in range(1500, 1760, 16):
                music.pitch(freq, 30)
                sleep(20)
            for freq in range(1760, 1500, -16):
                music.pitch(freq, 30)
                sleep(20)

----

Adding lights and sound: start_buggy function
-------------------------------------------------------

| Define the ``start_buggy()`` function below to be used before the while True loop.
| Get the line line sensor readings and display them to make sure that the buggy was over a consistent white surface to start off.
| Turn on front and rear lights using ``head_lights()``.
| Play the police siren.
| Turn on both front indicators as warning lights to place the buggy on a thin line track.

.. code-block:: python

    def start_buggy():
        left_sensor = line_sensor.line_sensor_read('left')
        right_sensor = line_sensor.line_sensor_read('right')
        display.scroll('L' + str(left_sensor), delay=60)
        display.scroll('R' + str(right_sensor), delay=60)
        head_lights()
        police_siren()
        both_indicators()

----

Adding lights and sound: add lights to line following and spin
-----------------------------------------------------------------

| Add lights to line following and spin functions.
| For ``follow_thin_line``, display arrows to indicate the direction the buggy will go and adjust the front lights depending on whether the buggy will go forward, turn or spin.
| For ``spin_from_obstacle``, clear the display and show both front indicators.

.. code-block:: python

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
    
    def spin_from_obstacle(spin_time=800):
        display.show(' ')
        both_indicators()
        buggy.left_motor(MAXTURN)
        buggy.right_motor(-MAXTURN)
        sleep(spin_time)

----

Version 3 Code for thin line following with lights and sound
-----------------------------------------------------------------

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

    CHANGETHRESHOLD = 40
    MAXSPEED = 1
    MINTURN = -1
    MAXTURN = 1
    MOTORTIME = 20
    SPINTIME = 800
    # Setup the Neopixels on pin8 with a length of 4 pixels
    LED_PIN = pin8
    NUM_PIXELS = 4
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
                music.pitch(freq, 30)
                sleep(20)
            for freq in range(1760, 1500, -16):
                music.pitch(freq, 30)
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
        follow_thin_line(MOTORTIME)
        # check for obstacle and spin and go back
        if distance_sensor.distance() < 10:
            spin_from_obstacle(SPINTIME)
        buggy.stop()
        sleep(10)

----

.. admonition:: Tasks

    #. Add siren sounds when the buggy spins to avoid an obstacle.
    #. Add a beep sound when the buggy turns left or right.
    #. Add constants for different LED colours and use them when the buggy spins around.
