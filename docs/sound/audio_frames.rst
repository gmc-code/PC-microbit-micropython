==========================
Audio: AudioFrames
==========================

AudioFrames
------------------

| An AudioFrame object is a list of 32 samples each of which is an unsigned byte (whole number between 0 and 255).
| Use ``frame = audio.AudioFrame()`` to create the audioframe object. 
| Use ``frame[i] = ...`` to fill all 32 samples as i changes from 0 to 31.
| It takes just over 4 ms to play a single frame.

----

Sawtooth AudioFrame
--------------------

| The sawtooth wave is a type of waveform known for its linear rise and sudden fall. 
| The code below creates an AudioFrame in which the 32 values decrease from 252 in steps of 8: 252, 244, 236, 228, 220, 212, 204, 196, 188, 180, 172, 164, 156, 148, 140, 132, 124, 116, 108, 100, 92, 84, 76, 68, 60, 52, 44, 36, 28, 20, 12, 4.
| This is a sound profile that starts high and decreases steadily.
| This doesn't play any sounds yet.

.. code-block:: python
        
    from microbit import *
    import audio


    def get_sawtooth_frame():
        frame = audio.AudioFrame()
        # len = 32
        for i in range(len(frame)):
            frame[i] = int(252 - i * 8)
        return frame



----

Generators to avoid memory limits
-----------------------------------

| Since an audio frame only goes for 4ms to 6ms, it needs to be repeated about 160 times to last for 1 second.
| ``audio.play`` plays an iterable (a list or generator) of AudioFrame instances.
| If the AudioFrame is repeated in a list, as in ``repeated_frame1`` below, the list size is limited to about 8000 iterations (about 50 seconds) as it takes up memory.
| This may be fine for short sounds; but is not good practice.

.. code-block:: python
        
    def repeated_frame1(frame, count):
        # will hit a memory problem after about 8000 repeats
        wave = []
        for i in range(count):
            wave.append(frame)
        return wave

| Generators are used in this case to avoid memory issues.
| Use ``yield`` in the for-loop to create a generator that releases each repeat of the ``frame`` as it is needed in the calling code.
| The function, ``repeated_frame``, uses a generator (via the yield keyword) to create an iterable object. 
| This means it generates each repetition on-the-fly each time you iterate over it.
| This is more memory-efficient than creating a large list or other collection. 
| This is especially useful if count is a large number.

.. code-block:: python
        
    def repeated_frame(frame, count):
        # use a generator to reduce memory usage
        for i in range(count):
            yield frame

| The code that plays a sawtooth audioframe is below. 
| Adjust ``repeat_count = 40`` to alter the length it is played.

.. code-block:: python
        
    from microbit import *  # Importing all the modules from microbit library
    import audio  # Importing the audio module

    def play_rep_frame(name, frame, count):
        """
        This function plays a repeated audio frame.
        
        Parameters:
        name (str): The name of the audio frame.
        frame (AudioFrame): The audio frame to be repeated.
        count (int): The number of times the frame is to be repeated.
        """
        # Generate the repeated audio frame
        wave = repeated_frame(frame, count)  
        # If an audio is already playing
        while audio.is_playing():  
            sleep(4)
            audio.stop()
        display.scroll(name, wait=False, delay=60)  
        # Display the name of the audio frame
        audio.play(wave, wait=False)

    def repeated_frame(frame, count):
        """
        This function generates a repeated audio frame using a generator to reduce memory usage.
        
        Parameters:
        frame (AudioFrame): The audio frame to be repeated.
        count (int): The number of times the frame is to be repeated.
        
        Returns:
        generator: A generator that yields the audio frame 'count' number of times.
        """
        for i in range(count):  # Repeat for 'count' number of times
            yield frame  # Yield the audio frame

    def get_sawtooth_frame():
        """
        This function generates a sawtooth audio frame.
        
        Returns:
        AudioFrame: A sawtooth audio frame.
        """
        frame = audio.AudioFrame()  # Create a new audio frame
        for i in range(len(frame)):  # For each sample in the audio frame
            frame[i] = int(252 - i * 8)  # Generate a sawtooth wave
        return frame  # Return the sawtooth audio frame

    repeat_count = 40  # The number of times the audio frame is to be repeated
    sawtooth_frame = get_sawtooth_frame()  # Get the sawtooth audio frame

    while True:  # Main loop
        if button_a.is_pressed():  # If the A-button is pressed
            play_rep_frame("saw", sawtooth_frame, repeat_count)  # Play the sawtooth audio frame
        sleep(100)  # Wait for 100 milliseconds

----

Common AudioFrame structures
-----------------------------------

| Sawtooth, square and triangle audioframes are constructed and played below.
| Each has a base form and a second function at a higher frequency.

.. code-block:: python
        
    from microbit import *  # Importing all the modules from microbit library
    import audio  # Importing the audio module

    def play_rep_frame(name, frame, count):
        """
        This function plays a repeated audio frame.
        
        Parameters:
        name (str): The name of the audio frame.
        frame (AudioFrame): The audio frame to be repeated.
        count (int): The number of times the frame is to be repeated.
        """
        wave = repeated_frame(frame, count)  # Generate the repeated audio frame
        while audio.is_playing():  # If an audio is already playing
            sleep(4)  # Wait for 4 milliseconds
            audio.stop()  # Stop the currently playing audio
        display.scroll(name, wait=False, delay=60)  # Display the name of the audio frame
        audio.play(wave, wait=False)  # Play the new audio frame

    def repeated_frame(frame, count):
        """
        This function generates a repeated audio frame using a generator to reduce memory usage.
        
        Parameters:
        frame (AudioFrame): The audio frame to be repeated.
        count (int): The number of times the frame is to be repeated.
        
        Returns:
        generator: A generator that yields the audio frame 'count' number of times.
        """
        for i in range(count):  # Repeat for 'count' number of times
            yield frame  # Yield the audio frame

    def get_sawtooth_frame():
        """
        This function generates a sawtooth audio frame.
        
        Returns:
        AudioFrame: A sawtooth audio frame.
        """
        frame = audio.AudioFrame()  # Create a new audio frame
        for i in range(len(frame)):  # For each sample in the audio frame
            frame[i] = int(252 - i * 8)  # Generate a sawtooth wave
        return frame  # Return the sawtooth audio frame

    def get_sawtooth2_frame():
        """
        This function generates a modified sawtooth audio frame.
        
        Returns:
        AudioFrame: A modified sawtooth audio frame.
        """
        frame = audio.AudioFrame()  # Create a new audio frame
        for i in range(len(frame)):  # For each sample in the audio frame
            if i < len(frame) // 2:
                frame[i] = int(252 - i * 16)
            else:
                frame[i] = int(252 - (i - 16) * 16)
        return frame  # Return the modified sawtooth audio frame

    def get_square_frame():
        """
        This function generates a square wave audio frame.
        
        Returns:
        AudioFrame: A square wave audio frame.
        """
        frame = audio.AudioFrame()  # Create a new audio frame
        for i in range(len(frame)):  # For each sample in the audio frame
            if i < len(frame) // 2:
                frame[i] = 252
            else:
                frame[i] = 0
        return frame  # Return the square wave audio frame

    def get_square2_frame():
        """
        This function generates a modified square wave audio frame.
        
        Returns:
        AudioFrame: A modified square wave audio frame.
        """
        frame = audio.AudioFrame()  # Create a new audio frame
        for i in range(len(frame)):  # For each sample in the audio frame
            if i < len(frame) // 4:
                frame[i] = 252
            elif i < len(frame) * 2 // 4:
                frame[i] = 0
            elif i < len(frame) * 3 // 4:
                frame[i] = 252
            else:
                frame[i] = 0
        return frame  # Return the modified square wave audio frame

    def get_triangle_frame():
        """
        This function generates a triangle wave audio frame.
        
        Returns:
        AudioFrame: A triangle wave audio frame.
        """
        frame = audio.AudioFrame()  # Create a new audio frame
        for i in range(len(frame)):  # For each sample in the audio frame
            if i < len(frame) // 2:
                frame[i] = i * 8
            else:
                frame[i] = 252 - (i - 16) * 8
        return frame  # Return the triangle wave audio frame

    def get_triangle2_frame():
        """
        This function generates a modified triangle wave audio frame.
        
        Returns:
        AudioFrame: A modified triangle wave audio frame.
        """
        frame = audio.AudioFrame()  # Create a new audio frame
        for i in range(len(frame)):  # For each sample in the audio frame
            if i < len(frame) // 4:
                frame[i] = i * 16
            elif i < len(frame) * 2 // 4:
                frame[i] = 252 - (i - 8) * 16
            elif i < len(frame) * 3 // 4:
                frame[i] = (i - 16) * 16
            else:
                frame[i] = 252 - (i - 24) * 16
        return frame  # Return the modified triangle wave audio frame


    repeat_count = 40
    sawtooth_frame = get_sawtooth_frame()
    sawtooth2_frame = get_sawtooth2_frame()
    square_frame = get_square_frame()
    square2_frame = get_square2_frame()
    triangle_frame = get_triangle_frame()
    triangle2_frame = get_triangle2_frame()

    while True:
        if pin_logo.is_touched():
            play_rep_frame("saw", sawtooth_frame, repeat_count)
            sleep(repeat_count * 5)
            play_rep_frame("saw2", sawtooth2_frame, repeat_count)
        elif button_a.is_pressed():
            play_rep_frame("sqr", square_frame, repeat_count)
            sleep(repeat_count * 5)
            play_rep_frame("sqr2", square2_frame, repeat_count)
        elif button_b.is_pressed():
            play_rep_frame("tri", triangle_frame, repeat_count)
            sleep(repeat_count * 5)
            play_rep_frame("tri2", triangle2_frame, repeat_count)
        sleep(100)

----

Yield from and yield in Generators
---------------------------------------

| Let's consider an example where we have a list of strings and we want to yield each character from each string. 
| In summary, this code prints the characters of several greetings, with each character separated by a comma. The `yield` and `yield from` keywords are used to create generators that produce these characters on-the-fly as they're needed. This is a common pattern in Python for producing a sequence of values in a memory-efficient way. 


.. code-block:: python

    def gen1(list_of_words):
        for word in list_of_words:
            for char in word:
                yield char

    def gen2():
        greetings = [
            ["Hello", "friend"],
            ["Greetings", "human"],
            ["G'day", "mate"],
        ]
        for greeting in greetings:
            print("")
            yield from gen1(greeting)

    # Use a loop to print the values generated by gen2
    for value in gen2():
        print(value, end=",")


1. `gen1(list_of_words)`: This is a generator function that takes a list of words as input. For each word in the list, it iterates over the characters in the word and yields each character one by one. The `yield` keyword here is used to produce a sequence of values over time, rather than computing them at once and returning them in a list for example. This can be more memory-efficient and flexible, especially for large sequences.

2. `gen2()`: This is another generator function. It defines a list of greetings, where each greeting is a list of words. It then iterates over these greetings, and for each greeting, it uses `yield from` to yield all characters from `gen1(greeting)`. 

3. The `yield from` statement is a convenient way to yield all values from another generator or iterable. In this case, it yields all characters from each greeting produced by `gen1`. This allows you to flatten the nested structure of the `greetings` list into a sequence of characters.

4. `for value in gen2(): print(value, end=",")`: This is a loop that iterates over the values yielded by `gen2()`, and prints each value followed by a comma. Because `gen2()` yields characters from the greetings, this will print all the characters in the greetings, each separated by a comma.


----

More complex AudioFrames
-------------------------------

| This code uses the microbit and audio libraries to generate and play a sequence of chords when the logo pin on the microbit is touched. 
| The chords are represented as lists of frequencies, and each frequency in the chord is played as a square wave. 
| The get_square_wave_frame function generates a square wave frame for a given frequency, and the play_chord function generates the audio frames for a chord and plays it. 
| The play_sequence function plays a sequence of chords.
| ``Yield`` and ``yield from`` are used to make it memory efficient.

.. code-block:: python

    from microbit import *
    import audio

    def get_square_wave_frame(frequency):
        """
        This function generates a square wave frame for a given frequency.
        
        Args:
            frequency (float): The frequency of the note in Hz.
            
        Returns:
            frame (audio.AudioFrame): A frame of the square wave at the given frequency.
        """
        frame = audio.AudioFrame()  # Initialize an empty audio frame
        period = int(7812.5 / frequency)  # The period of the waveform in samples
        
        # Generate the square wave
        for i in range(len(frame)):
            if (i // (period // 2)) % 2 == 0:
                frame[i] = 255  # High part of the wave
            else:
                frame[i] = 0  # Low part of the wave
                
        return frame

    def play_chord(frequencies):
        """
        This function generates the audio frames for a chord and plays it.
        
        Args:
            frequencies (list): A list of frequencies in the chord.
            
        Yields:
            frame (audio.AudioFrame): An audio frame of the chord to be played.
        """
        for frequency in frequencies:
            frame = get_square_wave_frame(frequency)  # Get the square wave frame for the frequency
            for _ in range(20):  # Play the note for a certain duration
                yield frame

    def play_sequence():
        """
        This function plays a sequence of chords.
        
        Yields:
            frame (audio.AudioFrame): An audio frame of the sequence to be played.
        """
        # Frequencies of the notes in the chords
        chords = [
            [392.00, 493.88, 587.33],  # G major (G4, B4, D5)
            [523.25, 659.25, 784.00],  # C major (C5, E5, G5)
            [587.33, 739.99, 880.00]   # D major (D5, F#5, A5)
        ]
        
        # Play each chord in the sequence
        for chord in chords:
            sleep(100)  # Wait for a short duration between chords
            yield from play_chord(chord)  # Play the chord

    # Main loop
    while True:
        # Check if the logo pin is touched
        if pin_logo.is_touched():
            # If the logo pin is touched, play the sequence of chords
            audio.play(play_sequence())
            sleep(10)

----

Advanced Technical Details
-----------------------------------

The ``audio`` module can consume an iterable (sequence, like list or tuple, or generator) of ``AudioFrame`` instances, each 32 samples at 7812.5 Hz, and uses linear interpolation to output a PWM signal at 32.5 kHz, which gives tolerable sound quality.

The function ``play`` fully copies all data from each ``AudioFrame`` before it calls ``next()`` for the next frame, so a sound source can use the same ``AudioFrame`` repeatedly.

----

Advanced Example
-----------------


| Here's a breakdown of what each part of the code does:

1. **Defining functions for generating and playing waves**:
    - `repeated_frame(frame, count)`: This function takes a frame (a single cycle of a waveform) and a count, and yields the same frame for the given count. This is used to repeat a waveform.
    - `show_wave(name, frame, duration=1000)`: This function takes a name, a frame, and a duration. It scrolls the name of the wave on the micro:bit's display, plays the audio of the wave for the given duration, and stops if button A is pressed.
    - `repeated_frames(frames, count)`: Similar to `repeated_frame`, but this function takes multiple frames and yields each frame for the given count. This is used to repeat a sequence of waveforms.
    - `show_waves(name, frames, duration=60)`: Similar to `show_wave`, but this function takes multiple frames. It scrolls the name of the wave on the micro:bit's display, plays the audio of the sequence of waves for the given duration, and stops if button A is pressed.
    - `generate_frames(wave_1, wave_2)`: This function takes two waves and generates a sequence of frames that transition smoothly from the first wave to the second.

2. **Defining functions for different waveforms**:
    - `sin_wave()`: This function generates a sine wave.
    - `tri_wave()`: This function generates a triangle wave.
    - `sq_wave()`: This function generates a square wave.
    - `saw_wave()`: This function generates a sawtooth wave.

3. **Main loop**: The main loop of the script continuously generates each type of wave and plays it using the `show_wave` function. It also generates a sequence of frames that transition from a triangle wave to a square wave and plays it using the `show_waves` function.



.. code-block:: python

    from microbit import *
    import audio
    import math


    def repeated_frame(frame, count):
        for _ in range(count):
            yield frame
    
    def show_wave(name, frame, duration=1000):
        display.scroll(name + " wave", wait=False, delay=80)
        audio.play(repeated_frame(frame, duration), wait=False)
        for _ in range(75):
            sleep(100)
            # Press button-A to skip to next wave.
            if button_a.was_pressed():
                display.clear()
                audio.stop()
                break

    ####

    def repeated_frames(frames, count):
        for frame in frames:
            for _ in range(count):
                yield frame
                
    def show_waves(name, frames, duration=60):
        display.scroll(name + " wave", wait=False, delay=80)
        audio.play(repeated_frames(frames, duration), wait=False)
        for _ in range(75):
            sleep(1000)
            # Press button-A to skip to next wave.
            if button_a.was_pressed():
                display.clear()
                audio.stop()
                break
                
    #Generate a waveform that goes from one wave to another wave, reasonably smoothly.
    def generate_frames(wave_1, wave_2, frame_count=10):
        frames = []
        for i in range(frame_count):
            frame = audio.AudioFrame()
            for j in range(len(wave_1)):
                frame[j] = (wave_1[j]*(frame_count-i) + wave_2[j]*i) //frame_count
            frames.append(frame)
        return frames
        
    #####

    def sin_wave():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            frame[i] = int(math.sin(math.pi*i/16)*124+128.5)
        return frame
        

    def tri_wave():
        frame = audio.AudioFrame()
        # QUARTER = 8; len(frame) = 32
        QUARTER = len(frame)//4
        for i in range(QUARTER):
            frame[i] = i*15
            frame[i+QUARTER] = 248-i*15
            frame[i+QUARTER*2] = 128-i*15
            frame[i+QUARTER*3] = i*15+8
        return frame
        

    def sq_wave():
        frame = audio.AudioFrame()
        # HALF = 16; len(frame) = 32
        HALF = len(frame)//2
        for i in range(HALF):
            frame[i] = 8
            frame[i+HALF] = 248
        return frame


    def saw_wave():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            frame[i] = 252-i*8
        return frame
        


    while True:
        sin = sin_wave()
        show_wave("Sine", sin)
        ##
        saw = saw_wave()
        show_wave("Sawtooth", saw)
        ##
        tri = tri_wave()
        show_wave("Triangle", tri)
        ##   
        square = sq_wave() 
        show_wave("Square", square)
        ##
        tri_squares = generate_frames(tri, square)
        show_waves("Tri_Squares", tri_squares)


----

The code below uses a sin wave generator.
Short sounds are made by looping through increasing frequency values.

.. code-block:: python

    from microbit import *
    import audio
    import math


    def repeated_frame(frame, count):
        for _ in range(count):
            yield frame


    def show_wave(name, frame, duration=1000):
        display.scroll(name, wait=False, delay=50)
        audio.play(repeated_frame(frame, duration), wait=False)
        for _ in range(20):
            sleep(50)
            # Press button-A to skip to next wave.
            if button_a.was_pressed():
                display.clear()
                audio.stop()
                break


    def sin_wave(frequency):
        frame = audio.AudioFrame()
        length = len(frame)
        for i in range(length):
            frame[i] = int(math.sin(2 * math.pi * frequency / 128 * i / length) * 124 + 128.5)
        return frame


    while True:
        # frequency = accelerometer.get_x()
        for frequency in range(20, 1024, 50):
            sin = sin_wave(frequency)
            show_wave(frequency, sin, duration=50)




