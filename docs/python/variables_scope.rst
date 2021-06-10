==========================
Variables Scope
==========================

Scope
--------------

| Scope is an 'area' in which a variable is defined, can be accessed and written to. 
| There are two types of variables: global and local. 
| By default, all variables defined within a function are local - they cannot be accessed outside of the function. 
| Since the scope within the function is different from the global one, a variable with the same name outside of the function is different to the variable within a function.

Local Variables
---------------------------

The code below attempts to use a ``name_age_greeting()`` function and increment age every time the function is called:

.. code-block:: python

    from microbit import *

    name = "Joe"
    age = 12

    def name_age_greeting():
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"


    display.scroll(name_age_greeting(), delay=70)
    display.scroll(name_age_greeting(), delay=70)
    display.scroll(name_age_greeting(), delay=70)


| When flashed the microbit displays the error message: ``Name Error: local variable referenced before assignment``.
| This is because the variable ``age`` within the function is not the same as the variable ``age`` outside of the ``name_age_greeting()`` function and the variable within the function has not has a value assigned to it.

----

Global  Variables
---------------------------

| To access the global variable inside the function, declare the variable ``age`` as ``global`` within the function:
| This will let Python know, that the age variable in the function is the same one in the global namespace.

.. code-block:: python

    from microbit import *

    name = "Joe"
    age = 12

    def name_age_greeting():
        global age
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    display.scroll(name_age_greeting(), delay=70)
    display.scroll(name_age_greeting(), delay=70)
    display.scroll(name_age_greeting(), delay=70)


.. warning:: Using global variables for functions like this is generally a bad practice and you should avoid it, since it makes the purpose of your functions less obvious and you can end up with messy code. A better way to do this is to pass variable ``age`` as one of the arguments of the function (example below).

----

Use arguments instead of global variables
-----------------------------------------------------

| Here is an example for a function that passes variables as arguments.
| The age variable is incremented outside of the function.

.. code-block:: python

    from microbit import *

    name = "Joe"
    age = 12

    def name_age_greeting(name, age):
        return "Hi " + name + ", you are " + str(age)

    display.scroll(name_age_greeting(name, age), delay=50)
    age += 1
    display.scroll(name_age_greeting(name, age), delay=50)
    age += 1
    display.scroll(name_age_greeting(name, age), delay=50)




Nonlocal variables
-------------------

| The nested functions below has a variable ``x`` which if different to the ``x`` in the outer function:

.. code-block:: python

    from microbit imp4

    def outer_func():
        x = 3
        display.scroll(x, delay=70)  # 3

        def inner_func():
            x = 7
            display.scroll(x, delay=70) # 7

        inner_func()
        display.scroll(x, delay=70) # 3

    outer_func()


| Nested functsions can use the keyword: ``nonlocal``, to make the variable in the nested function the same variable as in the outer function:

.. code-block:: python

# variable scope 5

    from microbit import *

    def outer_func():
        x = 3
        display.scroll(x, delay=70)  # 3

        def inner_func():
            nonlocal x
            x = 7
            display.scroll(x, delay=70) # 7

        inner_func()
        display.scroll(x, delay=70) # 7

    outer_func()




    
    



