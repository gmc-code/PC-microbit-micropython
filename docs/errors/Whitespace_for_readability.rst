====================================================
Whitespace for Readability
====================================================

Proper use of Whitespace improves readability
-------------------------------------------------------

| Whitespace is properly used to improve readability of lists.
| Whitespace (tabs, spaces, line endings) are ignored within a list, so a long list can be set out like that below, with all the Images lined up for easy reading.
| In setting it out like this, it is the usual practice to have a trailing comma after the last item in the list.

.. code-block:: python
    
    from microbit import *

    shape_list = [
        Image.TRIANGLE,
        Image.TRIANGLE_LEFT,
        Image.DIAMOND,
        Image.DIAMOND_SMALL,
    ]
    while True:
        display.show(shape_list, delay=100)

| Another acceptable version is below, withe the list over 2 lines.
| In setting it out like this, there is no trailing comma after the last item in the list.

.. code-block:: python
    
    from microbit import *

    shape_list = [Image.TRIANGLE, Image.TRIANGLE_LEFT, 
                Image.DIAMOND, Image.DIAMOND_SMALL]
    while True:
        display.show(shape_list, delay=100)