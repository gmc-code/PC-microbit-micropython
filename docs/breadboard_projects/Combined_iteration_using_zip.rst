=============================
Combined iteration using zip
=============================

| The zip function can combine multiple lists so that they can be iterated over together.
| See: https://www.w3schools.com/python/ref_func_zip.asp
| See: https://realpython.com/python-zip-function/#traversing-lists-in-parallel

----

zip 2 lists
------------------

| The code below uses the zip function to combine 2 lists so that they are like a list of tuples.
| The zip object, ``zip(list1, list2)``,  is like a list of tuples.
| Using ``list(zip(list1, list2))``, the list of tuples below is: ``[(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]``
| Each tuple has an element from each of the initial lists.
| A list of tuples can be iterated over using the syntax: ``for num, letter in tuple_list:``

| The code below has 2 lists that are iterated over together via the zip function.

.. code-block:: python

    from microbit import *

    list1 = [1, 2, 3, 4]
    list2 = ['a', 'b', 'c', 'd']
    for num, letter in zip(list1, list2):
        display.scroll(num, delay=80)
        display.scroll(letter, delay=80)

----

| In the code below, a pitch frequency and an image are combined into a tuple.
| This allows a different pitch to be played while each image is displayed.
| ``freqs = range(1760, 880, -128)`` produces a list like object containing 7 frequencies.
| The A button can be pressed to exit the while loop using ``break`` so that the sounds can be easily stopped.
| Pressing the reset button on the back of the microbit will restart the code.

.. code-block:: python

    from microbit import *
    import music

    freqs = range(1760, 880, -128)
    animal_images = [
        Image.RABBIT,
        Image.COW,
        Image.DUCK,
        Image.TORTOISE,
        Image.BUTTERFLY,
        Image.GIRAFFE,
        Image.SNAKE,
    ]
    while True:
        for freq, img in zip(freqs, animal_images):
            music.pitch(freq, duration=250)
            display.show(img, delay=250)
        if button_a.is_pressed():
            display.clear()
            break

----

| The code below zips the list of images and the list of frequencies in the A minor scale.
| ``for freq, img in zip(Am_freqs, animal_images)`` iterates over the zipped object, placing each frequency and each Image into the ``freq`` and ``img`` variables for use. 
| The A button can be pressed to exit the while loop using ``break`` so that the sounds can be easily stopped.
| Pressing the reset button on the back of the microbit will restart the code.

.. code-block:: python

    from microbit import *
    import music

    animal_images = [
        Image.HAPPY,
        Image.SMILE,
        Image.SAD,
        Image.CONFUSED,
        Image.ANGRY,
        Image.ASLEEP,
        Image.SURPRISED,
        Image.SILLY,
    ]
    Am_freqs = [440, 494, 523, 587, 659, 698, 784, 880]
    timing = 400
    while True:
        for freq, img in zip(Am_freqs, animal_images):
            display.show(img, delay=timing)
            music.pitch(freq, duration=timing)
        if button_a.is_pressed():
            display.clear()
            break

----

.. admonition:: Exercises

    #. Make a list of 8 arrows and a list of 8 frequencies to play. Write code to show each image as each frequency is played.
    #. Make a list of 12 clock hands and a list of 12 frequencies to play. Write code to show each image as each frequency is played.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Make a list of 8 arrows and a list of 8 frequencies to play. Write code to show each image as each frequency is played.

                .. code-block:: python

                    from microbit import *

            .. tab-item:: Q2

                Make a list of 12 clock hands and a list of 12 frequencies to play. Write code to show each image as each frequency is played.

                .. code-block:: python

                    from microbit import *

----

zip 3 lists
------------------

| The code below requires a breadboard with 3 LEDS.
| See: https://pc-microbit-micropython.readthedocs.io/en/latest/breadboards/LEDs_with_resistors.html
| The code below zips the list of images, the list of frequencies in the A minor scale as well as a list of pins to use.
| ``for freq, img, pinx in zip(freqs, animal_images, pins)`` iterates over the zipped object, placing each frequency, each Image, and each pin into the ``freq``, ``img`` and ``pins`` variables for use. 
| This allows a sound, an image and an LED to be used in the same for-loop.
| The A button can be pressed to exit the while loop using ``break`` so that the actions can be easily stopped.
| Pressing the reset button on the back of the microbit will restart the code.

.. code-block:: python

    from microbit import *
    import music

    freqs = [440, 494, 523, 587, 659, 698, 784]
    animal_images = [
        Image.RABBIT,
        Image.COW,
        Image.DUCK,
        Image.TORTOISE,
        Image.BUTTERFLY,
        Image.GIRAFFE,
        Image.SNAKE,
    ]
    pins = [pin0, pin1, pin2, pin1, pin0, pin1, pin2]
    timing = 400
    while True:
        for freq, img, pinx in zip(freqs, animal_images, pins):
            music.pitch(freq, duration=timing)
            display.show(img, delay=timing)
            pinx.write_digital(1)
            sleep(timing)
            pinx.write_digital(0)
        if button_a.is_pressed():
            display.clear()
            break

----

.. admonition:: Exercises

    #. Make a list of images, a list of pitches, and a list of LEDS and iterate over them by using the zip function.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Make a list of 8 arrows and a list of 8 frequencies to play. Write code to show each image as each frequency is played.

                .. code-block:: python

                    from microbit import *

            .. tab-item:: Q2

                Make a list of 12 clock hands and a list of 12 frequencies to play. Write code to show each image as each frequency is played.

                .. code-block:: python

                    from microbit import *