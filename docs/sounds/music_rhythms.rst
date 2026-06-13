==========================
Music Rhythms
==========================

Rhythm: Shave and a hair cut: two bits
-----------------------------------------

| See: `<https://en.wikipedia.org/wiki/Shave_and_a_Haircut
| The rhythm below is given by saying aloud: "Shave and a hair cut: two bits".
| Play this rhythm.

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=120)
    rhythm = ["C4:4", "C4:2", "C4:2", "C4:4", "C4:4", "R:4", "C4:4", "C4:4", "R:4"]


    while True:
        music.play(rhythm)

----

.. admonition:: Tasks

    .. image:: images/shave_and_a_haircut.png
        :scale: 100 %

    #. Modify the notes to match the image notes in the key of G.
    #. Modify the notes to match the image notes, but in the key of C.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the notes to match the image notes in the key of G.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=4, bpm=120)
                    rhythm = ["G4:4", "D4:2", "D4:2", "E4:4", "D4:4", "R:4", "F#4:4", "G4:4", "R:4"]

                    while True:
                        music.play(rhythm)

            .. tab-item:: Q2

                Modify the notes to match the image notes, but in the key of C.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=4, bpm=120)
                    rhythm = ["C5:4", "G4:2", "G4:2", "A4:4", "G4:4", "R:4", "B4:4", "C5:4", "R:4"]

                    while True:
                        music.play(rhythm)


----

Rhythm: Famous movie series 1
--------------------------------

| Play this rhythm.
| Can you identify the movie theme?

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=90)
    rhythm = ["C4:3", "C4:1", "R:2", "C4:2", "C4:2", "C4:2", "R:1", "C4:1", "R:2", "C4:2", "C4:2"]

    while True:
        music.play(rhythm)
        sleep(1000) # Give it a 1-second dramatic pause before repeating

----

.. admonition:: Tasks

    #. Replace the notes with: G, G, Bb, C5, G, G, F, F#.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Replace the notes with: G, G, Bb, C5, G, G, F, F#.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=4, bpm=90)
                    rhythm = ["G4:3", "G4:1", "R:2", "Bb4:2", "C5:2", "G4:2", "R:1", "G4:1", "R:2", "F4:2", "F#4:2"]

                    while True:
                        music.play(rhythm)
                        sleep(1000) # Give it a 1-second dramatic pause before repeating

----

Rhythm: Famous movie series 2
--------------------------------

| Play this rhythm.
| Can you identify the movie theme?

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=105)
    rhythm = [
        "C4:4", "C4:4", "C4:4", "C4:3", "C4:1",  # Dun, dun, dun, da-da
        "C4:4", "C4:3", "C4:1", "C4:8",          # Dun, da-da, dunnn
        "C5:4", "C5:4", "C5:4", "C5:3", "C4:1",  # Dun, dun, dun, da-da
        "C4:4", "C4:3", "C4:1", "C4:8"          # Dun, da-da, dunnn
    ]

    while True:
        music.play(rhythm)
        sleep(1000) # Give it a 1-second dramatic pause before repeating

----

.. admonition:: Tasks

    #. Replace the notes with: G, G, G, Eb, Bb, G, Eb, Bb, G, D, D, D, Eb, Bb, F#, Eb, Bb, G.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Replace the notes with: G, G, G, Eb, Bb, G, Eb, Bb, G, D, D, D, Eb, Bb, F#, Eb, Bb, G.

                .. code-block:: python

                    from microbit import *
                    import music

                    # 105 BPM gives it that perfect, driving military march pace
                    music.set_tempo(ticks=4, bpm=105)

                    # The definitive main melody of The Imperial March
                    imperial_march = [
                        "G4:4", "G4:4", "G4:4", "Eb4:3", "Bb4:1",  # Dun, dun, dun, da-da
                        "G4:4", "Eb4:3", "Bb4:1", "G4:8",          # Dun, da-da, dunnn
                        "D5:4", "D5:4", "D5:4", "Eb5:3", "Bb4:1",  # Dun, dun, dun, da-da
                        "F#4:4", "Eb4:3", "Bb4:1", "G4:8"          # Dun, da-da, dunnn
                    ]

                    while True:
                        music.play(imperial_march)
                        sleep(1000) # Give it a 1-second dramatic pause before repeating


----

Rhythm: Famous movie series 3
--------------------------------

| Play this rhythm.
| Can you identify the movie theme?

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=120)

    rhythm = [
        "C4:2", "C4:2", "C4:2", "C4:2",
        "C4:2", "C4:2", "C4:2", "C4:2"
    ]

    while True:
        music.play(rhythm)
        sleep(1000)

----

.. admonition:: Tasks

    #. Replace the notes with: E, F, G, C5, E5, F5, G5, C6.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Replace the notes with: E, F, G, C5, E5, F5, G5, C6.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=4, bpm=120)

                    super_mario = [
                        "E4:2", "F4:2", "G4:2", "C5:2",
                        "E5:2", "F5:2", "G5:2", "C6:2"
                    ]

                    while True:
                        music.play(super_mario)
                        sleep(1000)

----

Rhythm: Famous movie series 4
--------------------------------

| Play this rhythm.
| Can you identify the movie theme?

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=100)

    rhythm = [
        "C4:2", "C4:2", "C4:2", "C4:2",
        "C4:2", "C4:2", "C4:2"
    ]

    while True:
        music.play(rhythm)
        sleep(1000)

----

.. admonition:: Tasks

    #. Replace the notes with: E, G, A, A, A, G, E.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Replace the notes with: E, G, A, A, A, G, E.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=4, bpm=100)

                    jurassic_park = [
                        "E4:2", "G4:2", "A4:4",
                        "A4:2", "A4:2", "G4:2", "E4:4"
                    ]

                    while True:
                        music.play(jurassic_park)
                        sleep(1000)

----

Rhythm: Famous movie series 5
--------------------------------

| Play this rhythm.
| Can you identify the movie theme?

.. code-block:: python

    from microbit import *
    import music

    music.set_tempo(ticks=4, bpm=140)

    rhythm = [
        "C4:2", "C4:2", "C4:2", "C4:2",
        "C4:2", "C4:2", "C4:2", "C4:2"
    ]

    while True:
        music.play(rhythm)
        sleep(1000)

----

.. admonition:: Tasks

    #. Replace the notes with: E, G, A, A#, A, G, E, D.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Replace the notes with: E, G, A, Bb, A, G, E, D.

                .. code-block:: python

                    from microbit import *
                    import music

                    music.set_tempo(ticks=4, bpm=140)

                    pirates = [
                        "E4:2", "G4:2", "A4:2", "Bb4:2",
                        "A4:2", "G4:2", "E4:2", "D4:2"
                    ]

                    while True:
                        music.play(pirates)
                        sleep(1000)




