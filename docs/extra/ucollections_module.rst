==========================
ucollections
==========================

.. py:module:: ucollections

| MicroPython contains an ``ucollections`` module based upon the ``collections`` module in the Python standard library.
| This module has 2 collections from the standard python collections module.
| See: http://docs.micropython.org/en/v1.14/library/ucollections.html#module-ucollections
| See: https://mpython.readthedocs.io/en/master/library/pythonStd/ucollections.html



| namedtuple is a function
| OrderedDict is a class

----

ucollections.namedtuple
--------------------------

.. function:: ucollections.namedtuple(name, fields)

    | Create a new namedtuple type with a specific name and set of fields. 
    | A namedtuple is a subclass of tuple which allows access to its fields not just by numeric index, but also with an attribute access syntax using field names. 
    | Fields is a sequence of strings specifying field names. 
    | It can also be a a string with space-separated field named (but this is less efficient).


.. code-block:: python

    from microbit import *
    from ucollections import namedtuple as nt

    Point = nt('Point', ['x', 'y'])
    p = Point(3, y=4)     # instantiate with positional or keyword arguments

    disp(p[0], p[1])            # indexable like the plain tuple (11, 22)

    x, y = p                # unpack like a regular tuple
    print(x, y)

    print(p.x, p.y)           # fields also accessible by name

    print(p)                       # readable __repr__ with a name=value style

----

.. admonition:: Tasks

    #. Convert the code below to use a named tuple.
        .. code-block:: python

        from microbit import *

        # Define the pixels to be controlled
        # Each tuple/list contains x, y, and brightness values
        pixels = [
            (0, 0, 9),  # Top-left pixel, full brightness
            (2, 2, 5),  # Middle pixel, half brightness
            (4, 4, 1),  # Bottom-right pixel, low brightness
        ]

        while True:
            if button_a.was_pressed():
                # Turn on the defined pixels
                for pixel in pixels:
                    # unpacked tuple
                    x, y, brightness = pixel
                    display.set_pixel(x, y, brightness)
                sleep(2000)
                display.clear()
                            
    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Convert the code to use a named tuple.

                .. code-block:: python

                    from microbit import *
                    from collections import namedtuple

                    # Define a named tuple type called 'Pixel' with 'x', 'y' and 'brightness' fields
                    Pixel = namedtuple('Pixel', ['x', 'y', 'brightness'])

                    # Define the pixels to be controlled
                    pixels = [
                        Pixel(0, 0, 9),  # Top-left pixel, full brightness
                        Pixel(2, 2, 6),  # Middle pixel, half brightness
                        Pixel(4, 4, 3),  # Bottom-right pixel, low brightness
                    ]

                    while True:
                        if button_a.was_pressed():
                            # Turn on the defined pixels
                            for pixel in pixels:
                                display.set_pixel(pixel.x, pixel.y, pixel.brightness)
                            sleep(2000)
                            # Clear the display
                            display.clear()

----

ucollections.OrderedDict
--------------------------

| See: http://docs.micropython.org/en/v1.14/library/ucollections.html#module-ucollections

.. function:: ucollections.OrderedDict(name, fields)

    Create a dictionary type subclass which remembers and preserves the order of keys added. When ordered dict is iterated over, keys/items are returned in the order they were added.

| Functions: `clear, copy, get, items, keys, pop, popitem, setdefault, update, values`
| Methods: `fromkeys`
  
.. code-block:: python

    from microbit import *
    from ucollections import OrderedDict as Od

    # To make benefit of ordered keys, OrderedDict should be initialized
    # from sequence of (key, value) pairs.
    d = Od([("x", 1), ("y", 2)])
    # More items can be added as usual
    d["a"] = 3
    d["b"] = 4
    # print keys and values.
    for k, v in d.items():
        print(k, v)

.. code-block:: python

    from microbit import *
    from ucollections import OrderedDict as Od

    # Define the frames of the animation
    frames = Od([
        ("00000:00000:00000:00000:00900", 200),  # Frame 1: Ball at the bottom
        ("00000:00000:00000:00900:00000", 200),  # Frame 2: Ball in the middle
        ("00000:00000:00900:00000:00000", 200),  # Frame 3: Ball at the top
        ("00000:00900:00000:00000:00000", 200),  # Frame 4: Ball in the middle
        ("00900:00000:00000:00000:00000", 200),  # Frame 5: Ball at the bottom
        ("00000:00900:00000:00000:00000", 200),  # Frame 6: Ball in the middle
    ])

    while True:
        if button_a.was_pressed():
            # Play all frames in order
            for frame, delay in frames.items():
                display.show(Image(frame))
                sleep(delay)
            # Play frames 5 to 2 in reverse order
            for frame, delay in list(frames.items())[-2::-1]:
                display.show(Image(frame))
                sleep(delay)
