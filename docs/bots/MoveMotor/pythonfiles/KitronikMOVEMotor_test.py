# Motor tests for KitronikMOVEMotor@2.0.0

from microbit import *
import KitronikMOVEMotor


# setup buggy
buggy = KitronikMOVEMotor.MOVEMotor()
buggy.Stop()
sleep(500)

def straight_line_test():
    # straight line test with smooth start and stop
    # at high speed; decrease_left=5, decrease_right=0
    buggy.Forward(2, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Forward(5, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Forward(9, decrease_left=6, decrease_right=0)
    sleep(1000)
    buggy.Forward(5, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Forward(2, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Stop()
    sleep(500)
    buggy.Reverse(2, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Reverse(5, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Reverse(9, decrease_left=5, decrease_right=0)
    sleep(1000)
    buggy.Reverse(5, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Reverse(2, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Stop()
    sleep(2000)

def individual_motors_test():
    # individal motors
    for i in range(-10, 11, 2):
        buggy.LeftMotor(i)
        sleep(200)
    buggy.Stop()
    for i in range(10, -11, -2):
        buggy.RightMotor(i)
        sleep(200)
    buggy.Stop()
    sleep(2000)

def spin_test():
    buggy.Spin()
    sleep(1000)
    buggy.Spin(2.5)
    sleep(1000)
    buggy.Spin(10)
    sleep(1000)
    buggy.Spin(direction='left')
    sleep(1000)
    buggy.Spin(3, 'right')
    sleep(1000)
    buggy.Stop()
    sleep(2000)

def directions_test():
    buggy.Forward()
    sleep(1000)
    buggy.Reverse()
    sleep(1000)
    buggy.Forward(2.5)
    sleep(1000)
    buggy.Reverse(-2.5)
    sleep(1000)
    buggy.Forward(5)
    sleep(1000)
    buggy.Reverse(2)
    sleep(1000)
    buggy.Left()
    sleep(1000)
    buggy.Left(3)
    sleep(1000)
    buggy.Left(2, 'tight')
    sleep(1000)
    buggy.Left(5, 'wide')
    sleep(1000)
    buggy.Right()
    sleep(1000)
    buggy.Right(3)
    sleep(1000)
    buggy.Right(10, 'standard')
    sleep(1000)
    buggy.Right(tightness='tight')
    buggy.Stop()
    sleep(2000)

while True:
    straight_line_test()
    individual_motors_test()
    spin_test()
    directions_test()
