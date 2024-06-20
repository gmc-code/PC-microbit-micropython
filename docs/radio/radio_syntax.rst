====================================================
Radio syntax
====================================================

Radio Module
--------------

.. py:module:: radio

| The ``radio`` module allows microbits to send messages to each other via wireless networks.
| Firstly, import the ``radio`` module.

.. py:attribute:: import radio
    
    Import the radio module

.. code-block:: python

    from microbit import *
    import radio

----

Radio On and Off
-----------------

| To send or receive messages, the radio needs to be turned on.

.. py:function:: on()

    Turns the radio on.

.. code-block:: python

    from microbit import *
    import radio

    radio.on()

| Turn off the radio to saving power and memory.

.. py:function:: off()

    Turns off the radio, thus saving power and memory.

----

Radio group
------------------------

| Set the microbits to the same group number so they communicate with each other and only with those in the same group.
| Without setting the group number, all nearby microbits would be in group 0 and so would be able to communicate with each other by default.

.. py:function:: config(group=0)

    The ``group`` (default=0) is an 8-bit value (0-255) used with the
    ``address`` when filtering messages. Conceptually, "address" is like a
    house/office address and "group" is like the person at that address to
    which you want to send your message.

.. code-block:: python

    from microbit import *
    import radio

    radio.config(group=8)
    radio.on()


| Those working together should set the group to an integer from 0 to 255 so that only their microbits share messages.
| Set the length to the maximum value if sending long messages. Lengths greater that the default of 32 may be required if sending long strings.

.. code-block:: python

    from microbit import *
    import radio

    radio.on()
    radio.config(group=8, length=251)


----

Radio send and receive
------------------------

| `send()`: This method is used to send a string. The string is converted to bytes before it is transmitted. It's useful when you want to send text messages or commands that can be represented as strings. If you send a string with `send()`, you should use `receive()` to get the data as a string on the other end.

| When sending messages via the radio on the microbit, each character in the message will be converted to its ASCII representation, then to binary, and sent as a series of bytes. 
| In ASCII, A is represented by the number 65. In binary, 65 is 01000001. This is 8 bits of information, or 1 byte. 
| The length parameter in the radio configuration determines how many bytes (or characters) that can be sent in a single message.
| A byte is a unit of digital information that consists of 8 bits. A bit is the most basic unit of information in computing and can have only one of two values, 0 or 1.


.. py:function:: send(message)

    Sends a message string. This is the equivalent of
    ``send_bytes(bytes(message, 'utf8'))`` but with ``b'\x01\x00\x01'``
    prepended to the front (to make it compatible with other platforms that
    target the microbit).

.. code-block:: python

    from microbit import *
    import radio

    radio.on()
    radio.config(group=8, length=251)
    radio.send('hello')


.. py:function:: receive()

    Works in exactly the same way as ``receive_bytes`` but returns whatever was sent.
    Currently, it's equivalent to ``str(receive_bytes(), 'utf8')`` but with a
    check that the first three bytes are ``b'\x01\x00\x01'`` (to make it
    compatible with other platforms that may target the microbit). It strips
    the prepended bytes before converting to a string.

    A ``ValueError`` exception is raised if conversion to a string fails.

.. code-block:: python

    from microbit import *
    import radio

    radio.on()
    radio.config(group=8, length=251)
    

    while True:
        # send
        if button_a.was_pressed():
            radio.send('hello')
        # receive
        message = radio.receive()
        if message:
            display.scroll(message)


----

bytes
-------------

| `send_bytes()`: This method is used to send bytes. This is useful when you want to send data that can't be easily represented as a string, such as sensor data or binary data.
| If you send bytes with `send_bytes()`, you should use `receive_bytes()` to get the data as bytes on the other end. 


.. py:function:: send_bytes(message)

    Sends a message containing bytes.

.. py:function:: receive_bytes()

    Receive the next incoming message on the message queue. Returns ``None`` if
    there are no pending messages. Messages are returned as bytes.

.. py:function:: receive_bytes_into(buffer)

    Receive the next incoming message on the message queue. Copies the message
    into ``buffer``, trimming the end of the message if necessary.
    Returns ``None`` if there are no pending messages, otherwise it returns the length
    of the message (which might be more than the length of the buffer).

.. code-block:: python

    from microbit import *
    import radio

    radio.on()
    radio.config(group=8, length=251)
    

    while True:
        # send
        if button_a.was_pressed():
            radio.send_bytes(b'LATER')
        # receive
        message = radio.receive_bytes()
        if message:
            display.scroll(message)

----

Msg, Signal strength, timestamps
----------------------------------

.. py:function:: receive_full()

    Returns a tuple containing three values representing the next incoming
    message on the message queue. If there are no pending messages then
    ``None`` is returned.

    The three values in the tuple represent:

    * the next incoming message on the message queue as bytes.
    * the RSSI (signal strength): a value between 0 (strongest) and -255 (weakest) as measured in dBm.
    * a microsecond timestamp: the value returned by ``time.ticks_us()`` when the message was received.
    
    This function is useful for providing information needed for triangulation
    and/or trilateration (using distances) with other microbit devices.

| The code below uses receive_full which expects byte strings such as that from ``radio.send_bytes(b'later')``.
| B button pressing uses ``radio.send_bytes(b'later')``. This sends the string as bytes and is then received by ``radio.receive_full()`` as bytes as expected.
| A button pressing uses  ``radio.send('hello')``. Sending a string results in the bytes prefix being added ``b'\x01\x00\x01'``. This needs to be removed, otherwise "???" will appear before the string when received.


.. code-block:: python

    from microbit import *
    import radio

    radio.config(group=8, length=251)
    radio.on()

    while True:
        # send
        if button_a.was_pressed():
            radio.send('hello')
        elif button_b.was_pressed():
            radio.send_bytes(b'later')
        # receive
        details = radio.receive_full()
        if details:
            msg, rssi, timestamp = details
            decoded_msg = msg.replace(b'\x01\x00\x01', b'').decode()
            display.scroll(decoded_msg)
            display.scroll(rssi)
            display.scroll(timestamp)

----

Radio settings
-----------------------

| The full list of config settings are below. 
| If ``config`` is not called then the defaults are used.

.. py:function:: config(length=32, queue=3, channel=7, power=6, address=0x75626974, group=0, data_rate=radio.RATE_1MBIT)

    Configures various keyword based settings relating to the radio.

    The ``length`` (default=32) defines the maximum length, in bytes, of a
    message sent via the radio. 1 character = 1 byte. It can be up to 251 bytes long (254 - 3 bytes
    for S0, LENGTH and S1 preamble; the S0, LENGTH, and S1 are parts of the packet structure used in radio communication and are used to indicate the start of a packet, the length of the packet, and for error checking, respectively). 

    The ``queue`` (default=3) specifies the number of messages that can be
    stored on the incoming message queue. If there are no spaces left on the
    queue for incoming messages, then the incoming message is dropped.

    The ``channel`` (default=7) can be an integer value from 0 to 83
    (inclusive) that defines an arbitrary "channel" to which the radio is
    tuned. Messages will be sent via this channel and only messages received
    via this channel will be put onto the incoming message queue. Each step is
    1MHz wide, based at 2400MHz.

    The ``power`` (default=6) is an integer value from 0 to 7 (inclusive) to
    indicate the strength of signal used when broadcasting a message. The
    higher the value the stronger the signal, but the more power is consumed
    by the device. The numbering translates to positions in the following list
    of dBm (decibel milli-watt) values: [-30, -20, -16, -12, -8, -4, 0, 4].

    The ``address`` (default=0x75626974) is an arbitrary name, expressed as a
    32-bit address, that's used to filter incoming packets at the hardware
    level, keeping only those that match the address you set. The default used
    by other microbit related platforms is the default setting used here.

    The ``group`` (default=0) is an 8-bit value (0-255) used with the
    ``address`` when filtering messages. Conceptually, "address" is like a
    house/office address and "group" is like the person at that address to
    which you want to send your message.

    The ``data_rate`` (default=radio.RATE_1MBIT) indicates the speed at which
    data throughput takes place. Can be one of the following constants defined
    in the ``radio`` module : ``RATE_1MBIT`` or ``RATE_2MBIT``.

    .. note::

        A lower data rate of of 250kbit/sec is supported in microbit V1, and
        may be possible with microbit V2, but it is not guaranteed to work on
        all devices. To access this hidden feature for compatibility with V1
        pass ``2`` to the ``data_rate`` argument.



.. py:function:: reset()

    Reset the settings to their default values for the ``config`` function.


