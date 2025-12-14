====================================================
Radio temperature
====================================================

Indoor and outdoor temperature
------------------------------

| Set up the group in pairs with a value 0-255 by modifying the group in: ``radio.config(group=8)``.
| Turn on the radio using: ``radio.on()``
| Use different code for the outdoor microbit compared to the indoor.

| Outdoor: Set up the outdoor microbit so that it only sends the temperature every minute

.. code-block:: python

    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    while True:
        outdoor_temp = temperature()
        radio.send(str(outdoor_temp))
        sleep(60000)

| Indoor: Set up the indoor microbit so that pressing the A-button displays the indoor temperature and pressing the B-button displays the outdoor temperature.

.. code-block:: python

    from microbit import *
    import radio

    # Choose own group in pairs 0-255
    radio.config(group=8)
    # Turn on the radio
    radio.on()

    outdoorTemp = '-'

    while True:
        incoming_message = radio.receive()
        if incoming_message:
            outdoorTemp = incoming_message
        if button_a.was_pressed():
            display.scroll(str(temperature()))
        elif button_b.was_pressed():
            display.scroll(outdoorTemp)

----

.. admonition:: Tasks

    #. Modify the code of the microbits so that they both scroll the outdoor temperature every 60 seconds.
    #. Modify the code of the outdoor microbit so that when the outdoor microbit is reset along with pressing the A-button, the time between sends is 10 seconds. When it is reset along with pressing the B-button, the time between sends is 30 seconds. On reset with button pressing the sleep time is 60 seconds.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code of the microbits so that they both scroll the outdoor temperature every 60 seconds.

                .. code-block:: python

                    from microbit import *
                    import radio

                    # Choose own group in pairs 0-255
                    radio.config(group=8)
                    # Turn on the radio
                    radio.on()

                    while True:
                        outdoor_temp = temperature()
                        radio.send(str(outdoor_temp))
                        display.scroll(outdoor_temp)
                        sleep(60000)

                .. code-block:: python

                    from microbit import *
                    import radio

                    # Choose own group in pairs 0-255
                    radio.config(group=8)
                    # Turn on the radio
                    radio.on()

                    outdoor_temp = '-'

                    while True:
                        incoming_message = radio.receive()
                        if incoming_message:
                            outdoor_temp = incoming_message
                            display.scroll(outdoor_temp)
                        if button_a.was_pressed():
                            display.scroll(str(temperature()))
                        elif button_b.was_pressed():
                            display.scroll(outdoor_temp)



            .. tab-item:: Q2

                Modify the code of the outdoor microbit so that when the outdoor microbit is reset along with pressing the A-button, the time between sends is 10 seconds. When it is reset along with pressing the B-button, the time between sends is 30 seconds. On reset with button pressing the sleep time is 60 seconds.

                .. code-block:: python

                    from microbit import *
                    import radio

                    # Choose own group in pairs 0-255
                    radio.config(group=8)
                    # Turn on the radio
                    radio.on()

                    if button_a.was_pressed():
                        sleep_time = 10000
                    elif button_b.was_pressed():
                        sleep_time = 30000
                    else:
                        sleep_time = 60000

                    while True:
                        outdoor_temp = temperature()
                        radio.send(str(outdoor_temp))
                        display.scroll(outdoor_temp)
                        sleep(sleep_time)

----


.. admonition:: Tasks

    #. See: `<https://pc-microbit-micropython.readthedocs.io/en/latest/introduction/power_management.html>`_#deep-sleep-wake-via-run-every
    Modify the code of the outdoor microbit so that it uses deep sleep which is renewed every 24 hours, along with run_every to send the temperature every 60 seconds.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code of the outdoor microbit so that it uses deep sleep which is renewed every 24 hours, along with run_every to send the temperature every 60 seconds.

                .. code-block:: python

                    from microbit import *
                    import power
                    import radio

                    # Choose own group in pairs 0-255
                    radio.config(group=8)
                    # Turn on the radio
                    radio.on()

                    @run_every(s=60)
                    def wakeup_call():
                        outdoor_temp = temperature()
                        radio.send(str(outdoor_temp))
                        display.scroll(outdoor_temp)

                    day_ms = 24 * 60 * 60 * 1000
                    while True:
                        # renew deep sleep every day
                        power.deep_sleep(wake_on=None,ms=day_ms,run_every=True)

