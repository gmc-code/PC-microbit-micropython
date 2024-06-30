==========================
Audio frames
==========================

AudioFrame
------------------

.. py:class:: AudioFrame

    An ``AudioFrame`` object is a list of 32 samples each of which is an unsigned byte (whole number between 0 and 255).

It takes just over 4 ms to play a single frame.
The audio module can consume an iterable (sequence, like list or tuple, or generator) of **AudioFrame** instances, each 32 samples at 7812.5 Hz, and uses linear interpolation to output a PWM signal at 32.5 kHz, which gives tolerable sound quality.

----

Sawtooth
--------------

| The sawtooth wave is a type of waveform known for its linear rise and sudden fall. In this case, the 32 values start from 252 and decrease by 8 at each step.

| The code below generates a sawtooth wave and plays it on the micro:bit, stopping if button A is pressed. It also scrolls the name of the wave (“Sawtooth wave”) across the microbit's LED display. The wave continues to play until button A is pressed or the specified duration has passed. The wave pattern is printed to the console as well.


.. code-block:: python
        
    from microbit import *
    import audio


    def repeated_frame(frame, count):
        """
        Generator function that yields the same frame multiple times.

        Parameters:
        frame (audio.AudioFrame): The audio frame to be repeated.
        count (int): The number of times the frame is to be repeated.

        Yields:
        audio.AudioFrame: The same frame multiple times.
        """
        for i in range(count):
            yield frame


    # Press button-A to stop
    def show_wave(name, frame, duration=1500):
        """
        Displays the name of the wave on the micro:bit's LED display and plays the audio wave.
        Stops if button A is pressed.

        Parameters:
        name (str): The name of the wave to be displayed.
        frame (audio.AudioFrame): The audio frame to be played.
        duration (int, optional): The number of frames for which the audio is to be played. Defaults to 1500.
        """
        display.scroll(name + " wave", wait=False, delay=100)
        audio.play(repeated_frame(frame, duration), wait=False)
        for i in range(75):
            if button_a.is_pressed():
                display.clear()
                audio.stop()
                break
            sleep(100)

    frame = audio.AudioFrame()
    # len = 32
    for i in range(len(frame)):
        frame[i] = int(252 - i * 8)
        print(frame[i], end=" ")
    show_wave("Sawtooth", frame, duration=1000)


----

Advanced Technical Details
-----------------------------------

.. note::
    You don't need to understand this section to use the ``audio`` module.
    It is just here in case you wanted to know how it works.

The ``audio`` module can consume an iterable (sequence, like list or tuple, or
generator) of ``AudioFrame`` instances, each 32 samples at 7812.5 Hz, and uses
linear interpolation to output a PWM signal at 32.5 kHz, which gives tolerable
sound quality.

The function ``play`` fully copies all data from each ``AudioFrame`` before it
calls ``next()`` for the next frame, so a sound source can use the same
``AudioFrame`` repeatedly.

The ``audio`` module has an internal 64 sample buffer from which it reads
samples. When reading reaches the start or the mid-point of the buffer, it
triggers a callback to fetch the next ``AudioFrame`` which is then copied into
the buffer. This means that a sound source has under 4ms to compute the next
``AudioFrame``, and for reliable operation needs to take less 2ms (which is
32000 cycles, so should be plenty).

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
    def generate_frames(wave_1, wave_2):
        frames = []
        frame_count = 10
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
        ## Generate frames
        tri_squares = generate_frames(tri, square)
        show_waves("tri_squ", tri_squares)




