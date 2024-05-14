====================================================
Organising with selection and definitions
====================================================

Definitions
----------------------------------------

| Definitions help break up lengthy code into smaller well defined blocks.
| Definitions use the same naming conventions as for variables. In general, use lowercase letters.

| Rules for Python variable names:

    • A variable name must start with a letter or the underscore character
    • A variable name cannot start with a number
    • A variable name can only contain alpha-numeric characters (A-z, 0-9) and underscores ( _ )
    • Variable names are case-sensitive (``age``, ``Age`` and ``AGE`` are three different variables)

| Definitions start with the ``def`` keyword.
| All the code for a definition is indented.
| Below is an example of a definition that scrolls some text and displays an image.
| The definition is run by calling it via ``doA()``.

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
| The second example takes each block of code in the various branches of the if block and reallocates them to separate definitions.
| This makes the main block of code in the ``while True`` loop more compact and more readable.
| Each definition block can be easily edited and changed.
| Reorganising the code is called **refactoring**.

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

| Re-organised code using definitions:

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

| Side by side comparison:

.. image:: images/def_reorganised.png
    :scale: 80 %
    :align: center

----

.. admonition:: Tasks

    1.  Reorganise the code below to follow the structure of the examples above.

        .. code-block:: python
            
            from microbit import *

            while True:
                if button_a.is_pressed():
                    for char in 'go team':
                        display.scroll(char, delay=80)
                elif button_b.is_pressed():
                    for sport in ['swimming', 'rowing', 'canoeing']:
                        display.scroll(sport, delay=80)
                else:
                    display.clear()

    2.  Reorganise the code below to follow the structure of the examples above.

        .. code-block:: python
            
            from microbit import *

            while True:
                if button_a.is_pressed():
                    for num in range(1, 10, 2):
                        display.scroll(num, delay=80)
                elif button_b.is_pressed():
                    for num in range(8, -1, -2):
                        display.scroll(num, delay=80)
                else:
                    display.clear()

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Reorganise the code below to follow the structure of the examples above.

                .. code-block:: python

                    from microbit import *


                    def doA():
                        for char in 'go team':
                            display.scroll(char, delay=80)


                    def doB():
                        for sport in ['swimming', 'rowing', 'canoeing']:
                                display.scroll(sport, delay=80)


                    def doC():
                        display.clear()
                        

                    while True:
                        if button_a.is_pressed():
                            doA()
                        elif button_b.is_pressed():
                            doB()
                        else:
                            doC()

            .. tab-item:: Q2

                Reorganise the code below to follow the structure of the examples above.

                .. code-block:: python

                    from microbit import *


                    def doA():
                        for num in range(1, 10, 2):
                            display.scroll(num, delay=80)


                    def doB():
                        for num in range(8, -1, -2):
                            display.scroll(num, delay=80)


                    def doC():
                        display.clear()
                        

                    while True:
                        if button_a.is_pressed():
                            doA()
                        elif button_b.is_pressed():
                            doB()
                        else:
                            doC()




