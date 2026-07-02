====================================================
Basics Quiz
====================================================

Question 1
----------

.. multichoice::

    Which of the following is the correct statement to import the Micro:bit library according to the provided documentation?
    [x] from microbit import * | Correct. This uses lowercase letters, proper spacing, and includes the asterisk.
    [ ] from microbit import* | Incorrect. This is missing a space before the asterisk.
    [ ] from microbot import * | Incorrect. The library name 'microbit' is misspelled as 'microbot'.
    [ ] from microbit * | Incorrect. This completely omits the required 'import' keyword.

----

Question 2
----------

.. multichoice::

    According to the PEP 8 guide mentioned in the text, how many blank lines should follow a basic library import to separate it from the rest of the code?
    [x] 1 blank line | Correct. The PEP 8 standard specifies placing exactly one blank line after standard library imports.
    [ ] 0 blank lines | Incorrect. Leaving no blank line makes it harder to read.
    [ ] 2 blank lines | Incorrect. Two blank lines are typically reserved before or after top-level class or function definitions.
    [ ] 3 blank lines | Incorrect. Three blank lines are too much.

----

Question 3
----------

.. multichoice::

    What happens when you use the statement 'while True:' in Python?
    [x] The loop runs indefinitely because the condition is always evaluated as true. | Correct. Passing the boolean literal True directly causes the loop to run forever.
    [ ] The loop runs exactly once and terminates automatically. | Incorrect. A while loop keeps executing as long as its condition remains true.
    [ ] The program generates a syntax error immediately. | Incorrect. This is fully valid Python syntax and compiles correctly.
    [ ] The loop only runs if a Micro:bit button is actively being pressed. | Incorrect. The boolean condition True does not inspect hardware states automatically.

----

Question 4
----------

.. multichoice::

    Which of the following demonstrates a valid beginning line of an infinite loop in Python?
    [x] while True: | Correct. This correctly utilizes a lowercase 'while', a capitalized 'True', and ends with a colon.
    [ ] while true: | Incorrect. Python is case-sensitive, so the boolean literal must begin with an uppercase 'T'.
    [ ] While True: | Incorrect. The keyword 'while' must be entirely lowercase; capitalizing the 'W' causes a syntax error.
    [ ] while True | Incorrect. A while loop requires a colon at the end.

----

Question 5
----------

.. multichoice::

    When importing a module using 'from microbit import *', how does it affect the syntax prefix for functions like display.scroll()?
    [x] The 'microbit.' prefix can be entirely omitted. | Correct. Using a wildcard import allows shorter forms like display.scroll().
    [ ] The prefix must be changed to 'microbit*.' | Incorrect. The asterisk is an import syntax operator and cannot be appended to object reference paths.
    [ ] The full prefix 'microbit.display.scroll()' becomes mandatory. | Incorrect. The long prefix is used when the module is imported via 'import microbit'.
    [ ] The prefix must be replaced with 'mb.' | Incorrect. An alias like 'mb' is only available if explicitly defined using an 'as' clause.

----

Question 6
----------

.. multichoice::

    If you want to pause your program execution for exactly 2 seconds, which code statement should you use?
    [x] sleep(2000) | Correct. The sleep function takes an argument in milliseconds, and 2000 milliseconds equals 2 seconds.
    [ ] sleep(2) | Incorrect. Passing 2 will only pause the script for 2 milliseconds.
    [ ] sleep(20) | Incorrect. This would result in a pause of 20 milliseconds.
    [ ] sleep(0.2) | Incorrect. Decimal numbers are valid, but 0.2 represents less than one millisecond, not two seconds.

----

Question 7
----------

.. multichoice::

    What parameter unit is accepted by the sleep() function in MicroPython?
    [x] Milliseconds | Correct. The documentation specifies that sleep values represent time intervals measured in milliseconds.
    [ ] Seconds | Incorrect. Standard Python modules like 'time' use seconds, but the Micro:bit's direct sleep function uses milliseconds.
    [ ] Minutes | Incorrect. Minutes are far too large of a base unit for precise hardware runtime control setups.
    [ ] Microseconds | Incorrect. Microseconds are smaller than milliseconds and are not the primary unit for this basic sleep call.

----

Question 8
----------

.. multichoice::

    How are lines grouped inside a while-loop structure to show they belong inside the loop block?
    [x] They are indented, typically using a tab key or 4 spaces. | Correct. Python relies on clean whitespace indentation blocks to group statements together.
    [ ] They must be wrapped inside curly braces {}. | Incorrect. Curly braces are used to denote blocks in languages like C or Java, but not in Python.
    [ ] They must end with a semicolon (;). | Incorrect. Semicolons are used to separate multiple statements on a single line.
    [ ] They are placed entirely on a single line separated by commas. | Incorrect. While loops can stretch across multiple lines, and layout structures demand independent row indentation.

----

Question 9
----------

.. multichoice::

    If you need a secondary pause to last for a quarter of a second, what value should be passed to the sleep statement?
    [x] sleep(250) | Correct. Since 1000 milliseconds equals one second, a quarter of that duration is exactly 250 milliseconds.
    [ ] sleep(0.25) | Incorrect. Passing 0.25 pauses for a quarter of one millisecond.
    [ ] sleep(25) | Incorrect. This would result in a pause lasting 25 milliseconds, which is only 1/40th of a second.
    [ ] sleep(2.5) | Incorrect. This represents two and a half milliseconds rather than a quarter of a whole second.

----

Question 10
-----------

.. multichoice::

    According to standard code layout principles, when are 2 blank lines used after importing modules instead of 1?
    [x] When the imports are immediately followed by top-level classes or function definitions. | Correct. The documentation points out that advanced structures like classes require two surrounding blank spaces.
    [ ] When the program code is running on older Micro:bit hardware versions. | Incorrect. Spacing styles are determined by language readability rules, completely independent of hardware version iterations.
    [ ] When you want to stop a while loop from running indefinitely. | Incorrect. Whitespace changes formatting appearance but does not alter logical loop stopping conditions.
    [ ] Every time you use an asterisk in an import statement. | Incorrect. A single blank line is the default setup for normal procedural statements following a wildcard import.