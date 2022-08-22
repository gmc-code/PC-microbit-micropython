==========================
Potentiometer Class
==========================

| Create a class for the Potentiometer that makes it easy to:
    - get the potentiometer analog reading, 
    - keep track of the last reading, 
    - be able to tell if the potentiometer analog reading has changed 
    - and to convert the reading to a particular range, such as, from 0 to 10.
  
----

.. py:module:: Potentiometer

Potentiometer Syntax
----------------------------------------

.. py:function:: get_val()

    | Returns the potentiometer value from **0 to 1023**.

.. py:function:: was_changed()

    | Returns **True** if the potentiometer value changed, otherwise, **False**.

.. py:function:: get_scaled_val(scale=10)

    | Returns the potentiometer value scaled from **0 to scale** using a default scale of 10.

----

| The code below, first checks to see if the value of the potentiometer has changed, and then if it has, displays the value as a scaled value in the range 0 to 10 via ``display.show(pot.get_range(10))``.
| ``pot = Potentiometer()`` uses the default pin: pin0. 
| The pin is kept track of via the **self.io_pin** variable.
| To use **pin1** instead, use ``pot = Potentiometer(pin1)`` instead of ``pot = Potentiometer()``
| The line ``self.last_val = -1`` sets **last_val** to be a value it cannot be, -1, so that the first reading will be recognised as a change.

.. code-block:: python

    from microbit import *


    class Potentiometer:
        def __init__(self, io_pin=pin0):
            self.io_pin = io_pin
            self.last_val = -1

        def get_val(self):
            return self.io_pin.read_analog()

        def was_changed(self):
            curr_val = self.get_val()
            if self.last_val != curr_val:
                self.last_val = curr_val
                return True
            else:
                return False

        def get_scaled_val(self, scale=10):
            analog_read = self.get_val()
            scaled_read = scale * (analog_read / 1023)
            return int(scaled_read)


    pot = Potentiometer()
    while True:
        if pot.was_changed():
            display.show(pot.get_scaled_val(10))

----
 
.. admonition:: Tasks

    #. Modify the code to use a potentiometer to set the image to display.

        from microbit import *

        images = [
            Image.ARROW_N,
            Image.ARROW_NE,
            Image.ARROW_E,
            Image.ARROW_SE,
            Image.ARROW_S,
            Image.ARROW_SW,
            Image.ARROW_W,
            Image.ARROW_NW,
        ]

        img_num = 0
        while True:
            display.show(images[img_num])
            
    #. Modify the code to use a potentiometer to set the image to display.

        from microbit import *

        images = [
            Image.HAPPY,
            Image.SMILE,
            Image.SAD,
            Image.CONFUSED,
            Image.ANGRY,
            Image.ASLEEP,
            Image.SURPRISED,
            Image.SILLY,
            Image.FABULOUS,
            Image.MEH,
        ]

        img_num = 0
        while True:
            display.show(images[img_num])

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to use a potentiometer to set the image to display.

                .. code-block:: python

                    from microbit import *

                    images = [
                        Image.ARROW_N,
                        Image.ARROW_NE,
                        Image.ARROW_E,
                        Image.ARROW_SE,
                        Image.ARROW_S,
                        Image.ARROW_SW,
                        Image.ARROW_W,
                        Image.ARROW_NW,
                    ]
                    images_rng = len(images) - 1

                    class Potentiometer:
                        def __init__(self, io_pin=pin0):
                            self.io_pin = io_pin
                            self.last_val = -1

                        def get_val(self):
                            return self.io_pin.read_analog()

                        def was_changed(self):
                            curr_val = self.get_val()
                            if self.last_val != curr_val:
                                self.last_val = curr_val
                                return True
                            else:
                                return False

                        def get_range(self, rng):
                            analog_read = self.get_val()
                            scaled_read = rng * (analog_read / 1023)
                            return int(scaled_read)


                    pot = Potentiometer(pin1)
                    while True:
                        if pot.was_changed():
                            img_num = pot.get_range(images_rng)
                            display.show(face_images[img_num])

            .. tab-item:: Q2

                Modify the code to use a potentiometer to set the image to display.

                .. code-block:: python

                    from microbit import *

                    images = [
                        Image.HAPPY,
                        Image.SMILE,
                        Image.SAD,
                        Image.CONFUSED,
                        Image.ANGRY,
                        Image.ASLEEP,
                        Image.SURPRISED,
                        Image.SILLY,
                        Image.FABULOUS,
                        Image.MEH,
                    ]
                    images_rng = len(images) - 1


                    class Potentiometer:
                        def __init__(self, io_pin=pin0):
                            self.io_pin = io_pin
                            self.last_val = -1

                        def get_val(self):
                            return self.io_pin.read_analog()

                        def was_changed(self):
                            curr_val = self.get_val()
                            if self.last_val != curr_val:
                                self.last_val = curr_val
                                return True
                            else:
                                return False

                        def get_range(self, rng):
                            analog_read = self.get_val()
                            scaled_read = rng * (analog_read / 1023)
                            return int(scaled_read)


                    pot = Potentiometer(pin1)
                    while True:
                        if pot.was_changed():
                            img_num = pot.get_range(images_rng)
                            display.show(images[img_num])
