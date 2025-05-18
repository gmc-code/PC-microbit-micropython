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

    Returns the absolute value of a number.
    Arguments can be integers or floating-point numbers.

| The code deletes the file at index 1 in the list.

.. code-block:: python

    from microbit import *
    # import builtins

    while True:
        display.scroll(abs(-2.3))

----

all
-------------------

.. function:: all(iterable)

    If all elements of `iterable` are true (or the iterator is empty), return `True`, otherwise `False`.

.. code-block:: python

    from microbit import *
    # import builtins

    list1 = [1, 0, 1]
    list2 = [1, 1, 1]
    while True:
        display.scroll(all(all_list1))
        display.scroll("_")
        display.scroll(all(all_list2))

----

any
-------------------

.. function:: any(iterable)

    If any element of `iterable` is true, return `True`. If the iterator is empty, return `False`.


.. code-block:: python

    from microbit import *
    # import builtins

    list1 = [1, 0, 1]
    list2 = [0, 0, 0]
    while True:
        display.scroll(any(all_list1))
        display.scroll("_")
        display.scroll(any(all_list2))

----

bin
-------------------

.. function:: bin()

    Convert an integer to a binary string prefixed with "0b".

.. code-block:: python

    from microbit import *
    # import builtins

    val1 = bin(3)
    val2 = bin(-1)
    while True:
        display.scroll(val1)
        display.scroll("_")
        display.scroll(val2)

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
    # import builtins

    val1 = bool()
    val2 = bool(0)
    val3 = bool(1)
    val4 = bool(None)
    while True:
        display.scroll(val1)
        display.scroll("_")
        display.scroll(val2)
        display.scroll("/")
        display.scroll(val3)
        display.scroll("|")
        display.scroll(val4)

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
    # import builtins

    val1 = bytearray()
    val2 = bytearray(3)
    val3 = bytearray([2,4,6])
    val4 = bytearray("mb", 'utf-8')
    print(val1)
    print(val2)
    print(val3)
    print(val4)

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
    # import builtins

    val1 = bytes()
    val2 = bytes(2)
    val3 = bytes([2, 4, 6])
    val4 = bytes("mb", "utf-8")
    print(val1)
    print(val2)
    print(val3)
    print(val4)

----

callable
-------------------

.. function:: callable(object)

    Returns True if the specified `object` is callable, otherwise it returns False.

.. code-block:: python

    from microbit import *
    # import builtins

    def add2(a, b):
        return a + b

    print(callable(add2))
    print(callable(0))
    print(callable("mb"))

----

chr
-------------------

.. function:: chr(number)

    Returns the character that represents the specified unicode `number`.

.. code-block:: python

    from microbit import *
    # import builtins

    print(chr(0x30))
    print(chr(97))
    print(chr(8364))

----

classmethod
-------------------

See: https://www.programiz.com/python-programming/methods/built-in/classmethod

.. decorator:: classmethod()

    | Converts a regular method into a class method
    | Class methods can be called on a class or on an instance.

.. code-block:: python

    from microbit import *
    # import builtins

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
    # import builtins

    class Person:
        age = 15

        @classmethod
        def printAge(cls):
            print('The age is:', cls.age)

    Person.printAge()
    Person.age = 20
    Person.printAge()

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
    # import builtins

    print(complex(1, 2))
    print(complex(1))
    print(complex("1"))
    print(complex(1+2j))

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
    # import builtins

    class Coordinate:
        x = 10
        y = -5
        z = 0

    point1 = Coordinate()

    print('x = ',point1.x)
    print('y = ',point1.y)
    print('z = ',point1.z)

    delattr(Coordinate, 'z')
    print('--deleted z attribute--')

    print('x = ',point1.x)
    print('y = ',point1.y)

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

dict() Function to create a dictionary

::

    dict()                        # Create an empty dictionary
    {}
    dict(a='a', b='b', t='t')     # enter keyword
    {'a': 'a', 'b': 'b', 't': 't'}
    dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # Mapping function mode to construct dictionary
    {'three': 3, 'two': 2, 'one': 1}
    dict([('one', 1), ('two', 2), ('three', 3)])    # Iterative object method to construct the dictionary
    {'three': 3, 'two': 2, 'one': 1}



----

dir
-------------------

.. function:: dir(object)

dir() When a function has no parameters, it returns the list of variables, methods and defined types in the current range; when it has parameters, it returns the list of properties and methods of parameters.
If the parameter contains  __dir__(), if it doesn't contains __dir__(), This method will maximize the collection of parameter information.
- ``object`` -- object, variable, type.


----

divmod
-------------------

.. function:: divmod()

It takes two (non complex) numbers as arguments and returns a pair of quotients and remainder when integer division is performed. Mixed operand type, applicable to the rules of higher arithmetic operators.
For integers, results are consistent with (a // b, a % b). For floating-point numbers, the result is (q, a % b) , q is usually math.floor(a / b) but it might be smaller than 1.
In any case, Q * B + a% B and a are basically equal; if a% B is not zero, Its symbol is the same as B, and 0 < = ABS (a% B) < ABS (b).

::

         divmod(7, 2)
    (3, 1)h
         divmod(8, 2)
    (4, 0)
         divmod(8, -2)
    (-4, 0)
         divmod(3, 1.3)
    (2.0, 0.4000001)

----

Ellipsis
-------------------

| See: https://docs.python.org/3/library/constants.html
| The ellipsis can be uses instead of pass as a placeholder in functions.
| This is useful during development so that the unfinished function doesn't return an error.

.. code-block:: python

    from microbit import *
    # import builtins

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

.. function:: enumerate(sequence, [start=0])

enumerate() Function is used to combine a traversable data object (such as a list, tuple or string) into an index sequence, and list data and data subscripts. It is generally used in for-loop.

- ``sequence`` -- A sequence, iterator, or other object that supports iteration.
- ``start`` -- Subscript start position.

::

        seq = ['one', 'two', 'three']
         for i, element in enumerate(seq):
   ...     print i, element
   ...
    0 one
    1 two
    2 three

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
         exec("print ('runoob.com')")
    runoob.com

    #  Single line statement string
         exec ("""for i in range(5):
   ...     print ("iter time: %d" % i)
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
    print ("element list : ", list1)

    str="Hello World"
    list2=list(str)
    print ("element list : ", list2)

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
   ...     print (locals())
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

Returns the maximum value of the given parameter, which can be a sequence

::

    print ("max(80, 100, 1000) : ", max(80, 100, 1000))
    print ("max(-20, 100, 400) : ", max(-20, 100, 400))
    print ("max(-80, -20, -10) : ", max(-80, -20, -10))
    print ("max(0, 100, -400) : ", max(0, 100, -400))

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

    print ("min(80, 100, 1000) : ", min(80, 100, 1000))
    print ("min(-20, 100, 400) : ", min(-20, 100, 400))
    print ("min(-80, -20, -10) : ", min(-80, -20, -10))
    print ("min(0, 100, -400) : ", min(0, 100, -400))

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

    print ("pow(100, 2) : ", pow(100, 2))
    print ("pow(100, -2) : ", pow(100, -2))
    print ("pow(2, 4) : ", pow(2, 4))
    print ("pow(3, 0) : ", pow(3, 0))

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

    print ("round(70.23456) : ", round(70.23456))
    print ("round(56.659,1) : ", round(56.659,1))
    print ("round(80.264, 2) : ", round(80.264, 2))
    print ("round(100.000056, 3) : ", round(100.000056, 3))
    print ("round(-100.000056, 3) : ", round(-100.000056, 3))

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