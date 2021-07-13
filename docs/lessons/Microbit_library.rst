====================================================
Microbit library
====================================================

Import the microbit library
----------------------------------------

| The microbit requires a library or module for it to work.
| To use that library, always start the microbit code in Mu editor with:

.. code-block:: python

    from microbit import *

| All microbit libraries or modules are imported at the top of the file.
| Always place 2 blank lines following the the importing of libraries to separate those lines form the rest of the code.

| For other forms of importing libraries see:
| https://www.w3schools.com/python/python_modules.asp

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


