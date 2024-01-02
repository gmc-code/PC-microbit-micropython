==========================
Screen Class
==========================

.. admonition:: Exercise

    | Design a screen class that keeps track of the brightness of all pixels on the 5 by 5 LED display of the microbit.
    | Initialize the class instance with all pixels at 0 brightness.
    | Create a method to reset all pixels to 0 brightness.
    | Create a method to set all pixels to a given brightness.
    | Create a method to set all pixels to a random brightness.
    | Create a method to **show** the screen using the pixel brightness values.
    | Create a method to **set** a pixel brightness like the standard set_pixel method: ``.set_pixel(x, y, value)``.
    | Create a method to **get** a pixel brightness like the standard set_pixel method: ``.get_pixel(x, y, value)``.
    | Create a method to set the pixel brightness for a **row**.
    | Create a method to set the pixel brightness for a **column**.
    | Create a method to set the pixel brightness for a **random row**.
    | Create a method to set the pixel brightness for a **random column**.
    | Create a method to set the pixel brightness for a **random pixel**.
    | Create a method to set a random pixel brightness for a given pixel.
    | Create a method to set a random pixel brightness for a random pixel.
    | Create a method that returns the number of pixels with brightness greater than 0.
    | Create a method that returns the number of pixels with brightness greater than a specified value.
    | Create a method that returns the number of pixels with brightness of a specified value.

.. admonition:: Exercise solution

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Design a screen class.

                .. code-block:: python
                                        
                    from microbit import *
                    import random

                    class Screen:
                        def __init__(self):
                            self.pixels = [[0 for _ in range(5)] for _ in range(5)]

                        def reset(self, showpix=True):
                            self.pixels = [[0 for _ in range(5)] for _ in range(5)]
                            if showpix:
                                self.show()

                        def set_all(self, brightness, showpix=True):
                            self.pixels = [[brightness for _ in range(5)] for _ in range(5)]
                            if showpix:
                                self.show()
                    
                        def set_all_random(self, showpix=True):
                            self.pixels = [[random.randint(0, 9) for _ in range(5)] for _ in range(5)]
                            if showpix:
                                self.show()

                        def show(self):
                            for x in range(5):
                                for y in range(5):
                                    display.set_pixel(x, y, self.pixels[x][y])

                        def set_row(self, row, brightness, showpix=True):
                            self.pixels[row] = [brightness for _ in range(5)]
                            if showpix:
                                self.show()

                        def set_column(self, col, brightness, showpix=True):
                            for i in range(5):
                                self.pixels[i][col] = brightness
                            if showpix:
                                self.show()

                        def set_random_row(self, brightness, showpix=True):
                            self.pixels[random.randint(0, 4)] = [brightness for _ in range(5)]
                            if showpix:
                                self.show()
                    
                        def set_random_column(self,  brightness, showpix=True):
                            rany = random.randint(0, 4)
                            for x in range(5):
                                self.pixels[x][rany] = brightness
                            if showpix:
                                self.show()

                        def set_pixel(self, x, y, brightness, showpix=True):
                            self.pixels[x][y] = brightness
                            if showpix:
                                self.show()

                        def set_random_pixel(self, brightness, showpix=True):
                            x, y = random.randint(0, 4), random.randint(0, 4)
                            self.pixels[x][y] = brightness
                            if showpix:
                                self.show()

                        def set_random_brightness(self, x, y, showpix=True):
                            self.pixels[x][y] = random.randint(0, 9)
                            if showpix:
                                self.show()
                            
                        def set_random_pixel_random_brightness(self, showpix=True):
                            x, y = random.randint(0, 4), random.randint(0, 4)
                            self.pixels[x][y] = random.randint(0, 9)
                            if showpix:
                                self.show()

                        def get_pixel_brightness(self, x, y):
                            return self.pixels[x][y]
                            
                        def count_pixels_greater_than_zero(self):
                            return sum(pixel > 0 for row in self.pixels for pixel in row)
                        
                        def count_pixels_greater_than(self, brightness):
                            return sum(pixel > brightness for row in self.pixels for pixel in row)
                        
                        def count_pixels_of_value(self, brightness):
                            return sum(pixel == brightness for row in self.pixels for pixel in row)
----

.. admonition:: Exercise

    | Design some tests to make sure that the screen class is working as expected.

.. admonition:: Exercise solution

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Design some tests to make sure that the screen class is working as expected.

                .. code-block:: python
                                        
                    from microbit import *
                    import random

                    # Create an instance of the Screen class
                    screen = Screen()

                    # Set all pixels to a given brightness
                    screen.set_all(5)
                    sleep(500)

                    # Reset all pixels to 0 brightness
                    screen.reset()
                    sleep(500)

                    # Set all pixels to a random brightness
                    screen.set_all_random()
                    sleep(500)

                    # Set the pixel brightness for a row
                    screen.reset()
                    screen.set_row(0, 7)
                    sleep(500)

                    # Set the pixel brightness for a column
                    screen.reset()
                    screen.set_column(0, 7)
                    sleep(500)

                    # Set the pixel brightness for a random row
                    screen.reset()
                    screen.set_random_row(5)
                    sleep(500)

                    # Set the pixel brightness for a random column
                    screen.reset()
                    screen.set_random_column(6)
                    sleep(500)

                    # Set a pixel brightness like the standard set_pixel method
                    screen.reset()
                    screen.set_pixel(3, 2, 7)
                    sleep(500)

                    # Get a pixel brightness like the standard get_pixel method
                    brightness = screen.get_pixel_brightness(3, 2)

                    # Set the pixel brightness for a random pixel
                    screen.reset()
                    screen.set_random_pixel(6)
                    sleep(500)

                    # Set a random pixel brightness for a given pixel
                    screen.reset()
                    screen.set_random_brightness(2, 2)
                    sleep(500)

                    # Set a random pixel brightness for a random pixel
                    screen.reset()
                    screen.set_random_pixel_random_brightness()
                    sleep(500)

                    # Set all pixels to a random brightness
                    screen.set_all_random()
                    sleep(500)
                    # Get the number of pixels with brightness greater than 0
                    count = screen.count_pixels_greater_than_zero()
                    display.scroll(str(count))

                    # Set all pixels to a random brightness
                    screen.show()
                    sleep(500)
                    # Get the number of pixels with brightness greater than a specified value
                    count = screen.count_pixels_greater_than(5)
                    display.scroll(str(count))

                    # Set all pixels to a random brightness
                    screen.show()
                    sleep(500)
                    # Get the number of pixels with brightness of a specified value
                    count = screen.count_pixels_of_value(5)
                    display.scroll(str(count))
