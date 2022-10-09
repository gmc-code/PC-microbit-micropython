==========================
gc Module
==========================

| See: https://docs.micropython.org/en/latest/library/gc.html

.. py:function::  gc.mem_alloc()

    Return the number of bytes of heap RAM that are allocated.

.. code-block:: python

    from microbit import *
    import gc

    display.scroll(gc.mem_alloc())


.. py:function::  gc.mem_alloc()

    Return the number of bytes of available heap RAM, or -1 if this amount is not known.

.. code-block:: python

    from microbit import *
    import gc

    display.scroll(gc.mem_free())