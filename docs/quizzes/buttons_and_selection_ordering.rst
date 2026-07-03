====================================================
Buttons and Selection Code Ordering
====================================================

Question 1
----------

| Rearrange the lines below to create a simple program that continuously checks if Button A is pressed.
| If it is pressed, scroll the message "Yes".

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.scroll("Yes")

----

Question 2
----------

| Put the code snippets in order to build a program that shows the letter "A" when Button A is pressed, or clears the display completely when nobody is touching the board.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show("A")
        else:
            display.clear()

----

Question 3
----------

| Arrange the lines of code to check for a single click event history on Button B.
| When a click is detected, show a built-in happy face image.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_b.was_pressed():
            display.show(Image.HAPPY)

----

Question 4
----------

| A student wants to set up a linked selection chain.
| If Button A is down, show "A". If Button B is down instead, show "B". Otherwise, keep the screen clear.
| Put the blocks in the correct vertical structure.

.. ordering::
    :theme: light

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show("A")
        elif button_b.is_pressed():
            display.show("B")
        else:
            display.clear()

----

Question 5
----------

| Rearrange the segments to create a protected baseline counter.
| When Button A is clicked, use the min function to increase the counter variable by 1 but cap it so it cannot exceed 9.

.. ordering::
    :theme: light

    from microbit import *

    guess_number = 5
    while True:
        if button_a.was_pressed():
            guess_number = min(9, guess_number + 1)
        display.show(guess_number)
        sleep(200)



