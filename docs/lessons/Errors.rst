====================================================
Mu editor Errors
====================================================

| Working out what has gone wrong and how to fix it is a key part of everyday programming.
| Some errors will not show up using the **check** button, but instead, will be scrolled on the microbit as an error message when the microbit is flashed.
| They usually contains the line number for where you should start to identify and fix the issue.

| The examples below are the common errors that you need to be able to fix quickly.

| A syntax error occurs when the code language is not used properly.
| Press the **check** button in Mu editor to view syntax errors and other errors.

----

Import Errors
====================================================

Library not imported properly
---------------------------------------------

| Normally the full microbit is imported via ``from microbit import *``.

.. code-block:: python

    from microbit import 

| If the askterisk is left out, a red wavy line will be shown at the end of the line and a **Syntax error** is reported.
| It hints that the asterisk, *, is missing.

.. image:: images/import_error_1b.png
    :scale: 50 %

----

Misspelt library: undefined names
-----------------------------------

| If the microbit library is misspelt, then an error occurs, as shown below.

.. code-block:: python

    from microbot import *

.. image:: images/import_error_3.png
    :scale: 50 %

----

Imported library not used
--------------------------

| If the microbit library is imported via ``import microbit``, all microbit code needs to start with ``microbit.``.
| In the code below, the line should be: ``microbit.display.scroll('hello')``.
| If ``microbit.`` is left out, a red wavy line will be shown where the errors are.
| ``display`` will not be recognised since python has not been told that it is in microbit library.
| The microbit library will also appear not to be used.

.. code-block:: python

    import microbit


    display.scroll('hello')

.. image:: images/import_error_2.png
    :scale: 50 %

----

Missing colon
====================================================

If: Missing colon
-----------------------------------

| The correct code is below.
| When the A button is pressed, 'A' will be scrolled across the microbit.

.. code-block:: python

    from microbit import *


    if button_a.is_presed():
        display.scroll('A')

| If the colon is left out from the end of the ``if`` line, ``if button_a.is_presed()`` , an error occurs.

.. code-block:: python

    from microbit import *


    if button_a.is_presed():
        display.scroll('A')

| A red wavy line shown where the colon should have been. 
| A blue wavy line shows where the unexpected indentation occurred.
| The indentation is only needed after a colon.

.. image:: images/if_colon_error.png
    :scale: 50 %

----

else: Missing colon
-----------------------------------

| The correct code is below.
| When the A button is pressed, 'A' will be scrolled.
| If the A button is not pressed, 'X' will be scrolled.

.. code-block:: python

    from microbit import *


    if button_a.is_presed():
        display.scroll('A')
    else:
        display.scroll('X')        

| If the colon is left out from the end of the ``else`` line, an error occurs.

.. code-block:: python

    from microbit import *


    if button_a.is_presed():
        display.scroll('A')
    else
        display.scroll('X')   

| A red wavy line shown where the colon should have been. 
| A blue wavy line shows where the unexpected indentation occurred.
| The indentation is only needed after a colon.

.. image:: images/else_colon_error.png
    :scale: 50 %




----


Variable used which has no value
-----------------------------------

| ``display.scroll('hello')`` will scroll 'hello' across the microbit.
| If 'hello' is not in quotes, it will be treated as a variable.
| If ``display.scroll(hello)`` is used by accident, leaving out the quotes, an **undefined name** error occurs. 

.. code-block:: python

    from microbit import *


    display.scroll(hello)

.. image:: images/undefined_name_1.png
    :scale: 50 %


This can also be fixed by giving the variable a value, as shown below:

.. code-block:: python
    
    from microbit import *


    hello = 'Hi'
    display.scroll(hello)


