#!/usr/bin/env python3
import itertools
import pyttsx3
import random
import sys
import time

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

accidentals = [
    '♯',
    '♭',
    '♮',
    'double ♭',  # 𝄫
    'double 𝄪',  # 𝄪
]

interval_state = [
    'augmented',
    'perfect',
    'major',
    'minor',
    'diminished',
]

scale_degrees = {
    'I': ['1st', 'unison', 'tonic'],
    'II': ['2nd', 'supertonic'],
    'III': ['3rd', 'mediant'],
    'IV': ['4th', 'subdominant'],
    'V': ['5th', 'dominant'],
    'VI': ['6th', 'submediant'],
    'VII': ['7th', 'leading note', 'subtonic'],
    'VIII': ['8th', 'octave', 'octave-tonic'],
}



def major_or_perfect(turn, voice):
    interval = random.choice(tuple(scale_degrees))
    interval_name = random.choice(scale_degrees[interval])
    print('{0})\t {1}'.format(turn, interval))
    voice.say("{0}".format(interval_name))
    voice.runAndWait()


exercises = 1

def main():
    voice = pyttsx3.init()
    turn = 1
    while True:
        for i in range(exercises):
            major_or_minor(turn, voice)
        if "q" == input():
            sys.exit(0)
        else:
            turn += 1
        time.sleep(0.1)


if __name__ == "__main__":
    main()
