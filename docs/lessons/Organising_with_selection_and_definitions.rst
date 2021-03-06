====================================================
Organising with selection and definitions
====================================================

Defintions
----------------------------------------

| Use defintions for one purpose. 
| Defintions help break up lengthy code into smaller well defined blocks.
| Defintions use the same naming conventions as for variables. (See variables in the python section)
| Defintions start with the ``def`` keyword.
| All the code for a definition is indented.
| Below is an example of a defition that scrolls some text and displays an image.
| The defintion is run by calling it via ``doA()``.

.. code-block:: python

    from microbit import *
    
    def doA():
        display.scroll('A')
        display.show(Image.HAPPY)

        doA()

----

Organising blocks into definitions
----------------------------------------

| Compare the two code examples below. 
| The first example does not have any definitions.
| The second example takes each block of code in the various branches of the if block and reallocates tehm to separate definitions.
| This makes the main block of code in the ``while True`` loop more compact and more readable.
| Each definition block can be easily edited and changed.


| Basic unorganised code:

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.scroll('A')
            display.show(Image.HAPPY)
        elif button_b.is_pressed():
            display.scroll('B')
            display.show(Image.SAD)
        else:
            display.scroll('')
        sleep(1000)

| Organised code using definitions:

.. code-block:: python

    from microbit import *

    def doA():
        display.scroll('A')
        display.show(Image.HAPPY)

    def doB():
        display.scroll('B')
        display.show(Image.SAD)

    def doC():
        display.scroll('C')

    while True:
        if button_a.is_pressed():
            doA()
        elif button_b.is_pressed():
            doB()
        else:
            doC()
        sleep(1000)