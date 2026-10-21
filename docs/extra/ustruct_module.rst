==========================
ustruct
==========================

.. py:module:: ustruct

| The `ustruct` module in MicroPython is used to pack and unpack primitive data types.
| This module is particularly useful for handling binary data and interfacing with hardware that expects data in specific formats.
| See: `<https://docs.micropython.org/en/latest/library/struct.html>`_
| See: `<https://www.educative.io/answers/what-is-the-python-struct-module>`_

| The struct module in Python is used to convert native Python data types such as strings and numbers into a string of bytes and vice versa.

| Supported size/byte order prefixes: @, <, >, !.

| Supported format codes: b, B, h, H, i, I, l, L, q, Q, s, P, f, d (the latter 2 depending on the floating-point support).

----

.. function:: calcsize(fmt)

   Return the number of bytes needed to store the given *fmt*.

| '>hhh' is three 2-byte integers, so it needs 6 bytes.

.. code-block:: python

    from microbit import *
    import ustruct

    display.scroll(ustruct.calcsize('>hhh'), delay=80)  # 6
    display.scroll(ustruct.calcsize('>bi'), delay=80)   # 5



.. function:: pack(fmt, v1, v2, ...)

   Pack the values *v1*, *v2*, ... according to the format string *fmt*.
   The return value is a bytes object encoding the values.

| The temperature is packed into 2 bytes.

.. code-block:: python

    from microbit import *
    import ustruct

    packed = ustruct.pack('>h', temperature())
    display.scroll(len(packed), delay=80)  # 2
    display.scroll(str(packed), delay=80)  # e.g. b'\x00\x15'



.. function:: pack_into(fmt, buffer, offset, v1, v2, ...)

   Pack the values *v1*, *v2*, ... according to the format string *fmt*
   into a *buffer* starting at *offset*. *offset* may be negative to count
   from the end of *buffer*.

| The values 100 and -5 are packed into an existing bytearray.

.. code-block:: python

    from microbit import *
    import ustruct

    buf = bytearray(4)
    ustruct.pack_into('>hh', buf, 0, 100, -5)
    display.scroll(str(buf), delay=80)  # bytearray(b'\x00d\xff\xfb')



.. function:: unpack(fmt, data)

   Unpack from the *data* according to the format string *fmt*.
   The return value is a tuple of the unpacked values.

.. code-block:: python

    from microbit import *
    import ustruct

    data = b'\x00\x64\xff\xfb'
    values = ustruct.unpack('>hh', data)
    display.scroll(str(values), delay=80)  # (100, -5)



.. function:: unpack_from(fmt, data, offset=0, /)

   Unpack from the *data* starting at *offset* according to the format string
   *fmt*. *offset* may be negative to count from the end of *data*. The return
   value is a tuple of the unpacked values.

| The first 2 bytes are skipped by starting at offset 2.

.. code-block:: python

    from microbit import *
    import ustruct

    data = b'\x01\x02\x00\x64'
    values = ustruct.unpack_from('>h', data, 2)
    display.scroll(values[0], delay=80)  # 100



----

Pack and unpack
-------------------

.. code-block:: python

    from microbit import *
    import ustruct

    # Pack data
    packed_data = ustruct.pack('hhl', 1, 2, 3)
    # print(packed_data)  # Output: b'\x01\x00\x02\x00\x03\x00\x00\x00'
    display.scroll(str(packed_data), delay=80)

    # Unpack data
    unpacked_data = ustruct.unpack('hhl', packed_data)
    # print(unpacked_data)  # Output: (1, 2, 3)
    display.scroll(str(unpacked_data), delay=80)


----

Radio send and receive bytes
----------------------------------

| There are two microbits communicating via radio.
| Send accelerometer data from one microbit to another.
| Using ustruct.pack ensures the data is sent in a compact binary format.
| Using ustruct.unpack to convert the data back.
| Both micro:bits use the same radio group so that other micro:bits in the room don't interfere.
| The receiver checks the message is 6 bytes long (3 values of 2 bytes each) before unpacking it.

| Sender code:

.. code-block:: python

    from microbit import *
    import radio
    import ustruct

    radio.config(group=7)
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

    radio.config(group=7)
    radio.on()

    while True:
        incoming = radio.receive_bytes()
        if incoming and len(incoming) == 6:
            # Unpack the received binary data
            x, y, z = ustruct.unpack('>hhh', incoming)
            # Display the unpacked data
            display.scroll("X:{} Y:{} Z:{}".format(x, y, z), delay=80)
