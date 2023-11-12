==========================
Classes for the microbit
==========================

| See: https://www.w3schools.com/python/python_classes.asp

| Practical examples of using classes in coding on the microbit are found in pages with **Class** in their name.

Classes
------------

| Almost everything in Python is an object, with its own properties and methods.
| A Class is a "blueprint" for creating (instantiating) objects.
| The __init__() function assigns values to object properties when the object is created.
| The Objects created by calling classes can also contain methods. Methods in objects are functions that belong to the object. These functions use the self parameter to reference the current instance of the class, and to access variables that belong to the class.

----

Example code using classes for LED control
--------------------------------------------

It defines a class for an LED light, with methods to turn the light on and off. An instance of the class is created, and then in an infinite loop, the program checks if either of the two buttons on the micro:bit has been pressed. If button A was pressed, the LED light is turned on with a brightness of 9. If button B was pressed, the LED light is turned off. The loop then pauses for 100 milliseconds before checking the button states again. This allows the micro:bit to respond to button presses to control the LED light.

.. code-block:: python

    from microbit import *

    class LED():
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def on(self):
            display.set_pixel(self.x, self.y, 9)

        def off(self):
            display.set_pixel(self.x, self.y, 0)

    led = LED(3, 2)

    while True:
        if button_a.was_pressed():
            led.on()
        elif button_b.was_pressed():
            led.off()
        sleep(100)
