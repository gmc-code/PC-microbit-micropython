'''
https://musictheory.pugetsound.edu/mt21c/MajorKeySignatures.html
'''
from microbit import *
import music


# Octaves start on the note C.
# major scales
# sharp major scales; B# = C; E# = F
C_major = {"name": "C", "notes": "C4 D E F G A B C5"}
G_major = {"name": "G", "notes": "G4 A B C5 D E F# G"}
D_major = {"name": "D", "notes": "D4 E F# G A B C#5 D"}
A_major = {"name": "A", "notes": "A4 B C#5 D E F# G# A"}
E_major = {"name": "E", "notes": "E4 F# G# A B C#5 D# E"}
B_major = {"name": "B", "notes": "B4 C#5 D# E F# G# A# B"}
F_sharp_major = {"name": "F#", "notes": "F# G# A# B C#5 D# F F#"}
C_sharp_major = {"name": "C#", "notes": "C# D# F F# G# A# C5 C#"}

# flat major scales; Cb = B; Fb = E
F_major = {"name": "FM", "notes": "F4 G A Bb C5 D E F"}
B_flat_major = {"name": "Bb", "notes": "Bb4 C5 D Eb F G A Bb"}
E_flat_major = {"name": "Eb", "notes": "Eb4 F G Ab Bb C5 D Eb"}
A_flat_major = {"name": "Ab", "notes": "Ab4 Bb C5 Db Eb F G Ab"}
D_flat_major = {"name": "Db", "notes": "Db4 Eb F Gb Ab Bb C5 Db"}
G_flat_major = {"name": "Gb", "notes": "Gb4 Ab Bb B Db5 Eb F Gb"}
C_flat_major = {"name": "Cb", "notes": "B3 Db4 Eb E Gb Ab Bb B"}

circle_of_fifths_sharp_scales = [C_major, G_major, D_major, A_major, 
                                 E_major, B_major, F_sharp_major, C_sharp_major]

circle_of_fifths_flat_scales = [C_major, F_major, B_flat_major, E_flat_major,
                                 A_flat_major, D_flat_major, G_flat_major, C_flat_major]


music.set_tempo(ticks=8, bpm=240)
# Loop over each with 1sec between
for scale in circle_of_fifths_sharp_scales:
    name = scale["name"]
    notes = scale["notes"].split(" ")
    display.scroll(name, wait=False, delay=60)
    music.play(notes, wait=True)
    sleep(1000)
# Loop over each with 1sec between
for scale in circle_of_fifths_flat_scales:
    name = scale["name"]
    notes = scale["notes"].split(" ")
    display.scroll(name, wait=False, delay=60)
    music.play(notes, wait=True)
    sleep(1000)
