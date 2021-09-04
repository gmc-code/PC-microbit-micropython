# Motor tests for MOVEMotor module

from microbit import *
import MOVEMotor


# setup buggy
buggy = MOVEMotor.MOVEMotorMotors()
buggy.stop()
sleep(500)


def forward_backward_test():
    # forward(speed=1, duration=None, decrease_left=0, decrease_right=0)
    # backward(speed=1, duration=None, decrease_left=0, decrease_right=0)
    for i in range(2, 11, 1):
        buggy.forward(i, 1000)
        buggy.stop()
        buggy.backward(i, 1000)
        buggy.stop()
    buggy.stop()
    sleep(2000)

def straight_line_test():
    # forward(speed=1, duration=None, decrease_left=0, decrease_right=0)
    # backward(speed=1, duration=None, decrease_left=0, decrease_right=0)
    delta = 5
    buggy.forward(2, 200, delta, 0)
    buggy.forward(5, 200, delta, 0)
    buggy.forward(9, 1000, delta, 0)
    buggy.forward(5, 200, delta, 0)
    buggy.forward(2, 200, delta, 0)
    buggy.stop()
    buggy.backward(2, 200, delta, 0)
    buggy.backward(5, 200, delta, 0)
    buggy.backward(9, 1000, delta, 0)
    buggy.backward(5, 200, delta, 0)
    buggy.backward(2, 200, delta, 0)
    buggy.stop()
    sleep(2000)

def individual_motors_test():
    # left_motor(speed=1, duration=None)
    # right_motor(speed=1, duration=None)
    for i in range(-10, 11, 2):
        buggy.left_motor(i, 300)
    buggy.stop()
    for i in range(10, -11, -2):
        buggy.right_motor(i, 300)
    buggy.stop()
    sleep(2000)

def spin_test():
    # spin(speed=1, direction='left', duration=None)
    for i in range(2, 11, 2):
        buggy.spin(i, 'left', 500)
    buggy.stop()
    for i in range(2, 11, 2):
        buggy.spin(i, 'right', 500)
    buggy.stop()
    sleep(2000)

def turn_test():
    # left(speed=1, radius=25, duration=None)
    # right(speed=1, radius=25, duration=None)
    for i in range(2, 11, 2):
        buggy.left(i, 25, 400)
    buggy.stop()
    for i in range(2, 11, 2):
        buggy.right(i, 25, 400)
    buggy.stop()
    sleep(2000)

def zigzag_test(slow_speed=2, fast_speed=4, zigzag_count=5, zigzag_time=1000):
    for i in range(zigzag_count):
        buggy.left_motor(fast_speed)
        buggy.right_motor(slow_speed)
        sleep(zigzag_time)
        buggy.left_motor(slow_speed)
        buggy.right_motor(fast_speed)
        sleep(zigzag_time)
    for i in range(zigzag_count):
        buggy.left_motor(-slow_speed)
        buggy.right_motor(-fast_speed)
        sleep(zigzag_time)
        buggy.left_motor(-fast_speed)
        buggy.right_motor(-slow_speed)
        sleep(zigzag_time)
        buggy.stop()
        sleep(2000)

def polygon_test(spin_duration=240, sides=20):
    for i in range(sides):
        buggy.forward(3, 800)
        buggy.spin(1, 'left', spin_duration)
    buggy.stop()
    sleep(2000)

def spiral_test():
    for i in [10, 20, 40, 60, 80, 100]:
        buggy.left(3, i, duration=1000)
    buggy.stop()
    sleep(2000)

def oval_test():
    radii = [20, 40, 60, 80, 60, 40]
    durations = [500, 600, 1000, 1000, 1000, 600]
    for i in range(6):
        for r, d in zip(radii, durations):
            buggy.left(3, r, d)
    buggy.stop()
    sleep(2000)

def loops_test():
    radii = [10, 30, 80, 30]
    durations = [2000, 400, 1200, 400]
    for i in range(6):
        for r, d in zip(radii, durations):
            buggy.left(3, r, d)
    buggy.stop()
    sleep(2000)

while True:
    forward_backward_test()
    straight_line_test()
    individual_motors_test()
    spin_test()
    turn_test()
    zigzag_test()
    polygon_test()
    spiral_test()
    oval_test()
    loops_test()
    sleep(5000)
