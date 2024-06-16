====================================================
Radio Firefly
====================================================

Firefly
-------------

| This script essentially simulates a group of fireflies flashing in a random pattern, like you might see in nature. 
| Each micro:bit running this script acts like a firefly, flashing its LED display and occasionally causing other micro:bits in the same radio group to flash. 
| The randomness of the delays and re-broadcasts helps to create a natural, organic flashing pattern.

| ``flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]`` creates a list of images that represent different stages of a firefly's flash. 
| `Image().invert()`: This creates an inverted image of the micro:bit's LED display. Image() produces an image with all 25 LEDS at 0 brightness. The `invert()` function inverts the brightness of the LEDs, so they are all at maximum brightness (9).
| ``*(i/9)`` multiplies the inverted image by a fraction. When i is 9 it gives 1. When i is 0 it gives 0.
| ``for i in range(9, -1, -1)``: This is a loop that generates the numbers 9 down to 0. For each number `i`, it creates an image with brightness `i/9`, so the first image is at full brightness (9/9 = 1), and the last image is completely off (0/9 = 0).
| The resulting `flash` list is a sequence of 10 images that represent a firefly's flash fading out, from full brightness to off. 
| This list is used later in the script to display the flash animation on the micro:bit's LED display. 
| The ``display.show(flash, delay=100, wait=False)`` line in the script displays each image in the `flash` list in sequence, with a delay of 100 milliseconds between each image, creating the flashing effect.

.. code-block:: python

    # A micro:bit Firefly.
    # By Nicholas H. Tollervey. Released to the public domain.
    from microbit import *
    import radio
    import random
    
    # Choose the same group 0-255
    radio.config(group=8)
    # The radio won't work unless it's switched on.
    radio.on()

    # Create the "flash" animation frames
    flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]


    # Event loop.
    while True:
        # the A button sends a "flash" message.
        if button_a.was_pressed():
            radio.send('flash')
        # Read any incoming messages.
        incoming = radio.receive()
        if incoming == 'flash':
            # If there's an incoming "flash" message display
            # the firefly flash animation after a random short pause.
            sleep(random.randint(50, 350))
            display.show(flash, delay=100, wait=False)
            # Randomly re-broadcast the flash message after a slight delay.
            if random.randint(0, 9) == 0:
                sleep(500)
                radio.send('flash')


.. admonition:: Tasks

    #. Modify the code above so that the re-broadcast occurs with a 1 in 5 chance by changing the randint arguments.
    #. Modify the code above so that the re-broadcast occurs with a 1 in 2 chance by changing the randint arguments.
    #. Modify the code above so that the flash lasts twice as long by changing the value of the delay.
    #. Modify the code above so when the B button is pressed, a series of 5 flash messages are sent over 2 seconds.
    #. Replace the flash code with this code to flash an image  of a butterfly ``flash = [Image.BUTTERFLY*(i/9) for i in range(9, -1, -1)]``. Then vary the image used from a list of 4 images.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above so that the re-broadcast occurs with a 1 in 5 chance by changing the randint arguments.

                .. code-block:: python
                    
                    if random.randint(0, 5) == 0:

            .. tab-item:: Q2

                Modify the code above so that the re-broadcast occurs with a 1 in 2 chance by changing the randint arguments.

                .. code-block:: python
                    
                    if random.randint(0, 2) == 0:

            .. tab-item:: Q3

                Modify the code above so that the flash lasts twice as long by changing the value of the delay.

                .. code-block:: python
                    
                    display.show(flash, delay=200, wait=False)

            .. tab-item:: Q4

                Modify the code above so that the re-broadcast occurs with a 1 in 2 chance by changing the randint arguments.

                .. code-block:: python
                    
                    elif button_b.was_pressed():
                        for _ in range(5):
                            radio.send('flash')
                            sleep(500)

           .. tab-item:: Q5

                Replace the flash code with this code to flash an image  of a butterfly ``flash = [Image.BUTTERFLY*(i/9) for i in range(9, -1, -1)]``. Then vary the image used from a list of 4 images.

                .. code-block:: python
                    

                    # A micro:bit Firefly.
                    # By Nicholas H. Tollervey. Released to the public domain.
                    from microbit import *
                    import radio
                    import random

                    # Choose the same group 0-255
                    radio.config(group=8)
                    # The radio won't work unless it's switched on.
                    radio.on()

                    images = [Image.BUTTERFLY,Image.HEART,Image.PACMAN,Image.SMILE]
                    

                    def flash_img(images):
                        max_img_num = len(images) -1
                        img_num = random.randint(0, max_img_num)
                        img = images[img_num]   
                        flash = [img*(i/9) for i in range(9, -1, -1)]
                        return flash

                    # Event loop.
                    while True:
                        # the A button sends a "flash" message.
                        if button_a.was_pressed():
                            radio.send('flash')
                        # Read any incoming messages.
                        incoming = radio.receive()
                        if incoming == 'flash':
                            # If there's an incoming "flash" message display
                            # the flash animation after a random short pause.
                            sleep(random.randint(50, 350))
                            flash = flash_img(images)
                            display.show(flash, delay=100, wait=False)
                            # Randomly re-broadcast the flash message after a slight delay.
                            if random.randint(0, 9) == 0:
                                sleep(500)
                                radio.send('flash')
