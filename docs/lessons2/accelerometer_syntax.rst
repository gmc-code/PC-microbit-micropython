====================================================
Accelerometer syntax
====================================================

.. py:module:: accelerometer

| The accelerometer can measure changes in speed of movement in any direction.
| The accelerometer also provides convenience functions for detecting gestures. 
| The recognized gestures are: ``up``, ``down``, ``left``, ``right``, ``face up``, ``face down``, ``freefall``, ``3g``, ``6g``, ``8g``, ``shake``.
| The accelerometer range is from -2g to +2g.

----

Gesture Functions
-------------------

.. note::

    Gestures are not updated in the background so there needs to be constant calls to some accelerometer method to do the gesture detection. Usually gestures can be detected using a loop with a small :func:`sleep` delay.


.. py:function:: current_gesture()

    Return the name of the current gesture as a string. The gestures are: ``"up"``, ``"down"``, ``"left"``, ``"right"``, ``"face up"``, ``"face down"``, ``"freefall"``, ``"3g"``, ``"6g"``, ``"8g"``, ``"shake"``.

.. py:function:: is_gesture(name)

    Return True or False to indicate if the named gesture is currently active.

.. py:function:: was_gesture(name)

    Return True or False to indicate if the named gesture was active since the
    last call.

.. py:function:: get_gestures()

    | Return a tuple of the gesture history. The most recent is listed last.
    | Also clears the gesture history before returning.
    
----

Acceleration Functions
-------------------------

.. py:function:: get_x()

    Get the acceleration measurement in the ``x`` axis, as a positive or
    negative integer, depending on the direction. The measurement is given in
    milli-g within the range of +/- 2000mg, registered on a scale of values from 0 to 1024.

.. py:function:: get_y()

    Get the acceleration measurement in the ``y`` axis, as a positive or
    negative integer, depending on the direction. The measurement is given in
    milli-g within the range of +/- 2000mg, registered on a scale of values from 0 to 1024.

.. py:function:: get_z()

    Get the acceleration measurement in the ``z`` axis, as a positive or
    negative integer, depending on the direction. The measurement is given in
    milli-g within the range of +/- 2000mg, registered on a scale of values from 0 to 1024.

.. py:function:: get_values()

    Get the acceleration measurements in all axes at once, as a three-element
    tuple of integers ordered as X, Y, Z, each within the range of +/-2000mg, registered on a scale of values from 0 to 1024.

