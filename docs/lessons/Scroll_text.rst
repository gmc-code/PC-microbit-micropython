====================================================
Scrolling_text
====================================================

Display.scroll syntax
----------------------------------------

.. py:module:: display

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


Display.scroll examples
----------------------------------------

To continuously scroll a string across the display, and do it in the background,
you can use::

.. code-block:: python

    from microbit import *

    display.scroll('Hi')


----

.. admonition:: Tasks

    #. 
