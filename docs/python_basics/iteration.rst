==========================
Iteration
==========================

Iteration is one of the three basic control structures:

#. Sequence (steps in order)
#. Selection (branching using ``if`` ... ``elif`` ... ``else``)
#. Iteration (repetition or looping using ``while`` or ``for``)

Loops
-------------

Loops are a very useful structure in case you want to repeat a certain block of code several times over.
There are two types of loops: ``for`` loops, that keep count of the number of times a block of code is executed, and ``while`` loops which
perform an action until a condition you've specified is no longer true. 

----

For loops
-------------

There are times when you want to do an action a specific number of times, or you need to keep track of how many times it was performed. For example you'd like 
to turn on the LEDs on the uppermost horizontal and rightmost vertical side. You can use a ``for`` loop to change which LED lights up like this:

.. code-block:: python

    from microbit import *

    for i in range (5):
        # set the pixel in column 0, row i to 9 
        display.set_pixel(0, i, 9) 

        # set the pixel in column 4, row i to 9    
        display.set_pixel(4, i, 9)     

Here is another example.  You could use a ``for loop`` to turn on all the LEDs in sequence, one at a time:

.. code-block:: python

    from microbit import *

    display.clear()
    for x in range(0, 5):
        for y in range(0, 5):
            display.set_pixel(x, y, 9)  

The ``for loop`` lets you run a loop a specific number of times using a counter. The outer loop: ``for x in range(0,5):`` will execute the loop five times substituting ``x`` for consecutive values in the range ``0`` to ``4`` each time (in Python and most programming languages, we always start counting from ``0``). The loop will stop before it reaches 5, the final value in the range.

The inner loop: ``for y in range(0,5):`` will run the loop five times substituting ``y`` for consecutive values in the range ``0`` to ``4`` each time. Again, the loop will stop before it reaches the final value in the range.

----

While loops
------------------

One of the most common things you might want to do with a ``while`` loop is to do something forever, that is until the micro:bit
is turned off or reset. Maybe you have programmed your micro:bit with a game or perhaps it is collecting 
temperature data. Here is an example of some code to repeat forever:

.. code-block:: python

    from microbit import *

    while True:
        display.scroll("Hello UCL)

This code will repeatedly display the message ``Hello UCL``. You will likely have at least one ``while True:`` loop in your program
to keep the micro:bit going.

But what if you want to do an action only whilst something is happening? Perhaps you would like to display an image
if the temperature on the micro:bit goes below a certain value so you'll need to test the temperature:

.. code-block:: python

    from microbit import *

    while (temperature() < 18):
        display.scroll(Image.SAD)
        sleep(1000)

    display.show(Image.HAPPY)




