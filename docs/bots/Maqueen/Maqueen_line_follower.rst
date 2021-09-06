====================================================
Maqueen line follower
====================================================

| The maqueen buggy is best suited to following a thick track.

Set up buggy and sensors
----------------------------------------

| Import the maqueen module and set up the buggy and line sensor.

.. code-block:: python

    from microbit import *
    import maqueen


    buggy = maqueen.MaqueenMotors()
    buggy.stop()
    line_sensor = maqueen.MaqueenLineSensors()


