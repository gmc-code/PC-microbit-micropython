====================================================
EXT: Show text
====================================================

.. py:module:: display


display.show full syntax
----------------------------------------

| The use of the wait parameter is useful when wanting to show text and play sounds at the same time.

.. py:function:: show(value, delay=400, \*, wait=True, loop=False, clear=False)

    | Display letters/digits of a string, float, in sequence. 
    | Each letter, digit or image is shown with ``delay`` milliseconds between them. 
    | The default delay is 400ms. When no delay is specified the default of 400ms is used.

    The use of ``\*,`` in the syntax is to indicate that for those parameters after it, ``wait``, ``loop`` and ``clear``, the arguments must be specified using their keyword.

    If ``wait`` is ``True``, this function will block until the animation is finished.
    If ``wait`` is ``False``, the animation will happen in the background.

    If ``loop`` is ``True``, the animation will repeat forever.

    If ``clear`` is ``True``, the display will be cleared after it has finished.

----

.. admonition:: Tasks

    1. Experiment with the named parameters by trying them out with True or False to see what effect they have.
    2. Experiment with showing text using ``wait=False`` and playing sounds.

----

.. admonition:: Tip

    | **display.show** has a ``wait`` parameter that can be set to ``False`` so that displaying information on the microbit display doesn't hold up other actions like driving motors on a bot. 
    | e.g. ``display.show(motor_speed, wait=False)``


