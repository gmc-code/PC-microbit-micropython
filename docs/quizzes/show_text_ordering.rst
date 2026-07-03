====================================================
Show Text Code Ordering
====================================================

Question 1
----------

| A student wants to adjust the text transition speed on a digital prop.
| Arrange the code segments below to flash the word "GO" with a highly accelerated custom character delay of 150 milliseconds.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.show("GO", 150)


----

Question 2
----------

| Rearrange the lines below to create an ongoing loop that flashes a high-voltage warning symbol ("X") on the LED screen to alert workers.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.show("X")
        sleep(500)
        display.clear()
        sleep(500)

----

Question 3
----------

| Put the code snippets in order to build a live industrial thermostat display.
| The program must scroll the word "TEMP" first, followed immediately by the numeric value for the temperature, inside an ongoing monitoring loop.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        display.scroll("TEMP", delay=80)
        display.show(temperature())
        sleep(200)

----

Question 4
----------

| Order the lines below to build a secure message transmitter.
| The script should store a secret password string inside a variable named ``passcode`` first, and then continuously flash that variable character by character.

.. ordering::
    :theme: light

    from microbit import *

    passcode = "ZEBRA"
    while True:
        display.show(passcode)

----

Question 5
----------

| Rearrange the code segments to build an AFL stats app.
| The micro:bit should flash the label text "HIGH SCORE=" with a crisp delay of 150 milliseconds, and then immediately flash the highest ever score variable right after it.

.. ordering::
    :theme: light

    from microbit import *

    highest_score = "37.17 239"
    while True:
        display.show("HIGH SCORE=", 150)
        display.show(highest_score)



