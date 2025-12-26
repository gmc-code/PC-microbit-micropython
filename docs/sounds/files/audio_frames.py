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


# Generate a waveform that goes from one wave to another wave, reasonably smoothly.
def generate_frames(wave_1, wave_2, frame_count=10):
    frames = []
    for i in range(frame_count):
        frame = audio.AudioFrame()
        for j in range(len(wave_1)):
            frame[j] = (wave_1[j] * (frame_count - i) + wave_2[j] * i) // frame_count
        frames.append(frame)
    return frames

#####

def sin_wave():
    frame = audio.AudioFrame()
    for i in range(len(frame)):
        frame[i] = int(math.sin(math.pi * i / 16) * 124 + 128.5)
    return frame


def tri_wave():
    frame = audio.AudioFrame()
    # QUARTER = 8; len(frame) = 32
    QUARTER = len(frame) // 4
    for i in range(QUARTER):
        frame[i] = i * 15
        frame[i + QUARTER] = 248 - i * 15
        frame[i + QUARTER * 2] = 128 - i * 15
        frame[i + QUARTER * 3] = i * 15 + 8
    return frame


def sq_wave():
    frame = audio.AudioFrame()
    # HALF = 16; len(frame) = 32
    HALF = len(frame) // 2
    for i in range(HALF):
        frame[i] = 8
        frame[i + HALF] = 248
    return frame


def saw_wave():
    frame = audio.AudioFrame()
    for i in range(len(frame)):
        frame[i] = 252 - i * 8
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
