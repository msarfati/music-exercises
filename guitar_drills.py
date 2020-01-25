#!/usr/bin/env python3
import itertools
import pyttsx3
import random
import sys
import time

string_list = [
    'E4',
    'B3',
    'G3',
    'D3',
    'A2',
    'E2',
]

natural_notes = [
    'C',
    'D',
    'E',
    'F',
    'G',
    'A',
    'B',
]

sharp_notes = [
    'C♯',
    'D♯',
    'F♯',
    'G♯',
    'A♯',
]

flat_notes = [
    'D♭',
    'E♭',
    'G♭',
    'A♭',
    'B♭',
]

chords_major = [
    'C',
    'A',
    'G',
    'G6',
    'E',
    'D',
]

chords_minor = [
    'Em',
    'Am',
    'Dm',
]

chords_other = [
    'Asus2'
]

barre_chords = [*itertools.chain(*[
        *zip(
            map(lambda n: n + " Minor", natural_notes),
            map(lambda n: n + " Major", natural_notes)
        )
    ]
)]

# frets = itertools.chain(*[
#     # ['E4', 'F4', 'F♯4 / G♭4', 'G4', 'G♯4 / A♭4'],
#     # ['B3'],
#     # ['G3'],
#     # ['D3'],
#     # ['B3', 'C4', 'C♯4 / D♭4', 'D4', 'D♯4 / E♭4'],
#     # ['G3', 'G♯3 / A♭3', 'A3', 'A♯3 / B♭3', 'B3],
#     # ['D3', 'D♯3 / E♭3', 'E3', 'F3', 'F♯3 / G♭3'],
#     # ['A2', 'A♯2 / B♭2', 'B2', 'C3', 'C♯3 / D♭3', 'D3', 'D♯3 / E♭3', 'E3', 'F3', 'F♯3 / G♭3', 'G3', 'G♯3 / A♭3', 'A3'],
#     # ['F♯2', 'G♭2', 'G♯2', 'A♭2', ],
#     # ['E2', 'F2', 'F♯2', 'G♭2', 'G2', 'G♯2', 'A♭2', ],
#     ['E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3'],
# ])

frets = {
    'A': ['A2', 'B2', 'C3', 'D3', 'E3', 'F3', 'G3', 'A3'],
    'E': ['E2', 'F2', 'G2', 'A2', 'B2', 'C3', 'D3', 'E3'],
}

play_list = [
    # piano_o4,
    # string_list,
    natural_notes,
    sharp_notes,
    flat_notes,
    # frets,
    # chords_major,
    # chords_minor,
    # chords_other,
    # piano_say_note,
]

def random_fret(turn, voice):
    drill_root = random.choice(tuple(frets))
    drill = random.choice(frets[drill_root])
    print('{0})\t {1} on {2}'.format(turn, drill, drill_root))
    voice.say("{0}, on {1}.".format(drill, drill_root))
    voice.runAndWait()


def random_playlist(turn, voice):
    octave = ''
    drill = random.choice(play_list)
    print('{0})\t {1}'.format(turn, drill))
    voice.say(drill)
    voice.runAndWait()

def random_barre_chord(turn, voice):
    drill_root = random.choice(
        [
            'E',
            'A',
        ]
    )
    drill = random.choice(barre_chords)
    print('{0})\t {1} on {2}'.format(turn, drill, drill_root))
    voice.say("{0}, on {1}.".format(drill, drill_root))
    voice.runAndWait()



play_list = [*itertools.chain(*play_list)]

octaves = [str(i) for i in range(2,6)]  # Octaves 2 - 5

exercises = 1

def main():
    voice = pyttsx3.init()
    turn = 1
    while True:
        for i in range(exercises):
            # drill = random.choice(play_list)
            # octave = random.choice(octaves)
            # random_fret(turn, voice)
            random_barre_chord(turn, voice)
            # print('{0})\t {1}{2}'.format(turn, random.choice(play_list), random.choice(range(2, 6))))  # w/ octaves
        if "q" == input():
            sys.exit(0)
        else:
            turn += 1
        time.sleep(0.1)


if __name__ == "__main__":
    main()
