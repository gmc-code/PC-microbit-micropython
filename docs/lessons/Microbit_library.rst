====================================================
Microbit library
====================================================

Import the microbit library
----------------------------------------

| The microbit requires a library for it to work.
| To use that library, always start microbit code in Mu with:

.. code-block:: python

    from microbit import *

----

Micropython API
------------------------------------------

The main reference for using micropython with the microbit is at: https://microbit-micropython.readthedocs.io/en/v2-docs/index.html

Some references to using the microbit library have ``microbit.`` before the function or method. When importing the microbit library using: ``from microbit import *``, the ``microbit.`` prefix must be omitted.

e.g Use ``display.scroll("Hi")`` instead of ``microbit.display.scroll("Hi")``

For a list of what is available in the microbit library see: https://microbit-micropython.readthedocs.io/en/v2-docs/microbit_micropython_api.html

