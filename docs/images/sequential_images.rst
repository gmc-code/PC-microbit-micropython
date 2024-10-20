==========================
Sequential images
==========================

Feeling images
---------------------------------

| The SAD and HAPPY images are the basis of a sequence of similar images to express how you feel via button pressing.
| 3 new custom images are defined: dejected, better_meh, joy.
| Press the A-button to express more negative feelings.
| Press the B-button to express more positive feelings.


.. code-block:: python

    from microbit import *

    dejected = Image("09090:00000:09990:90009:99999")
    ok = Image("00000:09090:00000:99999:00000")
    joy = Image("09090:00000:99999:90009:09990")

    emotions = [dejected, Image.SAD, ok, Image.HAPPY, joy]
    current_emotion = 2

    while True:
        if button_a.get_presses():
            current_emotion = max(current_emotion - 1, 0)
        elif button_b.get_presses():
            current_emotion = min(current_emotion + 1, 4)
        display.show(emotions[current_emotion])

----

.. admonition:: Tasks

    #. Create a 5 image sequence for indicating focus levels with Image.DIAMOND_SMALL as index 1 in the list.
    #. Create a 4 custom image sequence for indicating sun brightness.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Create a 5 image sequence for indicating focus levels with Image.DIAMOND_SMALL as index 1 in the list.

                .. code-block:: python

                    from microbit import *

                    dot = Image("00000:00000:00900:00000:00000")
                    corner_square = Image("00000:09090:00000:09090:0000")
                    diamond_edges = Image("09090:90009:0000:90009:09090")
                    corners = Image("90009:00000:0000:00000:90009")

                    shapes = [dot, Image.DIAMOND_SMALL, corner_square, diamond_edges, corners]
                    current_shape = 2

                    while True:
                        if button_a.get_presses():
                            current_shape = max(current_shape - 1, 0)
                        elif button_b.get_presses():
                            current_shape = min(current_shape + 1, 4)
                        display.show(shapes[current_shape])

            .. tab-item:: Q2

                Create a 4 custom image sequence for indicating sun brightness.

                .. code-block:: python

                    from microbit import *

                    # Define the images
                    dot = Image("00000:00000:00900:00000:00000")
                    small_cross = Image("00000:00900:09990:00900:00000")
                    square = Image("00000:09990:09990:09990:00000")
                    large_cross = Image("90909:09990:99999:09990:90909")

                    # Create the sequence of shapes
                    shapes = [dot, small_cross, square, large_cross]
                    current_shape = 0

                    while True:
                        if button_a.get_presses():
                            current_shape = max(current_shape - 1, 0)
                        elif button_b.get_presses():
                            current_shape = min(current_shape + 1, len(shapes) - 1)
                        display.show(shapes[current_shape])