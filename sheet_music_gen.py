#!/usr/bin/env python3
import itertools
import random
import sys
import time

notes = [
    'c',
    'd',
    'e',
    'f',
    'g',
    'a',
    'b',
]

accidentals = [
    '',
    '',
    '',
    '',
    '',
    'is',  # sharp
    'es',  # flat
]

time_value = [
    # '1',
    # '2',
    # '3',
    '4',
]

treble_octaves = [
    "'",
    "''",
    # "'''",
]

bass_octaves = [
    ",",
    "",
]

def gen_bar(clef='treble'):
    return " ".join([make_note(clef) for i in range(4)]) + " | "


def make_note(clef='treble'):
    note = random.choice(notes)
    accidental = random.choice(accidentals)
    note_len = random.choice(time_value)

    if clef == 'bass':
        octave = random.choice(bass_octaves)
    else:
        octave = random.choice(treble_octaves)

    # print(octave)
    # print(type(octave))
    return note + accidental + octave + note_len


def gen_staff(clef='treble', bars=40):
    return "".join([gen_bar(clef) for i in range(bars + 1)])


def main():

    template_path = './lilypond_grandstaff_template.ly'
    template = ''

    with open(template_path, 'r+') as f_template:
        template = f_template.read()
        f_template.close()

    template = template.replace("%REPLACE_TREBLE1%", gen_staff('treble'))
    template = template.replace("%REPLACE_BASS1%", gen_staff('bass'))

    filename = "drill_" + str(time.time()).replace('.', '_')
    template = template.replace("%REPLACE_TITLE%", filename)

    ly_out_path = filename + ".ly"
    with open(ly_out_path, "w+") as ly_out:
        ly_out.write(template)
        ly_out.close()
    print(ly_out_path)

if __name__ == "__main__":
    main()
