# pin_touch_test
from microbit import *

while True:
    if button.a.is_pressed():
        display.show(1)
    elif button.a.is_pressed():
        display.show(2)
    else:
        display.show(3)
    sleep(500)

