==========================
ucollections
==========================

.. py:module:: ucollections

| MicroPython contains an ``ucollections`` module based upon the ``collections`` module in the Python standard library.
| This module has 2 collections from the standard python collections module.
| See: https://docs.micropython.org/en/latest/library/collections.html#collections.namedtuple
| See: https://docs.micropython.org/en/latest/library/collections.html#collections.OrderedDict

----

namedtuple
--------------------------

Create a new namedtuple type with a specific name and set of fields. A namedtuple allows access to its fields not just by numeric index, but also using field names. Fields is a sequence of strings specifying field names. It can also be a string with space-separated field named (but this is less efficient).

.. function:: ucollections.namedtuple(name, fields)

    :param name: The name of the new tuple subclass.
    :type name: str
    :param fields: A string with space-separated field names or a list of field names.
    :type fields: str or list
    :return: A new tuple subclass with named fields.
    :rtype: namedtuple


| Create a named tuple for a point, x, y.

.. code-block:: python

   from microbit import *
   from ucollections import namedtuple as nt

   Point = nt('Point', ['x', 'y'])
   p = Point(3, 4)     # instantiate with positional arguments
   print(p.x, p.y)           # fields accessible by name
   p2 = Point(x=2, y=5)     # instantiate keyword arguments
   print(p2.x, p2.y)           # fields accessible by name


----

Logging button presses
------------------------

.. code-block:: python

    from microbit import *
  from ucollections import namedtuple as nt

  # Define a namedtuple for button press events
  ButtonEvent = nt('ButtonEvent', ['button', 'timestamp'])

  events = []

  while True:
      if button_a.was_pressed():
          event = ButtonEvent('A', running_time())
          events.append(event)
          display.scroll("A pressed")
      elif button_b.was_pressed():
          event = ButtonEvent('B', running_time())
          events.append(event)
          display.scroll("B pressed")

      # Display logged events
      if button_a.is_pressed() and button_b.is_pressed():
          for event in events:
              display.scroll("Button:{} Time:{}".format(event.button, event.timestamp))
          events.clear()

      sleep(100)


----

OrderedDict
--------------------------

| Create a dictionary type subclass which remembers and preserves the order of keys added.
| When ordered dict is iterated over, keys or items are returned in the order they were added.

.. function:: ucollections.OrderedDict(name, fields)

    Create a dictionary type subclass which remembers and preserves the order of keys added.
    When ordered dict is iterated over, keys or items are returned in the order they were added.


Using an OrderedDict to store LED patterns
--------------------------------------------------

.. code-block:: python

    from microbit import *
    from ucollections import OrderedDict as Od
    import random

    # Create an OrderedDict to store LED patterns
    patterns = Od()
    patterns['heart'] = Image.HEART
    patterns['small_heart'] = Image.HEART_SMALL
    patterns['happy'] = Image.HAPPY
    patterns['smile'] = Image.SMILE

    # Main loop
    while True:
        if button_a.was_pressed():
            # Display each pattern in sequence
            for name, pattern in patterns.items():
                display.show(pattern)
                sleep(500)
        elif button_b.was_pressed():
            # Display a random pattern
            for _ in range(len(patterns)):
                pattern = random.choice(list(patterns.values()))
                display.show(pattern)
                sleep(500)

Using an OrderedDict to store accelerometer readings
------------------------------------------------------

.. code-block:: python

    from microbit import *
    from ucollections import OrderedDict as Od

    # Create an OrderedDict to store sensor data
    sensor_data = Od()

    # Main loop
    while True:
        # Collect and store sensor data
        for i in range(5):
            x, y, z = accelerometer.get_x(), accelerometer.get_y(), accelerometer.get_z()
            sensor_data['xyz_{}'.format(i+1)] = (x, y, z)
            sleep(800)

        # Wait for button press
        while not(button_a.is_pressed()) and not(button_b.is_pressed()):
            sleep(1000)

        if button_a.is_pressed():
            # Display the collected sensor data
            for reading, values in sensor_data.items():
                display.scroll('{}: {}'.format(reading, values), delay=90)
            # Wait for button release to avoid repeated actions
            while button_a.is_pressed():
                sleep(10)

        elif button_b.is_pressed():
            # Calculate and display summary statistics
            total_readings = len(sensor_data)
            sum_x, sum_y, sum_z = 0, 0, 0

            for values in sensor_data.values():
                sum_x += values[0]
                sum_y += values[1]
                sum_z += values[2]

            avg_x = sum_x // total_readings
            avg_y = sum_y // total_readings
            avg_z = sum_z // total_readings

            display.scroll('Total: {}'.format(total_readings), delay=60)
            display.scroll('Avg X: {}'.format(avg_x), delay=60)
            display.scroll('Avg Y: {}'.format(avg_y), delay=60)
            display.scroll('Avg Z: {}'.format(avg_z), delay=60)

            # Wait for button release to avoid repeated actions
            while button_b.is_pressed():
                sleep(10)

        # Optionally clear sensor data for the next loop
        sensor_data.clear()
