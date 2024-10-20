==========================
ustruct
==========================

.. py:module:: ustruct

| The `ustruct` module in MicroPython is used to pack and unpack primitive data types.
| This module is particularly useful for handling binary data and interfacing with hardware that expects data in specific formats.
| see: https://docs.micropython.org/en/latest/library/struct.html

.. function:: calcsize(fmt)

   Return the number of bytes needed to store the given *fmt*.

.. function:: pack(fmt, v1, v2, ...)

   Pack the values *v1*, *v2*, ... according to the format string *fmt*.
   The return value is a bytes object encoding the values.

.. function:: pack_into(fmt, buffer, offset, v1, v2, ...)

   Pack the values *v1*, *v2*, ... according to the format string *fmt*
   into a *buffer* starting at *offset*. *offset* may be negative to count
   from the end of *buffer*.

.. function:: unpack(fmt, data)

   Unpack from the *data* according to the format string *fmt*.
   The return value is a tuple of the unpacked values.

.. function:: unpack_from(fmt, data, offset=0, /)

   Unpack from the *data* starting at *offset* according to the format string
   *fmt*. *offset* may be negative to count from the end of *data*. The return
   value is a tuple of the unpacked values.

 Pack and unpack
-------------------

.. code-block:: python

    from microbit import *
    import ustruct

    # Pack data
    packed_data = ustruct.pack('hhl', 1, 2, 3)
    print(packed_data)  # Output: b'\x01\x00\x02\x00\x03\x00\x00\x00'

    # Unpack data
    unpacked_data = ustruct.unpack('hhl', packed_data)
    print(unpacked_data)  # Output: (1, 2, 3)

Radio send and receive bytes
----------------------------------

| THer are two microbits communicating via radio.
| Send accelerometer data from one microbit to another.
| Using ustruct.pack ensures the data is sent in a compact binary format.
| Using ustruct.unpack to convert the data back.

| Sender code:

.. code-block:: python

    from microbit import *
    import radio
    import ustruct

    radio.on()

    while True:
        x = accelerometer.get_x()
        y = accelerometer.get_y()
        z = accelerometer.get_z()
        # Pack the data into a binary format
        packed_data = ustruct.pack('>hhh', x, y, z)
        # Send the packed data over radio
        radio.send_bytes(packed_data)

        sleep(1000)

| Receiver code:

.. code-block:: python

    from microbit import *
    import radio
    import ustruct

    radio.on()

    while True:
        incoming = radio.receive_bytes()
        if incoming:
            # Unpack the received binary data
            x, y, z = ustruct.unpack('>hhh', incoming)
            # Display the unpacked data
            display.scroll("X:{} Y:{} Z:{}".format(x, y, z), delay=80)
