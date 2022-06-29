====================================================
Microbit library
====================================================

Import the microbit library
----------------------------------------

| The microbit requires a library or module for it to work.
| To use that library, always start the microbit code in Mu editor with:

.. code-block:: python

    from microbit import *

----

.. admonition:: Questions

    Describe the error in attempting to import the microbit library.

    #. ``from microbit import``
    #. ``from microbit import*``
    #. ``from microbot import *``
    #. ``from microbit *``

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                ``from microbit import`` error

                .. code-block:: python

                    # missing * at end
                    from microbit import *

            .. tab-item:: Q2

                ``from microbit import*`` error

                .. code-block:: python

                    # missing space before *
                    from microbit import *

            .. tab-item:: Q3

                ``from microbot import *`` error

                .. code-block:: python

                    # microbit misspelt
                    from microbit import *

            .. tab-item:: Q4

                ``from microbit *`` error

                .. code-block:: python

                    # missing import before *
                    from microbit import *

----

Blank Lines
------------------------------------------
    
| All microbit libraries or modules are imported at the top of the file.
| Place **1 blank line** following the the importing of libraries to separate those lines from the rest of the code.
| The PEP8 guide states that there should be 1 blank line after the library imports. In more advanced code, classes or definitions should have 2 blank lines before and after them. So 2 blank lines after importing is used when followed by a class or definition.
| For advanced users, see full PEP 8 guide at: https://www.python.org/dev/peps/pep-0008/

.. Note::

    | Surround top-level function and class definitions with two blank lines.
    | Method definitions inside a class are surrounded by a single blank line.
    | Extra blank lines may be used (sparingly) to separate groups of related functions.
    | Use blank lines in functions, sparingly, to indicate logical sections.

----

.. admonition:: Questions

    1.  How could the layout of the code be improved?

    .. code-block:: python

        from microbit import *


        while True:
            display.scroll(char, delay=80)

    2.  How could the layout of the code be improved?

    .. code-block:: python

        from microbit import *
        num = 12
        while True:
            display.scroll(num, delay=80)


    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                How could the layout of the code be improved?
                Remove the extra blank line after the library import.

                .. code-block:: python

                    from microbit import *

                    while True:
                        display.scroll(char, delay=80)

            .. tab-item:: Q2

                How could the layout of the code be improved?
                Add a blank line after the library import.


                .. code-block:: python

                    from microbit import *

                    num = 12
                    while True:
                        display.scroll(num, delay=80)

----

| For other forms of importing libraries see:
| https://www.w3schools.com/python/python_modules.asp


| Importing using ``from module_name import *`` is not recommended for general python use.
| It is used here to keep the microbit syntax shorter.

| On other websites, references to the microbit library syntax may have ``microbit.`` before the function or method. 
| e.g ``microbit.display.scroll("Hi")``
| This is because it assumes that the microbit library has been imported using ``import microbit``.
| When importing the microbit library using: ``from microbit import *``, the ``microbit.`` prefix is omitted.
| e.g This allows the shorter form, ``display.scroll("Hi")``, instead of the longer form, ``microbit.display.scroll("Hi")``.

----

Micropython API
------------------------------------------

| The main reference for using micropython with the microbit is at:
| https://microbit-micropython.readthedocs.io/en/v1.0.1/index.html
| For new microbits (v2) from 2022 see:
| https://microbit-micropython.readthedocs.io/en/v2-docs/index.html

| For a list of what is available in the microbit library see:
| https://microbit-micropython.readthedocs.io/en/v1.0.1/microbit_micropython_api.html
| For new microbits (v2) from 2022 see:
| https://microbit-micropython.readthedocs.io/en/v2-docs/microbit_micropython_api.html


