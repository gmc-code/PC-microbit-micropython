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
        frame[i] = int(math.sin(2 * math.pi * frequency/128 * i / length) * 124 + 128.5)
    return frame

while True:
    frequency = accelerometer.get_x()
    for frequency in range(20, 1024, 50):
        sin = sin_wave(frequency)
        show_wave(frequency, sin, duration=50)

