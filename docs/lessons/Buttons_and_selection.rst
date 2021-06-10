====================================================
Buttons and selection
====================================================

PC-Microbit-Micropython documentation!
----------------------------------------

# https://microbit-micropython.readthedocs.io/en/latest/tutorials/hello.html
# https://microbit-micropython.readthedocs.io/en/latest/tutorials/buttons.html

# from libraryname import methods, * for everything
from microbit import *

# event loop, infinite, goes without stopping
while True:
    if button_a.is_pressed():
        display.show("A")
    elif button_b.is_pressed():
        display.show("B")
    else:
        display.show("C")

from microbit import *

while True:
    if button_a.is_pressed() and button_b.is_pressed():
        display.show(Image.ARROW_N)
    elif button_a.is_pressed():
        display.show(Image.ARROW_W)
    elif button_b.is_pressed():
        display.show(Image.ARROW_E)
    else:
        display.show(" ")
    sleep(100)
