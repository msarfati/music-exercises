#!/bin/bash -x
# Asssumes on MacOS that `lilypond` is aliased to exec /Applications/LilyPond.app/Contents/Resources/bin/lilypond "$@"
filename=$(./sheet_music_gen.py)
lilypond $filename