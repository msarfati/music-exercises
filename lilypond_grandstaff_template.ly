\version "2.18.2"
\header {
    title = "%REPLACE_TITLE%"
    composer = "Michael Sarfati"
}
#(set-global-staff-size 25)
\absolute {
    \override Score.SpacingSpanner.strict-note-spacing = ##t
    \set Score.proportionalNotationDuration = #(ly:make-moment 1/16)
    <<
        \new Staff { \clef "treble" %REPLACE_TREBLE%  }
        \new Staff { \clef "bass" %REPLACE_BASS% }
    >>
}
