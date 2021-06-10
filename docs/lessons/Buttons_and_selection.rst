====================================================
Buttons and selection
====================================================

See https://microbit-micropython.readthedocs.io/en/latest/tutorials/buttons.html

----

Button is pressed
----------------------------------------

| ``button_a.is_pressed()`` returns ``True`` if the A button is being pressed or ``False`` if not.
| ``button_b.is_pressed()`` returns ``True`` if the B button is being pressed or ``False`` if not.

----

Selection
----------------------------------------

| ``if``, ``elif`` and ``else`` provide choices or branches in the code.
| Each end with a colon, ``:``.
| ``if``, ``elif`` have a condition that returns ``True`` or ``False``. Their indented code block runs if the condition is True.
| Multiple  ``elif`` can be used to provide more choices.
| The ``else`` block only runs if all hte previous conditions were ``False``.

----

If
----------------------------------------

| The code below checks if the A button is pressed and displays "A" if it is.

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show("A")
        sleep(200)

----

If else
----------------------------------------

| The code below checks if the A button is pressed and displays "A" if it is or "X" if not.

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show("A")
        else:
            display.show("X")
        sleep(200)

----

If elif
----------------------------------------

| The code below checks if the A button is pressed and displays "A" if it is.
| If A is not pressed, the code then checks if the B button is pressed and displays "B" if it is.

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show("A")
        elif button_b.is_pressed():
            display.show("B")
        sleep(200)

----

If elif else
----------------------------------------

| The code below checks if the A button is pressed and displays "A" if it is.
| If A is not pressed, the code then checks if the B button is pressed and displays "B" if it is.
| If neither A not B is pressed, "X" is displayed.

.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed():
            display.show("A")
        elif button_b.is_pressed():
            display.show("B")
        else:
            display.show("X")
        sleep(200)


----

If elif elif else
----------------------------------------

| The code below first checks whether both buttons are pressed. 
| The logical keyword ``and`` requires both conditions to be True for the combined condition to be True.
| If either button is not pressed the combined condition with be False.


.. code-block:: python

    from microbit import *

    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            display.show(Image.ARROW_N)
        elif button_a.is_pressed():
            display.show(Image.ARROW_W)
        elif button_b.is_pressed():
            display.show(Image.ARROW_E)
        else:
            display.show(" ")
        sleep(100)


