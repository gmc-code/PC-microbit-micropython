==========================
Audio: AudioFrames
==========================

AudioFrames
------------------

| An AudioFrame object is a list of 32 samples each of which is an unsigned byte (whole number between 0 and 255).
| Use ``frame = audio.AudioFrame()`` to create the audioframe object. 
| Use ``frame[i] = ...`` to fill all 32 samples as i changes from 0 to 31.
| ``audio.play`` requires an iterable (a list or generator) of **AudioFrame** instances, each 32 samples.
| Since an audio frame only goes for 4ms, it needs to be repeated 250 times to last for 1 second.
| If it is repeated in a list, as in ``repeated_frame1`` below, the size is limited to about 8000 iterations (about 20seconds) as it takes up memory.

.. code-block:: python
        
    def repeated_frame1(frame, count):
        # will hit a memory problem after about 8000 repeats
        wave = []
        for i in range(count):
            wave.append(frame)
        return wave

| Generators are used in this case to avoid memory issues.
| Use ``yield`` in the for-loop to create a generator that releases each repeat of the ``frame`` as it is needed in the calling code.
| The function, ``repeated_frame``, uses a generator (yield keyword) to create an iterable object. This means it generates each repetition on-the-fly each time you iterate over it, which is more memory-efficient than creating a large list or other collection. This is especially useful if count is a large number.

.. code-block:: python
        
    def repeated_frame(frame, count):
        # use a generator to reduce memory usage
        for i in range(count):
            yield frame

| Final code that plays a sawtooth audioframe for about 2 seconds:

.. code-block:: python
        
    from microbit import *
    import audio


    def play_rep_frame(name, frame, count):
        wave = repeated_frame(frame, count)
        while audio.is_playing():
            sleep(4)
            audio.stop()
        display.scroll(name, wait=False, delay=60)
        audio.play(wave, wait=False)
        
    def repeated_frame(frame, count):
        # use a generator to reduce memory usage
        for i in range(count):
            yield frame

    def get_sawtooth_frame():
        frame = audio.AudioFrame()
        # len = 32
        for i in range(len(frame)):
            frame[i] = int(252 - i * 8)
        return frame

    repeat_count = 100
    sawtooth_frame = get_sawtooth_frame()

    while True:
        if button_a.is_pressed():
            play_rep_frame("saw", sawtooth_frame, repeat_count)
        sleep(100)

----

Common AudioFrame structures
-----------------------------------

| Sawtooth, square and triangle audioframes are constructed and played below.

.. code-block:: python
        
    from microbit import *
    import audio


    def play_rep_frame(name, frame, count):
        wave = repeated_frame(frame, count)
        while audio.is_playing():
            sleep(4)
            audio.stop()
        display.scroll(name, wait=False, delay=60)
        audio.play(wave, wait=False)
        
    def repeated_frame(frame, count):
        # use a generator to reduce memory usage
        for i in range(count):
            yield frame

    def get_sawtooth_frame():
        frame = audio.AudioFrame()
        # len = 32
        for i in range(len(frame)):
            frame[i] = int(252 - i * 8)
        return frame


    def get_sawtooth2_frame():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            if i < len(frame) // 2:
                frame[i] = int(252 - i * 16)
            else:
                frame[i] = int(252 - (i - 16) * 16)
        return frame

    def get_square_frame():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            if i < len(frame) // 2:
                frame[i] = 252
            else:
                frame[i] = 0
        return frame
        
    def get_square2_frame():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            if i < len(frame) // 4:
                frame[i] = 252
            elif i < len(frame) * 2 // 4:
                frame[i] = 0
            elif i < len(frame) * 3 // 4:
                frame[i] = 252
            else:
                frame[i] = 0
        return frame

    def get_triangle_frame():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            if i < len(frame) // 2:
                frame[i] = i * 8
            else:
                frame[i] = 252 - (i - 16) * 8
        return frame
        
    def get_triangle2_frame():
        frame = audio.AudioFrame()
        for i in range(len(frame)):
            if i < len(frame) // 4:
                frame[i] = i * 16
            elif i < len(frame) * 2 // 4:
                frame[i] = 252 - (i - 8) * 16
            elif i < len(frame) * 3 // 4:
                frame[i] = (i - 16) * 16
            else:
                frame[i] = 252 - (i - 24) * 16
        return frame

    repeat_count = 100
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

