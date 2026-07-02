====================================================
Show Text Quiz
====================================================

Question 1
----------

.. multichoice::

    What is the default delay time between characters when using the ``display.show()`` function without specifying a custom delay?
    [ ] 150 milliseconds | Incorrect. 150ms is the default delay for the text scrolling function, not the show function.
    [ ] 200 milliseconds | Incorrect. 200ms is a custom short delay option mentioned in the tasks.
    [x] 400 milliseconds | Correct. The documentation specifies that each character or digit is shown with a default of 400ms between them.
    [ ] 500 milliseconds | Incorrect. 500ms is used for pauses or custom slower displays.

----

Question 2
----------

.. multichoice::

    What happens to the micro:bit LED display after executing a basic ``display.show(3.14)`` statement without any additional clearing commands?
    [ ] The display goes completely blank immediately. | Incorrect. The function does not clear itself automatically by default.
    [ ] The text will continuously flash on and off. | Incorrect. Flashing requires a loop with explicit clear and sleep states.
    [x] The final digit or character ('4') remains visible on the display. | Correct. After using display.show, the last digit or character is left displayed on the screen.
    [ ] The micro:bit restarts to reset the screen. | Incorrect. Hardware resets do not occur from a standard display call.

----

Question 3
----------

.. multichoice::

    Which function should be called to completely wipe or remove the last left-over character from the micro:bit screen?
    [ ] display.reset() | Incorrect. There is no reset function in the display module for this purpose.
    [x] display.clear() | Correct. The display.clear() function is explicitly used to remove the last character from the display.
    [ ] display.sleep() | Incorrect. Sleep is a global function used to pause program execution time, not clear the screen.
    [ ] display.show(None) | Incorrect. Passing None is invalid syntax for removing text characters.

----

Question 4
----------

.. multichoice::

    What is the primary difference between the behavior of these two code examples?

    **Example A:**

    .. code-block:: python

        display.show(3.14)

    **Example B:**

    .. code-block:: python

        while True:
            display.show(3.14)
            display.clear()
            sleep(2000)

    [ ] Example A repeats infinitely while Example B runs only once. | Incorrect. It is the opposite; Example B contains an infinite loop block.
    [x] Example A leaves the digit "4" static on the screen, while Example B clears it and creates a 2-second blank pause before repeating. | Correct. Example A leaves the final character up, whereas Example B deliberately blanks the display periodically.
    [ ] Example B throws a syntax error because of the sleep statement. | Incorrect. Sleep is completely valid and keeps the screen blank for a short time.
    [ ] They display characters at completely different speeds. | Incorrect. Both use the default character delay speed.

----

Question 5
----------

.. multichoice::

    If a developer sets the parameter ``clear=True`` inside ``display.show('Hi', clear=True)``, what action is performed automatically?
    [ ] The entire script terminates immediately after showing 'Hi'. | Incorrect. It does not stop execution of the script.
    [ ] The string is displayed in reverse character order. | Incorrect. Character order remains sequentially normal.
    [x] The screen clears the final character automatically once the sequence finishes. | Correct. If clear is True, the display will be cleared after it has finished showing the sequence.
    [ ] The character delay drops down to 0ms automatically. | Incorrect. The character-to-character delay parameter is independent of clearing.

----

Question 6
----------

.. multichoice::

    Which of the following lines correctly sets a custom delay of 150ms between sequence characters using keyword arguments?
    [x] display.show(5.64, delay=150) | Correct. This properly specifies the value and uses the named parameter syntax.
    [ ] display.show(5.64, 150ms) | Incorrect. Appending 'ms' to a number is invalid syntax in Python.
    [ ] display.show(delay=150) | Incorrect. The sequence value to display is entirely missing from this function call.
    [ ] display.show("5.64" + 150) | Incorrect. This attempts to perform an invalid addition between a string and an integer.

----

Question 7
----------

.. multichoice::

    Look closely at the following code structure:

    .. code-block:: python

        from microbit import *

        while True:
            display.show('I like the ', delay=200)
            display.show('NBA', delay=400)
            display.clear()
            sleep(2000)

    What is the core design purpose of modifying the delay parameters in this specific way?
    [ ] To conserve the physical battery life of the micro:bit device. | Incorrect. Adjusting screen delays does not materially alter device power modes.
    [x] To use a shorter delay for initial text context, and a longer, more readable delay for the main info. | Correct. Varying speeds allows secondary structural text to pass quickly and core content slowly.
    [ ] To make the text 'NBA' scroll across the display horizontally. | Incorrect. The show function sequences elements statically one character at a time; it does not scroll.
    [ ] To ensure the loop finishes running after 2000 iterations. | Incorrect. A while True condition loops indefinitely regardless of internal delays.

----

Question 8
----------

.. multichoice::

    What data types can be successfully passed as the first argument into the ``display.show()`` function sequence?
    [ ] Only text strings wrapped in quotation marks. | Incorrect. It can process numerical digits directly too.
    [ ] Integers only. | Incorrect. Strings and decimals can be shown just as easily.
    [x] Strings, floats, and integers. | Correct. The function sequentially displays letters or digits from strings, floating-point decimals, or whole integers.
    [ ] Strictly lists or boolean objects. | Incorrect. These are not supported data sequences for standard sequential text display.

----

Question 9
----------

.. multichoice::

    A student wants to display the word "ABC" such that the final character 'C' is removed right away, followed by a brief half-second pause. Which option is correct?
    [ ] .. code-block:: python

            display.show("ABC")
            sleep(500)
        | Incorrect. This does not use clear parameters or clear commands, leaving 'C' stuck on screen.
    [x] .. code-block:: python

            display.show("ABC", clear=True)
            sleep(500)
        | Correct. It automatically removes the last character via clear=True and pauses for 500ms (half a second).
    [ ] .. code-block:: python

            display.show("ABC", clear=False)
            sleep(50)
        | Incorrect. This explicitly stops the character from being cleared, and pauses for only 50ms.
    [ ] .. code-block:: python

            display.show("ABC", delay=500)
        | Incorrect. This merely slows the timing between characters to 500ms instead of creating a final blank screen pause.

----

Question 10
-----------

.. multichoice::

    Why are variables useful when passing statistics (like player names or scores) to a series of ``display.show()`` instructions?
    [ ] They are mandatory because the function cannot display raw values. | Incorrect. Raw values can easily be passed directly to the function parameters.
    [x] They make it easy to see, organize, and edit data values at the top of the program without messing up the logic. | Correct. Isolating variables keeps the core display loop clean and easy to modify.
    [ ] They automatically convert standard text into a scrolling animation. | Incorrect. Variables hold data but do not change the core behavior of the show function.
    [ ] They clear the memory blocks of the micro:bit hardware automatically. | Incorrect. Variables occupy space in execution memory and do not perform cleanup tasks.

