====================================================
Photo-editing techniques: image masks
====================================================

Masks
----------

| Masks are a list of values used to adjust the brightness of each pixel.
| The sample mask below is an array made up of 5 lists of 5 values.
| Each value in the array is designed to be multiplied by the corresponding pixel brightness (then divided by 9) to get new pixel brightnesses. 
| The value for each pixel can be obtained using list indexing.
| Using an index of 0, down_right_mask[0] gives the list, [9, 8, 7, 6, 5].
| Using an index of 1 on this list, down_right_mask[0][1], gives 8.
| Each indexed value the array, array[y][x] corresponds to a pixel at position x, y.

.. code-block:: python

    down_right_mask = [
        [9, 8, 7, 6, 5],
        [8, 7, 6, 5, 4],
        [7, 6, 5, 4, 3],
        [6, 5, 4, 3, 2],
        [5, 4, 3, 2, 1],
    ]

