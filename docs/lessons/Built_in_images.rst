====================================================
Built in images
====================================================

| The microbit library contains several built in images.
| e.g ``Image.HEART``
| The ``Image`` object must have a capital ``I``.
| The built in image name must be in capitals.  e.g ``HEART`` not ``heart``.
| No quotation marks are used. e.g ``Image.HEART`` not ``'Image.HEART'``.
| The same syntax that was used to show text can be used for images.
| When typing in ``Image.``, as soon as the stop is typed a drop list of images will be displayed in Mu editor to allow selection of an image.

----

Display.show a built in Image
----------------------------------------

.. py:function:: show(image)

    | Display an image.

| The code below displays a heart.

.. code-block:: python

    from microbit import *


    display.show(Image.HEART)

----

.. admonition:: Tasks

    #. Write code to show an ARROW_N.    
    #. Write code to show a GIRAFFE.   
    #. Write code to show a SMILE.   

----

Display.show a list of images
----------------------------------------

| A list of images can be displayed in sequence.

.. py:function:: show(imagelist, delay=400)

    | Display images from a list in sequence.
    | Each image in a list of images is shown with ``delay`` milliseconds between them.

.. code-block:: python

    from microbit import *


    display.show([Image.HAPPY, Image.SMILE, Image.SAD, Image.CONFUSED, Image.ANGRY], delay=500)

----

.. admonition:: Tasks

    #. Write code to show a list of 3 different animals with an 0.5 sec delay between them.    
    #. Write code to show a list of 4 different arrows with an 0.4 sec delay between them.   
    #. Write code to show a list of 3 different shapes with an 0.3 sec delay between them.    

----

Image lists
----------------------------------------

| When the list of images is more than a few, it is usual to put the list in a variable.
| The code below displays a list of shapes, so the vaibale name chosen is ``shape_list``.

.. code-block:: python

    from microbit import *


    shape_list = [
        Image.TRIANGLE,
        Image.TRIANGLE_LEFT,
        Image.DIAMOND,
        Image.DIAMOND_SMALL,
        Image.SQUARE,
        Image.SQUARE_SMALL
    ]
    display.show(shape_list, delay=100)

----

.. admonition:: Tasks

    #. Write code to use a variable, ``animal_list``, to show a list of 3 different animals with an 0.5 sec delay between them.    
    #. Write code to use a variable to show a list of 4 different arrows with an 0.4 sec delay between them.   
    #. Write code to use a variable to show a list of 3 different music images with an 0.3 sec delay between them.

----

Built-in Image lists
----------------------------------------

| When the list of images is more than a few, it is usual to put the list in a variable.
| The code below displays the built-in list of clock images.
| The built-in lists of images are called ``Image.ALL_CLOCKS`` and ``Image.ALL_ARROWS``:

.. code-block:: python

    from microbit import *


    display.show(Image.ALL_CLOCKS, loop=True, delay=100)

----

.. admonition:: Tasks

    #. Write code to display the images in the built-in image list: ``Image.ALL_ARROWS``.    

----

Image sentences
----------------------------------------

| The code below makes a sentence using words and images.
| Delays, using ``sleep(300)`` are used to prevent it from being too fast to see.

.. code-block:: python

    from microbit import *


    while True:
        display.scroll('I')
        sleep(300)
        display.show(Image.HEART)
        sleep(300)
        display.show(Image.GIRAFFE)
        sleep(300)

----

.. admonition:: Tasks

    #. Write a few different code sentences combining words and images.

----

All Images
----------------------------------------

| The code below displays all the built in images.

.. code-block:: python

    from microbit import *


    built_in_images = [Image.HEART, Image.HEART_SMALL,
                        Image.HAPPY, Image.SMILE, Image.SAD, Image.CONFUSED,
                        Image.ANGRY, Image.ASLEEP, Image.SURPRISED, Image.SILLY,
                        Image.FABULOUS, Image.MEH, Image.YES, Image.NO,
                        Image.CLOCK12, Image.CLOCK11, Image.CLOCK10, Image.CLOCK9,
                        Image.CLOCK8, Image.CLOCK7, Image.CLOCK6, Image.CLOCK5,
                        Image.CLOCK4, Image.CLOCK3,Image.CLOCK2, Image.CLOCK1,
                        Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE,
                        Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW,
                        Image.TRIANGLE, Image.TRIANGLE_LEFT, Image.CHESSBOARD,
                        Image.DIAMOND, Image.DIAMOND_SMALL, Image.SQUARE,
                        Image.SQUARE_SMALL, Image.RABBIT, Image.COW,
                        Image.MUSIC_CROTCHET, Image.MUSIC_QUAVER,
                        Image.MUSIC_QUAVERS, Image.PITCHFORK, Image.XMAS,
                        Image.PACMAN, Image.TARGET, Image.TSHIRT,
                        Image.ROLLERSKATE, Image.DUCK, Image.HOUSE, Image.TORTOISE,
                        Image.BUTTERFLY, Image.STICKFIGURE, Image.GHOST, Image.SWORD,
                        Image.GIRAFFE, Image.SKULL, Image.UMBRELLA, Image.SNAKE]

    while True:
        display.show(built_in_images, delay=100)

