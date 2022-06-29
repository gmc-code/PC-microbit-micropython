====================================================
Variable Errors
====================================================


Variable used which has no value
-----------------------------------

| ``display.scroll('hello')`` will scroll 'hello' across the microbit.
| If 'hello' is not in quotes, it will be treated as a variable.
| If ``display.scroll(hello)`` is used by accident, leaving out the quotes, an **undefined name** error occurs. 

.. code-block:: python

    from microbit import *

    display.scroll(hello)


.. image:: images/undefined_name_1.png
    :scale: 50 %


This can also be fixed by giving the variable a value, as shown below:

.. code-block:: python
    
    from microbit import *

    hello = 'Hi'
    display.scroll(hello)


