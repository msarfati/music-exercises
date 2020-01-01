#!/usr/bin/env python3
import itertools
import random
import sys
import time

string_list = [
    'e string',
    'B string',
    'G string',
    'D string',
    'A string',
    'E string',
]

natural_notes = [
    'C note',
    'D note',
    'E note',
    'F note',
    'G note',
    'A note',
    'B note',
]

accidental_notes = [
    'C# note',
    'D# note',
    'E# note',
    'F# note',
    'G# note',
    'A# note',
    'B# note',
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

frets_1to3 = itertools.chain(*[
    ['E4', 'F4', 'F♯4 / G♭4', 'G4'],
    ['B3', 'C4', 'C♯4 / D♭4', 'D4'],
    ['G3', 'G♯3 / A♭3', 'A3', 'A♯3 / B♭3'],
    ['D3', 'D♯3 / E♭3', 'E3', 'F3'],
    ['A2', 'A♯2 / B♭2', 'B2', 'C3'],
    ['E2', 'F2', 'F♯2 / G♭2', 'G2'],
])

play_list = [
    # string_list,
    # natural_notes,
    # accidental_notes,
    frets_1to3,
    # chords_major,
    # chords_minor,
    # chords_other,
]

play_list = [*itertools.chain(*play_list)]

exercises = 4

def main():
    turn = 1
    while True:
        for i in range(exercises):
            print('{0})\t {1}'.format(turn, random.choice(play_list)))
        if "q" == input():
            sys.exit(0)
        else:
            turn += 1
        time.sleep(0.1)


if __name__ == "__main__":
    main()
