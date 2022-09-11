==========================
Pixel Classes
==========================

Pixel animation using classes
--------------------------------

| The Class ``LED`` is used to create several LED objects used in the animation.
| e.g **led02 = LED(0, 2)** creates a pixel at x = 0 and y = 2. 
| The **on** method controls the microbit LED brightness. 
| e.g. **led02.on()** set the pixel at x = 0 and y = 2 to the default brightnes of 9.
| The **off** method sets the pixel to 0 brightness. 

| A list of LED objects can be used in an animation: led_list = [led02, led12, led22, led32, led42]

.. code-block:: python

    from microbit import *
    import random


    class LED():
        def __init__(self, x=2, y=2):
            self.x = x
            self.y = y
        
        def on(self, brightness=9):
            display.set_pixel(self.x, self.y, brightness)

        def off(self):
            display.set_pixel(self.x, self.y, 0)


    led02 = LED(0, 2)
    led12 = LED(1, 2)
    led22 = LED(2, 2)
    led32 = LED(3, 2)
    led42 = LED(4, 2)

    led_list = [led02, led12, led22, led32, led42]

    while True:
        for ledxy in led_list:
            ledxy.on()
            sleep(100)
        for ledxy in led_list:
            ledxy.off()
            sleep(100)

.. admonition:: Tasks

    #. Modify the code to use the **brightness** parameter with a brightness of 6.   
    #. 

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to use a **brightness** parameter in the init function and replace the **2** in the **show** method with the parameter variable. Create **mypix** with a brightness of 6.

                .. code-block:: python

----

Pixel Classes using accelerometer
-------------------------------------------

| The code below draws a pixel on the display. The Pixel class keeps track of the pixel position. 
| The ``acc_x_change()`` and ``acc_y_change()`` functions return the change in x and y as the microbit is tilted.
| These are passed to the ``move`` method of the Pixel object as in ``mypix.move(acc_x_change(),acc_y_change())``
| The ``move`` method uses ``min`` amd ``max`` to prevent the x or y values going outside the range 0 to 4, as seen in ``self.x_position = min(4, max(0, self.x_position + x_delta))``
| The **show** method sets the pixel with brightness 9, then 2, so that it appears to blink.

.. code-block:: python

    # pixel class with accelerometer
    from microbit import *


    class Pixel:
        def __init__(self, x_position=2, y_position=2):
            self.x_position = x_position
            self.y_position = y_position

        def move(self, x_delta, y_delta):
            self.x_position = min(4, max(0, self.x_position + x_delta))
            self.y_position = min(4, max(0, self.y_position + y_delta))

        def show(self):
            display.set_pixel(self.x_position, self.y_position, 9)
            sleep(50)
            display.set_pixel(self.x_position, self.y_position, 2)

        
    def acc_x_change():
        sensitivity = 100
        accx = accelerometer.get_x()
        if accx < -sensitivity:
            xd = -1
        elif accx > sensitivity:
            xd = 1
        else:
            xd = 0
        return xd
        

    def acc_y_change():
        sensitivity = 300
        accy = accelerometer.get_y()
        if accy < sensitivity:
            yd = -1
        elif accy > sensitivity:
            yd = 1
        else:
            yd = 0
        return yd


    # Create an instance of a pixel object
    mypix = Pixel()
    mypix.show()
    while True:
        mypix.move(acc_x_change(),acc_y_change())
        mypix.show()
        sleep(500)


----
 
.. admonition:: Tasks

    #. Modify the code to use a **brightness** parameter in the init function and replace the **2** in the **show** method with the parameter variable. Create **mypix** with a brightness of 6.   
    #. Add a **clear** method to the class, and use it to clear the display if the A button was pressed.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to use a **brightness** parameter in the init function and replace the **2** in the **show** method with the parameter variable. Create **mypix** with a brightness of 6.

                .. code-block:: python

                    from microbit import *


                    class Pixel:
                        def __init__(self, x_position=2, y_position=2, brightness=2):
                            self.x_position = x_position
                            self.y_position = y_position
                            self.brightness = brightness

                        def move(self, x_delta, y_delta):
                            self.x_position = min(4, max(0, self.x_position + x_delta))
                            self.y_position = min(4, max(0, self.y_position + y_delta))

                        def show(self):
                            display.set_pixel(self.x_position, self.y_position, 9)
                            sleep(50)
                            display.set_pixel(self.x_position, self.y_position, self.brightness)


                    def acc_x_change():
                        sensitivity = 100
                        accx = accelerometer.get_x()
                        if accx < -sensitivity:
                            xd = -1
                        elif accx > sensitivity:
                            xd = 1
                        else:
                            xd = 0
                        return xd
                        

                    def acc_y_change():
                        sensitivity = 300
                        accy = accelerometer.get_y()
                        if accy < sensitivity:
                            yd = -1
                        elif accy > sensitivity:
                            yd = 1
                        else:
                            yd = 0
                        return yd


                    # Create an instance of a pixel object
                    mypix = Pixel(brightness=6)
                    mypix.show()
                    while True:
                        mypix.move(acc_x_change(),acc_y_change())
                        mypix.show()
                        sleep(500)

            .. tab-item:: Q2

                Add a **clear** method to the class, and use it to clear the display if the A button was pressed.

                .. code-block:: python

                    from microbit import *


                    class Pixel:
                        def __init__(self, x_position=2, y_position=2, brightness=2):
                            self.x_position = x_position
                            self.y_position = y_position
                            self.brightness = brightness

                        def move(self, x_delta, y_delta):
                            self.x_position = min(4, max(0, self.x_position + x_delta))
                            self.y_position = min(4, max(0, self.y_position + y_delta))

                        def show(self):
                            display.set_pixel(self.x_position, self.y_position, 9)
                            sleep(50)
                            display.set_pixel(self.x_position, self.y_position, self.brightness)

                        def clear(self):
                            for x in range(5):
                                for y in range(5):
                                    display.set_pixel(x, y, 0)


                    def acc_x_change():
                        sensitivity = 100
                        accx = accelerometer.get_x()
                        if accx < -sensitivity:
                            xd = -1
                        elif accx > sensitivity:
                            xd = 1
                        else:
                            xd = 0
                        return xd


                    def acc_y_change():
                        sensitivity = 300
                        accy = accelerometer.get_y()
                        if accy < sensitivity:
                            yd = -1
                        elif accy > sensitivity:
                            yd = 1
                        else:
                            yd = 0
                        return yd


                    # Create an instance of a pixel object
                    mypix = Pixel(brightness=6)
                    mypix.show()
                    while True:
                        if button_a.was_pressed():
                            mypix.clear()
                        mypix.move(acc_x_change(), acc_y_change())
                        mypix.show()
                        sleep(500)



