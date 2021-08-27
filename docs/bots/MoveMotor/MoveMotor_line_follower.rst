====================================================
MoveMotor line follower
====================================================

Track templates
----------------------------------------

| The track templates have various track segments that can be cut out to make a line following track.
| For a track with a thin line download the word file :download:`MOVEMotor.py module <files/linefollowtiles -thin.docx>`.
| For a track with a thick line download the word file :download:`MOVEMotor.py module <files/linefollowtiles -thick.docx>`.


Line following code
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
    leftSensorStart = line_sensor.line_sensor_read('left')
    rightSensorStart = line_sensor.line_sensor_read('right')
    distance_sensor = MOVEMotor.MOVEMotorDistanceSensors()

    calflag = True
    thin_line_follow_flag = True
    CHANGETHRESHOLD = 40
    MAXSPEED = 2
    MINTURN = -1
    MAXTURN = 1
    # Setup the Neopixels on pin8 with a length of 4 pixels
    NUM_PIXELS = 4
    LED_PIN = pin8
    buggyLights = leds(LED_PIN, NUM_PIXELS)
    DULL_WHITE = (20, 20, 20)
    DULL_YELLOW = (35, 25, 0)
    DULL_RED = (20, 0, 0)

    def rear_lights():
        buggyLights[2] = DULL_RED
        buggyLights[3] = DULL_RED

    def front_lights(left, right):
        buggyLights[0] = left
        buggyLights[1] = right
        rear_lights()
        buggyLights.show()

    def head_lights():
        front_lights(DULL_WHITE, DULL_WHITE)

    def left_indicator():
        front_lights(DULL_YELLOW, DULL_WHITE)

    def right_indicator():
        front_lights(DULL_WHITE, DULL_YELLOW)

    def both_indicator():
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
        leftSensor = line_sensor.line_sensor_read('left')
        rightSensor = line_sensor.line_sensor_read('right')
        blackleft = leftSensor + CHANGETHRESHOLD < leftSensorStart
        blackright = rightSensor + CHANGETHRESHOLD < rightSensorStart
        if not(blackleft) and not(blackright):
            display.show(Image.ARROW_N)
            head_lights()
            buggy.left_motor(MAXSPEED)
            buggy.right_motor(MAXSPEED)
        elif blackleft and not(blackright):
            display.show(Image.ARROW_W)
            left_indicator()
            buggy.left_motor(MINTURN)
            buggy.right_motor(MAXTURN)
        elif blackright and not(blackleft):
            display.show(Image.ARROW_E)
            right_indicator()
            buggy.left_motor(MAXTURN)
            buggy.right_motor(MINTURN)
        else:
            display.show(' ')
            both_indicator()
            buggy.left_motor(MAXTURN)
            buggy.right_motor(-MAXTURN)

    def follow_thick_line():
        leftSensor = line_sensor.line_sensor_read('left')
        rightSensor = line_sensor.line_sensor_read('right')
        blackleft = leftSensor + CHANGETHRESHOLD < leftSensorStart
        blackright = rightSensor + CHANGETHRESHOLD < rightSensorStart
        if not(blackleft) and not(blackright):
            display.show(' ')
            both_indicator()
            buggy.left_motor(MAXTURN)
            buggy.right_motor(-MAXTURN)
        elif blackleft and not(blackright):
            display.show(Image.ARROW_E)
            left_indicator()
            buggy.left_motor(MINTURN)
            buggy.right_motor(MAXTURN)
        elif blackright and not(blackleft):
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
            both_indicator()
            buggy.left_motor(MAXTURN)
            buggy.right_motor(-MAXTURN)


    while True:
        sleep(20)
        buggy.stop_left()
        buggy.stop_right()
        sleep(10)
        if calflag:
            leftSensor = line_sensor.line_sensor_read('left')
            rightSensor = line_sensor.line_sensor_read('right')
            display.scroll('L' + str(leftSensor), delay=60)
            display.scroll('R' + str(rightSensor), delay=60)
            head_lights()
            police_siren()
            both_indicator()
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

