==========================
Screen Class challenge
==========================

| Design a screen class that keeps track of the brightness of all pixels on the 5 by 5 LED display of the microbit.
| Initialize the class instance with all pixels at 0 brightness.
| Create a method to reset all pixels to 0 brightness.
| Create a method to set all pixels to a given brightness.
| Create a method to set all pixels to a random brightness.
| Create a method to show the screen using the pixel brightness values.
| Create a method to set a pixel brightness like the standard set_pixel method: ``.set_pixel(x, y, value)``.
| Create a method to get a pixel brightness like the standard set_pixel method: ``.get_pixel(x, y, value)``.
| Create a method to set the pixel brightness for a row.
| Create a method to set the pixel brightness for a column.
| Create a method to set the pixel brightness for a column.
| Create a method to set the pixel brightness for a random pixel.
| Create a method to set a random pixel brightness for a given pixel.
| Create a method to set a random pixel brightness for a random pixel.
| Create a method that returns the number of pixels with brightness greater than 0.
| Create a method that returns the number of pixels with brightness greater than a specified value.
| Create a method that returns the number of pixels with brightness of a specified value.


----

Test the code below and see if it meets the challenges above.

.. code-block:: python

    from microbit import *
    import random

    class Screen:
        def __init__(self):
            self.pixels = [[0 for _ in range(5)] for _ in range(5)]

        def reset(self):
            self.pixels = [[0 for _ in range(5)] for _ in range(5)]

        def set_all(self, brightness):
            self.pixels = [[brightness for _ in range(5)] for _ in range(5)]

        def set_random(self):
            self.pixels = [[random.randint(0, 9) for _ in range(5)] for _ in range(5)]

        def show(self):
            for x in range(5):
                for y in range(5):
                    display.set_pixel(x, y, self.pixels[x][y])

        def set_pixel(self, x, y, value):
            self.pixels[x][y] = value

        def get_pixel(self, x, y):
            return self.pixels[x][y]

        def set_row(self, row, value):
            self.pixels[row] = [value for _ in range(5)]

        def set_column(self, column, value):
            for i in range(5):
                self.pixels[i][column] = value

        def set_random_pixel(self, value):
            x, y = random.randint(0, 4), random.randint(0, 4)
            self.pixels[x][y] = value

        def set_random_value(self, x, y):
            self.pixels[x][y] = random.randint(0, 9)

        def set_random_pixel_random_value(self):
            x, y = random.randint(0, 4), random.randint(0, 4)
            self.pixels[x][y] = random.randint(0, 9)

        def count_pixels_greater_than_zero(self):
            return sum(value > 0 for row in self.pixels for value in row)

        def count_pixels_greater_than(self, value):
            return sum(pixel > value for row in self.pixels for pixel in row)

        def count_pixels_of_value(self, value):
            return sum(pixel == value for row in self.pixels for pixel in row)
