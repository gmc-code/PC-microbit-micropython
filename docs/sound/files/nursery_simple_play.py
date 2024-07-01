from microbit import *
import music


twinkle_twinkle = ['c4:4', 'c:4', 'g:4', 'g:4', 'a:4', 'a:4', 'g:8',
    'f:4', 'f:4', 'e:4', 'e:4', 'd:4', 'd:4', 'c:8', 'g:4', 'g:4',
    'f:4', 'f:4', 'e:4', 'e:4', 'd:8', 'g:4', 'g:4', 'f:4', 'f:4',
    'e:4', 'e:4', 'd:8', 'c:4', 'c:4', 'g:4', 'g:4', 'a:4', 'a:4',
    'g:8', 'f:4', 'f:4', 'e:4', 'e:4', 'd:4', 'd:4', 'c:8'
]
baa_baa_black_sheep = ['g4:4', 'g:4', 'd5:4', 'd:4', 'e:2', 'e:2',
    'e:2', 'e:2', 'd:4', 'r:4', 'c:4', 'c:4', 'b4:4', 'b:4',
    'a:4', 'a:4', 'g:4', 'r:4', 'd5:4', 'd:2', 'd:2', 'c:4',
    'c:4', 'b4:4', 'b:2', 'b:2', 'a:4', 'r:4', 'd5:4', 'd:2',
    'd:2', 'c:2', 'c:2', 'c:2', 'c:2', 'b4:4', 'b:2', 'b:2',
    'a:4', 'r:4', 'g:4', 'g:4', 'd5:4', 'd:4', 'e:2', 'e:2',
    'e:2', 'e:2', 'd:4', 'r:4', 'c:4', 'c:4', 'b4:4', 'b:4',
    'a:4', 'a:4', 'g:4', 'r:4'
]
row_your_boat = ['c4:12', 'c:12', 'c:9', 'd:3', 'e:12', 'e:9', 'd:3',
    'e:9', 'f:3', 'g:24', 'c5:4', 'c:4', 'c:4', 'g4:4', 'g:4',
    'g:4', 'e:4', 'e:4', 'e:4', 'c:4', 'c:4', 'c:4', 'g:9', 'f:3',
    'e:9', 'd:3', 'c:24'
]
itsy_bitsy_spider = ['c4:2', 'f:4', 'f:2', 'f:4', 'g:2', 'a:6', 'a:4',
    'a:2', 'g:4', 'f:2', 'g:4', 'a:2', 'f:6', 'r:4', 'f:2', 'a:6',
    'a:4', 'bb:2', 'c5:6', 'c:6', 'bb4:4', 'a:2', 'bb:4', 'c5:2',
    'a4:6', 'r:6', 'f:6', 'f:4', 'g:2', 'a:6', 'a:6', 'g:4',
    'f:2', 'g:4', 'a:2', 'f:6', 'c:4', 'c:2', 'f:4', 'f:2', 'f:4',
    'g:2', 'a:6', 'a:4', 'a:2', 'g:4', 'f:2', 'g:4', 'a:2', 'f:6',
    'r:4'
]
old_macdonald = ['g4:4', 'g:4', 'g:4', 'd:4', 'e:4', 'e:4', 'd:8',
    'b:4', 'b:4', 'a:4', 'a:4', 'g:12', 'd:4', 'g:4', 'g:4',
    'g:4', 'd:4', 'e:4', 'e:4', 'd:8', 'b:4', 'b:4', 'a:4', 'a:4',
    'g:12', 'd:2', 'd:2', 'g:4', 'g:4', 'g:4', 'd:2', 'd:2',
    'g:4', 'g:4', 'g:8', 'g:2', 'g:2', 'g:4', 'g:2', 'g:2', 'g:4',
    'g:2', 'g:2', 'g:2', 'g:2', 'g:4', 'g:4', 'g:4', 'g:4', 'g:4',
    'd:4', 'e:4', 'e:4', 'd:8', 'b:4', 'b:4', 'a:4', 'a:4',
    'g:16'
]
mary_had_a_little_lamb = ['b4:4', 'a:4', 'g:4', 'a:4', 'b:4', 'b:4',
    'b:8', 'a:4', 'a:4', 'a:8', 'b:4', 'd5:4', 'd:8', 'b4:4',
    'a:4', 'g:4', 'a:4', 'b:4', 'b:4', 'b:4', 'b:4', 'a:4', 'a:4',
    'b:4', 'a:4', 'g:16'
]
hickory_dickory_dock = ['f#4:2', 'g:2', 'a:2', 'g:2', 'f#:2', 'e:2',
    'f#:6', 'r:4', 'f#:2', 'f#:4', 'a:2', 'g:4', 'e:2', 'f#:6',
    'r:4', 'f#:2', 'f#:4', 'f#:2', 'a:4', 'a:2', 'g:4', 'g:2',
    'b:6', 'a:2', 'b:2', 'a:2', 'g:2', 'f#:2', 'e:2', 'd:6',
    'r:6'
]
jack_and_jill = ['e4:4', 'e:2', 'e:4', 'e:2', 'a:4', 'a:2', 'a:4',
    'a:2', 'b:4', 'b:2', 'b:4', 'b:2', 'c#5:6', 'a4:6', 'e4:4',
    'e:2', 'e:4', 'e:2', 'f#:4', 'f#:2', 'f#:4', 'f#:2', 'e:4',
    'd:2', 'c#:4', 'b3:2', 'a:6', 'a:6'
]
humpty_dumpty = ['e4:4', 'g:2', 'f:4', 'a:2', 'g:2', 'a:2', 'b:2',
    'c5:4', 'r:2', 'e4:4', 'g:2', 'f:4', 'a:2', 'g:2', 'e:2',
    'c:2', 'd:4', 'r:2', 'e:2', 'e:2', 'g:2', 'f:2', 'f:2', 'a:2',
    'g:2', 'a:2', 'b:2', 'c5:4', 'r:2', 'e:2', 'e:2', 'c:2',
    'f:2', 'f:2', 'e:2', 'd:2', 'c:2', 'b4:2', 'c5:6'
]

# dictionary with details for each song
nursery_rhymes_dict = {
    "twinkle_twinkle": {"ticks": 4, "bpm": 140, "notes": twinkle_twinkle},
    "baa_baa_black_sheep": {"ticks": 4, "bpm": 140, "notes": baa_baa_black_sheep},
    "row_your_boat": {"ticks": 12, "bpm": 140, "notes": row_your_boat},
    "itsy_bitsy_spider": {"ticks": 4, "bpm": 180, "notes": itsy_bitsy_spider},
    "old_macdonald": {"ticks": 4, "bpm": 120, "notes": old_macdonald},
    "mary_had_a_little_lamb": {"ticks": 4, "bpm": 140, "notes": mary_had_a_little_lamb},
    "hickory_dickory_dock": {"ticks": 4, "bpm": 160, "notes": hickory_dickory_dock},
    "jack_and_jill": {"ticks": 4, "bpm": 140, "notes": jack_and_jill},
    "humpty_dumpty": {"ticks": 4, "bpm": 120, "notes": humpty_dumpty},
}

nursery_rhymes_list = [
    "baa_baa_black_sheep",
    "hickory_dickory_dock",
    "humpty_dumpty",
    "itsy_bitsy_spider",
    "jack_and_jill",
    "mary_had_a_little_lamb",
    "old_macdonald",
    "row_your_boat",
    "twinkle_twinkle",
]

while True:
    # Play each nursery rhyme in the dictionary
    for rhyme_name in nursery_rhymes_list:
        rhyme_dict = nursery_rhymes_dict[rhyme_name]
        rhyme_notes_var = rhyme_dict["notes"]
        tickspeed = rhyme_dict["ticks"]
        tempo = rhyme_dict["bpm"]
        display.scroll(rhyme_name, wait=False, delay=60)
        music.set_tempo(ticks=tickspeed, bpm=tempo)
        music.play(rhyme_notes_var, wait=True)
        sleep(1000)
