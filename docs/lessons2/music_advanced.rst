==========================
Music advanced
==========================

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html

.. py:module:: music

----

Random notes Task
----------------------------------------

| Design code to generate random notes, using separate lists of possibilities for each feature of a note:
* **note name**
* **octave**
* **length**
| Make sure the octave is a string. e.g **octave 4** can be converted to **"4"** using **str(4)**.
| Make sure the note length is a string. e.g **2** can be converted to **"2"** using **str(2)**.
| Build the full note specification by concatenating each part.
| i.e. **note name** + **octave** + **":"** + **length**
| e.g. **c4:2**
| Create a list of notes, a list of octaves and a list of durations that are to be used.
| Create a defintion that takes as parameters the list of notes, the list of octaves and the list of durations, then randomly chooses one from each, joins them together and returns a full note.
| Then, play therandomly generated notes.

| Scaffold for the task:

.. code-block:: python

    from microbit import *
    import random
    import music

    notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
    octaves = [3, 4, 5]
    durations = [1, 2, 4, 8]

    def get_random_note(notes, octaves, durations):
        note = random.choice(......)
        # convert numbers to strings so they ccan be joined
        octave = str(random.choice(.......))
        duration = str(random.choice(.......))
        full_note = ..... + ...... + ":" + ......
        return .......

    while True:
        random_note = get_random_note(..... )
        music.play(.....)


.. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: play random notes
                
                .. code-block:: python

                    from microbit import *
                    import random
                    import music

                    notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
                    octaves = [3, 4, 5]
                    durations = [1, 2, 4, 8]

                    def get_random_note(notes, octaves, durations):
                        note = random.choice(notes)
                        # convert numbers to strings so they ccan be joined
                        octave = str(random.choice(octaves))
                        duration = str(random.choice(durations))
                        full_note = note + octave + ":" + duration
                        return full_note

                    while True:
                        random_note = get_random_note(notes, octaves, durations)
                        music.play(random_note)

----

.. admonition:: Tasks

    #. Include a note modification parameter to sharpen, flatten or leave the note unchanged.
    #. Create a function to return a random list of notes, given the number of notes, then play the list.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Include a note modification parameter to sharpen, flatten or leave the note unchanged.

                .. code-block:: python

                    from microbit import *
                    import random
                    import music


                    notes = ["c", "d", "e", "f", "g", "a", "b"]
                    modifiers = ["#", "b", ""]
                    octaves = [3, 4, 4, 4, 4, 5]
                    durations = [2, 3, 4, 2, 3, 4, 2, 3, 4, 8]


                    def get_random_note(notes, modifiers, octaves, durations):
                        note = random.choice(notes)
                        modifier = random.choice(modifiers)
                        octave = str(random.choice(octaves))
                        duration = str(random.choice(durations))
                        full_note = note + modifier + octave + ":" + duration
                        return full_note


                    while True:
                        random_note = get_random_note(notes, modifiers, octaves, durations)
                        music.play(random_note)


            .. tab-item:: Q2

                Create a function to return a random list of notes, given the number of notes, then play the list.

                .. code-block:: python

                    from microbit import *
                    import random
                    import music

                    notes = ["c", "d", "e", "f", "g", "a", "b"]
                    octaves = [3, 4, 4, 4, 4, 5]
                    durations = [2, 3, 4, 2, 3, 4, 2, 3, 4, 8]


                    def get_random_note(notes, octaves, durations):
                        note = random.choice(notes)
                        octave = str(random.choice(octaves))
                        duration = str(random.choice(durations))
                        full_note = note + octave + ":" + duration
                        return full_note


                    def get_random_notes(note_count):
                        tune = []
                        for i in range(note_count):
                            tune.append(get_random_note(notes, octaves, durations))
                        return tune


                    while True:
                        random_notes = get_random_notes(10)
                        music.play(random_notes)
                        sleep(2000)

----

Scales generator
----------------------------------------

See: https://piano-music-theory.com/2016/05/31/major-scales/
See; https://appliedguitartheory.com/lessons/how-to-determine-the-key-of-a-song/

| Design code to generate the notes in a major scale, given the key and the octave. 
| Create a list of keys that use sharps and a list of keys that use flats.

| Scaffold for the task:

.. code-block:: python

    from microbit import *
    import random
    import music


    major_steps = [2, ......, 1]
    minor_steps = [2, ......, 2]


    def get_2oct(octave, notes):
        notes_oct1 = [i + str(octave) for i in notes]
        notes_oct2 = [i + str(octave + 1) for i in notes]
        notes_2oct = notes_oct1 + notes_oct2
        return notes_2oct


    def get_key_notes(key_note):
        sharp_keys = ["c", "g", "d", "a", "e", "b", "f#", "c#"]
        # flat_keys = ["c", "f", "bb", "eb", "ab", "db", "gb", "cb"]
        sharp_key_notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
        flat_key_notes = ["c", "db", "d", "eb", "e", "f", "gb", "g", "ab", "a", "bb", "b"]
        if key_note in sharp_keys:
            return ...............
        else:
            return ...............


    def get_scale(key_note, octave, scale_steps):
        notes = get_key_notes(......)
        notes2oct = get_2oct(....., no.....tes)
        note_index = notes2oct.index(..... + str(.....))
        scale = [notes2oct[.........]]
        for i in scale_steps:
            note_index += i
            scale.append(notes2oct[........])
        return scale


    while True:
        scale_notes = get_scale("c", 4, major_steps)
        # print(scale_notes)
        music.play(........)
        sleep(1000)
        scale_notes = get_scale("e", 4, minor_steps)
        # print(scale_notes)
        music.play(........)
        sleep(1000)



 .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Scales generator
                
                .. code-block:: python

                    from microbit import *
                    import random
                    import music


                    major_steps = [2, 2, 1, 2, 2, 2, 1]
                    minor_steps = [2, 1, 2, 2, 1, 2, 2]


                    def get_2oct(octave, notes):
                        notes_oct1 = [i + str(octave) for i in notes]
                        notes_oct2 = [i + str(octave + 1) for i in notes]
                        notes_2oct = notes_oct1 + notes_oct2
                        return notes_2oct


                    def get_key_notes(key_note):
                        sharp_keys = ["c", "g", "d", "a", "e", "b", "f#", "c#"]
                        # flat_keys = ["c", "f", "bb", "eb", "ab", "db", "gb", "cb"]
                        sharp_key_notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
                        flat_key_notes = ["c", "db", "d", "eb", "e", "f", "gb", "g", "ab", "a", "bb", "b"]
                        if key_note in sharp_keys:
                            return sharp_key_notes
                        else:
                            return flat_key_notes


                    def get_scale(key_note, octave, scale_steps):
                        notes = get_key_notes(key_note)
                        notes2oct = get_2oct(octave, notes)
                        note_index = notes2oct.index(key_note + str(octave))
                        scale = [notes2oct[note_index]]
                        for i in scale_steps:
                            note_index += i
                            scale.append(notes2oct[note_index])
                        return scale


                    while True:
                        scale_notes = get_scale("c", 4, major_steps)
                        print(scale_notes)
                        music.play(scale_notes)
                        sleep(1000)
                        scale_notes = get_scale("e", 4, minor_steps)
                        print(scale_notes)
                        music.play(scale_notes)
                        sleep(1000)


