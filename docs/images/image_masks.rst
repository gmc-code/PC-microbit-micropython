====================================================
Image masks
====================================================

Masks
----------

| Masks are a list of values used to adjust the brightness of each pixel.
| The sample mask below is an array made up of 5 lists of 5 values.
| Each value in the array is multiplied by the corresponding pixel brightness to get new pixel brightnesses. 
| Each vvalue can be obtained using list indexing.
| down_right_mask[0] gives the list, [9, 8, 7, 6, 5].
| Indexing this list, down_right_mask[0][1], gives 8.
| Each indexed value the array, array[y][x] corresponds to a pixel at position x, y.

.. code-block:: python

    down_right_mask = [
        [9, 8, 7, 6, 5],
        [8, 7, 6, 5, 4],
        [7, 6, 5, 4, 3],
        [6, 5, 4, 3, 2],
        [5, 4, 3, 2, 1],
    ]
