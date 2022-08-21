====================================================
Radio examples
====================================================


.. code-block:: python

    # A micro:bit Firefly.
    # By Nicholas H.Tollervey. Released to the public domain.
    from microbit import *
    import radio
    import random
    

    # Create the "flash" animation frames
    flash = [Image().invert()*(i/9) for i in range(9, -1, -1)]

    # The radio won't work unless it's switched on.
    radio.on()

    # Event loop.
    while True:
        # Button A sends a "flash" message.
        if button_a.was_pressed():
            radio.send('flash')  # a-ha
        # Read any incoming messages.
        incoming = radio.receive()
        if incoming == 'flash':
            # If there's an incoming "flash" message display
            # the firefly flash animation after a random short
            # pause.
            sleep(random.randint(50, 350))
            display.show(flash, delay=100, wait=False)
            # Randomly re-broadcast the flash message after a
            # slight delay.
            if random.randint(0, 9) == 0:
                sleep(500)
                radio.send('flash')  # a-ha

    