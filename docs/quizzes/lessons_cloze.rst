====================================================
Lessons Cloze Review
====================================================

Question 1
----------

| Complete the code to import the micro:bit library and scroll a simple text message.

.. cloze::

    from microbit *[ import | include ]* *

    while True:
        display.*[ scroll | show ]*("Hello")

----

Question 2
----------

| Complete the statement to check if the A-button is being pressed down at this exact split-second.

.. cloze::

    from microbit import *

    while True:
        if button_a.*[ is_pressed | was_pressed | has_pressed ]*():
            display.show("A")

----

Question 3
----------

| Fill in the missing syntax to loop through every character in a secret word text variable.

.. cloze::

    from microbit import *

    passcode = "ZEBRA"
    for letter *[ in | of | range ]* passcode:
        display.*[ show | write ]*(letter)
        sleep(300)

----

Question 4
----------

| Complete the program to flash the numbers 0, 1, and 2 onto the screen using the range() function and a custom delay of 400 milliseconds.

.. cloze::

    from microbit import *

    for count in range(*[ 3 | 2 | 1 ]*):
        display.show(count)
        sleep(*[ 400 | "400" | delay=400 ]*)

----

Question 5
----------

| Finish this selection structure so that it falls back to a default "catch-all" action if no buttons are down.

.. cloze::

    if button_a.is_pressed():
        display.show("A")
    *[ elif | if | else if ]* button_b.is_pressed():
        display.show("B")
    *[ else | default | finish ]*:
        display.clear()

----

Question 6
----------

| Complete this data-tracking script to safely check if a click happened in the past and automatically reset the log.

.. cloze::

    from microbit import *

    while True:
        if button_b.*[ was_pressed | is_pressed | cleared ]*():
            display.show(Image.HAPPY)
        *[ sleep | wait | pause ]*(100)

----

Question 7
----------

| Complete the parameters to scroll a numeric variable with a fast custom delay speed of 50 milliseconds.

.. cloze::

    from microbit import *

    score = 950
    while True:
        display.scroll("SCORE=", *[ 50 | delay=500 | "50" ]*)
        display.scroll(score)

----

Question 8
----------

| Finish the loop punctuation and matching variable setup to scroll the characters of the string step-by-step.

.. cloze::

    from microbit import *

    *[levels|char]* = "level 1 to 9"
    for char in levels*[ : | ; | , ]*
        display.scroll(*[ char | levels ]*)

----

Question 9
----------

| Complete the program to flash a word character-by-character with a faster transition window of 150 milliseconds.

.. cloze::

    from microbit import *

    while True:
        display.show("GO", *[ 150 | 400 | "150ms" ]*)

----

Question 10
-----------

| Complete this script which prevents an integer variable from exceeding a ceiling of 9 when Button A is pressed.

.. cloze::

    from microbit import *

    guess_number = 5
    while True:
        if button_a.was_pressed():
            guess_number = *[ min | max | limit ]*(9, guess_number + 1)
        display.show(guess_number)



