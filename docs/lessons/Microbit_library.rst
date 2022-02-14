====================================================
Microbit library
====================================================

Import the microbit library
----------------------------------------

| The microbit requires a library or module for it to work.
| To use that library, always start the microbit code in Mu editor with:

.. code-block:: python

    from microbit import *


----

.. admonition:: Questions

    Describe the error in attempting to import the microbit library.

    #. ``from microbit import``
    #. ``from microbit import*``
    #. ``from microbot import *``
    #. ``from microbit *``

----

| All microbit libraries or modules are imported at the top of the file.
| Always place **2 blank lines** following the the importing of libraries to separate those lines from the rest of the code.
| The PEP8 guide is to have 1 blank line after the library imports, but in more advanced cdoe, when classes or definitions are next, then since they should have 2 blank lines before and after them, it is just simpler to use 2 blank lines are importing.
| For advanced users, see full PEP 8 guide at: https://www.python.org/dev/peps/pep-0008/

----

| For other forms of importing libraries see:
| https://www.w3schools.com/python/python_modules.asp

.. Warning:: 

    | Importing using ``from module_name import *`` is not recommended for general python use.
    | It is used here to keep the microbit syntax shorter.

----

Micropython API
------------------------------------------

| The main reference for using micropython with the microbit is at:
| https://microbit-micropython.readthedocs.io/en/v1.0.1/index.html
| For new microbits (v2) from 2022 see:
| https://microbit-micropython.readthedocs.io/en/v2-docs/index.html

| References to the microbit library syntax may have ``microbit.`` before the function or method. 
| e.g ``microbit.display.scroll("Hi")``
| This is because it assumes that the microbit library has been imported using ``import microbit``.
| When importing the microbit library using: ``from microbit import *``, the ``microbit.`` prefix is omitted.
| e.g This allows the shorter form, ``display.scroll("Hi")``, instead of the longer form, ``microbit.display.scroll("Hi")``.

| For a list of what is available in the microbit library see:
| https://microbit-micropython.readthedocs.io/en/v1.0.1/microbit_micropython_api.html
| For new microbits (v2) from 2022 see:
| https://microbit-micropython.readthedocs.io/en/v2-docs/microbit_micropython_api.html


