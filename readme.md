# V plotter with spool kinematics

Python code for inverse and forward kinematics.

![calculationdiagram](spool.PNG "Calculation Diagram")

## Legend

Points (brown)
- `C` center of circle (spool)
- `P` plotting point
- `T` tangent point, line to circle

Lengths (blue)
- `r` radius of circle
- `c` length of line in contact with circle
- `s` length of line from tangent to point
- `h` distance between plotting point and circle center

Angles (green)
- `a` section of circle with line contact
- `b` interior angle of right triangle
- `n` part angle of `b` above horizontal
- `m` part angle of `b` below horizontal

## Description

Length of line is measured from the top of the spool, consisting
of sections `c` in contact with the spool, and section `s` running
to point `P`.

Inverse kinematic calculation: given point to plot `P` find length
of line.

(later, todo) Forward kinematic calculation: given two lengths of line, find
plotting point `P`.

## Tests

Diagram of test cases in test.txt. Values in the test are in
agreement with 'Analyze, Length' measurements in the Rhino.

![testsdiagram](tests.PNG "Tests Diagram")

Test #3 is interesting in that it shows that the top of the spool is an
arbitrary line length measurement starting point.
The effect of the calculation is as if the length of the line
not touching the spool is added, and the length of the line which
would touch if wrapped around is subtracted.