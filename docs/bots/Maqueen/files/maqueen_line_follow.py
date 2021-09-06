# line follow with lights and buzzer
from microbit import *
import music
import maqueen


buggy = maqueen.MaqueenMotors()
buggy.stop()
line_sensor = maqueen.MaqueenLineSensors()
distance_sensor = maqueen.MaqueenDistanceSensors()
headlights = maqueen.MaqueenHeadLights()
leds = maqueen.MaqueenNeoPixels()

MAXSPEED = 3
MINTURN = 0
MAXTURN = 3
MOTORTIME = 20
SPINTIME = 530

def police_siren():
    for i in range(3):
        for freq in range(1500, 1760, 16):
            music.pitch(freq, 30, wait=False)
            sleep(20)
        for freq in range(1760, 1500, -16):
            music.pitch(freq, 30, wait=False)
            sleep(20)

def follow_thick_line(drive_time=20):
    # stay on black track; turn away from white
    left_sensor = line_sensor.line_sensor_read('left')
    right_sensor = line_sensor.line_sensor_read('right')
    black_left = (left_sensor == 0)
    black_right = (right_sensor == 0)
    if not(black_left) and not(black_right):
        display.show(' ')
        leds.both_indicators()
        headlights.set_headlights(left=1, right=1)
        buggy.left_motor(-MAXTURN)
        buggy.right_motor(-MAXTURN)
    elif black_left and not(black_right):
        display.show(Image.ARROW_E)
        leds.left_indicator()
        headlights.set_headlights(left=1, right=0)
        buggy.left_motor(MINTURN)
        buggy.right_motor(MAXTURN)
    elif black_right and not(black_left):
        display.show(Image.ARROW_W)
        leds.right_indicator()
        headlights.set_headlights(left=0, right=1)
        buggy.left_motor(MAXTURN)
        buggy.right_motor(MINTURN)
    else:
        # black_right and black_left
        display.show(Image.ARROW_N)
        leds.front_lights()
        headlights.set_headlights(left=0, right=0)
        buggy.left_motor(MAXSPEED)
        buggy.right_motor(MAXSPEED)
    sleep(drive_time)

def spin_from_obstacle(spin_time=530):
    display.show(' ')
    leds.both_indicators()
    headlights.set_headlights(left=1, right=1)
    buggy.spin(speed=5, direction='left', duration=spin_time)

def start_buggy():
    headlights.set_headlight(headlight='left', on=1)
    headlights.set_headlight(headlight='right', on=1)
    leds.front_lights()
    police_siren()
    leds.both_indicators()
    left_sensor = line_sensor.line_sensor_read('left')
    right_sensor = line_sensor.line_sensor_read('right')
    display.scroll('L' + str(left_sensor), delay=60)
    display.scroll('R' + str(right_sensor), delay=60)
    headlights.set_headlight(headlight='left', on=0)
    headlights.set_headlight(headlight='right', on=0)

start_buggy()
while True:
    if button_a.is_pressed():
        MAXSPEED = 3
        MINTURN = 0
        MAXTURN = 3
    elif button_b.is_pressed():
        MAXSPEED = 5
        MINTURN = 0
        MAXTURN = 4
    follow_thick_line(MOTORTIME)
    # check for obstacle and spin and go back
    if distance_sensor.distance() < 10:
        spin_from_obstacle(SPINTIME)
    buggy.stop()
    sleep(10)
