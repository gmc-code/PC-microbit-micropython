====================================================
Radio images
====================================================

Boats
-------------

.. image:: images/boat_sinking.gif
    :scale: 60 %
    :align: center

| The code below sends multiple image strings then converts those to images on the receiving microbit.

.. code-block:: python

    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    # Define the boat images as strings
    boat1 = '05050:05050:05050:99999:09990'
    boat2 = '00000:05050:05050:05050:99999'
    boat3 = '00000:00000:05050:05050:05050'
    boat4 = '00000:00000:00000:05050:05050'
    boat5 = '00000:00000:00000:00000:05050'
    boat6 = '00000:00000:00000:00000:00000'

    sinking_boats = [boat1, boat2, boat3, boat4, boat5, boat6]

    while True:
        if button_a.was_pressed():
            # Send each boat image over radio
            for boat in sinking_boats:
                radio.send(boat)
                sleep(500)  # Delay between each image
        else:
            # Receive the boat image
            received = radio.receive()
            if received in sinking_boats:
                # Convert the received string back to an image and display it
                display.show(Image(received))


.. admonition:: Tasks

    #. Modify the code above to add an animation of the boat rising when the B-button is pressed.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above to add an animation of the boat rising when the B-button is pressed.

                .. code-block:: python
                
                    from microbit import *
                    import radio

                    # Choose own group in pairs 0-255
                    radio.config(group=8)
                    # Turn on the radio
                    radio.on()

                    # Define the boat images as strings
                    boat1 = '05050:05050:05050:99999:09990'
                    boat2 = '00000:05050:05050:05050:99999'
                    boat3 = '00000:00000:05050:05050:05050'
                    boat4 = '00000:00000:00000:05050:05050'
                    boat5 = '00000:00000:00000:00000:05050'
                    boat6 = '00000:00000:00000:00000:00000'

                    sinking_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
                    rising_boats = sinking_boats[::-1]
                    # rising_boats = [boat6, boat5, boat4, boat3, boat2, boat1]

                    while True:
                        if button_a.was_pressed():
                            # Send each boat image over radio
                            for boat in sinking_boats:
                                radio.send(boat)
                                sleep(500)  # Delay between each image
                        elif button_b.was_pressed():
                            # Send each boat image over radio
                            for boat in rising_boats:
                                radio.send(boat)
                                sleep(500)  # Delay between each image
                        else:
                            # Receive the boat image
                            received = radio.receive()
                            if received in sinking_boats:
                                # Convert the received string back to an image and display it
                                display.show(Image(received))

----

Manual image lists
------------------------

.. image:: images/rps.gif
    :scale: 60 %
    :align: center


| Below is code for the rock paper scissors images.

.. code-block:: python

    from microbit import *

    # Define images strings for Rock, Paper and Scissors
    rock = '00000:09990:99999:09990:00000:'
    paper = '99999:90009:90009:90009:99999:'
    scissors = '99009:99090:00900:99090:99009:'

    # Put the image strings in a list
    image_strings = [rock, paper, scissors]


.. admonition:: Tasks

    #. Modify the code above send one random image from the rps_images image list.
    #. Modify the code above send three random images from the rps_images image list as an animation affect.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above send one random image from the rps_images image list.

                .. code-block:: python
                
                    from microbit import *
                    import radio
                    import random

                    # Choose own group in pairs 0-255
                    radio.config(group=8)
                    # Turn on the radio
                    radio.on()

                    # Define image_strings for Rock, Paper and Scissors
                    rock = '00000:09990:99999:09990:00000:'
                    paper = '99999:90009:90009:90009:99999:'
                    scissors = '99009:99090:00900:99090:99009:'

                    # Put the image_strings in a list
                    image_strings = [rock, paper, scissors]


                    def get_rps_image():
                        image_string = random.choice(image_strings)
                        return image_string


                    def send_image():
                        image_string = get_rps_image()
                        radio.send(image_string)


                    def receive_image():
                        # Receive a message from the radio
                        incoming = radio.receive()
                        if incoming:
                            try:
                                display.show(Image(incoming))
                            except:
                                display.show(incoming, delay=100)


                    while True:
                        if button_a.was_pressed():
                            send_image()
                        # Receive the image
                        receive_image()


            .. tab-item:: Q2

                Modify the code above send three random images from the rps_images image list as an animation affect.

                .. code-block:: python
                
                    from microbit import *
                    import radio
                    import random

                    # Choose own group in pairs 0-255
                    radio.config(group=8)
                    # Turn on the radio
                    radio.on()

                    # Define image_strings for Rock, Paper and Scissors
                    rock = '00000:09990:99999:09990:00000:'
                    paper = '99999:90009:90009:90009:99999:'
                    scissors = '99009:99090:00900:99090:99009:'

                    # Put the image_strings in a list
                    image_strings = [rock, paper, scissors]


                    def get_rps_image():
                        image_string = random.choice(image_strings)
                        return image_string


                    def send_image():
                        image_string = get_rps_image()
                        radio.send(image_string)


                    def receive_image():
                        # Receive a message from the radio
                        incoming = radio.receive()
                        if incoming:
                            try:
                                display.show(Image(incoming))
                            except:
                                display.show(incoming, delay=100)


                    while True:
                        if button_a.was_pressed():
                            for _ in range(3):
                                send_image()
                                sleep(200)
                            # sleep(500)
                        # Receive the image
                        receive_image()


----

Built in images
---------------------

.. image:: images/faces.gif
    :scale: 60 %
    :align: center


| The code below chooses 5 random built in images from a list and sends them one at a time as strings by radio.

.. code-block:: python

    from microbit import *
    import radio
    import random

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()


    # Function to extract numbers from the image string
    def extract_image_string(image):
        # Convert the image to a string
        full_image_string = str(image)
        # Replace the colon and newline characters with an empty string
        image_string = full_image_string.replace("'", "").replace("\n", "").replace(" ", "")
        image_string = image_string.replace("(", "").replace(")", "").replace("Image", "")
        return image_string


    images = [Image.HAPPY, Image.SMILE, Image.SAD, Image.CONFUSED, Image.ANGRY, Image.ASLEEP, 
                Image.SURPRISED, Image.SILLY, Image.FABULOUS, Image.MEH]


    def get_rand_images(num):
        # num must be less than len(images)
        new_images = []
        while len(new_images) < num:
            image = random.choice(images)
            if image not in new_images:
                new_images.append(image)
        return new_images


    def send_image():
        for img in get_rand_images(5):  # Send 5 images
            radio.send(extract_image_string(img))
            sleep(500)  # Delay between each image


    def receive_image():
        # Receive a message from the radio
        incoming = radio.receive()
        if incoming:
            try:
                display.show(Image(incoming))
            except:
                display.show(incoming, delay=100)


    while True:
        if button_a.was_pressed():
            send_image()
        # Receive the image
        receive_image()

.. admonition:: Exercise

    #. Modify the code above to send 3 random images from a list of animal images.


