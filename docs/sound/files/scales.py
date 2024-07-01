from microbit import *
import music

# Octaves start on the note C.
# major scales
C_major = {"name": "CM", "notes": "C4 D E F G A B C5", "tempo": 120}
D_major = {"name": "DM", "notes": "D4 E F# G A B C#5 D", "tempo": 120}
E_major = {"name": "EM", "notes": "E4 F# G# A B C#5 D# E", "tempo": 120}
F_major = {"name": "FM", "notes": "F4 G A Bb C5 D E F", "tempo": 120}
G_major = {"name": "GM", "notes": "G4 A B C5 D E F# G", "tempo": 120}
A_major = {"name": "AM", "notes": "A4 B C#5 D E F# G# A", "tempo": 120}
B_major = {"name": "bM", "notes": "B4 C#5 D# E F# G# A# B", "tempo": 120}
# sharp major scales
C_sharp_major = {"name": "C#M", "notes": "C# D# F F# G# A# C5 C#", "tempo": 120}
D_sharp_major = {"name": "D#M", "notes": "D# F G G# A# C5 D D#", "tempo": 120}
F_sharp_major = {"name": "F#M", "notes": "F# G# A# B C#5 D# F F#", "tempo": 120}
G_sharp_major = {"name": "G#M", "notes": "G# A# C5 C# D# F G G#", "tempo": 120}
A_sharp_major = {"name": "A#M", "notes": "A# C5 D D# F G A A#", "tempo": 120}
# flat major scales
D_flat_major = {"name": "DbM", "notes": "Db4 Eb F Gb Ab Bb C5 Db", "tempo": 120}
E_flat_major = {"name": "EbM", "notes": "Eb4 F G Ab Bb C5 D Eb", "tempo": 120}
G_flat_major = {"name": "GbM", "notes": "Gb4 Ab Bb B Db5 Eb F Gb", "tempo": 120}
A_flat_major = {"name": "AbM", "notes": "Ab4 Bb C5 Db Eb F G Ab", "tempo": 120}
B_flat_major = {"name": "BbM", "notes": "Bb4 C5 D Eb F G A Bb", "tempo": 120}

# minor scales
C_minor = {"name": "Cm", "notes": "C4 D D# F G G# A# C5", "tempo": 120}
D_minor = {"name": "Dm", "notes": "D4 E F G A A# C5 D", "tempo": 120}
E_minor = {"name": "Em", "notes": "E4 F# G A B C5 D E", "tempo": 120}
F_minor = {"name": "Fm", "notes": "F4 G G# A# C5 C# D# F", "tempo": 120}
G_minor = {"name": "Gm", "notes": "G4 A A# C5 D D# F G", "tempo": 120}
A_minor = {"name": "Am", "notes": "A4 B C5 D E F G A", "tempo": 120}
B_minor = {"name": "bm", "notes": "B4 C#5 D E F# G A B", "tempo": 120}
# sharp Minor scales
C_sharp_minor = {"name": "C#m", "notes": "C# D# E F# G# A B C#5", "tempo": 120}
D_sharp_minor = {"name": "D#m", "notes": "D# F F# G# A# B C#5 D#", "tempo": 120}
F_sharp_minor = {"name": "F#m", "notes": "F# G# A B C#5 D E F#", "tempo": 120}
G_sharp_minor = {"name": "G#m", "notes": "G# A# B C#5 D# E F# G#", "tempo": 120}
A_sharp_minor = {"name": "A#m", "notes": "A# C5 D D# F G G# A#", "tempo": 120}
# flat Minor scales
D_flat_minor = {"name": "Dbm", "notes": "Db Eb E Gb Ab A C5 Db", "tempo": 120}
E_flat_minor = {"name": "Ebm", "notes": "Eb F Gb Ab Bb B Db5 Eb", "tempo": 120}
G_flat_minor = {"name": "Gbm", "notes": "Gb Ab A B Db5 Eb E Gb", "tempo": 120}
A_flat_minor = {"name": "Abm", "notes": "Ab Bb B Db5 Eb E Gb Ab", "tempo": 120}
B_flat_minor = {"name": "Bbm", "notes": "Bb C5 Db Eb F Gb Ab Bb", "tempo": 120}

music.set_tempo(ticks=4, bpm=80)
major_scales = [C_major, D_major, E_major, F_major, G_major, A_major, B_major]
major_scales_sharp =[C_sharp_major, D_sharp_major, F_sharp_major, G_sharp_major, A_sharp_major]
major_scales_flat =[D_flat_major, E_flat_major, G_flat_major, A_flat_major, B_flat_major]
minor_scales = [C_minor, D_minor, E_minor, F_minor, G_minor, A_minor, B_minor]
minor_scales_sharp = [C_sharp_minor, D_sharp_minor, F_sharp_minor, G_sharp_minor, A_sharp_minor]
minor_scales_flat = [D_flat_minor, E_flat_minor, G_flat_minor, A_flat_minor, B_flat_minor]

all_scales = [major_scales, major_scales_sharp, major_scales_flat, minor_scales, minor_scales_sharp, minor_scales_flat]
# Loop over each
for scale_group in all_scales:
    for scale in scale_group:
        name = scale["name"]
        notes = scale["notes"].split(" ")
        tempo = scale["tempo"]
        display.scroll(name, wait=False, delay=60)
        music.set_tempo(ticks=8, bpm=tempo)
        music.play(notes, wait=True)
        sleep(1000)
