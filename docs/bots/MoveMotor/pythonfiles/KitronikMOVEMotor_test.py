# Motor tests for KitronikMOVEMotor@2.0.0

from microbit import *
import KitronikMOVEMotor


# setup buggy
buggy = KitronikMOVEMotor.MOVEMotor()
buggy.Stop()
sleep(500)
pause = 1000
while True:
    display.show(6)
    # decrease_left=0, decrease_right=0
    buggy.Forward(2, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Forward(5, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Forward(9, decrease_left=6, decrease_right=0)
    sleep(3000)
    buggy.Forward(5, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Forward(2, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Stop()
    display.show(5)
    sleep(500)
    buggy.Reverse(2, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Reverse(5, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Reverse(9, decrease_left=5, decrease_right=0)
    sleep(3000)
    buggy.Reverse(5, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Reverse(2, decrease_left=0, decrease_right=0)
    sleep(200)
    buggy.Stop()
    sleep(5000)

while True:
    for i in range(0, 11, 2):
        buggy.LeftMotor(i)
        buggy.RightMotor(i)
        sleep(200)
    for i in range(10, 0, -2):
        buggy.LeftMotor(i)
        buggy.RightMotor(i)
        sleep(200)
    buggy.Forward(9)
    sleep(pause)
    buggy.Reverse(5)
    sleep(pause)
    buggy.Spin(1, 'left')

    sleep(pause)
    buggy.Spin(3, 'right')
    sleep(pause)
    buggy.Left(2, 'tight')
    sleep(pause)
    buggy.Left(4)
    sleep(pause)
    buggy.Right(6, 'wide')
    sleep(pause)
    buggy.Stop()
    sleep(pause)
