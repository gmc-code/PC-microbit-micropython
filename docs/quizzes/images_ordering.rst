====================================================
Built-in Images Code Ordering
====================================================

Question 1
----------

| Put the lines of code in order to show a built-in happy face on the micro:bit screen.

.. ordering::
    :theme: light

    from microbit import *

    display.show(Image.HAPPY)

----

Question 2
----------

| Arrange the code segments to create an ongoing animation loop that displays a built-in heart image, pauses for 700ms, clears the display, and pauses again for 300ms before repeating.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.show(Image.HEART)
        sleep(700)
        display.clear()
        sleep(300)

----

Question 3
----------

| A student wants to flash a warning arrow on the screen.
| Order the blocks below to show the built-in arrow pointing North, pause for 200 milliseconds, and then show the arrow pointing South.

.. ordering::
    :theme: light

    from microbit import *

    display.show(Image.ARROW_N)
    sleep(200)
    display.show(Image.ARROW_S)

----

Question 4
----------

| Put the instructions in the correct vertical order to build a program that shows the same series of faces on the micro:bit display, but with a 1 sec pause between each series.

.. ordering::
    :theme: light

    from microbit import *

    face_list = [Image.HAPPY, Image.SMILE, Image.SAD]
    while True:
        display.show(face_list, delay=500)
        sleep(1000)

----

Question 5
----------

| Order the lines below to create a program that scrolls the letter "I" across the display, pauses for 300 milliseconds, shows a built-in heart image, pauses for 500 milliseconds, and finally shows a built-in diamond image for 1 second before repeating the sequence.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.scroll('I')
        sleep(300)
        display.show(Image.HEART)
        sleep(500)
        display.show(Image.DIAMOND)
        sleep(1000)



