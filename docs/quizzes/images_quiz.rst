====================================================
Built-in Images Quiz
====================================================

Question 1
----------

.. multichoice::

    How many built-in images are roughly available within the microbit library according to the documentation?
    [ ] Around 10 images | Incorrect. There are far more than 10 built-in choices.
    [ ] Exactly 25 images | Incorrect. The library offers a much wider variety of pre-drawn selections.
    [x] Over 60 images | Correct. The library contains over 60 built-in images that have specific names.
    [ ] More than 500 images | Incorrect. While extensive, it does not contain hundreds of images by default.

----

Question 2
----------

.. multichoice::

    Which of the following lines correctly displays a built-in heart image on the micro:bit?
    [x] display.show(Image.HEART) | Correct. This uses a capital 'I' for Image, all uppercase for HEART, and no quotes.
    [ ] display.show(image.HEART) | Incorrect. The Image object must be written with a capital 'I'.
    [ ] display.show(Image.heart) | Incorrect. The built-in image name must be written in full capitals.
    [ ] display.show('Image.HEART') | Incorrect. No quotation marks should be used around the image reference.

----

Question 3
----------

.. multichoice::

    According to standard code naming principles outlined in the text, what case style should be used for naming constants?
    [ ] lower case letters | Incorrect. Lowercase is typically reserved for variables and functions.
    [ ] CapWords formatting | Incorrect. CapWords (CamelCase) is standard formatting for class structures.
    [x] ALLCAPS formatting | Correct. Naming principles specify that constants should be written in ALLCAPS, such as PIN or HEART.
    [ ] snake_case with numbers | Incorrect. Standard constants avoid mixed or lowercase configurations.

----

Question 4
----------

.. multichoice::

    In Python code architecture, how are the components ``Image`` and ``HEART`` classified?
    [ ] Image is a variable and HEART is a function. | Incorrect. Neither component represents an action function or plain value variable.
    [x] Image is a class and HEART is a constant within that class. | Correct. The text notes that Image with a capital letter behaves as a class, and HEART is a constant within it.
    [ ] Image is a string literal and HEART is a keyword argument. | Incorrect. They lack quotation marks and do not behave as keyword parameters.
    [ ] Both components are considered standard structural variables. | Incorrect. Variables use lower case letters, unlike these components.

----

Question 5
----------

.. multichoice::

    What convenient feature triggers automatically inside the Python Editor when you type ``Image.`` (including the dot)?
    [ ] The code executes and uploads onto your connected micro:bit automatically. | Incorrect. Typing code does not trigger immediate script flashing.
    [ ] The editor highlights the phrase with a syntax error warning instantly. | Incorrect. This is proper syntax and does not prompt warnings.
    [x] A drop list of available images is displayed for easy selection. | Correct. As soon as the stop/dot is typed after Image, a drop list appears to let you pick an image.
    [ ] The editor automatically converts the expression into a text string. | Incorrect. It remains a native object path reference.

----

Question 6
----------

.. multichoice::

    Which function is used to output a built-in image to the micro:bit LED grid?
    [ ] ``display.scroll()`` | Incorrect. Scrolling is primarily for animating text messages across the screen horizontally.
    [x] ``display.show()`` | Correct. The exact same syntax used to show sequential text is utilized to display images.
    [ ] ``display.draw()`` | Incorrect. There is no draw function for displaying standard built-in images.
    [ ] ``display.image()`` | Incorrect. Image is a class structure reference, not a direct display function name.

----

Question 7
----------

.. multichoice::

    Look at the following code snippet:

    .. code-block:: python

        from microbit import *

        shape_images = [
                        Image.TRIANGLE,
                        Image.DIAMOND,
                        Image.SQUARE,
                    ]

        while True:
            display.show(shape_images, delay=250)

    What is the outcome when this script runs on the micro:bit?
    [ ] An error occurs because display.show() cannot accept list structures. | Incorrect. Lists are fully supported to create animations.
    [ ] The word "shape_images" scrolls across the display panel horizontally. | Incorrect. It renders the referenced image data types, not text strings.
    [x] The micro:bit plays an animation cycling through a triangle, diamond, and square sequentially. | Correct. Passing an array list of images to display.show() loops through them sequentially.
    [ ] The screen displays all three geometric shapes simultaneously stacked together. | Incorrect. The 5x5 LED matrix can only depict one frame at a time.

----

Question 8
----------

.. multichoice::

    When animating a sequence list of images using ``display.show(object_images, delay=250)``, what does the ``delay`` parameter represent?
    [ ] The duration in seconds that the entire animation loop runs before stopping. | Incorrect. Delay sets a millisecond value, and loops continuously within while structures.
    [x] The time interval in milliseconds between showing each consecutive image frame. | Correct. The delay controls the timing pause separating each listed frame item sequence during playback.
    [ ] The quantity of individual LED lights activated on each step. | Incorrect. LED activation coordinates are mapped by the specific image template layout.
    [ ] The pause duration applied prior to starting the program script. | Incorrect. It determines live runtime animation transition speeds instead.

----

Question 9
----------

.. multichoice::

    Which of the following configurations is an example of a valid built-in object image name according to the tasks in the documentation?
    [ ] Image.triangle | Incorrect. Built-in constants require fully capitalized text strings.
    [ ] Image.ROLLERSKATE_SMALL | Incorrect. Small variations are noted for shapes like DIAMOND_SMALL, but not rollerskate.
    [x] Image.ROLLERSKATE | Correct. Image.ROLLERSKATE is explicitly included under the valid object image listings within the documentation tasks.
    [ ] Image.CHESS_BOARD | Incorrect. The constant name is written together as CHESSBOARD without an underscore separator.

----

Question 10
-----------

.. multichoice::

    Which of the following lists contains only valid geometric shape image names as structured in the documentation exercises?
    [x] Image.TRIANGLE, Image.DIAMOND, Image.SQUARE | Correct. These are all accurately classified as shape constants inside the code challenges.
    [ ] Image.GHOST, Image.SWORD, Image.SKULL | Incorrect. These item constants are categorized as object images rather than shapes.
    [ ] Image.triangle, Image.diamond, Image.square | Incorrect. These options fail because constant names are completely lowercase.
    [ ] Image.TARGET, Image.HOUSE, Image.UMBRELLA | Incorrect. These represent object entities instead of shape models.


