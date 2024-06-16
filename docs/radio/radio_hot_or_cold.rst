====================================================
Radio Hot or Cold
====================================================

Beacons
-------------------------

| Set up the group with a value 0-255 by changing the group value from 8 in: ``radio.config(group=8)``.
| code for the beacon in the Hot-Or-Cold game. The seekers look for beacons and display hot or cold hints based on the distance. 


.. code-block:: python
    
    from microbit import *
    import radio


    # Set radio group to 1
    radio.config(group=1)
    # Set transmit power to 6
    radio.config(power=6)

    whie True:
        # Send the number 0
        radio.send(0)
        # Show the heart icon
        display.show(Image.HEART)
        # Pause for a moment
        sleep(1000)
        # Show the small heart icon
        display.show(Image.SMALL_HEART)

    
----

.. admonition:: Exercise

    #. Modify the power level to 2, 3, 4 or 5.

----

Certainly! Below is the equivalent MicroPython code for the microbit based on the provided JavaScript:

.. code-block:: python
    
    from microbit import *
    import radio


    # Set radio group to 1
    radio.config(group=1)
    # Set the received message handler
    radio.on()

    # Function to handle received messages
    def on_received_message():
        message = radio.receive()
        if message:
            # Get the signal strength
            signal_strength = radio.receive_full()[1]
            # Show the signal strength
            display.show(signal_strength)


