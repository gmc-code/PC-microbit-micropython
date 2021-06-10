====================================================
Show_text
====================================================

Display.show syntax
----------------------------------------

.. py:module:: display

.. py:function:: show(value, delay=400, \*, wait=True, loop=False, clear=False)

    If ``value`` is a string, float or integer, display letters/digits in sequence.
    Otherwise, if ``value`` is an iterable sequence of images, display these images in sequence.
    Each letter, digit or image is shown with ``delay`` milliseconds between them.

    If ``wait`` is ``True``, this function will block until the animation is
    finished, otherwise the animation will happen in the background.

    If ``loop`` is ``True``, the animation will repeat forever.

    If ``clear`` is ``True``, the display will be cleared after the iterable has finished.

    Note that the ``wait``, ``loop`` and ``clear`` arguments must be specified
    using their keyword.

.. note::

    If using a generator as the ``iterable``, then take care not to allocate any memory
    in the generator as allocating memory in an interrupt is prohibited and will raise a
    ``MemoryError``.

