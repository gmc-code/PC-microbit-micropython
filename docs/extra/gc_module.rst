==========================
gc module
==========================

| Garbage Collector: A background process that runs in MicroPython to reclaim unused memory in the heap.
| See: https://docs.micropython.org/en/latest/library/gc.html
| Normally, a collection is triggered only when a new allocation cannot be satisfied, i.e. on an out-of-memory condition.

----

.. py:function::  gc.enable()

    Enable automatic garbage collection.

.. code-block:: python

    from microbit import *
    import gc

    gc.enable()
    
----

.. py:function::  gc.disable()

    Disable automatic garbage collection. Heap memory can still be allocated, and garbage collection can still be initiated manually using gc.collect().

.. code-block:: python

    from microbit import *
    import gc

    gc.disable()

----

.. py:function::  gc.isenabled()

    Return True if garbage collection is enabled; False is disabled.

.. code-block:: python

    from microbit import *
    import gc

    print(gc.isenabled())
    gc.disable()
    print(gc.isenabled())
    gc.enable()
    print(gc.isenabled())

----

.. py:function::  gc.collect()

    Run a garbage collection.

.. code-block:: python

    from microbit import *
    import gc

    gc.collect()
    
----

.. py:function::  gc.mem_alloc()

    Return the number of bytes of heap RAM that are allocated.

.. code-block:: python

    from microbit import *
    import gc

    display.scroll(gc.mem_alloc())

----

.. py:function::  gc.mem_free()

    Return the number of bytes of available heap RAM, or -1 if this amount is not known.

.. code-block:: python

    from microbit import *
    import gc

    display.scroll(gc.mem_free())

----

.. py:function::  gc.threshold([amount])

    | Set or query the additional GC allocation threshold.  
    | A garbage collection will be triggered each time after the amount bytes have been allocated, since the previous time such an amount of bytes have been allocated. 
    | **amount** is specified as less than the full heap size, (usually 64512), with the intention to trigger a collection earlier than when the heap becomes exhausted, and in the hope that an early collection will prevent excessive memory fragmentation.
    | Calling the function without argument will return the current value of the threshold. 
    | A value of -1 means a disabled allocation threshold.

.. code-block:: python

    from microbit import *
    import gc

    gc.threshold(1024)
    print(gc.threshold())

