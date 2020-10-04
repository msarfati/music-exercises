#!/usr/bin/env python3
import itertools
import pyttsx3
import random
import sys
import time

keys = [
    'C',
    'D',
    'E',
    'F',
    'G',
    'A',
    'B',
    'C♯',
    'D♯',
    'F♯',
    'G♯',
    'A♯',
    'D♭',
    'E♭',
    'G♭',
    'A♭',
    'B♭',
]

intervals = [
    "unison",
    "minor 2nd",
    "major 2nd",
    "minor 3rd",
    "major 3rd",
    "perfect 4th",
    "tritone",  # (augmented 4th, diminished 5th)
    "perfect 5th",
    "minor 6th",
    "major 6th",
    "minor 7th",
    "major 7th",
    "octave",
]

def drill_intervals(turn, voice):
    interval = random.choice(intervals)
    drill = interval
    print(f'{turn}: {drill.capitalize()}')
    voice.say(f"{drill}.")
    voice.runAndWait()


def drill_intervals_in_key(turn, voice):
    root = random.choice(keys)
    interval = random.choice(intervals)
    drill = f'{interval.capitalize()} in key of {root}.'
    print(f'{turn}: {drill}')
    voice.say(f"{drill}.")
    voice.runAndWait()


def main():
    turn = 1
    voice = pyttsx3.init()
    while True:
        # drill_intervals(turn, voice)
        drill_intervals_in_key(turn, voice)
        if "q" == input():
            sys.exit(0)
        else:
            turn += 1
        time.sleep(0.1)


if __name__ == "__main__":
    main()
