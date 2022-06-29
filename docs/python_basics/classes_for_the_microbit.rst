==========================
Classes for the microbit
==========================

| See: https://www.w3schools.com/python/python_classes.asp

| Practical examples of using classes in coding on the microbit are included below.

Classes
------------
| Almost everything in Python is an object, with its own properties and methods.
| A Class is like an object constructor, or a "blueprint" for creating objects.
| The __init__() function assigns values to object properties when the object is created.
| The Objects created by calling classes can also contain methods. Methods in objects are functions that belong to the object. These functions use the self parameter to reference the current instance of the class, and to access variables that belong to the class.


Potentiometer Classes
----------------------------

| Create a class for the Potentiometer that makes it easy to gets its analog reading, keep track of the last reading, be able to tell if it has changed and to converted the reading to a particular range like 0 to 10.
| The code below first checks to see if the value of the potentiometer has changed, and then if it has, displays the value as a scaled value in the range 0 to 10.
| ``Potentiometer()`` will use the default pin: pin0. This is coded via: ``def __init__(self, io_pin=pin0)``


.. code-block:: python

    # potentiometer using class
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

        def get_range(self, rng):
            analog_read = self.get_val()
            scaled = rng * (analog_read / 1023)
            return int(scaled)

    # this defaults to pin0
    # to use pinl1 instead use pot = Potentiometer(pin1)
    pot = Potentiometer()
    while True:
        if pot.was_changed():
            display.show(pot.get_range(10))


----

Pixel Classes
-------------------

| The code below draws a pixel on the display. The Pixel class keeps track of the pixel position. 
| The ``acc_x_change()`` and ``acc_y_change()`` functions return the change in x and y as the microbit is tilted.
| These are passed to the ``move`` method of the Pixel object as in ``mypix.move(acc_x_change(),acc_y_change())``
| The ``move`` method uses ``min`` amd ``max`` to prevent the x or y values going outside the range 0 to 4, as seen in ``self.x_position = min(4, max(0, self.x_position + x_delta))``

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

Pixel animation using classes
--------------------------------

| The Class ``LED`` is used to create several LED objects used in the animation.
| The definitions within the class allow easy use of methods to control the microbit LED brightness. 

.. code-block:: python

    # pixel class
    from microbit import *
    import random


    class LED():
        def __init__(self, x=2, y=2):
            self.x = x
            self.y = y
        
        def intensity(self, varbrightness=9):
            display.set_pixel(self.x, self.y, varbrightness)

        def on(self, brightness=9):
            display.set_pixel(self.x, self.y, brightness)

        def off(self):
            display.set_pixel(self.x, self.y, 0)


    led02 = LED(0, 2)
    led12 = LED(1, 2)
    led22 = LED(2, 2)
    led32 = LED(3, 2)
    led42 = LED(4, 2)

    led22.on()
    sleep(500)
    led22.off()
    sleep(500)
        
        
    led_list = [led02, led12, led22, led32, led42]
    led_list_rev = led_list.copy()
    led_list_rev.reverse()

    while True:
        for i in range(1,9):
            for ledxy in led_list:
                ledxy.intensity(i)
                sleep(40)
                ledxy.off()
                sleep(10)
            for ledxy in led_list_rev:
                ledxy.intensity(i)
                sleep(40)
                ledxy.off()
                sleep(10)
        for i in range(50):
            ledxy = random.choice(led_list)
            intensity_level = random.randrange(1,9)
            ledxy.intensity(intensity_level)
            sleep(60)
            ledxy.off()
            sleep(40)
