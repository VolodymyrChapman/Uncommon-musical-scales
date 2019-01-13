Nerdy background:

Most Western music is composed of seven modes (scales; e.g. Lydian, Ionian etc.) that are a set of 8 notes from one note (let's say A) to the next A along (this end point is called the octave, from the Greek root oct-, meaning 8). 

The number of notes in between one note (again, let's say A) to the next A along(its octave) is 11 (don't trust my word for it, count yourselves using the note 'line' below!; # means sharp (the black keys on a keyboard)).

A  A#  B  C  C#  D   D#  E   F   F#   G    G#   A (the octave) 

With a little combination maths, we can calculate that there are 462 ways in which we could make the journey from a note to its octave. My question is, what do the other 455 modes sound like?
 
(Okay, some bands love to use unusual combinations (Tool, Primus etc.), and technically, about 30 modes have significant usage if we include gypsy/bebop modes - so, if you're lucky, you've heard up to 7% of the possible scales. I wouldn't stand for that)  

--------------------------------------------------------------
*For curious and scientifically-critical (CSC) sorts, here's the maths:
       n!            11!
-------------- =   ------------ = 462
(n - p)!  x p!     (11-6)! x 6!

where:
n = number of notes to choose from (this is 11, since there are 11 notes between A and the next A along)
p = number of steps (this is 6, since the first and last notes (A and the next octave note (a higher pitch A must definitely be in our scale so we can discount them from our calculation).

#also, to anyone asking why a combination and not a permutation, well, the order we choose the notes in isn't important. 
If we did do this as a permutation calculation, we would be working out the number of melodies we could make with 8 notes, which would be pretty awesome, and I invite the CSC lot to do cool projects on unusual melodies. Do it! Share it on GitHub! Be avant-garde!
--------------------------------------------------------------

The 'All combinations from A1 to A2 listed.csv' contains all 462 combinations from A1(the first A on a keyboard) to its octave (A2).

I want to structure the data into midi files (using python 3.7 then Sonic pi?) which can be shared and used to make some funky, prog rocky jam.

The first steps of the structuring stuff are in 'read all combinations.py'.

Happy jamming!

Volodymyr (Vlad) Chapman
13/01/2019
