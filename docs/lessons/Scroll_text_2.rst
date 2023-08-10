====================================================
EXT: Scroll text
====================================================

.. py:module:: display

display.scroll full syntax
----------------------------------------

| The use of the wait parameter is useful when wanting to scroll text and play sounds at the same time.

.. py:function:: scroll(value, delay=150, \*, wait=True, loop=False, monospace=False)

    | Scrolls ``value`` horizontally on the display.
    | ``value`` can be an integer or float (a decimal) or a string.
    | The ``delay`` parameter controls how fast the text scrolls.
    | The default delay is 150ms. When no delay is specified the default of 150ms is used.

    The use of ``\*,`` in the syntax is to indicate that for those parameters after it, ``wait``, ``loop`` and ``monospace``, the arguments must be specified using their keyword. e.g ``wait=True`` is needed; not simply ``True``.

    If ``wait`` is ``True``, this function will block until the animation is finished.
    If ``wait`` is ``False``, the animation will happen in the background.

    If ``loop`` is ``True``, the animation will repeat forever.

    If ``monospace`` is ``True``, the characters will all take up 5 pixel-columns
    in width, otherwise there will be exactly 1 blank pixel-column between each
    character as they scroll.

----

.. admonition:: Exercise

    1. Experiment with the named parameters by trying them out with True or False to see what effect they have.
    2. Experiment with scrolling text using ``wait=False`` and playing sounds.

