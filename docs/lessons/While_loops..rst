====================================================
While_loops
====================================================

PC-Microbit-Micropython documentation!
----------------------------------------


from microbit import *

while True:
    a = 2
    while a < 4:
        b = 1
        while b < 10:
            display.scroll(a * b, delay=50)
            b += 1
        a += 1

