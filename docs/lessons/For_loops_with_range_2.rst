====================================================
EXT: for-loops using the range function
====================================================

----

Advanced: nested for-loops with range function
-------------------------------------------------

| What does this code do?

.. code-block:: python
    
    from microbit import *

    while True:
        for startnum in range(4):
            for n in range(startnum, startnum + 5, 2):
                display.scroll(n, delay=40)

