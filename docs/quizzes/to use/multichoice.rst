================================================
Multi-Choice Directive Documentation
================================================

----

Example 1: Single Correct (Default)
------------------------------------

.. multichoice::

    Which of these does an equality check in Python?

    [x] == | Correct.
    [ ] = | Incorrect. That does assignment
    [ ] !== | Incorrect. Not equals to
    [ ] <= | Incorrect. Less than or equals to

----

Example 4: Code Block Layout Inside Question
--------------------------------------------

.. multichoice::
    :theme: dark

    What is the output of the following code?

    .. code-block:: python

        x = 5
        y = 2
        print(x ** y)

    [x] 25 | Correct: `**` is exponentiation, so output is 25
    [ ] 5^2
    [ ] 10
    [ ] 7

----

Example 5: Multiple Correct Answers
-----------------------------------

.. multichoice::

    Which of the following are Python data types?

    [x] int | Integer type
    [x] str | String type
    [ ] html | Not a Python type
    [x] float | Floating-point number

