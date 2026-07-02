====================================================
Scroll Text Quiz
====================================================

Question 1
----------

.. multichoice::

    What is the default scrolling delay for the ``display.scroll()`` function if no delay parameter is specified?
    [ ] 50ms | Incorrect. 50ms is used for rapid scrolling.
    [ ] 100ms | Incorrect. 100ms is a custom short delay.
    [x] 150ms | Correct. The default delay is 150ms when no delay is explicitly provided.
    [ ] 300ms | Incorrect. 300ms is used for slow scrolling.

----

Question 2
----------

.. multichoice::

    Which of the following data types can be passed directly into the ``display.scroll()`` function?
    [x] String, integer, and float | Correct. It can scroll text strings, whole numbers (integers), and decimals (floats).
    [ ] String only | Incorrect. The function is flexible and accepts integers and floats directly as well.
    [ ] Integer and float only | Incorrect. It can also scroll text messages wrapped in quotes.
    [ ] String and integer only | Incorrect. Floating-point decimal numbers are also fully supported.

----

Question 3
----------

.. multichoice::

    What will happen when the following code block executes?

    .. code-block:: python

        from microbit import *

        while True:
            display.scroll('Hi', 50)

    [ ] The text will scroll slowly for 50 seconds. | Incorrect. The number represents milliseconds, not seconds.
    [ ] The text will scroll 50 times and then stop. | Incorrect. The while loop ensures it repeats indefinitely.
    [x] The text will scroll horizontally across the display rapidly with a 50ms delay. | Correct. A smaller delay number makes the text scroll faster than the default 150ms.
    [ ] The text will flash on the screen instead of scrolling. | Incorrect. It will still scroll horizontally.

----

Question 4
----------

.. multichoice::

    Which of the following lines of code demonstrates a valid way to scroll a message with a custom delay?
    [x] display.scroll('Hi', delay=150) | Correct. You can explicitly name the keyword argument 'delay'.
    [x] display.scroll('Hi', 150) | Correct. You can pass the number directly as a positional second argument.
    [ ] display.scroll(delay=150, 'Hi') | Incorrect. Positional arguments cannot follow keyword arguments in Python.
    [ ] display.scroll('Hi' + 150) | Incorrect. You cannot concatenate a string and an integer directly like this.

----

Question 5
----------

.. multichoice::

    Look at the following code block:

    .. code-block:: python

        from microbit import *

        while True:
            display.scroll('I like to watch', delay=60)
            display.scroll('AFL', delay=120)

    Which text scrolls across the micro:bit LED display at a slower pace?
    [ ] 'I like to watch' | Incorrect. A delay of 60ms makes this text move faster.
    [x] 'AFL' | Correct. A delay of 120ms is a longer pause between frames, making it scroll more slowly.
    [ ] They scroll at exactly the same speed. | Incorrect. They use different delay values.
    [ ] Neither, the code will result in a syntax error. | Incorrect. This is perfectly valid code.

----

Question 6
----------

.. multichoice::

    Why might you choose to use variables with ``display.scroll()``, as shown in the code below?

    .. code-block:: python

        from microbit import *

        player = 'Locket'
        goals = 1360
        display.scroll(player)

    [ ] Variables make the micro:bit scroll text significantly faster. | Incorrect. Variables do not alter execution or hardware speed.
    [x] It separates the data values from their use, making the code easier to read and edit. | Correct. Keeping values at the top makes editing straightforward.
    [ ] Variables are required because display.scroll() cannot accept raw strings. | Incorrect. Raw strings work perfectly fine.
    [ ] It prevents the code from repeating infinitely. | Incorrect. Infinite repetition is controlled by the while loop structure.

----

Question 7
----------

.. multichoice::

    What type of data value is stored in the variable ``goals_per_game`` in the following script?

    .. code-block:: python

        goals_per_game = 4.84
        display.scroll(goals_per_game)

    [ ] String | Incorrect. Strings must be wrapped inside quotation marks.
    [ ] Integer | Incorrect. Integers represent whole numbers without a decimal point.
    [x] Float | Correct. A number containing a decimal point is represented as a floating-point number.
    [ ] Boolean | Incorrect. Booleans only represent True or False values.

----

Question 8
----------

.. multichoice::

    Which line of code correctly scrolls an integer value directly without formatting it as a text string?
    [ ] display.scroll("12") | Incorrect. The quotation marks turn this value into a string.
    [x] display.scroll(12) | Correct. Passing a whole number without quotation marks passes it as an integer.
    [ ] display.scroll(12.0) | Incorrect. The inclusion of a decimal point makes this value a float.
    [ ] display.scroll(int='12') | Incorrect. This is invalid argument syntax for the scroll function.

----

Question 9
----------

.. multichoice::

    What is the core purpose of placing ``display.scroll()`` statements inside a ``while True:`` loop structure?
    [ ] To check if the Micro:bit hardware has connected properly. | Incorrect. The loop does not handle hardware checking.
    [ ] To scroll the text exactly one single time. | Incorrect. Code inside the loop keeps executing over and over.
    [x] To continuously repeat the text scrolling action in an infinite loop. | Correct. The loop block keeps running as long as the condition evaluates to True.
    [ ] To automatically adjust the scrolling speed based on string length. | Incorrect. Speed remains fixed to the delay parameter value.

----

Question 10
-----------

.. multichoice::

    A student wants to scroll the text message "Born 2015" quickly using a 100ms delay. Which implementation is correct?
    [x] display.scroll("Born 2015", delay=100) | Correct. This uses a valid string and sets a quick 100ms delay.
    [ ] display.scroll(Born 2015, 100) | Incorrect. The text characters will cause a syntax error because they lack quotes.
    [ ] display.scroll("Born 2015", delay=300) | Incorrect. A 300ms delay makes the text scroll slowly, not quickly.
    [ ] display.scroll(2015, delay=100) | Incorrect. This only passes the integer, leaving out the text context "Born ".

