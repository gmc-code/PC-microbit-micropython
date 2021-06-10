====================================================
For loops with range
====================================================

PC-Microbit-Micropython documentation!
----------------------------------------

from microbit import *

x = range(6)
while True:
    for n in x:
        display.scroll(n, delay=50)
    sleep(1000)

----

from microbit import *

x = range(1, 5)
while True:
    for n in x:
        display.scroll(n, delay=50)
    sleep(1000)


----


from microbit import *

x = range(1, 6, 2)
while True:
    for n in x:
        display.scroll(n, delay=50)
    sleep(1000)






