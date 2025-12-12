==========================
builtins
==========================

| All built-in functions do not require explicit importing of the builtins module.
| See: https://docs.python.org/3/library/functions.html
| See: https://mpython.readthedocs.io/en/master/library/pythonStd/builtins.html

----

abs
-------------------

.. function:: abs(number)

    Returns the absolute value of a number. This is the values made positive.
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

    If all elements of `iterable` are true (or the iterator is empty), return `True`, otherwise `False`.

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
| It converts the booleans True or False to a string then takes a slice iva [0] to scroll just "T" or "F".

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

    If any element of `iterable` is true, return `True`. If the iterator is empty, return `False`.


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
        display.scroll("__")

----

bool
-------------------

.. class:: bool(boolean)

    Used to convert a given parameter to a boolean type. If there is no parameter, return `False`.

| False is returned by:
| * constants defined to be false: None and False.
| * zero of any numeric type: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
| * empty sequences and collections: '', (), [], {}, set(), range(0)
| See: https://www.w3schools.com/python/python_booleans.asp

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

See: https://www.programiz.com/python-programming/methods/built-in/bytearray

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

    Returns True if the specified `object` is callable, otherwise it returns False.

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

    Returns the character that represents the specified unicode `number`.

.. code-block:: python

    from microbit import *

    print(chr(0x30))
    print(chr(97))
    print(chr(8364))
    display.scroll(chr(0x30))
    display.scroll(chr(97))
    display.scroll(chr(8364))  #--can't display so ? instead

    '''
    0
    a
    €
    '''

----

classmethod
-------------------

| Think of a normal method as specific to an object, while a class method is shared across all objects of the class.

See: https://www.programiz.com/python-programming/methods/built-in/classmethod

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
    |  If the first parameter is a character string, it is interpreted as a complex number and must be called without a second parameter.
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

    # Trigger error
    print('z = ',point1.z)


----

dict
-------------------

.. class:: dict(**kwarg)
.. class:: dict(mapping, **kwarg)
.. class:: dict(iterable, **kwarg)

- ``**kwargs`` -- keyword
- ``mapping`` -- element container.
- ``iterable`` -- iteratable object.

.. function:: dict()

    | create a dictionary


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

    dir() When a function has no parameters, it returns the list of variables, methods and defined types in the current range.
    When it has parameters, it returns the list of properties and methods of parameters.
    If the parameter contains  __dir__(), if it doesn't contains __dir__(), This method will maximize the collection of parameter information.
    - ``object`` -- object, variable, type.


.. code-block:: python

    from microbit import *
    import music


    # List of valid micro:bit objects to inspect
    objects_to_check = [
        ("Button A", button_a),
        ("Display", display),
        ("Accelerometer", accelerometer),
        ("Temperature", temperature()),
        ("Compass", compass),
        ("Pins", pin0),
        ("music", music)
    ]

    # Function to print attributes while skipping dunder methods
    def display_attributes(obj_name, obj):
        print(obj_name + ": ")
        for attribute in dir(obj):
            if not attribute.startswith("__"):  # Skip dunder methods
                print(attribute)
        print("____________")

    # Loop through objects and print attributes
    for name, obj in objects_to_check:
        display_attributes(name, obj)

    '''
    Button A:
    get_presses
    is_pressed
    was_pressed
    ____________
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
    ____________
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
    ____________
    Temperature:
    from_bytes
    to_bytes
    ____________
    Compass:
    calibrate
    clear_calibration
    get_field_strength
    get_x
    get_y
    get_z
    heading
    is_calibrated
    ____________
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
    ____________
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
    __________

    '''

----

divmod
-------------------

.. function:: divmod(a, b)

    | Perform integer division and return the quotient and remainder as a tuple.
    | `a` and `b` are non-complex numbers.
    | For integers, the result is `(a // b, a % b)`, following standard division rules.
    | For floating-point numbers, the result is `(q, a % b)`, where `q` is usually `math.floor(a / b)`, but may be smaller than 1.
    | The relationship `q * b + a % b == a` holds, ensuring consistency.
    | If `a % b` is not zero, it has the same sign as `b`, with `0 <= abs(a % b) < abs(b)`.


.. code-block:: python

    from microbit import *

    # List of divmod calculations
    calculations = [
        ("7//2", divmod(7, 2)),
        ("8//2", divmod(8, 2)),
        ("8//-2", divmod(8, -2)),
        ("3//1.3", divmod(3, 1.3))
    ]

    # Scroll results on micro:bit
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

.. function:: ...

    | Represents an **ellipsis** (three dots) used as a placeholder.
    | Commonly used inside functions to indicate future implementation.
    | Equivalent to `pass`, meaning it does nothing when executed.


| See: https://docs.python.org/3/library/constants.html
| The ellipsis can be uses instead of pass as a placeholder in functions.
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

eval() Function to execute a string expression and return the value of the expression.

- ``expression`` -- expression form.
- ``globals`` -- variable scope, global namespace, if provided, it must be a dictionary object.
- ``locals`` -- variable scope, global namespace, if provided, can be any mapping object.


::

        x = 7
         eval( '3 * x' )
    21
         eval('pow(2,2)')
    4
         eval('2 + 2')
    4
         n=81
         eval("n + 4")
    85

----

exec
-------------------

.. function:: exec(object[, globals[, locals]])

exec Execute Python statements stored in strings or files, Exec can execute more complex Python code than eval.

- ``object``: Required parameter, indicating the Python code to be specified. It must be a string or code object. If the object is a string, the string is first parsed into a set of Python statements and then executed (unless a syntax error occurs). If the object is a code object, it is simply executed.
- ``globals``: Optional parameter, representing the global namespace (storing global variables), If provided, it must be a dictionary object.
- ``locals``: Optional parameter indicating the current local namespace (storing local variables), If provided, it can be any mapping object. If this parameter is ignored, it will take the same value as globals.

::

        exec('print("Hello World")')
    Hello World
    # Single line statement string
         exec("print('runoob.com')")
    runoob.com

    #  Single line statement string
         exec ("""for i in range(5):
   ...     print("iter time: %d" % i)
   ... """)
    iter time: 0
    iter time: 1
    iter time: 2
    iter time: 3
    iter time: 4

----

filter
-------------------

.. function:: filter(function, iterable)

Used to filter sequence and filter out unqualified elements, Returns an iterator object. If you want to convert it to a list, you can use list () to convert it.

- ``function`` -- Judgement function.
- ``iterable`` -- Iterable objects.

Filter out all the odd numbers in the list::

    def is_odd(n):
        return n % 2 == 1

    tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    new_list = list(tmplist)
    print(new_list)

----

float
-------------------

.. class:: float([x])

float() Function to convert integers and strings to floating-point numbers.

::

        float(1)
    1.0
         float(112)
    112.0
         float(-123.6)
    -123.6
         float('123')     # string
    123.0

----

format
-------------------

.. function:: format(value[, format_spec])

Functions for formatting strings str.format(), It enhances string formatting. format Function can accept unlimited arguments, position may not in sequence. The basic syntax is to replace the previous% with {} and:.  For more detailed syntax, please refer to CPython 'Format String Syntax'  <https://docs.python.org/zh-cn/3.7/library/string.html#format-specification-mini-language>`_

::

        "{} {}".format("hello", "world")    # Do not set the specified location, in the default order.
    'hello world'

         "{0} {1}".format("hello", "world")  # Set specified location
    'hello world'

         "{1} {0} {1}".format("hello", "world")  # Set specified location
    'world hello world

----

getattr
-------------------

.. function:: getattr(object, name[, default])

Used to return an object property value.

::

        class A(object):
   ...     bar = 1
   ...
         a = A()
         getattr(a, 'bar')        # Get property bar value
    1
         getattr(a, 'bar2')       # Property bar2 does not exist, triggering exception
    Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
    AttributeError: 'A' object has no attribute 'bar2'
         getattr(a, 'bar2', 3)    # Property bar2 does not exist, but the default value is set


----

globals
-------------------

.. function:: globals()

globals() Function returns all global variables in the current location as dictionary type.

----

hasattr
-------------------

.. function:: hasattr(object, name)

Judgement object if it contains corresponding attributes.

- ``object`` -- object.
- ``name`` -- string, property name.

::

    class Coordinate:
        x = 10
        y = -5
        z = 0

    point1 = Coordinate()
    print(hasattr(point1, 'x'))
    print(hasattr(point1, 'y'))
    print(hasattr(point1, 'z'))
    print(hasattr(point1, 'no'))  # no such attribute

The output::

    True
    True
    True
    False

----

hash
-------------------

.. function:: hash(object)

Returns the hash value of the object, (if any). Hash value is an integer. The quick key  use to compare elements in the dictionary. Numeric variables of the same size have the same hash value.

----

help
-------------------

.. function:: help([object])

Check the detail description for purpose of the function or module.

----

hex
-------------------

.. function:: hex(x)

Converts an integer to a lowercase hexadecimal string prefixed with "0x".

::

    hex(255)
    '0xff'
    hex(-42)
    '-0x2a'

----

id
-------------------

.. function:: id([object])

Get the id of the object.

----

input
-------------------

.. function:: input([prompt])

Receive a standard input data and return it as string type.

----

int
-------------------

.. class:: int([x])
.. class:: int(x,base=10)

Converts a string or number to an integer.

- ``x`` -- String or number.
- ``base`` -- Decimal number, default decimal

----

isinstance
-------------------

.. function:: isinstance(object, classinfo)

Returns true if the object argument is an instance of the classInfo argument, or an instance of a (direct, indirect, or virtual) subclass.
If the object is not an object of the given type, the function always returns false. Returns true if classInfo is a tuple of object type (or multiple recursion element groups), and if object is an instance of any of them.
If classInfo is neither a type nor a type tuple or a recursive tuple of type, a typeError exception will be triggered.


.. admonition:: isinstance() and type() differences

    - `type()` does not consider a subclass as a parent type, and does not consider inheritance.
    - `isinstance()` Consider that the subclass is a parent type, and consider inheritance relationship.

    To judge whether two types are the same, it is recommended to use isinstance().

----

issubclass
-------------------

.. function:: issubclass(class, classinfo)

Returns true if class is a subclass (direct, indirect, or virtual) of classInfo. ClassInfo can be a tuple of a class object, and each element in classInfo is checked.
In other cases, a typeError exception will be triggered.

::

    class A:
        pass
    class B(A):
        pass

    print(issubclass(B,A))    # return True


----

iter
-------------------

.. function:: iter(object[, sentinel])

Used to generate iterators.
- ``object`` -- Object gather that support iterations.
- ``sentinel`` -- If the second parameter is sent, the parameter object must be a callable object (such as a function). At this time, ITER creates an iterator object, which will be called every time the iterator object's __next__() method, object is called.

::

        lst = [1, 2, 3]
         for i in iter(lst):
   ...     print(i)
   ...
    1
    2
    3

----

len
-------------------

.. function:: len()

Returns the length of an object (character, list, tuple, etc.) or the number of items.
::

        str = "runoob"
         len(str)             # String length
    6
         l = [1,2,3,4,5]
         len(l)               # Number of list elements
    5

----

list
-------------------

.. class:: list()

Used to convert a tuple or string to a list.

::

    aTuple = (123, 'Google', 'baidu', 'Taobao')
    list1 = list(aTuple)
    print("element list : ", list1)

    str="Hello World"
    list2=list(str)
    print("element list : ", list2)

the output::

    element list :  [123, 'Google', 'Runoob', 'Taobao']
    element list :  ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']

----

locals
-------------------

.. function:: locals()

Returns all local variables in the current location as dictionary type.

::

        def runoob(arg):    # Two local variables: arg、z
   ...     z = 1
   ...     print(locals())
   ...
         runoob(4)
    {'z': 1, 'arg': 4}      # Returns a dictionary of name / value pairs


----

map
-------------------

.. function:: map(function, iterable,...)

map() The specified sequence is mapped according to the provided function. Returns an iterator that applies a function to each item in Iterable and outputs its result.
If an additional Iterable parameter is entered, the function must accept the same number of arguments and be applied to items obtained in parallel from all iteratable objects.
When there are multiple iterable objects, the whole iteration will end when the shortest one is exhausted.

::

        def square(x) :            # compute square sum
   ...     return x ** 2
   ...
         map(square, [1,2,3,4,5])   # compute the square sum of each element list
    [1, 4, 9, 16, 25]
         map(lambda x: x ** 2, [1, 2, 3, 4, 5])  # use lambda anonymous function
    [1, 4, 9, 16, 25]

    # Two lists are provided to add the list data in the same location
         map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
    [3, 7, 11, 15, 19]

----

max
-------------------

.. function:: max()

Returns the maximum value of the given argument, which can be a sequence

::

    print("max(80, 100, 1000) : ", max(80, 100, 1000))
    print("max(-20, 100, 400) : ", max(-20, 100, 400))
    print("max(-80, -20, -10) : ", max(-80, -20, -10))
    print("max(0, 100, -400) : ", max(0, 100, -400))

The output::

    max(80, 100, 1000) :  1000
    max(-20, 100, 400) :  400
    max(-80, -20, -10) :  -10
    max(0, 100, -400) :  100

----

memoryview
-------------------

.. class:: memoryview()

Returns the memory view object for the given parameter. The so-called memory view object refers to packaging the data supporting the buffer protocol and allowing Python code access without copying the object.

::

    v = memoryview(bytearray("abcefg"))

    v[1]
    98
    v[-1]

    103
    v[1:4]

    <memoryview>
    bytes(v[1:4)
    b'bce'


----

min
-------------------

.. function:: min()

Returns the minimum value of a given parameter, which can be a sequence.
::

    print("min(80, 100, 1000) : ", min(80, 100, 1000))
    print("min(-20, 100, 400) : ", min(-20, 100, 400))
    print("min(-80, -20, -10) : ", min(-80, -20, -10))
    print("min(0, 100, -400) : ", min(0, 100, -400))

The output::

    min(80, 100, 1000) :  80
    min(-20, 100, 400) :  -20
    min(-80, -20, -10) :  -80
    min(0, 100, -400) :  -400


----

next
-------------------

.. function:: next(iterator[, default])


Returns the next entry for the iterator. Get the next element by calling the iterator's __next__(). If the iterator is exhausted, the given default is returned, and if there is no default value, StopIteration is triggered.
::

    # First, to get the iterator object:
    it = iter([1, 2, 3, 4, 5])
    # loop:
    while True:
        try:
            # Get the next value:
            x = next(it)
            print(x)
        except StopIteration:
            # Exit loop when StopIteration is encountered
            break

----

object
-------------------

.. class:: object()

----

oct
-------------------

.. function:: oct()

Convert an integer to an octal string.

::

        oct(10)
    '012'
         oct(20)
    '024'
         oct(15)
    '017'


----

open
-------------------

.. function:: open()

open() Method is used to open a file and return the file object. This function is required during the processing of the file. If the file cannot be opened, an oserror will be thrown.
Note: used open() Method must close the file object, that is, call the close() method.

open() The common form of a function is to receive two parameters: file name and mode::

    open(file, mode='r')

mode Is an optional string that specifies the mode of opening the file. The default value is ' r ' , which means it opens in text mode and reads. Other common modes are: write 'w' (Truncate existing files)  ;
Exclusive creation 'x'  ; write to add 'a'  (On some UNIX systems, no matter where the current file pointer is, all writes are appended to the end of the file) 。Available modes are:

=========  =================================
Mode       Description
'r'        Read (default)
'w'        Write, and truncate the file first
'x'        Exclusive creation, failure if file already exists
'a'        Write, append at the end if the file exists
'b'        binary mode
't'        Text mode (default)
'+'        Update disk file (read and write)
=========  =================================

The default mode is 'r' (Open and read text, same as 'rt'). For binary write, Open 'w+b' mode and truncate file to 0 bytes;  'r+b' Will not be truncated。

----

ord
-------------------

.. function:: ord(c)

This is the inverse function of chr(). It takes a string (Unicode character) as a parameter and returns an integer representing the corresponding Unicode.

::

        ord('a')
    97
         ord('€')
    8364


----

pow
-------------------

.. function:: pow(x, y[, z])

Returns the value of X Y (Y power of x).

::

    print("pow(100, 2) : ", pow(100, 2))
    print("pow(100, -2) : ", pow(100, -2))
    print("pow(2, 4) : ", pow(2, 4))
    print("pow(3, 0) : ", pow(3, 0))

The output::

    pow(100, 2) :  10000
    pow(100, -2) :  0.0001
    pow(2, 4) :  16
    pow(3, 0) :  1

----

print
-------------------

.. function:: print(*objects, sep=' ', end='\n', file=sys.stdout)

In printout, the most common function.

    - ``objects`` : Plural, indicating that multiple objects can be output once. When printing multiple objects, separate them.
    - ``sep`` : Use a space as the interval to separate the multiple objects.
    - ``end`` : Used to set what to end with. The default value is newline \n.
    - ``file`` : The object to write.

::

         print(1)
    1
         print("Hello World)
    Hello World
         a = 1
         b = 'w3school'
         print(a, b)
    1 w3school
         print("aaa""bbb")
    aaabbb
         print("aaa","bbb")
    aaa bbb

         print("www","w3school","com",sep=".") # Set the interval space
    www.w3school.com

----

property
-------------------

.. decorator:: property()

property() Function to return property values in a new class. Using the 'property' function as a decorator can easily create read-only properties:

Property's getter, setter and delete methods can also be used as decorators::

    class C(object):
        def __init__(self):
            self._x = None

        @property
        def x(self):
            """I'm the 'x' property."""
            return self._x

        @x.setter
        def x(self, value):
            self._x = value

        @x.deleter
        def x(self):
            del self._x

----

range
-------------------

.. function:: range()

range() the function returns an iterable object (the type is an object), not a list type, so the list will not be printed when printing.

Function syntax:

    - ``range(stop)``
    - ``range(start, stop[, step])``

::

    range(5)
    range(0, 5)
         for i in range(5):
   ...     print(i)
   ...
    0
    1
    2
    3
    4
    list(range(5))
    [0, 1, 2, 3, 4]
    list(range(0))
    []


For case with two or three parameters (second construction method)::

        list(range(0, 30, 5))
    [0, 5, 10, 15, 20, 25]
         list(range(0, 10, 2))
    [0, 2, 4, 6, 8]
         list(range(0, -10, -1))
    [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
         list(range(1, 0))
    []




----

repr
-------------------

.. function:: repr()

Returns a string containing a printable representation of an object.
::

        s = 'baidu'
         repr(s)
    "'baidu'"
         dict = {'baidu': 'baidu.com', 'google': 'google.com'}
         repr(dict)
    "{'google': 'google.com', 'baidu': 'baidu.com'}"


----

reversed
-------------------

.. function:: reversed(seq)

Returns an inverted iterator.

::

    # string
    seqString = 'Runoob'
    print(list(reversed(seqString)))

    # tuple
    seqTuple = ('R', 'u', 'n', 'o', 'o', 'b')
    print(list(reversed(seqTuple)))

    # range
    seqRange = range(5, 9)
    print(list(reversed(seqRange)))

    # list
    seqList = [1, 2, 4, 3, 5]
    print(list(reversed(seqList)))

The output::

    ['b', 'o', 'o', 'n', 'u', 'R']
    ['b', 'o', 'o', 'n', 'u', 'R']
    [8, 7, 6, 5]
    [5, 3, 4, 2, 1]

----

round
-------------------

.. function:: round(x [, n])

Returns the rounding value of floating-point number x.

    - ``x`` - Numeric expression.
    - ``n`` - Indicates from decimal places, where x needs to be rounded, and the default value is 0

::

    print("round(70.23456) : ", round(70.23456))
    print("round(56.659,1) : ", round(56.659,1))
    print("round(80.264, 2) : ", round(80.264, 2))
    print("round(100.000056, 3) : ", round(100.000056, 3))
    print("round(-100.000056, 3) : ", round(-100.000056, 3))

The output::

    round(70.23456) :  70
    round(56.659,1) :  56.7
    round(80.264, 2) :  80.26
    round(100.000056, 3) :  100.0
    round(-100.000056, 3) :  -100.0

----

set
-------------------

.. class:: set([iterable])

set() Function to create an unordered and unrepeatable element set, which can be used for relationship testing, deletion of duplicate data, and calculation of intersection, subtraction, union, etc

         x = set('runoob')
         y = set('google')
         x, y
    ({'b', 'u', 'n', 'o', 'r'}, {'e', 'l', 'g', 'o'})     # Deleted duplicate
         x & y         # intersection
    {'o'}
         x | y         # union
    {'e', 'u', 'o', 'n', 'r', 'l', 'g', 'b'}
         x - y         # subtraction
    {'b', 'u', 'n', 'r'}
    >

----

setattr
-------------------

.. function:: setattr(object, name, value)

setattr() Function corresponding Function getattr(), Used to set the value of a property that does not necessarily exist.

Assign values to existing properties::

        class A(object):
   ...     bar = 1
   ...
         a = A()
         getattr(a, 'bar')          # get attribute bar value
    1
         setattr(a, 'bar', 5)       # set attribute bar value
         a.bar
    5

If the property does not exist, a new object property will be created and assigned::

        class A():
   ...     name = "runoob"
   ...
         a = A()
         setattr(a, "age", 28)
         print(a.age)
    28


----

slice
-------------------

.. class:: slice()

----

sorted
-------------------

.. function:: sorted(iterable, *, key=None, reverse=False)

Sort all objects that can be iterated

- ``iterable`` -- Iterable object.
- ``key`` -- It is mainly used to compare elements with only one parameter. The parameters of specific functions are taken from the iterable objects, and one element of the iterable objects is specified for sorting.
- ``reverse`` -- collation, reverse=True descending order ,  reverse=False ascending order (default) 。

sorted the easiest way to use::

        sorted([5, 2, 3, 1, 4])
    [1, 2, 3, 4, 5]                      # ascending order as default

Using key to sort in reverse order::

        example_list = [5, 0, 6, 1, 2, 7, 3, 4]
         result_list = sorted(example_list, key=lambda x: x*-1)
         print(result_list)
    [7, 6, 5, 4, 3, 2, 1, 0]


To reverse sorting, also by passing into the third parameter::

        example_list = [5, 0, 6, 1, 2, 7, 3, 4]
         sorted(example_list, reverse=True)
    [7, 6, 5, 4, 3, 2, 1, 0]

----

staticmethod
-------------------

.. decorator:: staticmethod()

Method to convert to static method.

Static methods do not receive the first implicit parameter. To declare a static method, use this syntax::

    class C:
        @staticmethod
        def f(arg1, arg2,...):...

Static method calls can be made on a class (such as C.f()) It can also be done on the instance (such as C().f())。

----

str
-------------------

.. class:: str()

Function to convert an object to a str object。

::

        s = 'w3cschool'
         str(s)
    'W3Cschool'
         dict = {'w3cschool': 'w3cschool', 'google': 'google.com'};
         str(dict)
    "{'google': 'google.com', 'w3cschool': 'w3cschool.cn'}"


----

sum
-------------------

.. function:: sum(iterable[, start])

::

        sum([0,1,2])
    3
         sum((2, 3, 4), 1) # Add 1 after calculating the sum of the tuples.
    10
         sum([0,1,2,3,4], 2) # Add 2 after calculating the sum of the list.
    12

----

super
-------------------

.. function:: super()

super() Function is a method used to call the parent class (superclass)。

::

    class A:
        def add(self, x):
            y = x+1
            print(y)
    class B(A):
        def add(self, x):
            super().add(x)
    b = B()
    b.add(2)  # 3

----

tuple
-------------------

.. class:: tuple()

To convert list to tuple.

::

        list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
         tuple1=tuple(list1)
         tuple1
    ('Google', 'Taobao', 'Runoob', 'Baidu')

----

type
-------------------

.. function:: type()

type() Function returns the type of object if ave only the first argument, Three parameters return the new type object.

- ``type(object)``
- ``type(name, bases, dict)``

    - ``name`` -- Name of the class.
    - ``bases`` -- Tuple of base class.
    - ``dict`` -- Dictionaries, namespace changes defined within classes.

.. Hint:: isinstance() 与 type() differences

    - type() The subclass is not considered as a parent type, and inheritance is not considered.
    - isinstance() The subclass is considered as a type of parent class, and inheritance relationship is considered.

    **To judge whether two types are the same, recommended to use isinstance()。**

::

         type(1)
    <type 'int'>
         type('runoob')
    <type 'str'>
         type([2])
    <type 'list'>
         type({0:'zero'})
    <type 'dict'>
         x = 1
         type( x ) == int    # Judge whether the types are equal
    True

    # Three parameters
         class X(object):
   ...     a = 1
   ...
         X = type('X', (object,), dict(a=1))  # Generate a new type X
         X
    <class '__main__.X'>

type() and isinstance() differences::

    class A:
        pass
    s
    class B(A):
        pass

    isinstance(A(), A)    # returns True
    type(A()) == A        # returns True
    isinstance(B(), A)    # returns True
    type(B()) == A        # returns False

----

zip
-------------------

.. function:: zip([iterable,...])

zip() The function is used to package the iteratable objects as parameters, pack the object corresponding elements into tuples, and then return the objects composed of these tuples. The advantage of this is that it saves a lot of memory.

We can use the list() transformation to output the list. If the number of elements of each iterator is different, the length of the returned list is the same as that of the shortest object. Using the * operator, the tuple can be decompressed into a list.

::

        a = [1,2,3]
         b = [4,5,6]
         c = [4,5,6,7,8]
         zipped = zip(a,b)     # Return an object
         zipped
    <zip object at 0x103abc288>
         list(zipped)  # list() convert to list
    [(1, 4), (2, 5), (3, 6)]
         list(zip(a,c))              # The number of elements is consistent with the shortest list
    [(1, 4), (2, 5), (3, 6)]

         a1, a2 = zip(*zip(a,b))          # 与 zip 相反, zip(*) It can be understood as decompression, returning to two-dimensional matrix
         list(a1)
    [1, 2, 3]
         list(a2)
    [4, 5, 6]


----

Exceptions
----------

See: https://docs.python.org/3/library/exceptions.html

.. exception:: ArithmeticError

.. exception:: AssertionError

.. exception:: AttributeError

.. exception:: BaseException

.. exception:: EOFError

.. exception:: Exception

.. exception:: GeneratorExit

.. exception:: ImportError

.. exception:: IndentationErro

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