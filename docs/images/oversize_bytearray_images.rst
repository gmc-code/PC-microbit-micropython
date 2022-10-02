====================================================
Oversize Byte array images
====================================================

Wide array
----------------------------------------------------------

| An example of a wide array is shown below.
| It has 5 rows, but 20 columns.
| Each row has the same pixel brightness pattern.
| The pixel brightness is a gradient from left to right of decreasing brightness then increasing brightness.
| The last 4 columns match the first 4 columns to make sure that a sideways animation is smooth.
| After the last 4 columns are displayed, the next image will be the first 5 columns or vica versa.

.. code-block:: python

    from microbit import *

    wide_arr = [
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
    ]

| The **wide_arr** list has to be converted to the form (a single list with no nesting) required to be used by the bytearray function.
            
| A simplest approach is to use the extend method for each nested list indexed as **wide_arr[y]**.

.. code-block:: python

    from microbit import *


    wide_arr = [
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
    ]

    img_array = list()
    for y in range(5):
        img_array.extend(wide_arr[y])


| Below is the first draft of code that animates the array from right to left.
| The wide_img is first made using **wide_img = Image(width, 5, bytearray(img_array))**
| Then it is shifted by i pixels (where i is from 0 to 15) to the left using **wide_img.shift_left(i)**
| Note that in the range function **(width - 3)** the aim is to get the last 5 pixels: 8, 9, 8, 7, 6.
| The end 6 corresponds to the index given by **width - 1**. 
| The end frame starts with the 8 which corresponds to the index given by **width - 5**. 
| Since range stops 1 before the stop value, **range(width - 4)** is needed. 

.. code-block:: python

    from microbit import *

    wide_arr = [
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
    ]

    width = len(wide_arr[0])
    img_array = list()
    for y in range(5):
        img_array.extend(wide_arr[y])
            
    wide_img = Image(width, 5, bytearray(img_array))

    while True:
        for i in range(width - 4):
            shown_img = wide_img.shift_left(i)
            display.show(shown_img)
            sleep(100)

----

.. admonition:: Tasks

    #. Modify the code to use a function that returns the **wide_img** from the **wide_arr**.
 
    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code to use a function that returns the **wide_img** from the **wide_arr**.

                    .. code-block:: python
                        
                        from microbit import *


                        wide_arr = [
                            [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
                            [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
                            [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
                            [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
                            [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6],
                        ]


                        def get_wide_img_from_array(wide_arr):
                            img_array = list()
                            for y in range(5):
                                img_array.extend(wide_arr[y])
                            width = len(wide_arr[0])
                            wide_img = Image(width, 5, bytearray(img_array))
                            return wide_img


                        wide_img = get_wide_img_from_array(wide_arr)
                        width = len(wide_arr[0])
                        while True:
                            for i in range(width - 4):
                                shown_img = wide_img.shift_left(i)
                                display.show(shown_img)
                                sleep(100)


----

.. admonition:: Exercise

    #. Design your own wide array and explore shifting left.
 
| An example is a diagonal wide array:

.. code-block:: python

    wide_arr = [
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5],
        [8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4],
        [7, 6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3],
        [6, 5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2],
        [5, 4, 3, 2, 1, 2, 3, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    ]


----

Tall array
----------------------------------------------------------

| An example of a tall array is shown below.
| It has 5 rows, but 20 columns.

.. code-block:: python

    from microbit import *

    tall_arr = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5],
        [6, 6, 6, 6, 6],
        [7, 7, 7, 7, 7],
        [8, 8, 8, 8, 8],
        [9, 9, 9, 9, 9],
        [9, 9, 9, 9, 9],
        [8, 8, 8, 8, 8],
        [7, 7, 7, 7, 7],
        [6, 6, 6, 6, 6],
        [5, 5, 5, 5, 5],
        [4, 4, 4, 4, 4],
        [3, 3, 3, 3, 3],
        [2, 2, 2, 2, 2],
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4],
    ]

    height = len(tall_arr)
    img_array = list()
    for y in range(height):
        for x in range(5):
            img_array.append(tall_arr[y][x])
    tall_img = Image(5, height, bytearray(img_array))

    while True:
        for i in range(height - 5):
            shown_img = tall_img.shift_up(i)
            display.show(shown_img)
            sleep(100)

----

.. admonition:: Exercise

    #. Modify the code to use a function that returns the **tall_img** from the **tall_arr**.
    #. Design your own tall array and explore shifting up.
 
----

.. admonition:: Exercise

    #. Design your own big array (tall and wide), modify a function to produce the image from it, and explore shifting up and right in combination.
 
 





