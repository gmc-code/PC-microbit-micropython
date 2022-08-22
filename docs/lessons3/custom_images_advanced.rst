====================================================
Custom images advanced
====================================================

.. py:module:: display

Image()
-----------------------------

| The basic syntax for showing an image is:

.. py:function:: Image()

    | Returns an empty image object, with each pixel of brightness 0.
    | **Image()** is equivalent to:
    | Image(
        '00000:'
        '00000:'
        '00000:'
        '00000:'
        '00000:'
        )

----

Invert
-----------------------------

| The basic syntax for showing an image is:

.. py:function:: Image()

    | Returns an empty image object, with each pixel of brightness 0.
    | **Image()** is equivalent to:
    | Image(
        '00000:'
        '00000:'
        '00000:'
        '00000:'
        '00000:'
        )

.. code-block:: python

    from microbit import *
    

    # Create the "flash" animation frames. Can you work out how it's done?
    flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

    while True:
        if button_a.was_pressed():
            display.show(flash, delay=100, wait=False)
        if button_b.was_pressed():
            display.show(flash, delay=300, wait=False)

