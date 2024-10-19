==========================
os module
==========================

.. py:module:: log

| This module lets you log data to a ``MY_DATA`` file saved on a microbit.
| The data is structured in a table format and it can be viewed and plotted with
a browser.

See: `data logging page of the microbit.org website
<https://microbit.org/get-started/user-guide/data-logging/>`_.

----

set_labels
----------------

.. py:function:: set_labels(*labels, timestamp=log.SECONDS)

    Set up the log file header.

    :param \*labels: Any number of positional arguments, each corresponding to
        an entry in the log header. e.g. ``log.set_labels("X", "Y", "Z")``
    :param timestamp: Select the timestamp unit that will be automatically
        added as the first column in every row. Timestamp values can be one of
        ``log.MILLISECONDS``, ``log.SECONDS``, ``log.MINUTES``, ``log.HOURS``,
        ``log.DAYS`` or ``None`` to disable the timestamp. The default value
        is ``log.SECONDS``.

    Ideally this function should be called a single time, before any data is
    logged, to configure the data table header once.

    If a log file already exists when the programme starts, or if this function
    is called multiple times, it will check the labels already defined in the
    log file.
    If this function call contains any new labels not already present, it will
    generate a new header row with the additional columns.

    By default the first column contains a time stamp for each row. The time
    unit can be selected via the ``timestamp`` argument, e.g.
    ``log.set_labels("temp", timestamp=log.MINUTES)``



set_mirroring
----------------------

| This means that when you enable serial mirroring, every row of data that is logged will also be printed to the serial output, allowing you to monitor the data in real-time via a serial console.

.. py:function:: set_mirroring(serial)

    Configure mirroring of the data logging activity to the serial output.

    :param serial: ``True`` enables mirroring data to the serial output.

    Serial mirroring is disabled by default.
    When enabled, every row of data that is logged will also be printed to the serial output, allowing monitoring of the data in real-time via a serial console.


delete
---------------

.. py:function:: delete(full=False)

    Delete the contents of the log, including headers.

    :param full: ``True`` selects a "full" erase and ``False`` selects the
        "fast" erase method.

    To add the log headers again the ``set_labels`` function should to be
    called after this function.

    There are two erase modes; "full" completely removes the data from the
    physical storage, and "fast" invalidates the data without removing it.


add
------------

.. py:function:: add( data_dictionary, /, *, **kwargs)

    Add a data row to the log.

    There are two ways to log data with this function:

    #. Via keyword arguments, each argument name representing a label.

       * e.g. ``log.add(X=compass.get_x(), Y=compass.get_y())``

    #. Via a dictionary, each dictionary key representing a label.

       * e.g. ``log.add({ "X": compass.get_x(), "Y": compass.get_y() })``

    The keyword argument option can be easier to use, and the dictionary option
    allows the use of spaces (and other special characters), that could not be
    used with the keyword arguments.

    New labels not previously specified via the ``set_labels`` function, or by
    a previous call to this function, will trigger a new header entry to be
    added to the log with the extra labels.

    Labels previously specified and not present in a call to this function will
    be skipped with an empty value in the log row.

    :raise OSError: When the log is full this function raises an ``OSError``
        exception with error code 28 ``ENOSPC``, which indicates there is no
        space left in the device.

----

Temperature logging every 5 min
-------------------------------------

.. code-block:: python

    from microbit import *
    import power
    import log

    # Log the temperature every 5 minutes
    @run_every(min=5)
    def log_temperature():
        log.add(temp=temperature())

    while True:
        # Display the temperature when button A is pressed
        if button_a.is_pressed():
            display.scroll(temperature())
        # To go sleep, wake up when button A is pressed, and ensure the
        # function scheduled with run_every still executes in the background
        power.deep_sleep(wake_on=button_a, run_every=True)


Temperature and light logging every 5 min
-------------------------------------

.. code-block:: python

    from microbit import *
    import log

    # Configure the labels and select a time unit for the timestamp
    log.set_labels('temp', 'brightness', timestamp=log.SECONDS)

    # Send each data row to the serial output
    log.set_mirroring(True)

    continue_logging = True

    # This decorator schedules this function to run every 7s and 500ms for 8 readings per minute
    @run_every(s=7, ms=500)
    def log_data():
        """Log the temperature and light level, and display an icon."""
        global continue_logging
        if continue_logging:
            display.show(Image.SURPRISED)
            try:
                log.add(temp=temperature(), brightness=display.read_light_level())
            except OSError:
                continue_logging = False
                display.scroll("Log full")
            sleep(500)

    while True:
        if button_b.is_pressed():
            display.show(Image.CONFUSED)
            # Delete the log file using the "full" options, which takes
            # longer but ensures the data is wiped from the device
            log.delete(full=True)
            continue_logging = True
        elif button_a.is_pressed():
            display.show(Image.HAPPY)
            # Log only the light level, the temp entry will be empty. If the log
            # is full this will throw an exception and the programme will stop
            log.add({"brightness": display.read_light_level()})
        else:
            display.show(Image.ASLEEP)
        sleep(500)


