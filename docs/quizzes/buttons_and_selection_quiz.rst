====================================================
Buttons and Selection Quiz
====================================================

Question 1
----------

.. multichoice::

    Which button is located on the left-hand side of the micro:bit front panel?
    [x] Button A | Correct. Button A is on the left side, and Button B is on the right side.
    [ ] Button B | Incorrect. Button B is positioned on the right side of the board.
    [ ] Button C | Incorrect. There is no physical button named Button C on the micro:bit.
    [ ] The Reset Button | Incorrect. The reset button is located on the back of the micro:bit next to the USB plug.

----

Question 2
----------

.. multichoice::

    Which method should you call if you want to check whether Button A is actively being held down at this exact instant?
    [x] button_a.is_pressed() | Correct. The ``.is_pressed()`` method checks the immediate, current state of the button.
    [ ] button_a.was_pressed() | Incorrect. This checks if the button was pressed at some point in the past since the last check.
    [ ] button_a.hold_down() | Incorrect. There is no method named hold_down() in the microbit library.
    [ ] button_a.click() | Incorrect. The microbit library does not use a method named click() to detect inputs.

----

Question 3
----------

.. multichoice::

    What type of answer (data type) do you get back when you ask ``button_b.is_pressed()``?
    [ ] A string (text inside quotes) | Incorrect. It returns a logical state, not a string of letters.
    [ ] An integer (a whole number like 1) | Incorrect. It does not return numbers.
    [x] A boolean value (True or False) | Correct. It returns True if the button is pressed, or False if it is not.
    [ ] A decimal float (like 1.0) | Incorrect. It only returns true/false conditions, never decimals.

----

Question 4
----------

.. multichoice::

    If a micro:bit program checks ``button_a.is_pressed()`` while nobody is touching the board, what value does it return?
    [ ] True | Incorrect. It will only return True if the button is physically pushed down.
    [x] False | Correct. Because the button is up and resting, the check evaluates to False.
    [ ] None | Incorrect. It consistently provides a clear boolean True or False answer.
    [ ] 0 | Incorrect. Button checks only return True or False.

----

Question 5
----------

.. multichoice::

    Look at the code statement below:

    .. code-block:: python

        if button_a.is_pressed():
            display.show("A")

    When will the letter "A" appear on the LED screen grid?
    [ ] Every time the micro:bit turns on. | Incorrect. It relies strictly on checking the physical button state.
    [ ] Only when Button B is held down. | Incorrect. This line explicitly tests the button_a hardware object.
    [x] When a user pushes down Button A. | Correct. The conditional code block only runs if button_a.is_pressed() evaluates to True.
    [ ] Never, because the code contains a logic error. | Incorrect. This is the standard syntax pattern used to check an input condition.

----

Question 6
----------

.. multichoice::

    If a program checks ``button_a.is_pressed()`` while the button is physically held down continuously, what value will it evaluate to on every check?
    [x] True | Correct. As long as the button remains actively pressed down, the method will consistently return True at that moment.
    [ ] False | Incorrect. It only returns False if the button is not being pressed at the exact moment of evaluation.
    [ ] None | Incorrect. The method returns a boolean value, not a None type object.
    [ ] 1 | Incorrect. Button state methods return booleans (True/False), not integers.

----

Question 7
----------

.. multichoice::

    What happens if you run a loop that continuously calls ``button_a.was_pressed()`` while the button is held down continuously?
    [ ] It returns True on every single loop iteration. | Incorrect. It only captures the initial transition event, not the ongoing state.
    [x] It returns True on the first check, and then returns False on subsequent checks until released and pressed again. | Correct. The method resets its history counter back to False immediately after being called, so it will not return True again until a new press occurs.
    [ ] It causes the micro:bit hardware to lock up. | Incorrect. This is normal conditional logic and will not cause a hardware freeze.
    [ ] It returns None. | Incorrect. It always returns a boolean value (True or False).

----

Question 8
----------

.. multichoice::

    Look at the following selection code block:

    .. code-block:: python

        if button_a.is_pressed() or button_b.is_pressed():
            display.show(Image.HAPPY)
        else:
            display.clear()

    Under what condition will the micro:bit display the happy face image?
    [ ] Only when Button A is pressed alone. | Incorrect. The statement can also evaluate to True if Button B is pressed.
    [ ] Only when both Button A and Button B are pressed together. | Incorrect. That would require the 'and' operator instead of 'or'.
    [x] When either Button A is pressed, Button B is pressed, or both are pressed. | Correct. The logical 'or' operator returns True if at least one of the conditions is true.
    [ ] Only when neither button is pressed. | Incorrect. If neither is pressed, the code branches to the 'else' block and clears the display.

----

Question 9
----------

.. multichoice::

    Look at the following selection control structure:

    .. code-block:: python

        if button_a.is_pressed():
            display.show("A")
        elif button_b.is_pressed():
            display.show("B")
        else:
            display.show("C")

    If neither Button A nor Button B is pressed, what will be displayed on the micro:bit?
    [ ] The letter "A" | Incorrect. The "if" condition requires Button A to be pressed.
    [ ] The letter "B" | Incorrect. The "elif" condition requires Button B to be pressed.
    [x] The letter "C" | Correct. When all preceding conditions in an if-elif chain evaluate to False, the final "else" block executes by default.
    [ ] The screen will remain completely clear. | Incorrect. The "else" block explicitly runs display.show("C").

----

Question 10
-------------

.. multichoice::

    Which of the following code blocks will display the letter "A" when Button A is pressed, display the letter "B" when Button B is pressed, and keep the screen clear when neither button is pressed?
    [x] .. code-block:: python

            if button_a.is_pressed():
                display.show("A")
            elif button_b.is_pressed():
                display.show("B")
            else:
                display.clear()
        | Correct. This properly routes each button state and uses the ``else`` clause to clear the screen when both conditions evaluate to False.
    [ ] .. code-block:: python

            if button_a.is_pressed():
                display.show("A")
            if button_b.is_pressed():
                display.show("B")
            else:
                display.clear()
        | Incorrect. Using two independent ``if`` statements means if Button A is pressed, the second ``if`` condition is evaluated separately, causing the ``else`` block to execute and clear the screen immediately.
    [ ] .. code-block:: python

            if button_a.is_pressed():
                display.show("A")
            elif button_b.is_pressed():
                display.show("B")
        | Incorrect. This block lacks an final ``else`` structural branch to clear the screen when idle.
    [ ] .. code-block:: python

            if button_a.is_pressed() and button_b.is_pressed():
                display.show("A")
            else:
                display.clear()
        | Incorrect. This checks if both buttons are held together, rather than handling them as separate, distinct button inputs.


