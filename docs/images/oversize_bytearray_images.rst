====================================================
Oversize Byte array images
====================================================

Wide array
----------------------------------------------------------

| An example of a wide array is shown below.
| It has 5 rows, but 21 columns.
| Each row has the same pixel brightness pattern.
| The pixel brightness is a gradient from left to right of decreasing brightness then increasing brightness.
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

| The **wide_arr** list has to be converted to the form (a single list with no nesting) required to be used by the bytearray function.

| This can be done by appending each element of each sublist indexed as **wide_arr[y][x]**.

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
            
| A simpler approach is to use the extend method for each nested list indexed as **wide_arr[y]**.

.. code-block:: python

    from microbit import *


    wide_arr = [
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
    ]

    img_array = list()
    for y in range(5):
        img_array.extend(wide_arr[y])


| Below is the first draft of code that animates the array from right to left.
| The wide_img is first made using **wide_img = Image(width, 5, bytearray(img_array))**
| Then it is shifted by i pixels (where i is from 0 to 15) to the left using **wide_img.shift_left(i)**

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
        img_array.extend(wide_arr[y])
            
    wide_img = Image(width, 5, bytearray(img_array))

    while True:
        for i in range(width - 5):
            shown_img = wide_img.shift_left(i)
            display.show(shown_img)
            sleep(100)

| Modify the code to use a function that returns the **wide_img** from the **wide_arr**.
| Modify the list building to use a list comprehension with teh next for loop.

