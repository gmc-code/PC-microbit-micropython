==========================
Music_advanced
==========================

| See: https://microbit-micropython.readthedocs.io/en/v2-docs/music.html

.. py:module:: music

----

Random notes Task
----------------------------------------

See: https://random-music-generators.herokuapp.com/melody

| Design code to generate random notes, using separate lists of possibilities for each feature of a note:  **note name**, **octave**, **length**.
| Use **random.choice(list_name)** to choose a random element from a list.
| Make sure the octave is a string. e.g **octave 4** can be converted to **"4"** using **str(4)**.
| Make sure the note length is a string. e.g **2** can be converted to **"2"** using **str(2)**.
| Build the full note specification by concatenating each part.
| i.e. **note name** + **octave** + **":"** + **length**
| e.g. **c4:2**
| Create a list of notes, a list of octaves and a list of durations that are to be used.
| Create a definition that takes as parameters the list of notes, the list of octaves and the list of durations, then randomly chooses one from each, joins them together and returns a full note.
| Then, play the randomly generated notes.

.. admonition:: Tasks

    #. Random notes Scaffold:

        .. code-block:: python

            from microbit import *
            import random
            import music

            notes = ['c', 'd', 'e', 'f', 'g', 'a', 'b']
            octaves = [3, 4, 5]
            durations = [1, 2, 4, 8]

            def get_random_note(notes, octaves, durations):
                note = random.choice(......)
                # convert numbers to strings so they can be joined
                octave = str(random.choice(.......))
                duration = str(random.choice(.......))
                full_note = ..... + ...... + ":" + ......
                return .......

            while True:
                random_note = get_random_note(....., ......, ...... )
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
                            # convert numbers to strings so they can be joined
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
    #. Create a function, **get_random_notes**, to return a random list of notes, given the number of notes. Use a for-loop to add the random notes to a list within the function. Play the notes when a button is pressed.
    #. Rewrite the function, **get_random_notes**, to use list comprehension.

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

                Create a function, **get_random_notes**, to return a random list of notes, given the number of notes. Use a for-loop to add the random notes to a list within the function. Play the notes when a button is pressed.

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
                        random_notes = []
                        for i in range(note_count):
                            random_notes.append(get_random_note(notes, octaves, durations))
                        return random_notes


                    while True:
                        if button_a.is_pressed():

                        random_notes = get_random_notes(10)
                        music.play(random_notes)
                        sleep(2000)

            .. tab-item:: Q3

                Rewrite the function, **get_random_notes**, to use list comprehension.

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
                        return [get_random_note(notes, octaves, durations) for i in range(note_count)] 


                    while True:
                        random_notes = get_random_notes(10)
                        music.play(random_notes)
                        sleep(2000)


----

Scales generator
----------------------------------------

| See: https://piano-music-theory.com/2016/05/31/major-scales/
| See: https://appliedguitartheory.com/lessons/how-to-determine-the-key-of-a-song/
| See: https://en.wikipedia.org/wiki/Key_signature#Scales_with_sharp_key_signatures

| Design code to generate the notes in a major scale, given the key and the octave. 
| Research the intervals for major and natural minor scales and place them in lists, **major_steps** and **minor_steps**. Define a function, **get_scale_steps(key_type)**, that returns the scale intervals for a Major or minor keys based on passing "M" for major and "m" for minor.
| Define a function, **get_2oct**,  to return 2 octaves of notes, starting at **c**,  given the start octave and the notes. Use list comprehension to take each not and add the octave to it as a string. e.g "c" and 4 are joined to become "c4".
| Define a function, **get_key_notes**,  to return the notes in a key given the key. Research the keys that have sharps in them (see: circle of fifths) and make a list of them, **sharp_keys**. Check to see if the key is in that list and return a list of all possible notes, starting at c, that include sharps, **["c", "c#", ...]**, or return the list of notes that includes flats, **["c", "db", ...]**.
| Define a function, **get_scale(key_note, key_type, octave)**, that returns the list of notes that include sharps or flats based on the key_note and key_type. Then build 2 octaves of notes based on those notes and the octave. Use the index method to get the index of the key_note in that 2 octave list. Then iterate through the scale_steps, adding the scale step interval to the index and append that note to the scale. Return the one octave scale.
| Test the definitions by playing some scales that include a scale with a sharp, and a scale with a flat, as well as both major and minor scales.

| Scaffold for the task:

.. code-block:: python

    from microbit import *
    import music


    def get_scale_steps(key_type):
        major_steps = [2, ......, 1]
        minor_steps = [2, ......, 2]
        if key_type == "M":
            return major_steps
        else:
            return ......


    def get_2oct(octave, notes):
        notes_oct1 = [i + str(octave) for i in notes]
        notes_oct2 = [..... + str(octave + ....) for .... in ........]
        notes_2oct = notes_oct1 + notes_oct2
        return notes_2oct


    def get_key_notes(key_note, key_type):
        major_sharp_keys = ["c", "g", "d", "a", "e", "b", "f#", "c#"]
        # major_flat_keys = ["c", "f", "bb", "eb", "ab", "db", "gb", "cb"]
        minor_sharp_keys = ["a", "e", "b", "f#", "c#", "g#", "d#", "a#"]
        # minor_flat_keys = ["a", "d", "g", "c", "f", "bb", "eb", "ab"]
        if key_type == "M":
            sharp_keys = ......
        else:
            sharp_keys = .....
        sharp_key_notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
        flat_key_notes = ["c", "db", "d", "eb", "e", "f", "gb", "g", "ab", "a", "bb", "b"]
        if key_note in ......:
            return sharp_key_notes
        else:
            return flat_key_notes


    def get_scale(key_note, key_type, octave):
        scale_steps = get_scale_steps(......)
        notes = get_key_notes(......)
        notes2oct = get_2oct(....., ........)
        note_index = notes2oct.index(..... + str(.....))
        scale = [notes2oct[.........]]
        for i in scale_steps:
            note_index += i
            scale.append(notes2oct[........])
        return scale


    while True:
        if button_a.is_pressed():
            scale_notes = get_scale("g", "M", 4)
            # print(scale_notes)
            music.play(scale_notes)
            sleep(1000)
            scale_notes = get_scale("e", "m", 4)
            # print(scale_notes)
            music.play(scale_notes)
            sleep(1000)
        elif button_b.is_pressed():
            scale_notes = get_scale("f", "M", 4)
            # print(scale_notes)
            music.play(scale_notes)
            sleep(1000)
            scale_notes = get_scale("d", "m", 4)
            # print(scale_notes)
            music.play(scale_notes)
            sleep(1000)


.. dropdown::
    :icon: codescan
    :color: primary
    :class-container: sd-dropdown-container

    .. tab-set::

        .. tab-item:: Scales generator
            
            .. code-block:: python

                from microbit import *
                import music


                def get_scale_steps(key_type):
                    major_steps = [2, 2, 1, 2, 2, 2, 1]
                    minor_steps = [2, 1, 2, 2, 1, 2, 2]
                    if key_type == "M":
                        return major_steps
                    else:
                        return minor_steps


                def get_2oct(octave, notes):
                    notes_oct1 = [i + str(octave) for i in notes]
                    notes_oct2 = [i + str(octave + 1) for i in notes]
                    notes_2oct = notes_oct1 + notes_oct2
                    return notes_2oct


                def get_key_notes(key_note, key_type):
                    major_sharp_keys = ["c", "g", "d", "a", "e", "b", "f#", "c#"]
                    # major_flat_keys = ["c", "f", "bb", "eb", "ab", "db", "gb", "cb"]
                    minor_sharp_keys = ["a", "e", "b", "f#", "c#", "g#", "d#", "a#"]
                    # minor_flat_keys = ["a", "d", "g", "c", "f", "bb", "eb", "ab"]
                    if key_type == "M":
                        sharp_keys = major_sharp_keys
                    else:
                        sharp_keys = minor_sharp_keys
                    sharp_key_notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
                    flat_key_notes = ["c", "db", "d", "eb", "e", "f", "gb", "g", "ab", "a", "bb", "b"]
                    if key_note in sharp_keys:
                        return sharp_key_notes
                    else:
                        return flat_key_notes


                def get_scale(key_note, key_type, octave):
                    scale_steps = get_scale_steps(key_type)
                    notes = get_key_notes(key_note, key_type)
                    notes2oct = get_2oct(octave, notes)
                    note_index = notes2oct.index(key_note + str(octave))
                    scale = [notes2oct[note_index]]
                    for i in scale_steps:
                        note_index += i
                        scale.append(notes2oct[note_index])
                    return scale


                while True:
                    if button_a.is_pressed():
                        scale_notes = get_scale("g", "M", 4)
                        # print(scale_notes)
                        music.play(scale_notes)
                        sleep(1000)
                        scale_notes = get_scale("e", "m", 4)
                        # print(scale_notes)
                        music.play(scale_notes)
                        sleep(1000)
                    elif button_b.is_pressed():
                        scale_notes = get_scale("f", "M", 4)
                        # print(scale_notes)
                        music.play(scale_notes)
                        sleep(1000)
                        scale_notes = get_scale("d", "m", 4)
                        # print(scale_notes)
                        music.play(scale_notes)
                        sleep(1000)

.. admonition:: Tasks

    #. Create a function, **get_random_notes(notes, note_count=5)**,  to return a random list of notes, given the notes and the number of notes, with default 5. Use list comprehension to generate the list. Play 5 random notes from the **g major** and 5 from the **a minor** scales on button pressing.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Scales generator
                
                .. code-block:: python

                    from microbit import *
                    import music
                    import random


                    def get_scale_steps(key_type):
                        major_steps = [2, 2, 1, 2, 2, 2, 1]
                        minor_steps = [2, 1, 2, 2, 1, 2, 2]
                        if key_type == "M":
                            return major_steps
                        else:
                            return minor_steps


                    def get_2oct(octave, notes):
                        notes_oct1 = [i + str(octave) for i in notes]
                        notes_oct2 = [i + str(octave + 1) for i in notes]
                        notes_2oct = notes_oct1 + notes_oct2
                        return notes_2oct


                    def get_key_notes(key_note, key_type):
                        major_sharp_keys = ["c", "g", "d", "a", "e", "b", "f#", "c#"]
                        # major_flat_keys = ["c", "f", "bb", "eb", "ab", "db", "gb", "cb"]
                        minor_sharp_keys = ["a", "e", "b", "f#", "c#", "g#", "d#", "a#"]
                        # minor_flat_keys = ["a", "d", "g", "c", "f", "bb", "eb", "ab"]
                        if key_type == "M":
                            sharp_keys = major_sharp_keys
                        else:
                            sharp_keys = minor_sharp_keys
                        sharp_key_notes = ["c", "c#", "d", "d#", "e", "f", "f#", "g", "g#", "a", "a#", "b"]
                        flat_key_notes = ["c", "db", "d", "eb", "e", "f", "gb", "g", "ab", "a", "bb", "b"]
                        if key_note in sharp_keys:
                            return sharp_key_notes
                        else:
                            return flat_key_notes


                    def get_scale(key_note, key_type, octave):
                        scale_steps = get_scale_steps(key_type)
                        notes = get_key_notes(key_note, key_type)
                        notes2oct = get_2oct(octave, notes)
                        note_index = notes2oct.index(key_note + str(octave))
                        scale = [notes2oct[note_index]]
                        for i in scale_steps:
                            note_index += i
                            scale.append(notes2oct[note_index])
                        return scale


                    def get_random_notes(notes, note_count=5):
                        random_notes = [random.choice(notes) for i in range(note_count)]
                        return random_notes

                    while True:
                        if button_a.is_pressed():
                            random_notes = get_random_notes(get_scale("g", "M", 4), 5)
                            print(random_notes)
                            music.play(random_notes)
                            sleep(1000)
                        elif button_b.is_pressed():
                            random_notes = get_random_notes(get_scale("a", "m", 4), 5)
                            print(random_notes)
                            music.play(random_notes)
                            sleep(1000)

.. admonition:: Tasks

    #. Create a dictionary of keys and their notes and save it to a file to be accessed on the microbit.
    #. Create a dictionary of tunes, save it to a file to be accessed on the microbit.

