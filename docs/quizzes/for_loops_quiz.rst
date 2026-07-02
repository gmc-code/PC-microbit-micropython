====================================================
For Loops Quiz
====================================================

Question 1
----------

.. multichoice::

    When iterating over a string using ``for char in welcome_string:``, what value is stored in the variable ``char`` on each step of the loop?
    [ ] The length of the string as an integer. | Incorrect. The loop yields individual characters, not the overall count.
    [ ] The complete string all at once. | Incorrect. A loop breaks the collection down element by element.
    [x] One single character from the string at a time, sequentially. | Correct. The text explains that each character in the string is placed in the variable in turn.
    [ ] The index position number of each letter. | Incorrect. It extracts the character contents directly, not their numerical index values.

----

Question 2
----------

.. multichoice::

    Look at this code example from the text:

    .. code-block:: python

        welcome_string = 'Hello'
        while True:
            for welcome_character in welcome_string:
                display.scroll(welcome_character)
            sleep(300)

    What is the physical display outcome on the micro:bit matrix?
    [ ] The word 'Hello' scrolls across the display as a single connected text unit. | Incorrect. Because it is inside a for loop, it scrolls character by character.
    [x] Each letter of 'Hello' scrolls across the screen individually, one after another, with a brief pause after the full word finishes. | Correct. The for loop forces each character to scroll separately before hitting the 300ms pause.
    [ ] The word 'Hello' flashes statically on the LED grid without moving. | Incorrect. The display.scroll() function causes text to move horizontally.
    [ ] The loop runs once and then terminates permanently due to a syntax error. | Incorrect. This is correct syntax and will repeat indefinitely.

----

Question 3
----------

.. multichoice::

    What parameter does the basic ``range(5)`` function take, and what sequence of integers does it generate?
    [ ] It takes a start point and generates: 1, 2, 3, 4, 5. | Incorrect. Python ranges start at 0 by default and stop before the end value.
    [x] It takes a stop value and generates five numbers: 0, 1, 2, 3, 4. | Correct. The text demonstrates that range(5) provides integers from 0 up to, but not including, 5.
    [ ] It takes a step index and generates: 0, 5, 10, 15, 20. | Incorrect. Without a third argument, the default increment step size is 1.
    [ ] It takes a count value and generates five 5s in a row. | Incorrect. It generates an arithmetic progression sequence.

----

Question 4
----------

.. multichoice::

    How must a nested loop structure be arranged to visit every coordinate location on the 5x5 micro:bit LED display grid?
    [ ] Two loops must be written completely separate from each other, one after the other. | Incorrect. Separate loops cannot iterate over coordinate combinations efficiently.
    [x] An inner loop controlling the X coordinates must run inside an outer loop controlling the Y coordinates. | Correct. The exercises demonstrate nesting an inner `for x in range(5)` loop inside an outer `for y in range(5)` loop to check all pixels.
    [ ] A single loop parameter containing `range(5, 5)` is used. | Incorrect. This is invalid syntax for traversing a multi-dimensional pixel grid.
    [ ] Loops are not needed because coordinates update automatically by default. | Incorrect. Iteration must be specified explicitly in code blocks.

----

Question 5
----------

.. multichoice::

    Which function is used to set the individual brightness level of a specific LED on the micro:bit grid?
    [ ] ``display.show_pixel(x, y, brightness)`` | Incorrect. This function name does not exist in the micro:bit library.
    [x] ``display.set_pixel(x, y, brightness)`` | Correct. The documentation challenges show that display.set_pixel() targets specific row and column coordinates.
    [ ] ``display.scroll_pixel(x, y)`` | Incorrect. Scrolling is an automated text/sequence function, not an individual LED setup tool.
    [ ] ``display.light(x, y)`` | Incorrect. This is incorrect method syntax.

----

Question 6
----------

.. multichoice::

    What are the valid boundary numbers for the coordinate positions and brightness arguments when using ``display.set_pixel(x, y, brightness)``?
    [ ] Coordinates from 1 to 5; brightness from 0 to 10. | Incorrect. Python structures use zero-indexed numbers for coordinates.
    [ ] Coordinates from 0 to 5; brightness from 1 to 9. | Incorrect. 5 is outside the index range for a 5x5 grid (0-4), and brightness starts at 0.
    [x] Coordinates from 0 to 4; brightness from 0 to 9. | Correct. A 5x5 grid runs from index 0 to 4, and brightness ranges from 0 (off) to 9 (maximum bright).
    [ ] Coordinates from -2 to 2; brightness from 0 to 100. | Incorrect. The grid does not use centered negative coordinates.

----

Question 7
----------

.. multichoice::

    Look at the following code block from the documentation solutions:

    .. code-block:: python

        for y in range(5):
            for x in range(5):
                display.set_pixel(x, y, 9)
                sleep(100)

    In what specific order will the LEDs light up on the display?
    [ ] They will all light up at the exact same millisecond. | Incorrect. The sleep statement introduces a delay between actions.
    [ ] They will light up column by column from top to bottom. | Incorrect. The outer loop controls the row, so rows take priority.
    [x] They will light up row by row from left to right. | Correct. The outer loop holds the row index (y) steady while the inner loop cycles across all columns (x) first.
    [ ] They will light up in a completely random sequence across the grid. | Incorrect. The numbers generated by range() follow a strict linear sequence.

----

Question 8
----------

.. multichoice::

    What happens if you change the inner loop statement from ``display.set_pixel(x, y, 9)`` to ``display.set_pixel(x, y, 0)`` in the grid filling program?
    [ ] The LEDs will glow with an intermediate dim lighting value. | Incorrect. 0 sets the brightness level to completely off.
    [x] The display will clear the pixels one by one, turning them off in sequence. | Correct. Setting the brightness value parameter to 0 turns off that specific targeted pixel.
    [ ] The micro:bit will throw an out of bounds runtime error. | Incorrect. 0 is a valid brightness argument.
    [ ] The animation speed will double automatically. | Incorrect. Animation speed is controlled exclusively by the sleep duration.

----

Question 9
----------

.. multichoice::

    Why is a 2D grid template list of list structures useful when working with micro:bit images, as shown in the advanced tasks?

    .. code-block:: python

        heart = [
            [0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 1, 1, 1, 0],
            [0, 0, 1, 0, 0]
        ]

    [ ] It automatically increases the operating memory speed of the hardware. | Incorrect. Data layouts do not boost processor hardware speeds.
    [x] It creates a clear visual map of which pixel coordinates should be active or inactive. | Correct. The 1s and 0s mimic the physical arrangement of the 5x5 LED panel, making layout mapping intuitive.
    [ ] It converts text string loops into numbers automatically. | Incorrect. Lists do not perform type translation tasks.
    [ ] It forces the program to terminate immediately after one cycle. | Incorrect. Run cycles are determined by loop conditions, not the variable data style.

----

Question 10
-----------

.. multichoice::

    How can you capture and store the coordinates of active pixels dynamically during a nested loop traversal so you can manipulate them later?
    [ ] By adding the values together directly into a single string variable. | Incorrect. Strings store flat text characters and cannot easily isolate pairs.
    [ ] By resetting the range boundaries of the loop container. | Incorrect. Loop boundaries stay fixed during execution.
    [x] By appending coordinate tuples like ``(x, y)`` into an empty tracking list. | Correct. The tasks demonstrate tracking active units by appending coordinate pairs to a list object, which can then be picked or popped.
    [ ] By increasing the global brightness argument parameter past 9. | Incorrect. Brightness cannot exceed 9 and does not track historical records.


