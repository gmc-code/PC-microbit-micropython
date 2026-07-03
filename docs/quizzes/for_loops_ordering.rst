====================================================
For Loops Code Ordering
====================================================

Question 1
----------

| A student wants to code an electronic laser fence alarm system.
| Rearrange the lines below to create a loop that cycles through each individual alert code letter inside the alarm state code string ``"ALERT"`` as part of his system's security protocol.

.. ordering::
    :theme: light

    from microbit import *

    for code_letter in "ALERT":
        display.show(code_letter)
        sleep(200)

----

Question 2
----------

| Put the code snippets in order to build an automated submarine sonar tracking scan.
| The program must cycle through a custom sequence of target depth values (100, 200, 300) and flash each numeric depth value onto the micro:bit display screen panel.

.. ordering::
    :theme: light

    from microbit import *

    depth_targets = [100, 200, 300]
    for meters in depth_targets:
        display.scroll(meters)

----

Question 3
----------

| A student wants to flash a secret password symbol by symbol on the screen.
| Order the lines to step through a sequence of single characters stored in a variable named ``secret_code`` to show them one by one with a dash between them.

.. ordering::
    :theme: light

    from microbit import *

    secret_code = "SOS"
    while True:
        for symbol in secret_code:
            display.show(symbol)
            sleep(400)
            display.show("-")
            sleep(400)

----

Question 4
----------

| Put the code lines in order to build a beacon that cycles through three warning status words (LOW, MED, HIGH) stored in a sequence list.
| It should scroll each status word completely across the display panel before moving to the next.

.. ordering::
    :theme: light

    from microbit import *

    warning_levels = ["LOW", "MED", "HIGH"]
    for status in warning_levels:
        display.scroll(status)
        sleep(500)

----

Question 5
----------

| Rearrange the lines to create a custom scoreboard display for a mini-game.
| The loop needs to look at a sequence of target scores (10, 25, 50) and show each milestone number on the display panel with a short pause between them.

.. ordering::
    :theme: light

    from microbit import *

    score_milestones = [10, 25, 50]
    for target_score in score_milestones:
        display.scroll(target_score)
        sleep(600)

