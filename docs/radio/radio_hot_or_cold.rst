====================================================
Radio Hot or Cold
====================================================

Beacons
-------------------------

| Set up the group value in: ``radio.config(group=8)``.
| Set the radio power so that it is not quite powerful enough to reach the whole room.``radio.config(power=6)``

.. code-block:: python
    
    from microbit import *
    import radio


    # Set radio group
    radio.config(group=8)
    # Set transmit power
    radio.config(power=1)
    # Set the received message handler
    radio.on()

    while True:
        # Send the number 0
        radio.send("0")
        # Show the heart icon
        display.show(Image.HEART)
        # Pause for a moment
        sleep(1000)
        # Show the small heart icon
        display.show(Image.HEART_SMALL)
    # Pause for a moment
        sleep(1000) 

    
----

.. admonition:: Exercise

    #. Modify the power level to 3, or 5 limit the distance of the beacons.

----

Seekers
-------------------------

| The seekers look for beacons and display the power reading.
| 0 is the strongest which indicates zero distance from the beacon.
| -255 is the weakest which indicates a long distance from the beacon.  

.. code-block:: python
    
    from microbit import *
    import radio


    # Set radio group
    radio.config(group=8)
    # Set the received message handler
    radio.on()

    # Function to handle received messages
    def on_received_message():
        incoming_full_details = radio.receive_full()
        if incoming_full_details:
            msg, rssi, timestamp = incoming_full_details
            # Show the signal strength
            display.scroll(rssi, delay=60)

    while True:
        # received
        on_received_message()

