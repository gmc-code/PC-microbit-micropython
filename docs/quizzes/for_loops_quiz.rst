====================================================
For Loops Quiz
====================================================

Question 1
----------

.. multichoice::

    What is the main purpose of using a "for loop" in a Python program?
    [x] To repeat a block of code a certain number of times or go through a sequence. | Correct. For loops let you step through items or repeat code cleanly.
    [ ] To turn off the micro:bit hardware completely. | Incorrect. For loops guide the path of your code rather than shutting down power.
    [ ] To change a variable from a number into text. | Incorrect. Loops repeat instructions instead of converting variable data types.
    [ ] To check if the reset button on the back has been pressed. | Incorrect. Checking inputs uses selection structures like if statements.

----

Question 2
----------

.. multichoice::

    When looping through a string text variable like "Welcome" using a for loop, what does the loop look at during each step?
    [ ] The entire word all at once | Incorrect. A for loop breaks the sequence down rather than processing it in one block.
    [x] One single character at a time | Correct. The loop steps through the string letter by letter, from left to right.
    [ ] Only the very first letter | Incorrect. The loop continues until it has checked every single character in the sequence.
    [ ] Only the spaces between words | Incorrect. It processes every active character inside the string variable.

----

Question 3
----------

.. multichoice::

    Look at this line of code: ``for character in "Hello":``
    What is the purpose of the word ``character`` in this statement?
    [ ] It is a permanent built-in keyword that Python requires. | Incorrect. This is a variable name chosen by the programmer.
    [ ] It is a command that clears the micro:bit screen. | Incorrect. Clearing the screen requires calling display.clear().
    [x] It is a temporary variable that holds the current letter during each step of the loop. | Correct. Each time the loop repeats, the next letter in the string is placed inside this variable.
    [ ] It changes the font style of the letters on the screen. | Incorrect. It manages code execution loop states instead of display font layouts.

----

Question 4
----------

.. multichoice::

    If a for loop is set up to step through the string variable text "winner", how many total times will the code block inside the loop repeat?
    [ ] 1 time | Incorrect. It repeats once for every single letter in the word.
    [ ] 5 times | Incorrect. Count the number of characters in the sequence carefully.
    [x] 6 times | Correct. The word "winner" contains exactly 6 letters, so the loop executes its inner code block 6 times.
    [ ] It will run forever and never stop. | Incorrect. A for loop stops automatically once it reaches the end of the sequence.

----

Question 5
----------

.. multichoice::

    Look at this loop statement: ``for digit in "2023":``
    What value will be stored inside the variable ``digit`` during the very first step of the loop?
    [x] "2" | Correct. Loops process sequences from start to finish, so it grabs the first character on the left first.
    [ ] "0" | Incorrect. This is the second character in the sequence layout.
    [ ] "3" | Incorrect. This is the final character at the end of the sequence.
    [ ] "2023" | Incorrect. The loop isolates individual elements rather than duplicating the entire string.

----

Question 6
----------

.. multichoice::

    What punctuation mark must always be placed at the very end of a ``for`` loop setup header line in Python?
    [ ] A period mark . | Incorrect. Python headers do not use standard sentence periods.
    [ ] A question mark ? | Incorrect. Question marks are not valid syntax markers in Python structure definitions.
    [x] A colon mark : | Correct. A colon tells Python that an indented block of instructions is starting right below it.
    [ ] A semicolon mark ; | Incorrect. Semicolons are not used to open loop blocks.

----

Question 7
----------

.. multichoice::

    How does Python know which lines of code belong inside your loop block and should be repeated?
    [ ] They are wrapped in giant quotation marks. | Incorrect. Quotes identify text string variables, not code structures.
    [x] They are indented (shifted inward) under the loop header line. | Correct. Consistent indentation groups blocks of code together in Python.
    [ ] They are written in capital letters. | Incorrect. Capitals are used for constants.
    [ ] They are placed below the for loop header and before the next blank line. | Incorrect. They must be indented, not just placed below the header.

----

Question 8
-----------

.. multichoice::

    Suppose you have a list containing exactly 4 names. If you loop through that list sequence using a ``for`` loop, how many total times will the instructions inside your loop block execute?
    [ ] 1 time | Incorrect. A for loop repeats for every individual element in the sequence, not just the first one.
    [ ] 5 times | Incorrect. The loop stops automatically once it reaches the end of the 4 items.
    [x] 4 times | Correct. The loop runs exactly once for each item in the collection sequence, resulting in 4 iterations.
    [ ] It will loop infinitely without stopping. | Incorrect. Unlike a while True statement, a for loop terminates naturally when the sequence is exhausted.

----

Question 9
-----------

.. multichoice::

    A student creates a list of items called ``tools`` containing 3 elements. They write a ``for item in tools:`` loop header. What value is placed inside the temporary variable ``item`` during the final run of the loop?
    [ ] All 3 items at the same time | Incorrect. The loop breaks the sequence down to process individual values step by step.
    [ ] The first item in the list | Incorrect. The first item is processed during the initial iteration on step one.
    [x] The very last item in the list | Correct. Python processes sequential structures from left to right, meaning the final item is assigned on the last iteration.
    [ ] A boolean value of True or False | Incorrect. The loop tracking variable copies the actual data item from the list.

----

Question 10
-----------

.. multichoice::

    A student creates two sequences: a list of colors (Red, Green) and a list of shapes (Circle, Star). They write the following nested loops:

    .. code-block:: python

        for color_item in colors:
            for shape_item in shapes:
                display.scroll(color_item + " " + shape_item)

    How many total combined pairs (lines of text) will be scrolled when this code runs?
    [ ] 2 lines | Incorrect. The outer loop runs 2 times, and for each of those steps, the inner loop must complete its full cycle.
    [ ] 3 lines | Incorrect. You must multiply the number of items in the first list by the number of items in the second list.
    [x] 4 lines | Correct. The outer loop runs 2 times, and for each step, the inner loop runs 2 times (2 multiplied by 2 equals 4 total loop combinations: Red Circle, Red Star, Green Circle, Green Star).
    [ ] 0 lines | Incorrect. Both lists contain active elements, so the inner scroll instruction executes completely.



