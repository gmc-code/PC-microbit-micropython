====================================================
Radio secrets
====================================================

Unique groups
-------------------------

| Set up the group with a value 0-255 by changing the group value from 8 in: ``radio.config(group=8)``.
| Turn on the radio using: ``radio.on()``
| Use ``button_a.was_pressed()`` to send a message, **"A"**.
| Scroll classes_for_the_microbit received messages.
| ``if incoming_message is not None:`` relies on ``radio.receive()`` returning **None** when there is no message received. 


.. code-block:: python
    
    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    while True:
        # send
        if button_a.was_pressed():
            radio.send("A")
        # receive
        incoming_message = radio.receive()
        if incoming_message is not None:
            display.scroll(incoming_message)

----

.. admonition:: Exercise

    #. Modify the code to send "Y" when A is pressed, and "N" when B is pressed in order to answer Yes/No questions in secret.

----

Caesar cipher
-------------------------

| Set up the group with a value 1 to 25 by changing the group value from 8 in: ``radio.config(group=8)``.
| Turn on the radio using: ``radio.on()``
| Enter a secret message to send.
| Scroll any received messages.
| ``if incoming_message is not None:`` relies on ``radio.receive()`` returning **None** when there is no message received. 

.. code-block:: python
    
    from microbit import *
    import radio

    # Set up radio with group from 1 to 25 to reuse it for the shift
    radio.on()
    group = 25
    radio.config(channel=7, group=group)

    # Caesar cipher parameters
    SHIFT = group
    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    SECRET = 'WE_ARE_GROUP' + str(group)

    def caesar_cipher(message, shift):
        """
        Apply a Caesar cipher to a message.
        """
        cipher_text = ''
        for char in message:
            if char in ALPHABET:
                # Shift character
                index = (ALPHABET.index(char) + shift) % len(ALPHABET)
                cipher_text += ALPHABET[index]
            else:
                cipher_text += char
        return cipher_text

    while True:
        # Check for incoming messages
        incoming = radio.receive()
        if incoming:
            # Decode and display the message
            message = caesar_cipher(incoming, -SHIFT)
            display.scroll(message)

        # Check button presses to send a secret message
        if button_a.was_pressed():
            cipher_text = caesar_cipher(SECRET, SHIFT)
            radio.send(cipher_text)

----

.. admonition:: Exercises

    #. Modify the group and secret.
    #. Try setting up random groups by setting the group to a random integer from 1 to 9. Also use a secret message based on that group number.

----

Caesar cipher 2
-------------------------

| What does this code do?
| What happens when the black reset button is pressed?


.. code-block:: python
    
    from microbit import *
    import radio
    import random

    # Set up radio with group from 1 to 6 to reuse it for the shift
    radio.on()

    # Caesar cipher parameters

    ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    group_x = random.randint(1, 3)
    radio.config(channel=7, group=group_x)
    SHIFT = group_x
    SECRET = 'UR' + str(group_x)

    def caesar_cipher(message, shift):
        """
        Apply a Caesar cipher to a message.
        """
        cipher_text = ''
        for char in message:
            if char in ALPHABET:
                # Shift character
                index = (ALPHABET.index(char) + shift) % len(ALPHABET)
                cipher_text += ALPHABET[index]
            else:
                cipher_text += char
        return cipher_text

    while True:
        # Check for incoming messages
        incoming = radio.receive()
        if incoming:
            # Decode and display the message
            message = caesar_cipher(incoming, -group_x)
            display.scroll(message)
        # Check button presses to send a secret message
        if button_a.was_pressed():
            cipher_text = caesar_cipher(SECRET, SHIFT)
            radio.send(cipher_text)
        elif button_b.was_pressed():
            display.scroll(SHIFT)
            

.. admonition:: Exercises

    #. CLass activity: Write code to randomly change the group number, choosing from 11 to 19, after a message is received or on pressing the B-button. Use the A-button to send a message. Keep count of the the number of messages received and pulse the diamond images after every 5 messages received.



