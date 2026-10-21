==========================
usys module
==========================

.. py:module:: usys

| See: `<https://docs.micropython.org/en/latest/library/sys.html>`_
| Some attributes are listed below. Use ``help(usys)`` to get the full list.
| These are values, not functions, so they are used without brackets, e.g. ``usys.platform``.

.. py:data::  version_info

    | The Python language version, as a tuple of ints.
    | e.g. (3, 4, 0)

.. code-block:: python

    from microbit import *
    import usys

    display.scroll(str(usys.version_info), delay=80)  # (3, 4, 0)



.. py:data::  version

    | The Python language version, as a string.
    | e.g. 3.4.0

.. code-block:: python

    from microbit import *
    import usys

    display.scroll(usys.version, delay=80)  # 3.4.0



.. py:data::  platform

    | The platform that MicroPython is running on.
    | e.g. microbit

.. code-block:: python

    from microbit import *
    import usys

    display.scroll(usys.platform, delay=80)  # microbit



.. py:data::  implementation

    | Information about the current MicroPython implementation, with these attributes:
    | name - string e.g. micropython, from ``usys.implementation.name``
    | version - tuple (major, minor, micro), e.g. (1, 18, 0), from ``usys.implementation.version``

.. code-block:: python

    from microbit import *
    import usys

    display.scroll(usys.implementation.name, delay=80)          # micropython
    display.scroll(str(usys.implementation.version), delay=80)  # (1, 18, 0)



.. py:data::  maxsize

    | The maximum integer value that can be stored in a native integer, which is 2,147,483,647 for a 32-bit system.

.. code-block:: python

    from microbit import *
    import usys

    display.scroll(usys.maxsize, delay=80)  # 2147483647
    if usys.maxsize > 2147483648:
        display.scroll("64-bit", delay=80)
    else:
        display.scroll("32-bit", delay=80)



.. py:data::  modules

    | A dictionary of loaded modules, not including builtin modules.
    | e.g. {'log': <module 'log'>, 'neopixel': <module 'neopixel'>}

| The log module shows in the list once it has been imported.

.. code-block:: python

    from microbit import *
    import usys

    import log

    display.scroll(str(list(usys.modules)), delay=80)  # ['log']



.. py:data::  path

    | A list of directories to search for imported modules.
    | e.g. ['', '.frozen']

.. code-block:: python

    from microbit import *
    import usys

    display.scroll(str(usys.path), delay=80)  # ['', '.frozen']



.. py:data::  byteorder

    | The byte order of the system ("little" or "big").
    | e.g. little

.. code-block:: python

    from microbit import *
    import usys

    display.scroll(usys.byteorder, delay=80)  # little



.. py:data::  argv

    | A list of arguments the current program was started with. e.g. []

.. code-block:: python

    from microbit import *
    import usys

    display.scroll(str(usys.argv), delay=80)  # []



----

| The code below scrolls all the values in one program.

.. code-block:: python

    from microbit import *
    import usys

    # print(help(usys))
    # print('version_info:', usys.version_info)
    display.scroll('version_info: ' + str(usys.version_info), delay=80)
    # print('version:', usys.version)
    display.scroll('version: ' + str(usys.version), delay=80)
    # print('platform:', usys.platform)
    display.scroll('platform: ' + str(usys.platform), delay=80)
    # print('implementation name:', usys.implementation.name)
    display.scroll('implementation name: ' + str(usys.implementation.name), delay=80)
    # print('implementation version:', usys.implementation.version)
    display.scroll('implementation version: ' + str(usys.implementation.version), delay=80)
    # print('maxsize:', usys.maxsize)
    display.scroll('maxsize: ' + str(usys.maxsize), delay=80)
    if usys.maxsize > 2147483648:
        # print('64-bit')
        display.scroll('64-bit', delay=80)
    else:
        # print('32-bit')
        display.scroll('32-bit', delay=80)
    # print('path:', usys.path)
    display.scroll('path: ' + str(usys.path), delay=80)
    # print('modules:', usys.modules)
    display.scroll('modules: ' + str(usys.modules), delay=80)
    # print('byteorder:', usys.byteorder)
    display.scroll('byteorder: ' + str(usys.byteorder), delay=80)
    # print('argv:', usys.argv)
    display.scroll('argv: ' + str(usys.argv), delay=80)

    '''
    version_info: (3, 4, 0)
    version: 3.4.0
    platform: microbit
    implementation name: micropython
    implementation version: (1, 18, 0)
    maxsize: 2147483647
    32-bit
    path: ['', '.frozen']
    modules: {}
    byteorder: little
    argv: []
    '''

