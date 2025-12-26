==========================
Music built in melodies
==========================

| See: `<https://microbit-micropython.readthedocs.io/en/stable/music.html>`_

.. py:module:: music

Built in music
----------------------------------------

| There are built-in melodies that can be found by typing ``music.``
| Melodies can be played using ``music.play(melody)`` where the melody is music. and a melody name in capitals.

.. code-block:: python

    from microbit import *
    import music

    music.play(music.POWER_UP)

| The code below uses a for-loop to loop through each melody in a given ``melodies_list`` and play it.


.. code-block:: python

    from microbit import *
    import music

    melodies_list = [music.DADADADUM, music.POWER_DOWN]
    for melody in melodies_list:
        music.play(melody)

----

All Built in melodies
----------------------------------------

| For a list of built-in melodies see: `<https://microbit-micropython.readthedocs.io/en/stable/music.html>`_
| The code below plays all the melodies.
| the A-button can be used to stop all sounds by first breaking out of the ``for`` loop, then the ``while True`` loop.

.. code-block:: python

    from microbit import *
    import music

    built_in_tunes = [music.DADADADUM, music.ENTERTAINER, music.PRELUDE,
                      music.ODE, music.NYAN, music.RINGTONE, music.FUNK, music.BLUES,
                      music.BIRTHDAY, music.WEDDING, music.FUNERAL, music.PUNCHLINE,
                      music.PYTHON, music.BADDY, music.CHASE, music.BA_DING,
                      music.WAWAWAWAA, music.JUMP_UP, music.JUMP_DOWN, music.POWER_UP,
                      music.POWER_DOWN]

    while True:
        for tune in built_in_tunes:
            music.play(tune)
            sleep(1000)
            if button_a.is_pressed():
                break
        if button_a.is_pressed():
            break
----

.. admonition:: Tasks

    #. Play any 3 melodies using a list.
    #. Use the choice function to randomly pick melodies from a melody list. See: `<https://www.w3schools.com/python/ref_random_choice.asp

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play any 3 melodies using a list.

                .. code-block:: python

                    from microbit import *
                    import music

                    melodies_list = [music.POWER_UP, music.DADADADUM, music.POWER_DOWN]
                    for melody in melodies_list:
                        music.play(melody)

            .. tab-item:: Q2

                Use the choice function to randomly pick melodies from a melody list. See: `<https://www.w3schools.com/python/ref_random_choice.asp

                .. code-block:: python

                    from microbit import *
                    import random
                    import music

                    melodies_list = [music.POWER_UP, music.DADADADUM, music.POWER_DOWN]

                    while True:
                        music.play(random.choice(melodies_list))
                        sleep(1000)

----

Melody notes
-------------------

| The notes for each built in melody are below.

.. code-block:: python

    from microbit import *
    import music

    dadadadum = [
        "r4:2", "g", "g", "g", "eb:8",
        "r:2", "f", "f", "f", "d:8"
    ]

    entertainer = [
        "d4:1", "d#", "e", "c5:2", "e4:1",
        "c5:2", "e4:1", "c5:3", "c:1", "d",
        "d#", "e", "c", "d", "e:2", "b4:1", "d5:2",
        "c:4"
    ]

    prelude = [
        "c4:1", "e", "g", "c5", "e", "g4", "c5", "e", "c4", "e",
        "g", "c5", "e", "g4", "c5", "e", "c4", "d", "g", "d5", "f",
        "g4", "d5", "f", "c4", "d", "g", "d5", "f", "g4", "d5", "f",
        "b3", "d4", "g", "d5", "f", "g4", "d5", "f", "b3", "d4", "g",
        "d5", "f", "g4", "d5", "f", "c4", "e", "g", "c5", "e", "g4",
        "c5", "e", "c4", "e", "g", "c5", "e", "g4", "c5", "e"
    ]

    ode = [
        "e4", "e", "f", "g", "g", "f", "e", "d", "c", "c", "d", "e",
        "e:6", "d:2", "d:8", "e:4", "e", "f", "g",
        "g", "f", "e", "d", "c", "c", "d", "e", "d:6",
        "c:2", "c:8"
    ]

    nyan = [
        "f#5:2", "g#", "c#:1", "d#:2",
        "b4:1", "d5:1", "c#", "b4:2", "b",
        "c#5", "d", "d:1", "c#", "b4:1",
        "c#5:1", "d#", "f#", "g#", "d#",
        "f#", "c#", "d", "b4", "c#5", "b4",
        "d#5:2", "f#", "g#:1", "d#",
        "f#", "c#", "d#", "b4", "d5", "d#", "d",
        "c#", "b4", "c#5", "d:2", "b4:1", "c#5",
        "d#", "f#", "c#", "d", "c#", "b4",
        "c#5:2", "b4", "c#5", "b4", "f#:1",
        "g#", "b:2", "f#:1", "g#", "b",
        "c#5", "d#", "b4", "e5", "d#", "e", "f#",
        "b4:2", "b", "f#:1", "g#", "b", "f#",
        "e5", "d#", "c#", "b4", "f#", "d#", "e",
        "f#", "b:2", "f#:1", "g#", "b:2",
        "f#:1", "g#", "b", "b", "c#5", "d#",
        "b4", "f#", "g#", "f#", "b:2", "b:1",
        "a#", "b", "f#", "g#", "b", "e5", "d#", "e",
        "f#", "b4:2", "c#5"
    ]
    ringtone = ["c4:1", "d", "e:2", "g", "d:1", "e", "f:2", "a", "e:1", "f", "g:2", "b", "c5:4"]

    funk = ["c2:2", "c", "d#", "c:1", "f:2", "c:1", "f:2", "f#", "g", "c", "c", "g", "c:1", "f#:2", "c:1", "f#:2", "f", "d#"]

    blues = ["c2:2", "e", "g", "a", "a#", "a", "g", "e", "c2:2", "e", "g", "a", "a#", "a", "g", "e", "f", "a", "c3", "d", "d#", "d", "c", "a2", "c2:2", "e", "g", "a", "a#", "a", "g", "e", "g", "b", "d3", "f", "f2", "a", "c3", "d#", "c2:2", "e", "g", "e", "g", "f", "e", "d"]

    birthday = ["c4:3", "c:1", "d:4", "c:4", "f", "e:8", "c:3", "c:1", "d:4", "c:4", "g", "f:8", "c:3", "c:1", "c5:4", "a4", "f", "e", "d", "a#:3", "a#:1", "a:4", "f", "g", "f:8"]

    wedding = ["c4:4", "f:3", "f:1", "f:8", "c:4", "g:3", "e:1", "f:8", "c:4", "f:3", "a:1", "c5:4", "a4:3", "f:1", "f:4", "e:3", "f:1", "g:8"]

    funeral = ["c4:4", "c:3", "c:1", "c:4", "d#:3", "d:1", "d:3", "c:1", "c:3", "b3:1", "c3:4"]

    punchline = ["c4:3", "g3:1", "f#", "g", "g#:3", "g", "r", "b", "c4"]

    python = ["d5:1", "b4", "r", "b", "b", "a#", "b", "g5", "r", "d", "d", "r", "b4", "c5", "r", "c", "c", "r", "d", "e:5", "c:1", "a4", "r", "a", "a", "g#", "a", "f#5", "r", "e", "e", "r", "c", "b4", "r", "b", "b", "r", "c5", "d:5", "d:1", "b4", "r", "b", "b", "a#", "b", "b5", "r", "g", "g", "r", "d", "c#:1", "r", "a", "a", "r", "a", "a:5", "g:1", "f#:2", "a:1", "a", "g#", "a", "e:2", "a:1", "a", "g#", "a", "d", "r", "c#", "d", "r", "c#", "d:2", "r:3"]

    baddy = ["c4:3", "r", "d:2", "d#", "r", "c", "r", "f#:8"]

    chase = ["a4:1", "b", "c5", "b4", "a:2", "r", "a:1", "b", "c5", "b4", "a:2", "r", "a:2", "e5", "d#", "e", "f", "e", "d#", "e", "b4:1", "c5", "d", "c", "b4:2", "r", "b:1", "c5", "d", "c", "b4:2", "r", "b:2", "e5", "d#", "e", "f", "e", "d#", "e"]

    ba_ding = ["b5:1", "e6:3"]

    wawawawaa = ["e4:3", "r:1", "d#:3", "r:1", "d:4", "r:1", "c#:8"]

    jump_up = ["c5:1", "d", "e", "f", "g"]

    jump_down = ["g5:1", "f", "e", "d", "c"]

    power_up = ["g4:1", "c5", "e", "g:2", "e:1", "g:3"]

    power_down = ["g5:1", "d#", "c", "g4:2", "b:1", "c5:3"]


    melodies = [dadadadum, entertainer, prelude, ode, nyan,
                ringtone, funk, blues, birthday, wedding,
                funeral, punchline, python, baddy, chase,
                ba_ding, wawawawaa, jump_up, jump_down, power_up, power_down]

    # Loop over each
    music.set_tempo(ticks=4, bpm=80)
    for melody in melodies:
        music.play(melody, wait=True)
        sleep(1000)


