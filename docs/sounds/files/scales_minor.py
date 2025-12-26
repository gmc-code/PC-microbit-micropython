'''
https://musictheory.pugetsound.edu/mt21c/MinorKeySignatures.html
'''
from microbit import *
import music

# Octaves start on the note C.
# sharp Minor scales; B# = C; E# = F
A_minor = {"name": "Am", "notes": "A4 B C5 D E F G A"}
E_minor = {"name": "Em", "notes": "E4 F# G A B C5 D E"}
B_minor = {"name": "Bm", "notes": "B4 C#5 D E F# G A B"}
F_sharp_minor = {"name": "F#m", "notes": "F# G# A B C#5 D E F#"}
C_sharp_minor = {"name": "C#m", "notes": "C# D# E F# G# A B C#5"}
G_sharp_minor = {"name": "G#m", "notes": "G# A# B C#5 D# E F# G#"}
D_sharp_minor = {"name": "D#m", "notes": "D# F F# G# A# B C#5 D#"}
A_sharp_minor = {"name": "A#m", "notes": "A# C5 D D# F G G# A#"}
# flat Minor scales; Cb = B; Fb = E
A_minor = {"name": "Am", "notes": "A4 B C5 D E F G A"}
D_minor = {"name": "Dm", "notes": "D4 E F G A Bb C5 D"}
G_minor = {"name": "Gm", "notes": "G4 A Bb C5 D Eb F G"}
C_minor = {"name": "Cm", "notes": "C4 D Eb F G Ab Bb C5"}
F_minor = {"name": "Fm", "notes": "F4 G Ab Bb C5 Db Eb F"}
B_flat_minor = {"name": "Bbm", "notes": "Bb C5 Db Eb F Gb Ab Bb"}
E_flat_minor = {"name": "Ebm", "notes": "Eb F Gb Ab Bb B Db5 Eb"}
A_flat_minor = {"name": "Abm", "notes": "Ab Bb B Db5 Eb E Gb Ab"}


circle_of_fifths_sharp_minor_scales = [A_minor, E_minor, B_minor, F_sharp_minor,
                                       C_sharp_minor, G_sharp_minor, D_sharp_minor, A_sharp_minor]

circle_of_fifths_flat_minor_scales = [A_minor, D_minor, G_minor, C_minor,
                                       F_minor, B_flat_minor, E_flat_minor, A_flat_minor]

music.set_tempo(ticks=8, bpm=240)
# Loop over each with 1sec between
for scale in circle_of_fifths_sharp_minor_scales:
    name = scale["name"]
    notes = scale["notes"].split(" ")
    display.scroll(name, wait=False, delay=60)
    music.play(notes, wait=True)
    sleep(1000)
# Loop over each with 1sec between
for scale in circle_of_fifths_flat_minor_scales:
    name = scale["name"]
    notes = scale["notes"].split(" ")
    display.scroll(name, wait=False, delay=60)
    music.play(notes, wait=True)
    sleep(1000)

