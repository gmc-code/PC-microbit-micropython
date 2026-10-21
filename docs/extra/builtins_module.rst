==========================
builtins
==========================

| All built-in functions do not require explicit importing of the builtins module.
| See: `<https://docs.python.org/3/library/functions.html>`_
| See: `<https://mpython.readthedocs.io/en/master/library/pythonStd/builtins.html>`_

----

abs
-------------------

.. function:: abs(number)

    Returns the absolute value of a number. Negative numbers are made positive.
    Arguments can be integers or floating-point numbers.

| The code scrolls the absolute value of -2.3.

.. code-block:: python

    from microbit import *

    while True:
        display.scroll(abs(-2.3))

----

all
-------------------

.. function:: all(iterable)

    If all elements of ``iterable`` are true (or the iterable is empty), return ``True``, otherwise ``False``.

| The code below gives examples of lists that evaluate to True or False.

.. code-block:: python

    from microbit import *

    listA = [1, 0, 1]  # Evaluates to False
    listB = [1, 1, 1]  # Evaluates to True
    listC = [True, False, True]  # Evaluates to False
    listD = [True, True, True]  # Evaluates to True
    listE = ["hello", "world", "microbit"]  # Evaluates to True (non-empty strings)
    listF = ["hello", "", "microbit"]  # Evaluates to False (contains an empty string)
    listG = ["", "", ""]  # Evaluates to False (all empty strings)
    listH = [Image.HEART, Image.HAPPY, Image.SAD]  # Evaluates to True (valid images)
    listI = [Image.HEART, None, Image.SAD]  # Evaluates to False (contains `None`)
    listJ = [0, "", None]  # Evaluates to False


    while True:
        display.scroll("A", 60)
        display.scroll(all(listA), 60)
        display.scroll("B", 60)
        display.scroll(all(listB), 60)
        display.scroll("C", 60)
        display.scroll(all(listC), 60)
        display.scroll("D", 60)
        display.scroll(all(listD), 60)
        display.scroll("E", 60)
        display.scroll(all(listE), 60)
        display.scroll("F", 60)
        display.scroll(all(listF), 60)
        display.scroll("G", 60)
        display.scroll(all(listG), 60)
        display.scroll("H", 60)
        display.scroll(all(listH), 60)
        display.scroll("I", 60)
        display.scroll(all(listI), 60)
        display.scroll("J", 60)
        display.scroll(all(listJ), 60)

| The code below gives examples of lists that evaluate to True or False.
| It converts the booleans True or False to a string then uses index [0] to scroll just "T" or "F".

.. code-block:: python

    from microbit import *

    listA = [1, 0, 1]  # False
    listB = [1, 1, 1]  # True
    listC = [True, False, True]  # False
    listD = [True, True, True]  # True
    listE = ["hello", "world", "microbit"]  # True
    listF = ["hello", "", "microbit"]  # False
    listG = ["", "", ""]  # False
    listH = [Image.HEART, Image.HAPPY, Image.SAD]  # True
    listI = [Image.HEART, None, Image.SAD]  # False
    listJ = [0, "", None]  # False

    while True:
        display.scroll("A", 60)
        display.scroll(str(all(listA))[0], 60)
        display.scroll("B", 60)
        display.scroll(str(all(listB))[0], 60)
        display.scroll("C", 60)
        display.scroll(str(all(listC))[0], 60)
        display.scroll("D", 60)
        display.scroll(str(all(listD))[0], 60)
        display.scroll("E", 60)
        display.scroll(str(all(listE))[0], 60)
        display.scroll("F", 60)
        display.scroll(str(all(listF))[0], 60)
        display.scroll("G", 60)
        display.scroll(str(all(listG))[0], 60)
        display.scroll("H", 60)
        display.scroll(str(all(listH))[0], 60)
        display.scroll("I", 60)
        display.scroll(str(all(listI))[0], 60)
        display.scroll("J", 60)
        display.scroll(str(all(listJ))[0], 60)



----

any
-------------------

.. function:: any(iterable)

    If any element of ``iterable`` is true, return ``True``. If the iterable is empty, return ``False``.


.. code-block:: python

    from microbit import *

    # Lists with suffixes A to H
    listA = [1, 2, 3]  # True (at least one nonzero)
    listB = [0, 0, 0]  # False (only zeros)

    listC = [True, False, True]  # True (at least one True)
    listD = [False, False, False]  # False (only False)

    listE = ["Hello", "", "World"]  # True (at least one non-empty string)
    listF = ["", "", ""]  # False (only empty strings)

    listG = [Image.HEART, None, Image.HAPPY]  # True (at least one valid image)
    listH = [None, None, None]  # False (only None values)

    while True:
        # Numbers
        display.scroll("A", 60)
        display.scroll(any(listA), 60)
        display.scroll("B", 60)
        display.scroll(any(listB), 60)

        # Booleans
        display.scroll("C", 60)
        display.scroll(any(listC), 60)
        display.scroll("D", 60)
        display.scroll(any(listD), 60)

        # Strings
        display.scroll("E", 60)
        display.scroll(any(listE), 60)
        display.scroll("F", 60)
        display.scroll(any(listF), 60)

        # Image Objects
        display.scroll("G", 60)
        display.scroll(any(listG), 60)
        display.scroll("H", 60)
        display.scroll(any(listH), 60)


----

bin
-------------------

.. function:: bin(value)

    | Convert an integer to a binary string prefixed with "0b".
    | Value is an integer.

.. code-block:: python

    from microbit import *

    val1 = bin(3)
    val2 = bin(-1)
    while True:
        display.scroll(val1)
        display.scroll("_")
        display.scroll(val2)
        display.scroll("_")

----

bool
-------------------

.. class:: bool(boolean)

    Used to convert a given parameter to a boolean type. If there is no parameter, return ``False``.

False is returned by:

* constants defined to be false: ``None`` and ``False``.
* zero of any numeric type: ``0``, ``0.0``
* empty sequences and collections: ``''``, ``()``, ``[]``, ``{}``, ``set()``, ``range(0)``

| See: `<https://www.w3schools.com/python/python_booleans.asp>`_

.. code-block:: python

    from microbit import *

    val1 = bool()
    val2 = bool(0)
    val3 = bool("")
    val4 = bool(None)
    val5 = bool([])
    while True:
        display.scroll(val1)
        display.scroll("_")
        display.scroll(val2)
        display.scroll("/")
        display.scroll(val3)
        display.scroll("|")
        display.scroll(val4)
        display.scroll("+")
        display.scroll(val5)

| These return True.

.. code-block:: python

    from microbit import *

    val1 = bool(1)  # True (nonzero number)
    val2 = bool(-5)  # True (negative number)
    val3 = bool("hello")  # True (non-empty string)
    val4 = bool(Image.YES)  # True (image)
    val5 = bool([1, 2, 3])  # True (non-empty list)

    while True:
        display.scroll(val1)
        display.scroll("_")
        display.scroll(val2)
        display.scroll("/")
        display.scroll(val3)
        display.scroll("|")
        display.scroll(val4)
        display.scroll("+")
        display.scroll(val5)


----

bytearray
-------------------

.. class:: bytearray()

    | Returns a new bytes array.
    | From a given length, e.g. bytearray(1) is zero-filled (\x00)
    | From an iterable of integers, e.g. bytearray(range(4))
    | From text given the encoding, e.g. bytearray("mb", 'utf-8')

See: `<https://www.programiz.com/python-programming/methods/built-in/bytearray>`_

.. code-block:: python

    from microbit import *

    val1 = bytearray()
    val2 = bytearray(3)
    val3 = bytearray([2,4,6])
    val4 = bytearray("mb", 'utf-8')
    print(val1)
    print(val2)
    print(val3)
    print(val4)

    '''
    bytearray(b'')
    bytearray(b'\x00\x00\x00')
    bytearray(b'\x02\x04\x06')
    bytearray(b'mb')
    '''

----

bytes
-------------------

.. class:: bytes()

    | The bytes() function returns a bytes object that cannot be modified.
    | It can convert objects into bytes objects, or create empty bytes object of the specified size.
    | From a given length, e.g. bytes(1) is zero-filled (\x00)
    | From an iterable of integers, e.g. bytes(range(4))
    | From text given the encoding, e.g. bytes("mb", 'utf-8')


.. code-block:: python

    from microbit import *

    val1 = bytes()
    val2 = bytes(2)
    val3 = bytes([2, 4, 6])
    val4 = bytes("mb", "utf-8")
    print(val1)
    print(val2)
    print(val3)
    print(val4)

    '''
    b''
    b'\x00\x00'
    b'\x02\x04\x06'
    b'mb'
    '''

----

callable
-------------------

.. function:: callable(object)

    Returns ``True`` if the specified ``object`` is callable, otherwise it returns ``False``.

.. code-block:: python

    from microbit import *

    def add2(a, b):
        return a + b

    print(callable(add2))  # True
    print(callable(callable))  # True
    print(callable("callable"))  # False

----

chr
-------------------

.. function:: chr(number)
    :no-index:

    Returns the character that represents the specified Unicode ``number``.

.. code-block:: python

    from microbit import *

    print(chr(0x30))
    print(chr(97))
    print(chr(8364))
    display.scroll(chr(0x30))
    display.scroll(chr(97))
    display.scroll(chr(8364))  # can't be displayed, so ? is shown instead

    '''
    0
    a
    €
    '''

----

classmethod
-------------------

| Think of a normal method as specific to an object, while a class method is shared across all objects of the class.

See: `<https://www.programiz.com/python-programming/methods/built-in/classmethod>`_

.. decorator:: classmethod()

    | Converts a regular method into a class method
    | Class methods can be called on a class or on an instance.

.. code-block:: python

    from microbit import *

    class Person:
        age = 15

        def printAge(cls):
            print('The age is:', cls.age)

    # create printAge class method
    Person.printAge = classmethod(Person.printAge)
    # call the class method
    Person.printAge()
    Person.age = 20
    Person.printAge()

| Using a decorator instead:

.. code-block:: python

    from microbit import *

    class Person:
        age = 15  # Class attribute

        def print_age(self, name):
            # Instance method (prints the object's name and its specific age)
            print(name + " Age: " + str(self.age))

        @classmethod
        def print_class_age(cls):
            # Class method (applies to all instances)
            print("Class Age: " + str(cls.age))

    # Create instances and call methods
    person1 = Person()
    person1.print_age("Person1")  # Displays "Person1 Age: 15"
    Person.print_class_age()  # Displays "Class Age: 15"

    # Modify the instance attribute and call method again
    person1.age = 16  # Changes only this object's age
    person1.print_age("Person1")  # Displays "Person1 Age: 16"
    Person.print_class_age()  # Displays "Class Age: 15" (unchanged)

    # Modify the class attribute and call class method again
    Person.age = 20  # Changes the class-wide age (affects future instances)
    Person.print_class_age()  # Displays "Class Age: 20"
    person1.print_age("Person1")  # Displays "Person1 Age: 16" (instance keeps its own value)
    # Create a second instance and call methods
    person2 = Person()
    person2.print_age("Person2")  # Displays "Person2 Age: 20" (inherits class value)


----

complex
-------------------

.. class:: complex([real[, imag]])

    | Returns a complex number with a value of real + imag * 1J, or converts a string or number to a complex number.
    | If the first parameter is a character string, it is interpreted as a complex number and must be called without a second parameter.
    | The second parameter cannot be a character string.
    | Each argument can be of any numeric type (including complex numbers).
    | If imag is omitted, the default value is zero, and the constructor performs numerical conversion like int and float.
    | If both arguments are omitted, 0j is returned.

.. code-block:: python

    from microbit import *

    print(complex(1, 2))
    print(complex(0, 4))
    print(complex("1"))
    print(complex(1-3j))

    '''
    (1+2j)
    4j
    (1+0j)
    (1-3j)
    '''

----

delattr
-------------------

.. function:: delattr(obj, name)

    | An argument is an object and a string.
    | The string must be a property of the object.
    | If the object allows it, the function deletes the specified property.
    | Such as delattr(x, 'foobar') equivalent to del x.foobar.

.. code-block:: python

    from microbit import *

    class Coordinate:
        x = 10
        y = -5
        z = 0

    point1 = Coordinate()

    print('x =',point1.x)
    print('y =',point1.y)
    print('z =',point1.z)

    delattr(Coordinate, 'z')
    print('--deleted z attribute--')

    print('x =',point1.x)
    print('y =',point1.y)

    # Trigger an AttributeError, since z no longer exists
    print('z =', point1.z)


----

dict
-------------------

.. class:: dict(**kwarg)
    :no-index:

.. class:: dict(mapping, **kwarg)
    :no-index:

.. class:: dict(iterable, **kwarg)
    :no-index:

Create a dictionary.

- ``**kwarg`` -- keyword arguments, e.g. ``dict(a=1, b=2)``.
- ``mapping`` -- another dictionary.
- ``iterable`` -- an iterable of ``(key, value)`` pairs.


.. code-block:: python

    from microbit import *

    # Creating dictionaries using different methods
    dictA = {}  # Empty dictionary
    dictB = dict(a='a', b='b', c='c')  # Using keyword arguments
    dictC = dict(zip(['one', 'two', 'three'], [1, 2, 3]))  # Using zip() mapping
    dictD = dict([('one', 1), ('two', 2), ('three', 3)])  # Using an iterable object

    # Function to scroll dictionary contents
    def scroll_dict(dictionary, name):
        display.scroll(name + ": ")
        for key, value in dictionary.items():
            display.scroll(str(key) + "=" + str(value) + " ")

    while True:
        scroll_dict(dictA, "A")  # Empty dictionary
        scroll_dict(dictB, "B")  # Keyword-based dictionary
        scroll_dict(dictC, "C")  # Zip mapping dictionary
        scroll_dict(dictD, "D")  # Iterable-based dictionary



----

dir
-------------------

.. function:: dir(object)

    With no argument, ``dir()`` returns a list of the names in the current scope.
    With an argument, it returns a list of the attributes and methods of that object.

    - ``object`` -- object, variable, type or module.


.. code-block:: python

    from microbit import *
    import music


    # List of valid micro:bit objects to inspect
    objects_to_check = [
        ("Button A", button_a),
        ("Display", display),
        ("Accelerometer", accelerometer),
        ("Integer (temperature reading)", temperature()),
        ("Compass", compass),
        ("Pins", pin0),
        ("music", music)
    ]

    # Function to print attributes while skipping dunder methods
    def display_attributes(obj_name, obj):
        print(obj_name + ": ")
        for attribute in dir(obj):
            if not attribute.startswith("_"):  # Skip names starting with _
                print(attribute)
        print("______")

    # Loop through objects and print attributes
    for name, obj in objects_to_check:
        display_attributes(name, obj)

    '''
    Button A:
    get_presses
    is_pressed
    was_pressed
    ______
    Display:
    clear
    get_pixel
    is_on
    off
    on
    read_light_level
    scroll
    set_pixel
    show
    ______
    Accelerometer:
    current_gesture
    get_gestures
    get_strength
    get_values
    get_x
    get_y
    get_z
    is_gesture
    set_range
    was_gesture
    ______
    Integer (temperature reading):
    from_bytes
    to_bytes
    ______
    Compass:
    calibrate
    clear_calibration
    get_field_strength
    get_x
    get_y
    get_z
    heading
    is_calibrated
    ______
    Pins:
    CAPACITIVE
    NO_PULL
    PULL_DOWN
    PULL_UP
    RESISTIVE
    get_analog_period_microseconds
    get_mode
    get_pull
    is_touched
    read_analog
    read_digital
    set_analog_period
    set_analog_period_microseconds
    set_pull
    set_touch_mode
    write_analog
    write_digital
    ______
    music:
    stop
    BADDY
    BA_DING
    BIRTHDAY
    BLUES
    CHASE
    DADADADUM
    ENTERTAINER
    FUNERAL
    FUNK
    JUMP_DOWN
    JUMP_UP
    NYAN
    ODE
    POWER_DOWN
    POWER_UP
    PRELUDE
    PUNCHLINE
    PYTHON
    RINGTONE
    WAWAWAWAA
    WEDDING
    get_tempo
    pitch
    play
    reset
    set_tempo
    ______

    '''

----

divmod
-------------------

.. function:: divmod(a, b)

    | Perform integer division and return the quotient and remainder as a tuple.
    | ``a`` and ``b`` are numbers.
    | For integers, the result is ``(a // b, a % b)``.
    | For floating-point numbers, the result is ``(q, a % b)``, where ``q`` is usually ``math.floor(a / b)``, but may be 1 less than that.
    | The relationship ``q * b + a % b == a`` holds (very nearly, for floats).
    | If ``a % b`` is not zero, it has the same sign as ``b``, with ``0 <= abs(a % b) < abs(b)``.


.. code-block:: python

    from microbit import *

    # List of divmod calculations
    calculations = [
        ("7//2", divmod(7, 2)),
        ("8//2", divmod(8, 2)),
        ("8//-2", divmod(8, -2)),
        ("3//1.3", divmod(3, 1.3))
    ]

    # Print results to the REPL
    for label, result in calculations:
        print(label + " = " + str(result))

    '''
    7//2 = (3, 1)
    8//2 = (4, 0)
    8//-2 = (-4, 0)
    3//1.3 = (2.0, 0.4000001)
    '''

----

Ellipsis
-------------------

.. data:: Ellipsis

    | Written as ``...`` (three dots). It can be used as a placeholder.
    | Commonly used inside functions to indicate future implementation.
    | Used on its own line, it does nothing when executed, like ``pass``.


| See: `<https://docs.python.org/3/library/constants.html>`_
| The ellipsis can be used instead of pass as a placeholder in functions.
| This is useful during development so that the unfinished function doesn't return an error.

.. code-block:: python

    from microbit import *

    def test_def():
        ...

    while True:
        if test_def() is None:
            display.scroll("...")
        else:
            display.scroll("#")


----

enumerate
-------------------

.. function:: enumerate(sequence, start=0)

    | Converts a traversable object (list, tuple, string, etc.) into an indexed sequence.
    | Commonly used in for-loops to iterate with index values.

    :param sequence: A sequence, iterator, or other object that supports iteration.
    :param start: (Optional) The starting index (default is 0).


.. code-block:: python

    from microbit import *

    # Sample list of strings
    strings = ["A", "B", "C"]

    while True:
        for index, string in enumerate(strings, start=1):  # Start index at 1
            display.scroll(str(index) + ": " + string)



----

eval
-------------------

.. function:: eval(expression[, globals[, locals]])

    Evaluate a string containing a Python expression and return its value.

    - ``expression`` -- the expression, as a string.
    - ``globals`` -- (optional) a dictionary to use as the global namespace.
    - ``locals`` -- (optional) a mapping to use as the local namespace.

.. code-block:: python

    from microbit import *

    x = 7
    print(eval('3 * x'))
    print(eval('pow(2, 2)'))
    print(eval('2 + 2'))
    n = 81
    print(eval('n + 4'))

    '''
    21
    4
    4
    85
    '''

----

exec
-------------------

.. function:: exec(object[, globals[, locals]])

    Execute Python statements stored in a string. ``exec`` can run more complex code than ``eval``, such as loops, but it always returns ``None``.

    - ``object`` -- the code to run, as a string.
    - ``globals`` -- (optional) a dictionary to use as the global namespace.
    - ``locals`` -- (optional) a mapping to use as the local namespace. If omitted, it is the same as ``globals``.

.. code-block:: python

    from microbit import *

    # Single line statement
    exec('print("Hello World")')

    # Multi-line statement
    exec("""for i in range(3):
        print("loop:", i)
    """)

    '''
    Hello World
    loop: 0
    loop: 1
    loop: 2
    '''

----

filter
-------------------

.. function:: filter(function, iterable)

    Keep only the items of ``iterable`` for which ``function`` returns ``True``.
    It returns an iterator. Use ``list()`` to convert it to a list.

    - ``function`` -- a function that returns ``True`` or ``False``.
    - ``iterable`` -- the items to filter.

| The code keeps only the odd numbers in the list.

.. code-block:: python

    from microbit import *

    def is_odd(n):
        return n % 2 == 1

    odd_numbers = list(filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    print(odd_numbers)

    '''
    [1, 3, 5, 7, 9]
    '''

----

float
-------------------

.. class:: float([x])

    Convert an integer or a string to a floating-point number.

.. code-block:: python

    from microbit import *

    print(float(1))
    print(float(112))
    print(float(-123.6))
    print(float('123'))  # from a string

    '''
    1.0
    112.0
    -123.6
    123.0
    '''

----

str.format
-------------------

.. method:: str.format(*args, **kwargs)

    | Insert values into the ``{}`` placeholders of a string.
    | Placeholders can be left empty (used in order) or numbered (used by position).
    | MicroPython on the micro:bit does not have the separate ``format()`` builtin function, so use the ``str.format()`` method instead.

.. code-block:: python

    from microbit import *

    print("{} {}".format("hello", "world"))       # default order
    print("{0} {1}".format("hello", "world"))     # by position
    print("{1} {0} {1}".format("hello", "world")) # positions can be repeated
    print("Temp: {}C".format(temperature()))

    '''
    hello world
    hello world
    world hello world
    Temp: 21C
    '''

----

getattr
-------------------

.. function:: getattr(object, name[, default])

    Return the value of the attribute called ``name`` (a string) of an object.
    If the attribute does not exist, ``default`` is returned. With no default, an ``AttributeError`` occurs.

.. code-block:: python

    from microbit import *

    class A:
        bar = 1

    a = A()
    print(getattr(a, 'bar'))      # attribute bar exists
    print(getattr(a, 'bar2', 3))  # bar2 does not exist, so the default 3 is returned
    print(getattr(a, 'bar2'))     # bar2 does not exist and no default: AttributeError

    '''
    1
    3
    AttributeError: 'A' object has no attribute 'bar2'
    '''

----

globals
-------------------

.. function:: globals()

    Return a dictionary of all the global variables.

----

hasattr
-------------------

.. function:: hasattr(object, name)

    Return ``True`` if the object has an attribute called ``name``, otherwise ``False``.

    - ``object`` -- the object.
    - ``name`` -- the attribute name, as a string.

.. code-block:: python

    from microbit import *

    class Coordinate:
        x = 10
        y = -5
        z = 0

    point1 = Coordinate()
    print(hasattr(point1, 'x'))
    print(hasattr(point1, 'y'))
    print(hasattr(point1, 'z'))
    print(hasattr(point1, 'no'))  # no such attribute

    '''
    True
    True
    True
    False
    '''

----

hash
-------------------

.. function:: hash(object)

    Return the hash value of the object (if it has one). The hash value is an integer, used to look up dictionary keys quickly. Numbers that are equal have the same hash value, e.g. ``hash(1) == hash(1.0)``.

----

help
-------------------

.. function:: help([object])

    Print a description of an object or module, e.g. ``help(display)``.
    ``help('modules')`` lists the built-in modules.

----

hex
-------------------

.. function:: hex(x)

    Convert an integer to a lowercase hexadecimal string prefixed with "0x".

.. code-block:: python

    from microbit import *

    print(hex(255))
    print(hex(-42))

    '''
    0xff
    -0x2a
    '''

----

id
-------------------

.. function:: id(object)

    Return the identity of an object, an integer that is unique to that object while it exists.

----

input
-------------------

.. function:: input([prompt])

    Read a line of text typed into the serial terminal and return it as a string.

----

int
-------------------

.. class:: int([x])
    :no-index:

.. class:: int(x, base=10)
    :no-index:

Convert a string or number to an integer.

- ``x`` -- a string or number. Floats are rounded towards zero.
- ``base`` -- the number base of the string (default 10).

.. code-block:: python

    from microbit import *

    print(int(3.9))
    print(int('42'))
    print(int('ff', 16))
    print(int('101', 2))

    '''
    3
    42
    255
    5
    '''

----

isinstance
-------------------

.. function:: isinstance(object, classinfo)

    Return ``True`` if ``object`` is an instance of ``classinfo``, or of a subclass of it, otherwise ``False``.
    ``classinfo`` can be a tuple of types, in which case ``True`` is returned if the object is an instance of any of them.

.. admonition:: isinstance() and type() differences

    - ``type()`` does not treat a subclass as being the same type as its parent class.
    - ``isinstance()`` treats a subclass as being the same type as its parent class.

    To check whether an object is of a given type, it is recommended to use ``isinstance()``.

.. code-block:: python

    from microbit import *

    print(isinstance(5, int))
    print(isinstance(5.0, int))
    print(isinstance("hi", (int, str)))

    '''
    True
    False
    True
    '''

----

issubclass
-------------------

.. function:: issubclass(class, classinfo)

    Return ``True`` if ``class`` is a subclass (direct or indirect) of ``classinfo``.
    ``classinfo`` can be a tuple of classes, in which case each one is checked.

.. code-block:: python

    from microbit import *

    class A:
        pass

    class B(A):
        pass

    print(issubclass(B, A))
    print(issubclass(A, B))

    '''
    True
    False
    '''

----

iter
-------------------

.. function:: iter(object)

    Return an iterator for an object that supports iteration, such as a list.
    Each call to ``next()`` on the iterator returns the next item.

.. code-block:: python

    from microbit import *

    lst = [1, 2, 3]
    for i in iter(lst):
        print(i)

    '''
    1
    2
    3
    '''

----

len
-------------------

.. function:: len(s)

    Return the length (number of items) of a string, list, tuple, dictionary, etc.

.. code-block:: python

    from microbit import *

    word = "microbit"
    print(len(word))     # string length
    numbers = [1, 2, 3, 4, 5]
    print(len(numbers))  # number of list items

    '''
    8
    5
    '''

----

list
-------------------

.. class:: list([iterable])

    Create a list, e.g. from a tuple or a string.

.. code-block:: python

    from microbit import *

    colours = ('red', 'green', 'blue')
    list1 = list(colours)
    print("list1:", list1)

    word = "Hello"
    list2 = list(word)
    print("list2:", list2)

    '''
    list1: ['red', 'green', 'blue']
    list2: ['H', 'e', 'l', 'l', 'o']
    '''

----

locals
-------------------

.. function:: locals()

    Return a dictionary of all the local variables.

.. code-block:: python

    from microbit import *

    def show_locals(arg):
        z = 1
        print(locals())

    show_locals(4)

    '''
    {'z': 1, 'arg': 4}
    '''

| The order of the items in the dictionary may vary.

----

map
-------------------

.. function:: map(function, iterable, ...)

    Apply ``function`` to every item of ``iterable`` and return an iterator of the results. Use ``list()`` to convert it to a list.
    If more than one iterable is given, the function must take that many arguments, and items are taken from each iterable in parallel. It stops when the shortest iterable runs out.

.. code-block:: python

    from microbit import *

    def square(x):
        return x ** 2

    print(list(map(square, [1, 2, 3, 4, 5])))                    # square each item
    print(list(map(lambda x: x ** 2, [1, 2, 3, 4, 5])))          # using a lambda function
    print(list(map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])))  # add two lists

    '''
    [1, 4, 9, 16, 25]
    [1, 4, 9, 16, 25]
    [3, 7, 11, 15, 19]
    '''

----

max
-------------------

.. function:: max(iterable)
              max(a, b, ...)

    Return the largest item in an iterable, or the largest of two or more arguments.

.. code-block:: python

    from microbit import *

    print("max(80, 100, 1000):", max(80, 100, 1000))
    print("max(-20, 100, 400):", max(-20, 100, 400))
    print("max(-80, -20, -10):", max(-80, -20, -10))
    print("max([0, 100, -400]):", max([0, 100, -400]))

    '''
    max(80, 100, 1000): 1000
    max(-20, 100, 400): 400
    max(-80, -20, -10): -10
    max([0, 100, -400]): 100
    '''

----

memoryview
-------------------

.. class:: memoryview(object)

    Return a memory view of an object that supports the buffer protocol, such as ``bytes`` or ``bytearray``.
    A memory view lets code access the data without copying it.

.. code-block:: python

    from microbit import *

    v = memoryview(bytearray(b"abcdef"))
    print(v[1])          # the byte value of 'b'
    print(v[-1])         # the byte value of 'f'
    print(bytes(v[1:4]))

    '''
    98
    102
    b'bcd'
    '''

----

min
-------------------

.. function:: min(iterable)
              min(a, b, ...)
    :no-index:

    Return the smallest item in an iterable, or the smallest of two or more arguments.

.. code-block:: python

    from microbit import *

    print("min(80, 100, 1000):", min(80, 100, 1000))
    print("min(-20, 100, 400):", min(-20, 100, 400))
    print("min(-80, -20, -10):", min(-80, -20, -10))
    print("min([0, 100, -400]):", min([0, 100, -400]))

    '''
    min(80, 100, 1000): 80
    min(-20, 100, 400): -20
    min(-80, -20, -10): -80
    min([0, 100, -400]): -400
    '''

----

next
-------------------

.. function:: next(iterator[, default])

    Return the next item from the iterator. If the iterator is finished, ``default`` is returned; with no default, a ``StopIteration`` exception occurs.

.. code-block:: python

    from microbit import *

    it = iter([1, 2, 3, 4, 5])
    while True:
        try:
            x = next(it)
            print(x)
        except StopIteration:
            # Exit the loop when there are no more items
            break

----

object
-------------------

.. class:: object()

    Return a new featureless object. ``object`` is the base class of all classes.

----

oct
-------------------

.. function:: oct(x)

    Convert an integer to an octal string prefixed with "0o".

.. code-block:: python

    from microbit import *

    print(oct(10))
    print(oct(20))
    print(oct(15))

    '''
    0o12
    0o24
    0o17
    '''

----

open
-------------------

.. function:: open(file, mode='r')

    Open a file on the micro:bit's file system and return a file object.
    If the file cannot be opened, an ``OSError`` occurs.

The micro:bit supports these modes:

=========  =================================
Mode       Description
=========  =================================
'r'        Read (default)
'w'        Write, replacing any existing file
'b'        Binary mode, e.g. 'rb' or 'wb'
't'        Text mode (default)
=========  =================================

| Appending ('a'), exclusive creation ('x') and read/write ('+') modes are not available on the micro:bit.
| Using ``with`` closes the file automatically when the block finishes.

.. code-block:: python

    from microbit import *

    with open('data.txt', 'w') as f:
        f.write('hello')

    with open('data.txt') as f:
        print(f.read())

    '''
    hello
    '''

----

ord
-------------------

.. function:: ord(c)

    The inverse of ``chr()``. Takes a single character and returns the integer Unicode code for it.

.. code-block:: python

    from microbit import *

    print(ord('a'))
    print(ord('€'))

    '''
    97
    8364
    '''

----

pow
-------------------

.. function:: pow(x, y)

    Return ``x`` to the power of ``y``. The same as ``x ** y``.

.. code-block:: python

    from microbit import *

    print("pow(100, 2):", pow(100, 2))
    print("pow(100, -2):", pow(100, -2))
    print("pow(2, 4):", pow(2, 4))
    print("pow(3, 0):", pow(3, 0))

    '''
    pow(100, 2): 10000
    pow(100, -2): 0.0001
    pow(2, 4): 16
    pow(3, 0): 1
    '''

----

print
-------------------

.. function:: print(*objects, sep=' ', end='\n')

    Print objects to the serial output (the REPL).

    - ``objects`` -- any number of objects to print, separated by commas.
    - ``sep`` -- the text put between objects. The default is a space.
    - ``end`` -- the text put at the end. The default is a newline ``\n``.

.. code-block:: python

    from microbit import *

    print(1)
    print("Hello World")
    a = 1
    b = 'microbit'
    print(a, b)
    print("aaa" "bbb")
    print("aaa", "bbb")
    print("www", "microbit", "org", sep=".")
    print("no newline", end="")
    print("!")

    '''
    1
    Hello World
    1 microbit
    aaabbb
    aaa bbb
    www.microbit.org
    no newline!
    '''

----

property
-------------------

.. decorator:: property()

    Turn a method into a property, so it can be used like an attribute.
    The property's setter and deleter can also be defined with decorators.

.. code-block:: python

    from microbit import *

    class C:
        def __init__(self):
            self._x = None

        @property
        def x(self):
            """I'm the 'x' property."""
            return self._x

        @x.setter
        def x(self, value):
            self._x = value

    c = C()
    c.x = 5    # uses the setter
    print(c.x) # uses the getter

    '''
    5
    '''

----

range
-------------------

.. class:: range(stop)
           range(start, stop[, step])

    Return a range object, a sequence of integers from ``start`` up to but not including ``stop``.
    A range is not a list. Use ``list()`` to see all its values.

.. code-block:: python

    from microbit import *

    for i in range(5):
        print(i)

    print(list(range(5)))
    print(list(range(0)))
    print(list(range(0, 30, 5)))
    print(list(range(0, 10, 2)))
    print(list(range(0, -10, -1)))
    print(list(range(1, 0)))

    '''
    0
    1
    2
    3
    4
    [0, 1, 2, 3, 4]
    []
    [0, 5, 10, 15, 20, 25]
    [0, 2, 4, 6, 8]
    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
    []
    '''

----

repr
-------------------

.. function:: repr(object)

    Return a string containing a printable representation of an object. Strings include their quotes.

.. code-block:: python

    from microbit import *

    s = 'microbit'
    print(str(s))
    print(repr(s))

    '''
    microbit
    'microbit'
    '''

----

reversed
-------------------

.. function:: reversed(seq)

    Return an iterator that goes through a sequence in reverse order.

.. code-block:: python

    from microbit import *

    # string
    print(list(reversed('Python')))

    # tuple
    print(list(reversed(('P', 'y', 't', 'h', 'o', 'n'))))

    # range
    print(list(reversed(range(5, 9))))

    # list
    print(list(reversed([1, 2, 4, 3, 5])))

    '''
    ['n', 'o', 'h', 't', 'y', 'P']
    ['n', 'o', 'h', 't', 'y', 'P']
    [8, 7, 6, 5]
    [5, 3, 4, 2, 1]
    '''

----

round
-------------------

.. function:: round(x[, n])

    Return ``x`` rounded to ``n`` decimal places.

    - ``x`` -- a number.
    - ``n`` -- the number of decimal places. The default is 0, which returns an integer.

.. code-block:: python

    from microbit import *

    print("round(70.23456):", round(70.23456))
    print("round(56.659, 1):", round(56.659, 1))
    print("round(80.264, 2):", round(80.264, 2))
    print("round(100.000056, 3):", round(100.000056, 3))
    print("round(-100.000056, 3):", round(-100.000056, 3))

    '''
    round(70.23456): 70
    round(56.659, 1): 56.7
    round(80.264, 2): 80.26
    round(100.000056, 3): 100.0
    round(-100.000056, 3): -100.0
    '''

----

set
----------

.. class:: set([iterable])

    Create an unordered collection with no repeated items. Sets can be used to remove duplicates and to find the intersection, union and difference of groups of items.

| Sets are unordered, so the items may print in a different order.

.. code-block:: python

    from microbit import *

    x = set('banana')
    y = set('apple')
    print(x)      # duplicates removed
    print(y)
    print(x & y)  # intersection: in both
    print(x | y)  # union: in either
    print(x - y)  # difference: in x but not y

    '''
    {'a', 'n', 'b'}
    {'a', 'p', 'l', 'e'}
    {'a'}
    {'a', 'n', 'b', 'p', 'l', 'e'}
    {'n', 'b'}
    '''

----

setattr
-------------------

.. function:: setattr(object, name, value)

    The partner of ``getattr()``. Set the attribute called ``name`` of an object to ``value``.
    If the attribute does not exist, it is created.

.. code-block:: python

    from microbit import *

    class A:
        bar = 1

    a = A()
    print(getattr(a, 'bar'))  # get attribute bar
    setattr(a, 'bar', 5)      # change attribute bar
    print(a.bar)
    setattr(a, 'age', 28)     # create a new attribute
    print(a.age)

    '''
    1
    5
    28
    '''

----

slice
-------------------

.. class:: slice(stop)
           slice(start, stop[, step])

    Return a slice object, which can be used to slice a sequence. ``s[slice(1, 4)]`` is the same as ``s[1:4]``.

----

sorted
-------------------

.. function:: sorted(iterable, *, key=None, reverse=False)

    Return a new sorted list from the items in ``iterable``.

    - ``iterable`` -- the items to sort.
    - ``key`` -- (optional) a function of one argument, applied to each item to decide its sort order.
    - ``reverse`` -- ``True`` sorts in descending order. ``False`` (default) sorts in ascending order.

.. code-block:: python

    from microbit import *

    example_list = [5, 0, 6, 1, 2, 7, 3, 4]
    print(sorted(example_list))                       # ascending order as default
    print(sorted(example_list, key=lambda x: x * -1)) # reverse order using key
    print(sorted(example_list, reverse=True))         # reverse order using reverse

    '''
    [0, 1, 2, 3, 4, 5, 6, 7]
    [7, 6, 5, 4, 3, 2, 1, 0]
    [7, 6, 5, 4, 3, 2, 1, 0]
    '''

----

staticmethod
-------------------

.. decorator:: staticmethod()

    Convert a method into a static method. A static method does not receive ``self`` or ``cls`` as its first argument.
    It can be called on the class, e.g. ``C.f()``, or on an instance, e.g. ``C().f()``.

.. code-block:: python

    from microbit import *

    class C:
        @staticmethod
        def add(a, b):
            return a + b

    print(C.add(2, 3))
    print(C().add(2, 3))

    '''
    5
    5
    '''

----

str
-------------------

.. class:: str(object)

    Convert an object to a string.

.. code-block:: python

    from microbit import *

    print(str(42) + " degrees")
    d = {'name': 'microbit', 'version': 2}
    print(str(d))

    '''
    42 degrees
    {'name': 'microbit', 'version': 2}
    '''

----

sum
-------------------

.. function:: sum(iterable[, start])

    Return the total of the items in ``iterable``, plus ``start`` (default 0).

.. code-block:: python

    from microbit import *

    print(sum([0, 1, 2]))
    print(sum((2, 3, 4), 1))      # add 1 to the total of the tuple
    print(sum([0, 1, 2, 3, 4], 2)) # add 2 to the total of the list

    '''
    3
    10
    12
    '''

----

super
-------------------

.. function:: super()

    Used inside a class to call a method of its parent class (superclass).

.. code-block:: python

    from microbit import *

    class A:
        def add(self, x):
            y = x + 1
            print(y)

    class B(A):
        def add(self, x):
            super().add(x)

    b = B()
    b.add(2)

    '''
    3
    '''

----

tuple
-------------------

.. class:: tuple([iterable])

    Create a tuple, e.g. from a list.

.. code-block:: python

    from microbit import *

    list1 = ['red', 'green', 'blue']
    tuple1 = tuple(list1)
    print(tuple1)

    '''
    ('red', 'green', 'blue')
    '''

----

type
-------------------

.. function:: type(object)
              type(name, bases, dict)

    With one argument, return the type of an object. With three arguments, create a new class.

    - ``name`` -- the name of the class.
    - ``bases`` -- a tuple of base classes.
    - ``dict`` -- a dictionary of the class attributes.

.. hint:: isinstance() and type() differences

    - ``type()`` does not treat a subclass as being the same type as its parent class.
    - ``isinstance()`` treats a subclass as being the same type as its parent class.

    **To check whether an object is of a given type, it is recommended to use isinstance().**

.. code-block:: python

    from microbit import *

    print(type(1))
    print(type('microbit'))
    print(type([2]))
    print(type({0: 'zero'}))
    x = 1
    print(type(x) == int)

    # Three arguments: create a new class X
    X = type('X', (object,), dict(a=1))
    print(X.a)

    '''
    <class 'int'>
    <class 'str'>
    <class 'list'>
    <class 'dict'>
    True
    1
    '''

| type() and isinstance() differences:

.. code-block:: python

    from microbit import *

    class A:
        pass

    class B(A):
        pass

    print(isinstance(A(), A))  # True
    print(type(A()) == A)      # True
    print(isinstance(B(), A))  # True
    print(type(B()) == A)      # False

----

zip
-------------------

.. function:: zip(*iterables)

    Combine iterables by pairing up their items in tuples, and return an iterator of the tuples. Use ``list()`` to convert it to a list.
    If the iterables have different lengths, it stops when the shortest one runs out.
    ``zip(*zipped)`` does the reverse, unzipping the tuples back into separate groups.

.. code-block:: python

    from microbit import *

    a = [1, 2, 3]
    b = [4, 5, 6]
    c = [4, 5, 6, 7, 8]

    print(list(zip(a, b)))
    print(list(zip(a, c)))   # length matches the shortest list

    a1, a2 = zip(*zip(a, b)) # unzip
    print(list(a1))
    print(list(a2))

    '''
    [(1, 4), (2, 5), (3, 6)]
    [(1, 4), (2, 5), (3, 6)]
    [1, 2, 3]
    [4, 5, 6]
    '''


----

Exceptions
----------

See: `<https://docs.python.org/3/library/exceptions.html>`_

.. exception:: ArithmeticError

.. exception:: AssertionError

.. exception:: AttributeError

.. exception:: BaseException

.. exception:: EOFError

.. exception:: Exception

.. exception:: GeneratorExit

.. exception:: ImportError

.. exception:: IndentationError

.. exception:: IndexError

.. exception:: KeyboardInterrupt

.. exception:: KeyError

.. exception:: LookupError

.. exception:: MemoryError

.. exception:: NameError

.. exception:: NotImplementedError

.. exception:: OSError

.. exception:: OverflowError

.. exception:: RuntimeError

.. exception:: StopAsyncIteration

.. exception:: StopIteration

.. exception:: SyntaxError

.. exception:: SystemExit

.. exception:: TypeError

.. exception:: ValueError

.. exception:: ZeroDivisionError