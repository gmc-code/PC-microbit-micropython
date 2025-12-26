from microbit import *
import music

music.set_tempo(ticks=8, bpm=240)
triads = [["C4", "E4", "G4"], ["D4", "F4", "A4"], ["E4", "G4", "B4"], 
          ["F4", "A4", "C5"], ["G4", "B4", "D5"], ["A4", "C5", "E5"], ["B4", "D5", "F5"]]

while True:
    if button_a.was_pressed():
        for triad in triads:
            music.play(triad, wait=True)
            sleep(100)
        sleep(500)
    elif button_b.was_pressed():
        for triad in triads:
            music.play(triad[::-1], wait=True)
            sleep(100)
        sleep(500)

