==========================
Jupyter Tests
==========================

.. thebe-button:: Activate Jupyter Thebelab

----

.. jupyter-execute::

    def name_age_greeting(name, age):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting("Joe", 12))


----

.. jupyter-execute::

    def name_age_greeting2(name="John", age=99):
        age += 1
        return "Hi " + name + ", you are " + str(age) + " years old"

    print(name_age_greeting2())

----

.. math::

    ^{_{238}}_{_{92}}U \rightarrow \space ^{_{234}}_{_{90}}Th + \space ^{_{4}}_{_{2}}He


