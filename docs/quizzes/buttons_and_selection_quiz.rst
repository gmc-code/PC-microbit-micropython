====================================================
Buttons and Selection Quiz
====================================================

Question 1
----------

.. multichoice::

    What is the primary operational difference between the ``.is_pressed()`` method and the ``.was_pressed()`` method?
    [ ] They are identical methods and can be used completely interchangeably. | Incorrect. They track button states using different historical timing logic.
    [x] ``.is_pressed()`` checks if the button is down at that exact moment, while ``.was_pressed()`` checks if it was pressed since the last time the code checked. | Correct. The text outlines that `.is_pressed` looks at the active moment, whereas `.was_pressed` tracks state history since the last device check.
    [ ] ``.was_pressed()`` only works if the micro:bit is powered off. | Incorrect. Both require active live execution on powered hardware.
    [ ] ``.is_pressed()`` triggers an automatic 1000ms delay internally. | Incorrect. Any delays must be programmed explicitly using sleep statements.

----

Question 2
----------

.. multichoice::

    What data type is returned when evaluating a button checking method like ``button_a.is_pressed()``?
    [ ] String | Incorrect. It does not return text characters inside quotation marks.
    [ ] Integer | Incorrect. It does not output raw whole numbers like 1 or 0.
    [x] Boolean | Correct. The documentation explicitly states that it returns either ``True`` or ``False``.
    [ ] Float | Incorrect. It does not return fractional decimal numbers.

----

Question 3
----------

.. multichoice::

    Look at the following selection control block code:

    .. code-block:: python

        if button_a.is_pressed():
            display.show("A")
        elif button_b.is_pressed():
            display.show("B")

    What occurs if a user presses both Button A and Button B down at the exact same fraction of a second?
    [ ] The micro:bit displays the character "A" and then immediately flashes "B". | Incorrect. An `if-elif` chain stops evaluating after finding its first matching match.
    [x] Only the letter "A" is shown on the display. | Correct. Because the ``if`` condition is evaluated first, its block triggers and the ``elif`` branch for Button B is skipped entirely.
    [ ] The display panels clears itself automatically due to a runtime error. | Incorrect. This is structured logically and will not crash.
    [ ] A new custom combination image is drawn onto the screen matrix. | Incorrect. No graphic combinations occur unless explicitly programmed.

----

Question 4
----------

.. multichoice::

    Which of the following code patterns checks if BOTH buttons are being held down simultaneously?
    [x] ``if button_a.is_pressed() and button_b.is_pressed():`` | Correct. The ``and`` logical operator requires both individual button states to evaluate to True at the same time.
    [ ] ``if button_a.is_pressed() or button_b.is_pressed():`` | Incorrect. The ``or`` operator requires only one or the other button to be down, not necessarily both.
    [ ] ``if button_a.is_pressed() + button_b.is_pressed():`` | Incorrect. Combining button conditional methods with addition operators is improper syntax.
    [ ] ``if button_a.was_pressed() or button_b.was_pressed():`` | Incorrect. This checks if either button had a historical click event independently.

----

Question 5
----------

.. multichoice::

    What is the purpose of using the ``min()`` and ``max()`` functions when updating game variables like a ``guess_number``?
    [ ] To increase the execution speed of the tracking loop. | Incorrect. Math boundaries do not alter physical code execution velocities.
    [x] To set upper and lower boundaries (limits) so the variable doesn't go out of bounds. | Correct. The tasks demonstrate using functions like ``min(9, guess_number + 1)`` to prevent values from skipping outside specified limits.
    [ ] To clear out old values stored inside the micro:bit system memory. | Incorrect. Variable cleanup is handled natively by the runtime environment.
    [ ] To display multiple integers simultaneously on a single screen framework. | Incorrect. Numeric display limits are dictated by matrix resolutions.

----

Question 6
----------

.. multichoice::

    Consider the following program loop:

    .. code-block:: python

        while True:
            if button_a.was_pressed():
                display.show("A")
            else:
                sleep(100)

    Why is the ``sleep(100)`` statement placed inside the ``else:`` clause block?
    [ ] To speed up the processing capability of the selection structure. | Incorrect. Sleeping intentionally slows processing down.
    [ ] To clear out any existing images currently rendering on the grid matrix. | Incorrect. Clearing requires explicit command lines like ``display.clear()``.
    [x] To give the system a short rest and save processing resources when no button actions are happening. | Correct. It stops the loop from running at maximum speed when idle, which provides efficiency pauses.
    [ ] To force the loop condition to evaluate as False and exit. | Incorrect. A ``while True`` container loops infinitely until forced by a break statement.

----

Question 7
----------

.. multichoice::

    What happens to the internal click history counter immediately after you call the ``button_a.was_pressed()`` method?
    [ ] The history counter doubles its tracking capacity automatically. | Incorrect. It does not accumulate continuously after interrogation.
    [x] The counter resets back to False. | Correct. Calling ``.was_pressed()`` clears the history buffer status so it can start fresh tracking for future clicks.
    [ ] The micro:bit pauses execution mechanics for exactly 1000ms. | Incorrect. System delays are governed strictly by sleep statements.
    [ ] The button stops accepting any new real-world physical interactions. | Incorrect. Buttons stay continuously receptive during standard loop cycles.

----

Question 8
----------

.. multichoice::

    A student writes the code block below to increase a score value when pressing Button A:

    .. code-block:: python

        # Start value
        score = 5
        if button_a.was_pressed():
            score = min(9, score + 2)

    If the current value of ``score`` is 8, and the user presses Button A, what is the new value stored inside ``score``?
    [ ] 10 | Incorrect. The bounding check sets a structural cap that prevents it from reaching 10.
    [ ] 8 | Incorrect. The baseline number increases because it has space before hitting the absolute ceiling limit.
    [x] 9 | Correct. Adding 2 to 8 yields 10, but ``min(9, 10)`` returns 9, limiting the value to the max boundary.
    [ ] 5 | Incorrect. The value updates upward rather than resetting to its base initial state.

----

Question 9
----------

.. multichoice::

    Which of the following code blocks demonstrates the correct way to continuously decrease a variable called ``level`` by a step of 1 down to a minimum floor value of 1 using Button B?
    [x] .. code-block:: python

            if button_b.was_pressed():
                level = max(1, level - 1)
        | Correct. Subtracting 1 decreases the value, and passing it to ``max(1, ...)`` ensures it cannot fall below 1.
    [ ] .. code-block:: python

            if button_b.was_pressed():
                level = min(1, level - 1)
        | Incorrect. This forces the level to immediately drop to 1 or lower.
    [ ] .. code-block:: python

            if button_b.is_pressed():
                level = max(9, level + 1)
        | Incorrect. This adds to the level variable and checks against an incorrect upper constraint.
    [ ] .. code-block:: python

            if button_b.was_pressed():
                level = level - 1
        | Incorrect. This fails to implement a safety ceiling or floor value constraint entirely.

----

Question 10
-----------

.. multichoice::

    If you run code that contains an infinite ``while True:`` loop without adding any internal ``sleep()`` delays or scrolling actions, what is the resulting negative outcome?
    [ ] The Python editor automatically deletes the script files from storage. | Incorrect. Program tracking logic does not modify code storage spaces.
    [ ] The micro:bit changes its display parameters to reverse text orientation. | Incorrect. Formatting layouts are not dynamically inverted by processor load.
    [x] The processor will run continuously at maximum capacity without a rest, wasting power. | Correct. Including minor delay offsets keeps processing loops efficient.
    [ ] The hardware permanently locks up and can never be reprogrammed. | Incorrect. Micro:bits can always be safely rewritten with fresh code flashing sequences.


