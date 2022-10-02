====================================================
Oversize Byte array images
====================================================

Wide array
----------------------------------------------------------

| An example of a wide array is shown below.
| It has 5 rows, but 21 columns.
| Each row has the same pixel brightness pattern.
| The pixel brightness is a gradient form left to right of decreasing brightness then increasing brightness.
| The last 5 columns match the first 5 columns to make sure that a sideways animation is smooth.
| After the last 5 columns are displayed, the next image will be the first 5 columns or vica versa.

.. code-block:: python

    from microbit import *

    wide_arr = [
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
    ]

| The wise_arr list has to be converted to the form required to be used by the bytearray function.
| Below is the first draft of code that animates the array from right to left.

.. code-block:: python

    from microbit import *

    wide_arr = [
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
    ]
    width = len(wide_arr[0])
    img_array = list()
    for y in range(5):
        for x in range(width):
            img_array.append(wide_arr[y][x])
            
    wide_img = Image(width, 5, bytearray(img_array))

    while True:
        for i in range(width - 5):
            shown_img = wide_img.shift_left(i)
            display.show(shown_img)
            sleep(100)

| Modify the code ot use a function that returns the **wide_img** from the **wide_arr**.
| Modify the list building to use a list comprehension with teh next for loop.

