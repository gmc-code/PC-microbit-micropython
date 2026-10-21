==========================
math module
==========================

.. py:module:: math

The ``math`` module provides some basic mathematical functions for working with floating-point numbers.

| The micro:bit uses single-precision floats, so results are accurate to about 7 significant figures.
| Angles are in radians. Use ``math.degrees()`` and ``math.radians()`` to convert.


Functions
---------

.. function:: acos(x)

   Return the inverse cosine of ``x``.

| The angle whose cosine is 0.5 is 60 degrees.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.degrees(math.acos(0.5)), 1), delay=80)  # 60.0



.. function:: asin(x)

   Return the inverse sine of ``x``.

| The angle whose sine is 0.5 is 30 degrees.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.degrees(math.asin(0.5)), 1), delay=80)  # 30.0



.. function:: atan(x)

   Return the inverse tangent of ``x``.

| The angle whose tangent is 1 is 45 degrees.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.degrees(math.atan(1)), 1), delay=80)  # 45.0



.. function:: atan2(y, x)

   Return the principal value of the inverse tangent of ``y/x``.

| Unlike ``atan``, ``atan2`` uses the signs of y and x to give the angle in the correct quarter of the circle.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.degrees(math.atan2(1, 1)), 1), delay=80)    # 45.0
    display.scroll(round(math.degrees(math.atan2(1, -1)), 1), delay=80)   # 135.0



.. function:: ceil(x)

   Return an integer, being ``x`` rounded towards positive infinity.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(math.ceil(2.1), delay=80)   # 3
    display.scroll(math.ceil(-2.1), delay=80)  # -2



.. function:: copysign(x, y)

   Return ``x`` with the sign of ``y``.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(math.copysign(5, -1), delay=80)  # -5.0
    display.scroll(math.copysign(-5, 1), delay=80)  # 5.0



.. function:: cos(x)

   Return the cosine of ``x``.

| Angles are in radians, so convert degrees first.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.cos(math.radians(60)), 2), delay=80)  # 0.5



.. function:: degrees(x)

   Return radians ``x`` converted to degrees.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.degrees(math.pi), 1), delay=80)  # 180.0



.. function:: exp(x)

   Return the exponential of ``x``.

| ``exp(1)`` is the number e.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.exp(1), 3), delay=80)  # 2.718
    display.scroll(round(math.exp(2), 2), delay=80)  # 7.39



.. function:: fabs(x)

   Return the absolute value of ``x``.

| Unlike ``abs()``, ``fabs`` always returns a float.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(math.fabs(-3), delay=80)  # 3.0
    display.scroll(abs(-3), delay=80)       # 3



.. function:: floor(x)

   Return an integer, being ``x`` rounded towards negative infinity.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(math.floor(2.7), delay=80)   # 2
    display.scroll(math.floor(-2.7), delay=80)  # -3



.. function:: fmod(x, y)

   Return the remainder of ``x/y``.

| For negative numbers, ``fmod`` gives a different answer to the ``%`` operator.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(math.fmod(7, 3), delay=80)   # 1.0
    display.scroll(math.fmod(-7, 3), delay=80)  # -1.0
    display.scroll(-7 % 3, delay=80)            # 2



.. function:: frexp(x)

   Decomposes a floating-point number into its mantissa and exponent.
   The returned value is the tuple ``(m, e)`` such that ``x == m * 2**e``
   exactly.  If ``x == 0`` then the function returns ``(0.0, 0)``, otherwise
   the relation ``0.5 <= abs(m) < 1`` holds.

| 8 is 0.5 x 2**4.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(str(math.frexp(8)), delay=80)  # (0.5, 4)



.. function:: isfinite(x)

   Return ``True`` if ``x`` is finite.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(str(math.isfinite(1.5)), delay=80)           # True
    display.scroll(str(math.isfinite(float('inf'))), delay=80)  # False



.. function:: isinf(x)

   Return ``True`` if ``x`` is infinite.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(str(math.isinf(float('inf'))), delay=80)  # True
    display.scroll(str(math.isinf(1e30)), delay=80)        # False



.. function:: isnan(x)

   Return ``True`` if ``x`` is not-a-number

.. code-block:: python

    from microbit import *
    import math

    display.scroll(str(math.isnan(float('nan'))), delay=80)  # True
    display.scroll(str(math.isnan(0.0)), delay=80)         # False



.. function:: ldexp(x, exp)

   Return ``x * (2**exp)``.

| ``ldexp`` is the reverse of ``frexp``.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(math.ldexp(0.5, 4), delay=80)  # 8.0



.. function:: log(x)
              log(x, base)

   | With one argument, return the natural logarithm of *x*.
   | With two arguments, return the logarithm of *x* to the given *base*.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.log(math.e), 2), delay=80)  # 1.0
    display.scroll(round(math.log(100, 10), 2), delay=80)  # 2.0
    display.scroll(round(math.log(8, 2), 2), delay=80)     # 3.0



.. function:: modf(x)

   Return a tuple of two floats, being the fractional and integral parts of
   ``x``.  Both return values have the same sign as ``x``.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(str(math.modf(3.75)), delay=80)  # (0.75, 3.0)



.. function:: pow(x, y)

   Returns ``x`` to the power of ``y``.

| Unlike the ``**`` operator, ``math.pow`` always returns a float.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(math.pow(2, 10), delay=80)  # 1024.0
    display.scroll(2 ** 10, delay=80)         # 1024



.. function:: radians(x)

   Return degrees ``x`` converted to radians.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.radians(180), 4), delay=80)  # 3.1416



.. function:: sin(x)

   Return the sine of ``x``.

| Angles are in radians, so convert degrees first.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.sin(math.radians(30)), 2), delay=80)  # 0.5



.. function:: sqrt(x)

   Return the square root of ``x``.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(math.sqrt(16), delay=80)           # 4.0
    display.scroll(round(math.sqrt(2), 3), delay=80)  # 1.414



.. function:: tan(x)

   Return the tangent of ``x``.

| Angles are in radians, so convert degrees first.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.tan(math.radians(45)), 2), delay=80)  # 1.0



.. function:: trunc(x)

   Return an integer, being ``x`` rounded towards 0.

| ``trunc`` rounds towards 0, unlike ``floor``.

.. code-block:: python

    from microbit import *
    import math

    display.scroll(math.trunc(-2.7), delay=80)  # -2
    display.scroll(math.floor(-2.7), delay=80)  # -3



Constants
---------

.. data:: e

   base of the natural logarithm

.. code-block:: python

    from microbit import *
    import math

    display.scroll(round(math.e, 4), delay=80)  # 2.7183



.. data:: pi

   the ratio of a circle's circumference to its diameter

| The code calculates the area of a circle with radius 3.

.. code-block:: python

    from microbit import *
    import math

    radius = 3
    area = math.pi * radius ** 2
    display.scroll(round(area, 2), delay=80)  # 28.27



----

Tilt strength using sqrt
-------------------------------

| The accelerometer gives x, y and z values in milli-g.
| Pythagoras in 3D gives the total strength of the acceleration. Resting flat, it is about 1000 (1 g).

.. code-block:: python

    from microbit import *
    import math

    while True:
        x = accelerometer.get_x()
        y = accelerometer.get_y()
        z = accelerometer.get_z()
        strength = math.sqrt(x**2 + y**2 + z**2)
        display.scroll(int(strength))
        sleep(500)

Tilt angle using atan2
-------------------------------

| ``atan2`` gives the angle of tilt from the x and z accelerometer values.
| ``degrees`` converts the angle from radians to degrees.

.. code-block:: python

    from microbit import *
    import math

    while True:
        x = accelerometer.get_x()
        z = accelerometer.get_z()
        angle = math.degrees(math.atan2(x, -z))
        display.scroll(round(angle))
        sleep(500)

Rounding with floor and ceil
-------------------------------

.. code-block:: python

    from microbit import *
    import math

    # print(math.floor(2.7))   # 2
    display.scroll(str(math.floor(2.7)), delay=80)
    # print(math.ceil(2.1))    # 3
    display.scroll(str(math.ceil(2.1)), delay=80)
    # print(math.trunc(-2.7))  # -2
    display.scroll(str(math.trunc(-2.7)), delay=80)
    # print(math.pi)           # 3.141593
    display.scroll(str(math.pi), delay=80)
