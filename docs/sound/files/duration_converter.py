row_your_boat = [
    'c4:4', 'c4:4', 'c4:3', 'd4:1', 'e4:4',
    'e4:3', 'd4:1', 'e4:3', 'f4:1', 'g4:8',
    'c5:1.34', 'c5:1.34', 'c5:1.34', 'g4:1.34', 'g4:1.34', 'g4:1.34',
    'e4:1.34', 'e4:1.34', 'e4:1.34', 'c4:1.34', 'c4:1.34', 'c4:1.34',
    'g4:3', 'f4:1', 'e4:3', 'd4:1', 'c4:8'
]

# Adjust durations for triplets (1.3 beats)
for i in range(len(row_your_boat)):
    note, dur = row_your_boat[i].split(':')
    new_dur = int(float(dur) * 3)
    row_your_boat[i] = f"{note}:{new_dur}"

print(row_your_boat)