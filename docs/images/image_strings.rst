====================================================
Image strings
====================================================

Show image
----------------

| The basic syntax for showing an image is:

.. py:function:: display.show(image)

    | Display an image.

----

Image strings
----------------

| The basic syntax for creating an image from a string of 25 brightness values is:

.. py:function:: Image(string)

    | Create an image. 
    | string is a string of 25 brightness values with every 5 separated by a colon.
    | e.g. '01234:56789:09090:98765:43210'


| The image can be a string made up of a 25 integers where each integer is the brightness from 0 to 9, where 0 if off and 9 is full brightness.
| The 25 values are broken up into groups of 5 with a colon between them.
| Each group of 5 represents the brightness for a row on the microbit.
| e.g. ``Image('01234:56789:09090:98765:43210')``

.. sidebar::

    .. image:: images/square.png
        :scale: 50 %
        :align: center


| The code below shows a large bright square.

.. code-block:: python

    from microbit import *

    display.show(Image('99999:90009:90009:90009:99999'))

----

.. sidebar::

    .. image:: images/vertical_gradient.png
        :scale: 50 %
        :align: center


| The code below shows a vertical brightness gradient of dull to bright from the top to the bottom.

.. code-block:: python

    from microbit import *

    display.show(Image('11111:33333:55555:77777:99999'))

----

.. sidebar::

    .. image:: images/topleft_botright_gradient.png
        :scale: 50 %
        :align: center


| The code below shows a diagonal brightness gradient (dull to bright) from the top left to the bottom right.

.. code-block:: python

    from microbit import *

    display.show(Image('12345:23456:34567:45678:56789'))

----

.. admonition:: Tasks

    #. Write code for a large square of brightness 2.
    #. Write code for a vertical brightness gradient of bright to dull from the top down to the bottom.
    #. Write code for a horizontal brightness gradient of dull to bright from the left to right.
    #. Write code for a diagonal brightness gradient of dull to bright from the bottom left to the top right.   

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write code for a large square of brightness 2.

                    .. code-block:: python

                        from microbit import *

                        display.show(Image('22222:20002:20002:20002:22222'))

                .. tab-item:: Q2

                    Write code for a vertical brightness gradient of bright to dull from the top down to the bottom.

                    .. code-block:: python

                        from microbit import *

                        display.show(Image('99999:77777:55555:33333:11111'))

                .. tab-item:: Q3

                    Write code for a horizontal brightness gradient of dull to bright from the left to right.

                    .. code-block:: python

                        from microbit import *

                        display.show(Image('13579:13579:13579:13579:13579'))

                .. tab-item:: Q4

                    Write code for a diagonal brightness gradient of dull to bright from the bottom left to the top right. 

                    .. code-block:: python

                        from microbit import *

                        display.show(Image('56789:45678:34567:23456:12345'))
                    

----

Image strings: Multiplication of a line
----------------------------------------

| Strings can be replicated using multiplication.

.. py:function:: string * integer
   
   | Returns string + string + string .... integer times.

| e.g "Ha" * 3 returns "HaHaHa"

| The syntax for creating an Image by replicating a string representing one row is:

.. py:function:: Image(line_string * 5)

    | line_string is the first 5 pixel brightness values. e.g. "00000:"
    | e.g. Image("00000:" * 5) create an image with all pixels off.
    | e.g. Image("99999:" * 5) create an image with all pixels at full brightness.


| The code below creates a horizontal gradient by repeating a string of 5 brightness values, 5 times.

.. code-block:: python

    from microbit import *

    img = Image("13579:" * 5)
    display.show(img)


----

.. admonition:: Tasks

    #. Modify the code above to go from dim on the left edge to bright in the middle to dim on the right edge.
    #. Modify the code above to go from bright on the left edge to dim on the right edge.
    #. Write code to cycle between bright on the left edge to bight on the right edge.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Modify the code above to go from dim on the left edge to bright in the middle to dim on the right edge.

                    .. code-block:: python

                        from microbit import *

                        img = Image("15951:" * 5)
                        display.show(img)

                .. tab-item:: Q2

                    Modify the code above to go from bright on the left edge to dim on the right edge.

                    .. code-block:: python

                        from microbit import *

                        img = Image("97531:" * 5)
                        display.show(img)

                .. tab-item:: Q3

                    Write code to cycle between bright on the left edge to bight on the right edge.

                    .. code-block:: python

                        from microbit import *

                        while True:
                            img1 = Image("97531:" * 5)
                            display.show(img1)
                            sleep(300)
                            img2 = Image("13579:" * 5)
                            display.show(img2)
                            sleep(300)

----

Image strings: line by line
------------------------------

| The large square Image('99999:90009:90009:90009:99999') can be rewritten so that the 5 rows are lined up under each other like a 5 by 5 grid. Extra spaces can by used to line up each line.

.. code-block:: python

    from microbit import *

    large_square = Image('99999:'
                         '90009:'
                         '90009:'
                         '90009:'
                         '99999')
    display.show(large_square)


----

.. admonition:: Tasks

    #. Write code for a large square of brightness 3 by lining up the 5 rows of the image under each other.
    #. Write code for a small central square of brightness 9 by lining up the 5 rows of the image under each other.
    #. Write code for 2 symmetrically spaced central horizontal lines of brightness 5 by lining up the 5 rows of the image under each other. 
    #. Write code for 2 symmetrically spaced central vertical lines of brightness 5 by lining up the 5 rows of the image under each other.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write code for a large square of brightness 3 by lining up the 5 rows of the image under each other.

                    .. code-block:: python

                        from microbit import *

                        large_square = Image('33333:'
                                             '30003:'
                                             '30003:'
                                             '30003:'
                                             '33333')
                        display.show(large_square)

                .. tab-item:: Q2

                    Write code for a small central square of brightness 9 by lining up the 5 rows of the image under each other.

                    .. code-block:: python

                        from microbit import *

                        small_square = Image('00000:'
                                             '09990:'
                                             '09090:'
                                             '09990:'
                                             '00000')
                        display.show(small_square)


                .. tab-item:: Q3

                    Write code for 2 symmetrically spaced central horizontal lines of brightness 5 by lining up the 5 rows of the image under each other.

                    .. code-block:: python

                        from microbit import *

                        hor_lines = Image('00000:'
                                          '55555:'
                                          '00000:'
                                          '55555:'
                                          '00000')
                        display.show(hor_lines)

                .. tab-item:: Q4

                    Write code for 2 symmetrically spaced central vertical lines of brightness 5 by lining up the 5 rows of the image under each other.

                    .. code-block:: python

                        from microbit import *

                        vert_lines = Image('05050:'
                                           '05050:'
                                           '05050:'
                                           '05050:'
                                           '05050')
                        display.show(vert_lines)

----

Boat sinking animation
-----------------------------

| Several custom images can be stored in variables. e.g. boat1, boat2, boat3, boat4, boat5, boat6.
| Those variables can be put in a list. e.g. sinking_boats
| Since ``display.show`` can use a list of images, the list of custom images can be shown in sequence, making an animation.

.. code-block:: python

    from microbit import *

    boat1 = Image('05050:'
                  '05050:'
                  '05050:'
                  '99999:'
                  '09990')

    boat2 = Image('00000:'
                  '05050:'
                  '05050:'
                  '05050:'
                  '99999')

    boat3 = Image('00000:'
                  '00000:'
                  '05050:'
                  '05050:'
                  '05050')

    boat4 = Image('00000:'
                  '00000:'
                  '00000:'
                  '05050:'
                  '05050')

    boat5 = Image('00000:'
                  '00000:'
                  '00000:'
                  '00000:'
                  '05050')

    boat6 = Image('00000:'
                  '00000:'
                  '00000:'
                  '00000:'
                  '00000')

    sinking_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
    while True:
        display.show(sinking_boats, delay=500)

----

.. admonition:: Tasks

    #. Write a list variable, ``rising_boats``, that lists the boats in reverse order and animates a rising boat. Rather than manually listing the order, use ``list(reversed(sinking_boats))``.
    #. Combine the 2 animations to show a boat sinking and rising over and over again.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write a list variable, ``rising_boats``, that lists the boats in reverse order and animates a rising boat. Rather than manually listing the order, use ``list(reversed(sinking_boats))``. 

                    .. code-block:: python

                        from microbit import *

                        boat1 = Image("05050:" "05050:" "05050:" "99999:" "09990")
                        boat2 = Image("00000:" "05050:" "05050:" "05050:" "99999")
                        boat3 = Image("00000:" "00000:" "05050:" "05050:" "05050")
                        boat4 = Image("00000:" "00000:" "00000:" "05050:" "05050")
                        boat5 = Image("00000:" "00000:" "00000:" "00000:" "05050")
                        boat6 = Image("00000:" "00000:" "00000:" "00000:" "00000")

                        sinking_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
                        rising_boats = list(reversed(sinking_boats))

                        while True:
                            display.show(rising_boats, delay=500)


                .. tab-item:: Q2

                    Combine the 2 animations to show a boat sinking and rising over and over again.

                    .. code-block:: python

                        from microbit import *

                        boat1 = Image("05050:" "05050:" "05050:" "99999:" "09990")
                        boat2 = Image("00000:" "05050:" "05050:" "05050:" "99999")
                        boat3 = Image("00000:" "00000:" "05050:" "05050:" "05050")
                        boat4 = Image("00000:" "00000:" "00000:" "05050:" "05050")
                        boat5 = Image("00000:" "00000:" "00000:" "00000:" "05050")
                        boat6 = Image("00000:" "00000:" "00000:" "00000:" "00000")

                        sinking_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
                        rising_boats = list(reversed(sinking_boats))

                        while True:
                            display.show(sinking_boats, delay=500)
                            display.show(rising_boats, delay=500)

----

Rotating line animation
-----------------------------

| Create 4 custom images. line1, line2, line3, line4.
| line1: a horizontal line with y = 2.
| line2: a diagonal line from the top left to the bottom right.
| line3: a vertical line with x = 2.
| line4: a diagonal line from the top right to the bottom left.
| Create an animation in which the lines appear to rotate clockwise.
| Create an animation in which the lines appear to rotate anticlockwise.

----

Image gradients using  string definitions
--------------------------------------------

| The definition below, **horzgrad**, takes  2 arguments, width and height.
| The for-loop creates a string starting with a brightness of 1 and increasing by one to the width given, which should be 5 for the full width of the 5x5 grid.
| The string is then replicated for each line given by height, which is 5 for the full grid.
| **Image(horzgrad(5, 5))** results in **Image('12345:12345:12345:12345:12345:')**.

.. code-block:: python
        
    from microbit import *


    def horzgrad(w, h):
        string = ""
        for i in range(1, w + 1):
            string += str(i)
        return (string + ":") * h


    img_horzgrad = Image(horzgrad(5, 5))
    display.show(img_horzgrad)

----

.. admonition:: Tasks

    #. Write a vertgrad definition to produce: **Image('11111:22222:33333:44444:55555:')**.
    #. Write a diaggrad definition to produce: **Image('12345:23456:34567:45678:56789:')**.

    .. dropdown::
            :icon: codescan
            :color: primary
            :class-container: sd-dropdown-container

            .. tab-set::

                .. tab-item:: Q1

                    Write a vertgrad definition to produce: **Image('11111:22222:33333:44444:55555:')**.

                    .. code-block:: python

                        from microbit import *


                        def vertgrad(w, h):
                            string = ""
                            for i in range(1, h + 1):
                                string += (str(i) * w) + ":"
                            return string


                        img_vertgrad = Image(vertgrad(5, 5))
                        display.show(img_vertgrad)

                .. tab-item:: Q2

                    Write a diaggrad definition to produce: **Image('12345:23456:34567:45678:56789:')**.

                    .. code-block:: python

                        from microbit import *


                        def diaggrad(w, h):
                            string = ""
                            for j in range(1, h + 1):
                                for i in range(1, w + 1):
                                    string += str(i + j - 1)
                                string += ":"
                            return string


                        img_diaggrad = Image(diaggrad(5, 5))
                        display.show(img_diaggrad)

