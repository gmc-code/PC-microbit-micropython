====================================================
Scroll Text Code Ordering
====================================================

Question 1
----------

| Put the lines of code in order to scroll the word "Hello" across the micro:bit screen.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.scroll("Hello")

----

Question 2
----------

| Put the code snippets in order to create a program that scrolls a single whole integer number, followed by some text, inside an ongoing loop.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.scroll(5)
        display.scroll("houses")

----

Question 3
----------

| A student wants to adjust how fast their text slides across the display panel.
| Arrange the code segments below to scroll the first text fast and then the second text slowly.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.scroll("Fast", 50)
        display.scroll("Slow", 200)

----

Question 4
----------

| Order the lines below to build a script that stores a player's name and goals scored, and then continuously scrolls them on the LED panel with a delay of 1 second after each loop.

.. ordering::
    :theme: light

    from microbit import *

    player = "Donatello"
    goals = 19
    while True:
        display.scroll(player)
        display.scroll(goals)
        sleep(1000)

----

Question 5
----------

| Rearrange the code segments to create a variable stats display tracker.
| The micro:bit should scroll the text label "Runs=" at a rapid pace of 50 milliseconds, and then scroll the numeric score variable value right after it.

.. ordering::
    :theme: light

    from microbit import *

    runs = 952
    while True:
        display.scroll("Runs=", 50)
        display.scroll(runs)




