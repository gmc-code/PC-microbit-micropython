================================
Audio: built in sounds **V2**
================================

Expressive sounds  **V2**
--------------------------

| The built-in expressive sounds can be called using ``audio.play(Sound.SOUNDNAME)`` where SOUNDNAME is replaced with the name of a sound in capital letters.
| e.g. ``audio.play(Sound.GIGGLE)``

The built in sounds are

* Sound.GIGGLE
* Sound.HAPPY
* Sound.HELLO
* Sound.MYSTERIOUS
* Sound.SAD
* Sound.SLIDE
* Sound.SOARING
* Sound.SPRING
* Sound.TWINKLE
* Sound.YAWN


.. code-block:: python

    from microbit import *
    import audio

    audio.play(Sound.GIGGLE)


| The code below uses a for-loop to loop through each sound in the ``sound_list`` and play each sound.

.. code-block:: python

    from microbit import *
    import audio

    sound_list = [Sound.GIGGLE, Sound.TWINKLE]
    for sound in sound_list:
        audio.play(sound)

----

.. admonition:: Tasks

    #. Play the HELLO sound and scroll "hello" using wait=True for both.
    #. Play the HELLO sound and scroll "hello" using wait=False for the sound and wait=True for the text.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play the HELLO sound and scroll "hello" using wait=True for both.

                .. code-block:: python

                    from microbit import *
                    import audio

                    while True:
                        audio.play(Sound.HELLO, wait=True)
                        display.scroll("hello", wait=True)
                        sleep(1000)

            .. tab-item:: Q2

                Play the HELLO sound and scroll "hello" using wait=False for the sound and wait=True for the text.

                .. code-block:: python

                    from microbit import *
                    import audio

                    while True:
                        audio.play(Sound.HELLO, wait=False)
                        display.scroll("hello", wait=True)
                        sleep(1000)

----

All Built in sounds
----------------------------------------

| The code below plays all the built-in sounds.
| the A-button can be pressed to exit the for-loop then the while-loop using ``break``.
| Pressing the reset button on the back of the microbit will restart the code.

.. code-block:: python

    from microbit import *
    import audio

    built_in_sounds = [
        Sound.GIGGLE,
        Sound.HAPPY,
        Sound.HELLO,
        Sound.MYSTERIOUS,
        Sound.SAD,
        Sound.SLIDE,
        Sound.SOARING,
        Sound.SPRING,
        Sound.TWINKLE,
        Sound.YAWN,
    ]

    while True:
        for sound in built_in_sounds:
            if button_a.was_pressed():
                break
            audio.play(sound)
            sleep(500)
        if button_a.is_pressed():
            break

----

.. admonition:: Tasks

    #. Play any 3 built-in sounds using a list, separating them with a 1 second pause.
    #. Use the choice function to randomly pick a built-in sound from a sound list. See: `<https://www.w3schools.com/python/ref_random_choice.asp. Use button pressing to break out of the while-loop to stop playing sounds.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Play any 3 built-in sounds using a list, separating them with a 1 second pause.

                .. code-block:: python

                    from microbit import *
                    import audio

                    sound_list = [Sound.SAD, Sound.HAPPY, Sound.YAWN]
                    for sound in sound_list:
                        audio.play(sound)
                        sleep(1000)

            .. tab-item:: Q2

                Use the choice function to randomly pick a built-in sound from a sound list. See: `<https://www.w3schools.com/python/ref_random_choice.asp. Use button pressing to break out of the while-loop to stop playing sounds.

                .. code-block:: python

                    from microbit import *
                    import audio
                    from random import choice as rand_choice

                    sound_list = [Sound.SAD, Sound.HAPPY, Sound.YAWN]

                    while True:
                        audio.play(rand_choice(sound_list))
                        sleep(1000)
                        if button_a.is_pressed():
                            break

----

Sound name with sound
--------------------------

| The advanced code below uses ``replace`` methods on the string version of the sound to get the simple name of the sound for scrolling.
| The sound playing is started first, using the non-blocking form with ``wait=False``.
| The sound name is scrolled using the blocking form with ``wait=True``, so that the the next sound is not played till the scrolling has completed.

.. code-block:: python

    from microbit import *
    import audio

    sound_list = [Sound.GIGGLE, Sound.TWINKLE]
    for sound in sound_list:
        # Remove 'Sound(' from the start and ')' from the end
        sound_name = str(sound).replace("Sound('", '').replace("')", '')
        audio.play(sound, wait=False)
        display.scroll(sound_name, delay=80, wait=True)

.. admonition:: Tasks

    #. Modify the code above to use all built in sounds.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the code above to use all built in sounds.

                .. code-block:: python

                    from microbit import *
                    import audio

                    sound_list = [
                        Sound.GIGGLE,
                        Sound.HAPPY,
                        Sound.HELLO,
                        Sound.MYSTERIOUS,
                        Sound.SAD,
                        Sound.SLIDE,
                        Sound.SOARING,
                        Sound.SPRING,
                        Sound.TWINKLE,
                        Sound.YAWN,
                    ]

                    for sound in sound_list:
                        # Remove 'Sound(' from the start and ')' from the end
                        sound_name = str(sound).replace("Sound('", '').replace("')", '')
                        audio.play(sound, wait=False)
                        display.scroll(sound_name, delay=80, wait=True)

----

Built in sounds and images
---------------------------

| The following code uses a dictionary to associate sounds and images.
| It then displays the image and plays the sound.
| In the code ``for emotion, attributes in emotions.items():``, 'emotion, attributes' follow the pattern 'key, value', where emotion is the key and attribute is the value for that key.
| 'happy' is the first emotion (key). Its value, attribute, is a nested dictionary with keys 'sound' and 'image'.

.. code-block:: python

    from microbit import *
    import audio

    # Define the sounds and images for happy and sad emotions
    emotions = {
        'happy': {
            'sound': Sound.HAPPY,
            'image': Image.HAPPY
        },
        'sad': {
            'sound': Sound.SAD,
            'image': Image.SAD
        }
    }

    while True:
        for emotion, attributes in emotions.items():
            # Display the image
            display.show(attributes['image'])
            # Play the sound
            audio.play(attributes['sound'], wait=True)
            display.clear()
            sleep(1000)

----

.. admonition:: Tasks

    #. Modify the emotions dictionary to associate 2 other images with 2 other built in sounds. Use button pressing to utilize each one separately. Use a def block to do the image display and sound playing.

    .. dropdown::
        :icon: codescan
        :color: primary
        :class-container: sd-dropdown-container

        .. tab-set::

            .. tab-item:: Q1

                Modify the emotions dictionary to associate 2 other images with 2 other built in sounds. Use button pressing to utilize each one separately. Use a def block to do the image display and sound playing.

                .. code-block:: python

                    from microbit import *
                    import audio


                    emotions = {
                        'alert': {
                            'sound': Sound.TWINKLE,
                            'image': Image.DIAMOND
                        },
                        'tired': {
                            'sound': Sound.YAWN,
                            'image': Image.ASLEEP
                        }
                    }

                    def do_emotion(emotion):
                        display.show(emotions[emotion]['image'])
                            # Play the sound
                        audio.play(emotions[emotion]['sound'], wait=True)
                        display.clear()

                    while True:
                        if button_a.is_pressed():
                            do_emotion('alert')
                        elif button_b.is_pressed():
                            do_emotion('tired')
                        sleep(100)

