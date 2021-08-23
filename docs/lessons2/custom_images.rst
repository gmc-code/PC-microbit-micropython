====================================================
Custom images
====================================================

Image strings
----------------

| The basic syntax for showing an image is:

.. py:function:: show(image)

    | Display an image.


| The image can be a string made up of a 25 integers where each integer is the brightness from 0 to 9, where 0 if off and 9 is full brightness.
| The 25 values are broken up into 5 lines of 5 with a colon between them.
| e.g. Image("11111:33333:55555:77777:99999")

| The code below shows a vertical brightness gradient from the top to the bottom.

.. code-block:: python

    from microbit import *


    display.show(Image("11111:33333:55555:77777:99999"))
    
| The code below shows a diagonal brightness gradient from the top left to the bottom right.

.. code-block:: python

    from microbit import *


    display.show(Image("12345:23456:34567:45678:56789"))

----

.. admonition:: Tasks

    #. Write code for a horizontal brightness gradient from the left to right.
    #. Write code for a vertical brightness gradient from the bottom to the top.
    #. Write code for a diagonal brightness gradient from the bottom left to the top right.   

----

Image strings: line by line
------------------------------

| The vertical gradient Image("11111:33333:55555:77777:99999") can be rewritten so that the 5 rows are lined up under each other like a 5 by 5 grid. Extra spaces can by used to line up each line.

.. code-block:: python

    from microbit import *

    vertical_gradient = Image("11111:"
                              "33333:"
                              "55555:"
                              "77777:"
                              "99999")
    display.show(vertical_gradient)


----

.. admonition:: Tasks

    #. Write code for a diagonal brightness gradient by lining up the 5 rows under each other.   

----

Pixel controls
----------------------------------------

| Each pixel on the 5 by 5 grid can be controlled individually.

.. py:function:: display.set_pixel(x, y, value)

    Set the brightness of the LED at column x and row y to value, which has to be an integer between 0 and 9.


| The variable is then used to display the images: ``display.show(face_list, delay=500)``.

.. code-block:: python

    from microbit import *


    face_list = [Image.HAPPY, Image.SMILE, Image.SAD, Image.CONFUSED, Image.ANGRY]
    while True:
        display.show(face_list, delay=500)


| The code below displays a list of shapes, so the variable name chosen is ``shape_list``.
| Whitespace (tabes, spaces, line endings) are ignored within a list, so a long list can be set out like that below, with all the Images lined up for easy reading.

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
    while True:
        display.show(shape_list, delay=100)

----

.. admonition:: Tasks

    #. Write code to use a variable, ``animal_list``, to show a list of 3 different animals with an 0.5 sec delay between them.    
    #. Write code to use a variable to show a list of 4 different arrows with an 0.4 sec delay between them.   
    #. Write code to use a variable to show a list of 3 different music images with an 0.3 sec delay between them.

----

Built-in Image lists
----------------------------------------

| There are 2 built-in collections of images.
| They are: ``Image.ALL_CLOCKS`` and ``Image.ALL_ARROWS``.
| Both collections have images that follow a clockwise sequence.
| The code below displays the built-in collection of clock images.

.. code-block:: python

    from microbit import *


    while True:
        display.show(Image.ALL_CLOCKS, delay=100)

----

.. admonition:: Tasks

    #. Write code to display the images in the built-in image collection: ``Image.ALL_ARROWS``.

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

----

.. admonition:: Tasks

    #. Edit the built in images list from above to just include animals.
    #. Edit the built in images list from above to just include faces.
    #. Edit the built in images list from above to just include objects.
    #. Edit the built in images list from above to just include shapes.

----

Advanced use of Built-in Image lists
----------------------------------------

| Image.ALL_CLOCKS and Image.ALL_ARROWS are python objects that can be converted to lists of Image objects.
| Once converted to a list of Images, the list can be reversed to so that the images can be displayed in an anticlockwise direction instead of clockwise.

| ``list(Image.ALL_CLOCKS)`` can convert ``Image.ALL_CLOCKS`` to the list: 
| [Image.CLOCK12, Image.CLOCK1, Image.CLOCK2, Image.CLOCK3, Image.CLOCK4, Image.CLOCK5, Image.CLOCK6, Image.CLOCK7, Image.CLOCK8, Image.CLOCK9, Image.CLOCK10, Image.CLOCK11]

| ``list(Image.ALL_ARROWS)`` can convert ``Image.ALL_ARROWS`` to the list:
| [Image.ARROW_N, Image.ARROW_NE, Image.ARROW_E, Image.ARROW_SE, Image.ARROW_S, Image.ARROW_SW, Image.ARROW_W, Image.ARROW_NW]


Reverse direction of list using list slicing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| A list, ``arrow_list``, can be reversed using the slicing technique: ``arrow_list[::-1]``.
| ``arrow_list_anticlockwise = arrow_list[::-1]`` reverses the list and places it in a the variable ``arrow_list_anticlockwise``.

.. code-block:: python

    from microbit import *


    arrow_list = list(Image.ALL_ARROWS)
    arrow_list_anticlockwise = arrow_list[::-1]
    while True:
        display.show(arrow_list_anticlockwise, delay=200)


Reverse direction of list using the reversed function
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| A list, ``clock_list``, can be reversed using the reversed function: ``reversed(clock_list)``.
| The python object obtained from the reversed function can be converted to a list for reuse by using ``list(reversed(clock_list))`` and placing the result in the variable ``clock_list_anticlockwise``.

.. code-block:: python

    from microbit import *


    clock_list = list(Image.ALL_CLOCKS)
    clock_list_anticlockwise = list(reversed(clock_list))
    while True:
        display.show(clock_list_anticlockwise, delay=200)

----

.. admonition:: Tasks

    #. Write code to display all the clock images clockwise then anticlockwise.
    #. Write code to display all the arrow images clockwise then anticlockwise.
