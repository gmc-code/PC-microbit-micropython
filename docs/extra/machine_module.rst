==========================
machine module
==========================

.. py:module:: machine

| MicroPython contains a ``machine`` module with specific functions related to the microbit.

.. note::

   Many functions achieve direct and unrestricted access to the hardware blocks on a the microbit. Used incorrectly, this can lead to malfunction of the microbit, and in extreme cases, hardware damage.

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/machine.html


----

time_pulse_us
----------------

| ``time_pulse_us`` is used by distance sensors.
| See an example of its use at: https://pc-microbit-extension.readthedocs.io/en/latest/bots/Maqueen/Maqueen_distance_sensors.html

.. method:: machine.time_pulse_us(pin, pulse_level, timeout_us=1000000)

    Time a pulse on the given *pin*, and return the duration of the pulse in 
    microseconds. The *pulse_level* argument should be 0 to time a low pulse or
    1 to time a high pulse.

| e.g. ``pulse_time = machine.time_pulse_us(pin14, 1, 1160000)`` measures the time for the pulse to be reflected back.

#. If the current input value of the pin is different to *pulse_level*, the function first waits until the pin input becomes equal to *pulse_level*. The function will return -2 if there was timeout waiting for this condition.
#. It then times the duration that the pin is equal to *pulse_level*. If the pin is already equal to *pulse_level* then timing starts straight away. The function will return -1 if there was timeout waiting for this condition.
#. The timeout is the same for both cases and given by *timeout_us* in microseconds.

