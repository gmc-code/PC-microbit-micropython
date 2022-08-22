====================================================
Custom images advanced
====================================================

See: https://microbit-micropython.readthedocs.io/en/v2-docs/image.html

Image()
-----------------------------

| The basic syntax for showing creating an Image object is:

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

.. py:function:: Image().invert()

    | Return a new image by inverting the brightness of the pixels in the source image.
    | **Image().invert()** is equivalent to:
    | Image(
        '99999:'
        '99999:'
        '99999:'
        '99999:'
        '99999:'
      )

----

Image of a single string character
-----------------------------------------

.. py:function:: Image(character)

    | Returns an image object that represents the character.


.. code-block:: python

    from microbit import *

    my_image_letter = Image("m")
    my_image_letter2 = Image("w")
    my_image_overlap = my_image_letter + my_image_letter2

    while True:
        if button_a.is_pressed() and button_b.is_pressed():
            display.show(my_image_overlap)
        elif button_a.was_pressed():
            display.show(my_image_letter)
        elif button_b.was_pressed():
            display.show(my_image_letter2)
        sleep(800)

----

.. code-block:: python

    from microbit import *
    

    # Create the "flash" animation frames.
    flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

    while True:
        if button_a.was_pressed():
            display.show(flash, delay=100, wait=False)
        if button_b.was_pressed():
            display.show(flash, delay=300, wait=False)

