====================================================
For loops
====================================================

PC-Microbit-Micropython documentation!
----------------------------------------


from microbit import *

my_string = 'Hi Mb user'
while True:
    for letter in my_string:
        display.show(letter)
        sleep(200)
    sleep(500)

----

from microbit import *

my_list = [2, 3, 5, 7]
while True:
    for num in my_list:
        display.show(num)
        sleep(300)
        num = num * 2
        display.scroll(num, delay = 50)
        sleep(300)

----

from microbit import *

my_count = [1, 2, 3, 4]
my_list = [2, 3, 5]
while True:
    for count in my_count:
        for num in my_list:
            display.scroll(count * num, delay=100)
    sleep(1000)



----

from microbit import *

my_count = [7, 9]
my_list = [2, 3, 4, 5]
while True:
    for count in my_count:
        for num in my_list:
            display.scroll(count * num, delay=100)
    sleep(1000)

