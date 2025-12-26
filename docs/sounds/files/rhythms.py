# Import the necessary modules
from microbit import *
import music

# Define the rhythms
rhythms = {
    "3-2 Son Clave": ["C4:6", "C4:2", "R:4", "C4:4", "R:4", "C4:4", "C4:4", "R:4"],
    "3-2 Son Clave2": ["D4:4", "R:2", "A4:2", "R:4", "E4:4", "R:4", "G4:4", "A4:4", "R:4"],
    "2-3 Son Clave": ["R:4", "C4:4", "C4:4", "R:4", "C4:6", "C4:2", "R:4", "C4:4"],
    "Rumba Clave": ["C4:6", "C4:2", "R:6", "C4:2", "R:4", "C4:4", "C4:4", "R:4"],
    "Palitos sticks": ["C4:2", "C4:2", "R:2", "C4:2", "C4:2", "C4:2", "R:2", "C4:2", "C4:4", "C4:4", "C4:2", "C4:2", "R:2", "C4:2"],
    "Afro-Cuban 6/8": ["C4:3", "R:3", "C4:3", "R:3", "C4:3", "C4:3", "C4:3", "R:3", "C4:3","C4:3", "R:3", "C4:3"],
    "Shave and a Haircut, Two Bits": ["C4:4", "C4:2", "C4:2", "C4:4", "C4:4", "R:4", "C4:4", "C4:4", "R:4"],
    "Bo Diddley Beat": ["C4:3", "C4:3", "C4:2", "R:2", "C4:2", "C4:2", "R:2"],
    "Tresillo": ["D4:4", "R:2", "D4:4", "R:2", "C4:2", "R:2"],
    "Standard African Bell Pattern": ["C4:4", "C4:2", "R:2", "C4:2", "C4:2", "R:2", "C4:2", "R:2", "C4:4", "C4:2"],
    "Shuffle": ["C4:4", "C4:2", "C4:4", "C4:2", "C4:4", "C4:2", "C4:4", "C4:2"],
    "Shuffle2": ["A3:2", "A3:2", "R:2", "A3:2", "R:2", "A3:2", "R:2", "A3:2",
                "R:2", "A3:2", "R:2", "A3:2", "C4:4", "D4:4"],
    "Scotch Snap": ["C4:1", "C4:3", "C4:1", "C4:3", "C4:1", "C4:3", "C4:1", "C4:3"],
    "Scotch Snap2": ["C#4:1", "C#4:1", "R:2", "G#3:2", "G#3:1", "F#3:1", "R:2", "G#3:2"],
    "Scotch Snap3": ["C#4:1", "C#4:3", "G#3:2", "G#3:1", "F#3:3", "G#3:2"],
    "Bossa Nova": ["C4:6", "C4:6", "C4:8", "C4:6", "C4:6"],
    "Bossa Nova2": ["E4:4", "B3:4", "D4:4", "A3:2", "E4:2",
                 "R:2", "B3:4", "B3:2", "D4:4", "A3:4"],
    "5/4 Clave": ["C4:4", "R:2", "C4:4", "R:2", "C4:4", "C4:4"],
    "5/4 Clave2": ["G4:3", "G4:1", "R:2", "Bb4:2", "C5:2", "G4:2", "R:1", "G4:1", "R:2", "F4:2", "F#4:2"],
    "Football Clap": ["C4:4", "C4:4", "C4:2", "C4:2", "C4:4",
                       "C4:2", "C4:2", "C4:2", "C4:2", "R:2", "C4:2", "C4:4"], 
    "Football Clap2": ["G4:4", "G4:4", "A4:2", "A4:2", "F4:4",
                       "A4:2", "A4:2", "A4:2", "A4:2", "R:2", "C4:2", "C4:4"],
    "Shave and a hair cur: two bits": ["C4:3", "C4:2", "C4:1", "C4:3", "R:3", "C4:3", "C4:3", "R:3"]
}

# Play each rhythm
music.set_tempo(ticks=4, bpm=100)
for name, rhythm in rhythms.items():
    display.scroll(name, wait=False)
    for _ in range(4):
        music.play(rhythm)
    sleep(2000)  # Wait for 2 seconds between each rhythm
