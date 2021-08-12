# Motor tests for MOVEMotor module

from microbit import *
import MOVEMotor


# setup buggy
buggy = MOVEMotor.MOVEMotor_motors()
buggy.stop()
sleep(500)

def straight_line_test():
    # straight line test with smooth start and stop
    inc = 5
    buggy.forward(2, decrease_left=inc, decrease_right=0)
    sleep(200)
    buggy.forward(5, decrease_left=inc, decrease_right=0)
    sleep(200)
    buggy.forward(9, decrease_left=inc, decrease_right=0)
    sleep(1000)
    buggy.forward(5, decrease_left=inc, decrease_right=0)
    sleep(200)
    buggy.forward(2, decrease_left=inc, decrease_right=0)
    sleep(200)
    buggy.stop()
    sleep(500)
    buggy.backward(2, decrease_left=inc, decrease_right=0)
    sleep(200)
    buggy.backward(5, decrease_left=inc, decrease_right=0)
    sleep(200)
    buggy.backward(9, decrease_left=inc, decrease_right=0)
    sleep(1000)
    buggy.backward(5, decrease_left=inc, decrease_right=0)
    sleep(200)
    buggy.backward(2, decrease_left=inc, decrease_right=0)
    sleep(200)
    buggy.stop()
    sleep(2000)

def individual_motors_test():
    # individal motors
    for i in range(-10, 11, 2):
        buggy.left_motor(i)
        sleep(200)
    buggy.stop()
    for i in range(10, -11, -2):
        buggy.right_motor(i)
        sleep(200)
    buggy.stop()
    sleep(2000)

def spin_test():
    buggy.spin()
    sleep(1000)
    buggy.spin(2.5)
    sleep(1000)
    buggy.spin(10)
    sleep(1000)
    buggy.spin(direction='left')
    sleep(1000)
    buggy.spin(3, 'right')
    sleep(1000)
    buggy.stop()
    sleep(2000)

def forward_backward_test():
    buggy.forward()
    sleep(1000)
    buggy.backward()
    sleep(1000)
    buggy.forward(2.5)
    sleep(1000)
    buggy.backward(5)
    sleep(1000)
    buggy.stop()
    sleep(2000)

def turn_test():
    buggy.left()
    sleep(1000)
    buggy.left(3)
    sleep(1000)
    buggy.right(3)
    sleep(1000)
    buggy.right()
    sleep(1000)
    buggy.left(radius=25)
    sleep(1000)
    buggy.left(2, radius=25)
    sleep(1000)
    buggy.left(3, 25)
    sleep(1000)
    buggy.right(radius=25)
    sleep(1000)
    buggy.right(2, radius=25)
    sleep(1000)
    buggy.right(3, 25)
    sleep(1000)
    buggy.stop()
    sleep(2000)

def spiral_test():
    for i in [10, 20, 40, 60, 80, 100]:
        buggy.left(5, i)
        sleep(3000)
    buggy.stop()
    sleep(2000)

def polygon_test():
    for i in range(13):
        buggy.forward(3)
        sleep(800)
        buggy.spin(1)
        sleep(320)
    buggy.stop()
    sleep(2000)

def oval_test():
    dist = [20, 60, 70, 80, 70, 60]
    tdist = [200, 200, 400, 500, 400, 200]
    for i in range(6):
        for d, t in zip(dist, tdist):
            buggy.left(5, d)
            sleep(2 * t)
    buggy.stop()
    sleep(2000)


def loops_test():
    dist = [10, 30, 80, 30]
    tdist = [1000, 200, 600, 200]
    for i in range(6):
        for d, t in zip(dist, tdist):
            buggy.left(5, d)
            sleep(2 * t)
    buggy.stop()
    sleep(2000)


while True:
    straight_line_test()
    individual_motors_test()
    spin_test()
    forward_backward_test()
    turn_test()
    spiral_test()
    polygon_test()
    loops_test()
