================================================
Classifying Directive Documentation
================================================

The classifying directive creates an interactive categorization activity.
Users read a series of statements or code snippets and use dropdown menus to sort each item into its correct target category or structural "bin".

Syntax
-------------------

.. code-block:: rst

    .. classifying::
       :bins: Category 1, Category 2

       Item content text goes here | 0
       Another item content statement | 1

Options for the classifying directive
--------------------------------------

.. list-table:: Options for the classifying directive
   :widths: 20 15 65
   :header-rows: 1

   * - Option
     - Type
     - Description
   * - ``:bins:``
     - string
     - | A comma-separated list of category names
       | (supports 2 to 4 distinct classifications).
   * - ``:theme:``
     - string
     - | Sets the visual theme workspace wrapper.
       | Options are ``light`` (default) or ``dark`` (orangue hue).

| Syntax Rules: Items inside the body are split using a pipe delimiter (``|``) followed by the zero-based index of its correct bin.
| Index Mapping: The first bin declared in the ``:bins:`` option corresponds to index ``0``, the second to index ``1``, and so on.
| Shuffling: Items are automatically shuffled on page render and on Reset button click to eliminate pattern memorization giveaways.
| Visual Badges: When validated, inline symbols provide quick feedback right alongside choices.

----

Example 1: Operators vs. Data Structures
--------------------------------------------

The following example demonstrates sorting core Python language features into either syntax operators or built-in data structures using the default light theme.

.. code-block:: rst

    .. classifying::
       :bins: Operators, Data Structures

       + (Addition / Concatenation) | 0
       list (Sequential collection) | 1
       == (Equality comparison) | 0
       dict (Key-value mapping) | 1
       tuple (Immutable sequence) | 1

.. classifying::
   :bins: Operators, Data Structures

   + (Addition / Concatenation) | 0
   list (Sequential collection) | 1
   == (Equality comparison) | 0
   dict (Key-value mapping) | 1
   tuple (Immutable sequence) | 1

----

Example 2: Arithmetic vs. Logical Operators (Dark Theme)
-----------------------------------------------------------

The following example uses the ``:theme: dark`` setting to demonstrate sorting arithmetic and logical operators into their respective categories.

.. code-block:: rst

    .. classifying::
       :bins: Arithmetic, Logical
       :theme: dark

       // (Floor division) | 0
       and (Short-circuit conjunction) | 1
       % (Modulo remainder) | 0
       not (Boolean inversion) | 1
       ** (Exponentiation power) | 0

.. classifying::
   :bins: Arithmetic, Logical
   :theme: dark

   // (Floor division) | 0
   and (Short-circuit conjunction) | 1
   % (Modulo remainder) | 0
   not (Boolean inversion) | 1
   ** (Exponentiation power) | 0

----

Example 3: Mutable vs Immutable Object States
------------------------------------------------

Demonstrating strict item mapping rules utilizing custom labels matching foundational Python data structures.

.. code-block:: rst

    .. classifying::
       :bins: Mutable, Immutable

       Lists (e.g., [1, 2, 3]) | 0
       Tuples (e.g., (1, 2, 3)) | 1
       Strings (e.g., "Hello") | 1
       Dictionaries (e.g., {"a": 1}) | 0

.. classifying::
   :bins: Mutable, Immutable

   Lists (e.g., [1, 2, 3]) | 0
   Tuples (e.g., (1, 2, 3)) | 1
   Strings (e.g., "Hello") | 1
   Dictionaries (e.g., {"a": 1}) | 0

