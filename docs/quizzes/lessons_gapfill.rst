====================================================
Lessons Gapfill Review
====================================================

Question 1
----------

| A safety engineer is coding a heavy cargo lift warning flash.
| Fill in the gaps to make the screen flash each character of the word "UP" with an extra-fast custom character speed of 150 milliseconds.

.. gapfill::

    from microbit import *

    while True:
        display.*[show/scroll]*("UP", *[150/delay=150s]*)

----

Question 2
----------

| A student is making a solar tracker that displays a long message explaining where the sun is.
| Fill in the gaps to choose the correct function that slides long sentences smoothly sideways across the LEDs.

.. gapfill::

    from microbit import *

    while True:
        display.*[scroll/show]*("PANEL ALIGNED TO EAST")

----

Question 3
----------

| Complete this smart night-light script.
| It checks if Button A is pressed right at this exact split-second to turn on a bright smile, or clears the grid if left alone.

.. gapfill::

    from microbit import *

    while True:
        if button_a.*[is_pressed/was_pressed]*():
            display.show(Image.HAPPY)
        *[else/elif]*:
            display.clear()

----

Question 4
----------

| A developer is building a scoreboard that tracks a player's lives.
| Complete the loop header structure so it scans through every single character inside the life tracker string.

.. gapfill::

    from microbit import *

    health_bar = "HEARTS"
    *[for/while]* char *[in/of]* health_bar:
        display.show(char)
        sleep(500)

----

Question 5
----------

| This script builds an automatic greenhouse water mister that runs exactly 4 times in a row using a basic number generator block.
| Complete the function arguments so it loops precisely 4 times, starting its internal count at 0.

.. gapfill::

    from microbit import *

    for spray_count in *[range(4)/range(5)]*:
        display.show(*[spray_count+1/"spray_count"]*)
        sleep(500)
        display.show(Image.STICKFIGURE)
        sleep(500)
        display.clear()
        sleep(200)

----

Question 6
----------

| Complete this linked multi-choice control switch panel.
| If Button A is held down, show a text label. If Button B is held down instead, show a different label. Otherwise, wipe the screen.

.. gapfill::

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show("A")
        *[elif/else if]* button_b.is_pressed():
            display.show("B")
        *[else/default]*:
            display.clear()

----

Question 7
----------

| A gaming badge counts click history events.
| Fill in the gaps to capture if a user clicked a button in the past, automatically clearing out that memory log right after checking it.

.. gapfill::

    from microbit import *

    while True:
        if button_b.*[was_pressed/is_pressed]*():
            display.scroll("POINT ADDED")
        sleep(100)

----

Question 8
----------

| Complete this digital combination padlock script.
| It loops through a text string variable of secret passcode digits to reveal them one by one.

.. gapfill::

    from microbit import *

    passcode = "9021"
    for digit in *[passcode/digits]*:
        display.*[show/scroll]*(digit)
        sleep(300)

----

Question 9
----------

| Complete this speed-demon test loop that scrolls a player's custom lap time variable text with an advanced tracking delay of 75 milliseconds.

.. gapfill::

    from microbit import *

    lap_time = 14.2
    while True:
        display.scroll("LAP TIME=", *[75/delay=75]*)
        display.scroll(*[lap_time/time]*)

----

Question 10
-----------

| This arcade controller uses Button A to raise a high-score integer variable, but uses the mathematical min function to stop the score from going higher than 9.

.. gapfill::

    from microbit import *

    current_score = 5
    while True:
        if button_a.was_pressed():
            current_score = *[min/max]*(9, *[current_score + 1/current_score - 1]*)
        display.show(*[current_score/current_score+2]*)





