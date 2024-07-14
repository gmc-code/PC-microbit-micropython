====================================================
Radio Hot or Cold
====================================================

Beacons
-------------------------

| Set up the group value in: ``radio.config(group=8)``.
| Set the radio power so that it is not quite powerful enough to reach the whole room.
| ``radio.config(power=3)``

.. code-block:: python
    
    from microbit import *
    import radio


    # Set radio group
    radio.config(group=8)
    # Set transmit power
    radio.config(power=3)
    radio.on()

    while True:
        # Send the number 3 as a string
        radio.send("3")
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

    #. Modify the power level to 1 or 2 to limit the distance of the beacons.

----

Seekers
-------------------------

| The seekers look for beacons and display the power reading.
| 0 is the strongest value which indicates zero distance from the beacon.
| Typically, the strongest value read in testing has been -17, not 0.
| -255 is the weakest, which indicates a long distance from the beacon.  

.. code-block:: python
    
    from microbit import *
    import radio


    # Set radio group
    radio.config(group=8)
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
        sleep(200)

----

Hot and cold meter
---------------------


| Set up the group value in: ``radio.config(group=8)``.
| Set the radio power so that it is at the maximum power.
| ``radio.config(power=7)``

.. code-block:: python
    
    from microbit import *
    import radio


    # Set radio group
    radio.config(group=8)
    # Set transmit power
    radio.config(power=7)
    radio.on()

    while True:
        # Send the number 7 as a string
        radio.send("7")
        # Show the heart icon
        display.show(Image.HEART)
        # Pause for a moment
        sleep(1000)
        # Show the small heart icon
        display.show(Image.HEART_SMALL)
        # Pause for a moment
        sleep(1000) 


| Here is some code for a 5 level meter.
| Can you modify the the code to show 10 levels by using brightness of 4 and 9?

.. code-block:: python
    
    from microbit import *
    import radio


    radio.config(group=8)
    radio.on()


    def display_level(level):
        x_list = [0, 1, 2, 3, 4]
        # display
        if level < 2:
            y_val = 4
            y_list = None
            y_clear_list = [0, 1, 2, 3]
        elif level < 4:
            y_val = 3
            y_list = [4]
            y_clear_list = [0, 1, 2]
        elif level < 6:
            y_val = 2
            y_list = [3, 4]
            y_clear_list = [0, 1]
        elif level < 8:
            y_val = 1
            y_list = [2, 3, 4]
            y_clear_list = [0]
        elif level < 10:
            y_val = 0
            y_list = [1, 2, 3, 4]
            y_clear_list = None
        else:
            y_val = None
            y_list = [0, 1, 2, 3, 4]
            y_clear_list = None

        for x in x_list:
            if y_val is not None:
                display.set_pixel(x, y_val, val)
            if y_list is not None:
                for y in y_list:
                    display.set_pixel(x, y, 9)
            if y_clear_list is not None:
                for y in y_clear_list:
                    display.set_pixel(x, y, 0)


    while True:
        message = radio.receive_full()
        if message:
            signal = int(message[1])
            # scale signal strength to levels 0 to 9
            # the values here may need adjusting(-116, -17)
            level = scale(signal, from_=(-116, -17), to=(0, 9))
            display_level(level)

