====================================================
Scroll text
====================================================

.. py:module:: display

Display.scroll simple version
----------------------------------------

.. py:function:: scroll(value)

    | Scrolls ``value`` horizontally on the microbit LED display. 
    | If ``value`` is an integer or float (a decimal) it is first converted to a string using ``str()`` automatically.

To scroll the string, "Hi", across the display, use:

.. code-block:: python

    from microbit import *

    display.scroll('Hi')


To scroll the integer, 5, across the display, use:

.. code-block:: python

    from microbit import *

    display.scroll(5)


To scroll the float, 3.14, across the display, use:

.. code-block:: python

    from microbit import *

    display.scroll(3.14)


.. py:function:: scroll(value, delay=150, \*, wait=True, loop=False, monospace=False)

.. py:function:: scroll(value, delay=150, wait=True, loop=False, monospace=False)
Display.scroll full syntax
----------------------------------------



.. py:function:: scroll(value, delay=150, \*, wait=True, loop=False, monospace=False)

    Scrolls ``value`` horizontally on the display. If ``value`` is an integer or float (a decimal) it is
    first converted to a string using ``str()`` automatically. The ``delay`` parameter controls how fast
    the text is scrolling.

    If ``wait`` is ``True``, this function will block until the animation is
    finished, otherwise the animation will happen in the background.

    If ``loop`` is ``True``, the animation will repeat forever.

    If ``monospace`` is ``True``, the characters will all take up 5 pixel-columns
    in width, otherwise there will be exactly 1 blank pixel-column between each
    character as they scroll.

    The use of ``\*,`` in the syntax is to indicate that for those parameters after it, ``wait``, ``loop`` and ``monospace``, the arguments must be specified using their keyword.





----

.. admonition:: Tasks

    Experiment



