# line follow with lights and buzzer
from microbit import *
import maqueen


line_sensor = maqueen.MaqueenLineSensors()

def line_sensor_test():
    left_sensor = line_sensor.line_sensor_read('left')
    right_sensor = line_sensor.line_sensor_read('right')
    display.scroll('L' + str(left_sensor), delay=60)
    display.scroll('R' + str(right_sensor), delay=60)
    black_left = (left_sensor == 0)
    black_right = (right_sensor == 0)
    display.scroll('L' + str(black_left), delay=60)
    display.scroll('R' + str(black_right), delay=60)

while True:
    line_sensor_test()
    sleep(200)
