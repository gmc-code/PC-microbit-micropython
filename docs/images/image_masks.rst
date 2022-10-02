====================================================
Photo-editing techniques: image masks
====================================================

Masks
----------

| Masks are a list of values used to adjust the brightness of each pixel.
| The sample mask below is an array made up of 5 lists of 5 values.
| It is generally easier to lay the mask out in the 5 by 5 pattern like the LEDS on the microbit.

.. code-block:: python

    down_right_mask = [
        [9, 8, 7, 6, 5],
        [8, 7, 6, 5, 4],
        [7, 6, 5, 4, 3],
        [6, 5, 4, 3, 2],
        [5, 4, 3, 2, 1],
    ]

| Each value in the array is designed to be multiplied by the corresponding pixel brightness (then divided by 9) to get new pixel brightnesses. 
| The value for each pixel can be obtained using list indexing.
| Using an index of 0, down_right_mask[0] gives the list, [9, 8, 7, 6, 5].
| Using an index of 1 on this list, down_right_mask[0][1], gives 8.
| Each indexed value in the array, array[y][x] corresponds to a pixel at position x, y.

| The function, **get_masked_image_array(img, mask)**, takes an image, **img**, gets its image array using **get_image_array(img)**, does the multiplications and returns an image array.

.. code-block:: python
        
    from microbit import *


    def get_image_array(img):
        img_repr = repr(img)
        img_str = img_repr[7:-3]
        img_str = img_str.replace(":", "")
        img_array = [int(x) for x in img_str]
        return img_array


    def get_masked_image_array(img, mask):
        img_array = get_image_array(img)
        masked_img_array = list()
        for y in range(5):
            for x in range(5):
                mask_val = mask[y][x]
                img_val = img_array[y * 5 + x]
                new_img_val = min(9, int(mask_val * img_val / 9))
                masked_img_array.append(new_img_val)
        return masked_img_array


| Finally, **get_masked_image(img, mask)**, put these steps together and returns the masked image.

.. code-block:: python
        
    from microbit import *

    def get_masked_image(img, mask):
        masked_img_array = get_masked_image_array(img, mask)
        return Image(5, 5, bytearray(masked_img_array))

----

| The example below applies the **down_right_mask** mask to the TSHIRT image.

.. code-block:: python
        
    from microbit import *

    down_right_mask = [
        [9, 8, 7, 6, 5],
        [8, 7, 6, 5, 4],
        [7, 6, 5, 4, 3],
        [6, 5, 4, 3, 2],
        [5, 4, 3, 2, 1],
    ]


    def get_image_array(img):
        img_repr = repr(img)
        img_str = img_repr[7:-3]
        img_str = img_str.replace(":", "")
        img_array = [int(x) for x in img_str]
        return img_array


    def get_masked_image_array(img, mask):
        img_array = get_image_array(img)
        masked_img_array = list()
        for y in range(5):
            for x in range(5):
                mask_val = mask[y][x]
                img_val = img_array[y * 5 + x]
                new_img_val = min(9, int(mask_val * img_val / 9))
                masked_img_array.append(new_img_val)
        return masked_img_array


    def get_masked_image(img, mask):
        masked_img_array = get_masked_image_array(img, mask)
        return Image(5, 5, bytearray(masked_img_array))


    img = Image.TSHIRT
    while True:
        img_masked = get_masked_image(img, down_right_mask)
        display.show(img)
        sleep(800)
        display.show(img_masked)
        sleep(800)

----

Example Masks
---------------

| Some sample masks are provided here.


.. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: right_mask

                .. code-block:: python

                    right_mask = [
                        [9, 7, 5, 3, 1],
                        [9, 7, 5, 3, 1],
                        [9, 7, 5, 3, 1],
                        [9, 7, 5, 3, 1],
                        [9, 7, 5, 3, 1],
                    ]

            .. tab-item:: left_mask

                .. code-block:: python

                    left_mask = [
                        [1, 3, 5, 7, 9],
                        [1, 3, 5, 7, 9],
                        [1, 3, 5, 7, 9],
                        [1, 3, 5, 7, 9],
                        [1, 3, 5, 7, 9],
                    ]

            .. tab-item:: down_mask

                .. code-block:: python

                    down_mask = [
                        [9, 9, 9, 9, 9],
                        [7, 7, 7, 7, 7],
                        [5, 5, 5, 5, 5],
                        [3, 3, 3, 3, 3],
                        [1, 1, 1, 1, 1],
                    ]

            .. tab-item:: up_mask

                .. code-block:: python

                    up_mask = [
                        [1, 1, 1, 1, 1],
                        [3, 3, 3, 3, 3],
                        [5, 5, 5, 5, 5],
                        [7, 7, 7, 7, 7],
                        [9, 9, 9, 9, 9],
                    ]

            .. tab-item:: outwards_mask

                .. code-block:: python

                    outwards_mask = [
                        [4, 4, 4, 4, 4],
                        [4, 7, 7, 7, 4],
                        [4, 7, 9, 7, 4],
                        [4, 7, 7, 7, 4],
                        [4, 4, 4, 4, 4],
                    ]

            .. tab-item:: duller1_mask

                .. code-block:: python

                    duller1_mask = [
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                        [1, 1, 1, 1, 1],
                    ]

            .. tab-item:: duller5_mask

                .. code-block:: python

                    duller5_mask = [
                        [5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5],
                        [5, 5, 5, 5, 5],
                    ]



----

.. admonition:: Tasks

    #.  Write code apply a right mask to PACMAN.
    #.  Write code apply a left mask to GHOST.
    #.  Write code apply a up mask to RABBIT.
    #.  Write code apply a down mask to PITCHFORK.
    

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-containera 

            .. tab-set::

                .. tab-item:: Q1

                    Write code apply a right mask to PACMAN.

                    .. code-block:: python

                        from microbit import *
