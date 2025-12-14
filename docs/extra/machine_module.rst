==========================
machine module
==========================


.. py:module:: machine

| MicroPython contains a ``machine`` module with specific functions related to the microbit.
| See: `<https://microbit-micropython.readthedocs.io/en/stable/machine.html>`
| Some useful methods from the machine module are below.

----

time_pulse_us
----------------

| ``time_pulse_us`` is used by distance sensors.
| See an example of its use at: `<https://pc-microbit-extension.readthedocs.io/en/latest/bots/Maqueen/Maqueen_distance_sensors.html>`

.. method:: machine.time_pulse_us(pin, pulse_level, timeout_us=1000000)

   Return the duration of a pulse, in microseconds, on the given pin.

   :param pin: The pin to measure the pulse on. This should be a `Pin` object.
   :param pulse_level: The pulse level to measure (0 or 1).  0 to time a low pulse or
    1 to time a high pulse.
   :param timeout_us: The timeout in microseconds. Default is 1,000,000 microseconds (1 second).
   :returns: The duration of the pulse in microseconds, or -1 if the timeout was reached.

| e.g. ``pulse_time = machine.time_pulse_us(pin14, 1, 1160000)`` measures the time for the pulse to be reflected back.

#. If the current input value of the pin is different to *pulse_level*, the function first waits until the pin input becomes equal to *pulse_level*. The function will return -2 if there was timeout waiting for this condition.
#. It then times the duration that the pin is equal to *pulse_level*. If the pin is already equal to *pulse_level* then timing starts straight away. The function will return -1 if there was timeout waiting for this condition.
#. The timeout is the same for both cases and given by *timeout_us* in microseconds.

----

reset
---------

.. method:: machine.reset()

   Resets the microbit like pushing the external reset button and starts the program from the beginning.

