import mido

# Function to convert MIDI note number to note name
def note_number_to_name(note_number):
    notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
    octave = note_number // 12 - 1
    note = notes[note_number % 12]
    return f'{note}{octave}'

def midi_to_text(midi_path):
    mid = mido.MidiFile(midi_path)
    notes_list = []

    for i, track in enumerate(mid.tracks):
        print(f'Track {i}: {track.name}')
        for msg in track:
            if msg.type == 'note_on':
                notes_list.append(f'{note_number_to_name(msg.note)}:{msg.time}')

    print(notes_list)

midi_to_text("God_Rest_Ye_Merry_Gentlemen.mid")
