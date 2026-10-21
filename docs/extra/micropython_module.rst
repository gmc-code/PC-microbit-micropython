==========================
micropython module
==========================

.. py:module:: micropython

| Access and control MicroPython internals.
| See: `<https://microbit-micropython.readthedocs.io/en/stable/micropython.html>`_
| Some useful functions from the micropython module are below.

----

mem_info
-------------

.. py:function:: mem_info([verbose])

    Print information about the memory currently being used.
    If ``verbose`` is given, extra information is printed.

| Use the REPL to see the printout.

.. code-block:: python

    from microbit import *
    import micropython

    micropython.mem_info()

----

const
-------------

.. py:function:: const(expr)

    Mark a value as a constant that will not change.
    MicroPython can then substitute the value directly into the code, which saves memory.
    Constant names are usually written in capitals.

.. code-block:: python

    from microbit import *
    from micropython import const

    DELAY = const(500)

    while True:
        display.show(Image.HEART)
        sleep(DELAY)
        display.show(Image.HEART_SMALL)
        sleep(DELAY)

----

opt_level
-------------

.. py:function:: opt_level([level])

    Set or get the optimisation level used when compiling scripts.
    Called with no argument, it returns the current level.

.. code-block:: python

    from microbit import *
    import micropython

    # print(micropython.opt_level())
    display.scroll(str(micropython.opt_level()), delay=80)


