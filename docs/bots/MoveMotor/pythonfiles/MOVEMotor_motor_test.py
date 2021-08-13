# Motor tests for MOVEMotor module

from microbit import *
import MOVEMotor


# setup buggy
buggy = MOVEMotor.MOVEMotorMotors()
buggy.stop()
sleep(500)

def straight_line_test():
    # straight line test with smooth start and stop
    delta = 5
    buggy.forward(2, duration=200, decrease_left=delta, decrease_right=0)
    buggy.forward(5, duration=200, decrease_left=delta, decrease_right=0)
    buggy.forward(9, duration=600, decrease_left=delta, decrease_right=0)
    buggy.forward(5, duration=200, decrease_left=delta, decrease_right=0)
    buggy.forward(2, duration=200, decrease_left=delta, decrease_right=0)
    buggy.stop()
    buggy.backward(2, 200, delta, 0)
    buggy.backward(5, 200, delta, 0)
    buggy.backward(9, 1000, delta, 0)
    buggy.backward(5, 200, delta, 0)
    buggy.backward(2, 200, delta, 0)
    buggy.stop()
    sleep(2000)

def individual_motors_test():
    # individal motors
    for i in range(-10, 11, 2):
        buggy.left_motor(i, 200)
    buggy.stop()
    for i in range(10, -11, -2):
        buggy.right_motor(i, 200)
    buggy.stop()
    sleep(2000)

def spin_test():
    # speed=1, direction='left', duration=None)
    buggy.spin(duration=1000)
    buggy.spin(2.5, duration=1000)
    buggy.spin(10, duration=1000)
    buggy.spin(duration=1000, direction='left')
    buggy.spin(3, 'right', 1000)
    buggy.stop()
    sleep(2000)

def forward_backward_test():
    buggy.forward(duration=1000)
    buggy.backward(duration=1000)
    buggy.forward(2.5, 1000)
    buggy.backward(5, 1000)
    buggy.stop()
    sleep(2000)

def turn_test():
    buggy.left(duration=1000)
    buggy.left(3, duration=1000)
    buggy.right(3, duration=1000)
    buggy.right(duration=1000)
    buggy.left(radius=25, duration=1000)
    buggy.left(2, radius=25, duration=1000)
    buggy.left(3, 25, 1000)
    buggy.right(radius=25, duration=1000)
    buggy.right(2, radius=25, duration=1000)
    buggy.right(3, 25, 1000)
    buggy.stop()
    sleep(2000)

def spiral_test():
    for i in [10, 20, 40, 60, 80, 100]:
        buggy.left(5, i, duration=1000)
    buggy.stop()
    sleep(2000)

def polygon_test():
    for i in range(13):
        buggy.forward(3, 800)
        buggy.spin(1, 'left', 320)
    buggy.stop()
    sleep(2000)

def oval_test():
    dist = [20, 60, 70, 80, 70, 60]
    tdist = [400, 400, 800, 1000, 800, 400]
    for i in range(6):
        for d, t in zip(dist, tdist):
            buggy.left(5, d, t)
    buggy.stop()
    sleep(2000)

def loops_test():
    dist = [10, 30, 80, 30]
    tdist = [2000, 400, 1200, 400]
    for i in range(6):
        for d, t in zip(dist, tdist):
            buggy.left(5, d, t)
    buggy.stop()
    sleep(2000)

def duration_none_test():
    buggy.forward(duration=None)
    sleep(1000)
    buggy.stop()
    sleep(1000)
    buggy.backward(duration=None)
    sleep(1000)
    buggy.stop()
    sleep(1000)
    buggy.left(duration=None)
    sleep(1000)
    buggy.stop()
    sleep(1000)
    buggy.right(duration=None)
    sleep(1000)
    buggy.stop()
    sleep(1000)
    buggy.spin(duration=None)
    sleep(1000)
    buggy.stop()
    sleep(2000)

sleep(5000)
straight_line_test()
individual_motors_test()
spin_test()
forward_backward_test()
turn_test()
spiral_test()
polygon_test()
oval_test()
loops_test()
duration_none_test()
