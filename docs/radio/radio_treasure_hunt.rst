====================================================
Radio Treasure Hunt
====================================================

| For a treasure hunt, have some microbits to act as hidden treasure beacons; some as treasure hunters.

----
 
Treasure
-------------------------

| Set multiple devices to act as treasure beacons each with their own id as a string. ``treasure_id = '1'``
| Set up the group value in ``radio.config(group=8)``.
| Set the radio power to 0 so it can only be detected from close range ``radio.config(power=0)``. Power level 0 usually has a range less than 1 metre.
| Hide the treasure beacons.

.. code-block:: python
    
    from microbit import *
    import radio


    # Set radio group and transmit power
    radio.config(group=8, power=0)
    radio.on()

    treasure_id = '1' # change the number string for each treasure beacon
    display.scroll(treasure_id)
    sleep(2000)
    display.clear()

    while True:
        radio.send(treasure_id)
        sleep(200)

    
----

.. admonition:: Tasks

    #. Modify the code so that on pressing the A button the treasure_id is scrolled.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code so that on pressing the A button the treasure_id is scrolled. 

                .. code-block:: python

                    from microbit import *
                    import radio

                    # Set radio group and transmit power
                    radio.config(group=8, power=0)
                    radio.on()

                    treasure_id = '1' # change the number string for each treasure beacon
                    display.scroll(treasure_id)
                    sleep(2000)
                    display.clear()

                    while True:
                        radio.send(treasure_id)
                        sleep(200)
                        if button_a.was_pressed():
                            display.scroll(treasure_id)

----

Treasure hunters
-------------------------

| The treasure hunters look for treasure beacons and display the treasure id value.  

.. code-block:: python
    
    from microbit import *
    import radio


    # Set radio group
    radio.config(group=8)
    radio.on()

    while True:
        incoming_message = radio.receive()
        if incoming_message:
            display.scroll(incoming_message)
            sleep(200)

----

.. admonition:: Challenges
    
    #. See who can find the treasure first.

----

Buried Treasure
-------------------------

| Use the random module to set the treasure beacons id to a random single digit integer as a string. ``treasure_id = str(random.randint(1, 9))``
| Use the power module deep_sleep method to conserve power: ``power.deep_sleep(wake_on=button_a, ms=min_ms, run_every=True)``
| Use run_every as a decorator to send the radio message every 5 seconds using ``send_id``. 

.. code-block:: python
    
    from microbit import *
    import power
    import radio
    import random

    # Set radio group and transmit power
    radio.config(group=8, power=0)
    # Set the received message handler
    radio.on()

    treasure_id = str(random.randint(1, 9))
    display.show(treasure_id)
    sleep(2000)
    display.clear()

    @run_every(s=5)
    def send_id():
        radio.send(treasure_id)
        display.scroll(treasure_id)

    min_ms = 60 * 1000
    while True:
        # renew deep sleep every minute
        power.deep_sleep(wake_on=button_a, ms=min_ms, run_every=True)
        # display treasure_id
        if button_a.was_pressed():
            display.scroll(treasure_id)

----

.. admonition:: Tasks

    #. Modify the code so that pressing the B button changes the treasure_id to a new random integer between 1 and 9.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

               Modify the code so that pressing the B button changes the treasure_id to a new random integer between 1 and 9. 

                .. code-block:: python

                    from microbit import *
                    import power
                    import radio
                    import random

                    # Set radio group and transmit power
                    radio.config(group=8, power=0)
                    # Set the received message handler
                    radio.on()

                    treasure_id = str(random.randint(1, 9))
                    display.show(treasure_id)
                    sleep(2000)
                    display.clear()

                    @run_every(s=5)
                    def send_id():
                        radio.send(treasure_id)
                        display.scroll(treasure_id)

                    min_ms = 60 * 1000
                    while True:
                        # renew deep sleep every minute
                        power.deep_sleep(wake_on=(button_a, button_b), ms=min_ms, run_every=True)
                        # display treasure_id
                        if button_a.was_pressed():
                            display.scroll(treasure_id)
                        # change treasure_id
                        elif button_b.was_pressed():
                            treasure_id = str(random.randint(1, 9))
                            display.scroll(treasure_id)

----

Treasure collectors
-------------------------

| The treasure collectors remember the treasure ids that they have collected.
| Use a list to store the treasure ids, but check if the treasure_id is in the list to avoid adding duplicate values.

.. code-block:: python
    
    from microbit import *
    import radio

    # Set radio group
    radio.config(group=8)
    # Set the received message handler
    radio.on()

    # Create a set to store unique ids
    unique_ids = list()

    while True:
        incoming_message = radio.receive()
        if incoming_message:
            # If the message is not already in the list, append it
            if incoming_message not in unique_ids:
                unique_ids.append(incoming_message)
            display.scroll(incoming_message)
            sleep(200)
        if button_a.was_pressed():
            display.scroll("-")
            for treasure_id in unique_ids:
                display.scroll(treasure_id)
            display.scroll("-")

----

Sorting a list using a function as a sort key
---------------------------------------------------

.. py:function:: list.sort(reverse=True|False, key=myFunc)

    Sorts the list, ascending by default.
    
    :param reverse	Optional: reverse=True will sort the list descending. Default is reverse=False
    :param key	Optional: A function to specify the sorting criteria.

See: https://www.w3schools.com/python/ref_list_sort.asp

| The list below has strings of integers.
| A sort key is required to sort them numerically.
| The sort_int_strings function is used as the key. It returns the integer from each string.
| For each item in int_strings, the sort_int_strings function uses the item as an argument (which becomes the list_value in the function).
| The sort_int_strings function converts the string to an integer and returns it.
| The sort method then sorts the items in the list based on these integer values returned by the sort_int_strings function.
| So, in essence, list_value is a placeholder for each item in the list as the sort method goes through the list.


.. code-block:: python

    from microbit import *

    # A function that returns the integer from a string:
    def sort_int_strings(list_value):
        return int(list_value)

    int_strings = ['5', '4', '6', '3']
    int_strings.sort(key=sort_int_strings)
    for int_str in int_strings:
        display.scroll(int_str, delay=70)

| Alternatively, a function, sort_int_strings, can return the sorted list. 

.. code-block:: python

    from microbit import *

    # A function that sorts a list of integer strings based on their integer values:
    def sort_int_strings(lst):
        lst.sort(key=int)
        return lst

    int_strings = ['5', '4', '6', '3']
    int_strings = sort_int_strings(int_strings)
    for int_str in int_strings:
        display.scroll(int_str, delay=70)


.. admonition:: Tasks

    #. Modify the treasure collector code to scroll the treasure ids in ascending order. 

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code to scroll the treasure ids in ascending order. 

                .. code-block:: python

                    from microbit import *
                    import radio


                    # Set radio group
                    radio.config(group=8)
                    # Set the received message handler
                    radio.on()

                    # Create a list to store unique ids
                    unique_ids = list()


                    def sort_integer_strings(lst):
                        return sorted(lst, key=int)


                    while True:
                        incoming_message = radio.receive()
                        if incoming_message:
                            # If the message is not already in the list, append it
                            if incoming_message not in unique_ids:
                                unique_ids.append(incoming_message)
                            display.scroll(incoming_message)
                            sleep(200)
                        if button_a.was_pressed():
                            display.scroll("-")
                            for treasure_id in sort_integer_strings(unique_ids):
                                display.scroll(treasure_id)
                            display.scroll("-")

----

Find all the treasure
------------------------

| Rather than using random treasure ids from 1 to 9, the ids can be automatically incremented and looped.
| The hunters can show when they have collected all the treasure ids.

.. admonition:: Tasks

    #. Modify the treasure beacon code so that the treasure_id is changed every 12 seconds. Increment the id and loop it.
    #. Modify the treasure collector code so that the B button is used to display the number of treasure ids collected. 

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the treasure beacon code so that the treasure_id is changed every 12 seconds. Increment the id from 1 to 9 over and over again. 

                .. code-block:: python

                    from microbit import *
                    import power
                    import radio
                    import random

                    # Set radio group and transmit power
                    radio.config(group=8, power=0)
                    # Set the received message handler
                    radio.on()

                    # start at random id, not always 1.
                    treasure_id = str(random.randint(1, 9))
                    display.show(treasure_id)
                    sleep(2000)
                    display.clear()


                    @run_every(s=5)
                    def send_id():
                        radio.send(treasure_id)
                        display.scroll(treasure_id)


                    @run_every(s=12)
                    def change_id():
                        global treasure_id
                        if int(treasure_id) == 9:
                            treasure_id = str(1)
                        else:
                            treasure_id = str(int(treasure_id) + 1)
                        radio.send(treasure_id)
                        display.scroll(treasure_id)


                    min_ms = 60 * 1000
                    while True:
                        # renew deep sleep every minute
                        power.deep_sleep(wake_on=(button_a, button_b), ms=min_ms, run_every=True)
                        # display treasure_id
                        if button_a.was_pressed():
                            display.scroll(treasure_id)
                        # change treasure_id
                        elif button_b.was_pressed():
                            change_id()



            .. tab-item:: Q2

                Modify the treasure collector code so that the B button is used to display the number of treasure ids collected. 

                .. code-block:: python

                    from microbit import *
                    import radio


                    # Set radio group
                    radio.config(group=8)
                    # Set the received message handler
                    radio.on()


                    def sort_string_numbers(lst):
                        # Convert the strings to integers and sort the list
                        sorted_list = sorted(lst, key=int)
                        return sorted_list


                    # Create a set to store unique messages
                    unique_ids = list()

                    while True:
                        incoming_message = radio.receive()
                        if incoming_message:
                            # If the message is not already in the list, append it
                            if incoming_message not in unique_ids:
                                unique_ids.append(incoming_message)
                            display.scroll(incoming_message)
                            sleep(200)
                        if button_a.was_pressed():
                            display.scroll("-")
                            for treasure_id in sort_string_numbers(unique_ids):
                                display.scroll(treasure_id)
                            display.scroll("-")
                        elif button_b.was_pressed():
                            treasure_count = len(unique_ids)
                            display.scroll("*")
                            display.scroll(treasure_count)
                            display.scroll("*")


