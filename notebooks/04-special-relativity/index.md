# Volume IV — Special Relativity

Volume III ended on a cliffhanger. Maxwell's equations name a single speed,
$c=1/\sqrt{\mu_0\varepsilon_0}$, with no observer attached to it, and that one
fact refuses to fit inside the comfortable Galilean world where velocities simply
add. A speed relative to what? This volume is the answer, and the answer is not a
patch. It is a rebuild of space and time themselves.

We develop special relativity from the ground up, assuming none of it. We begin
with the crisis and the two postulates Einstein extracted from it, and from those
two sentences alone everything follows: the Lorentz transformation derived (not
asserted), the geometry of spacetime and its invariant interval, the famous
paradoxes dissolved by careful computation rather than hand-waving, relativistic
dynamics and the most famous equation in physics, and finally a first taste of
what happens when spacetime itself bends. The mathematics is light, mostly
algebra and a little linear algebra from Volume 0; the difficulty is entirely
conceptual, the steady refusal to let go of intuitions that turn out to be
provincial. We lean on the computer to make the abstract concrete: a number for
the fringe shift that was never seen, a worldline that maps to a worldline, a
clock that visibly runs slow.

A word on where this volume sits. The classic German curriculum, Nolting's
included, pairs special relativity with thermodynamics in a single fourth volume.
We deliberately break that pairing. Special relativity and thermodynamics share a
cover there for historical and pedagogical convenience, not because they belong
together; their methods, their questions, and their computational character are
almost entirely disjoint. So special relativity stands alone here as Volume IV,
and the thermal and statistical physics moves to where its tools are actually
forged and spent, in the statistical-mechanics volumes (V and VII). The ordering
of this course is by dependency and by computational kinship, not by tradition,
and this is one of the places that principle shows.

One cross-reference deserves flagging up front. [§3.12](../03-electrodynamics/relativistic-maxwell.ipynb), the capstone of
Volume III, *used* the machinery this volume *builds*: it rewrote electrodynamics
in the language of four-vectors and the field tensor, taking the Lorentz
transformation as given. The relationship is inverted on purpose. There we
assumed relativity to reveal that electricity and magnetism are one object; here
we earn relativity from physical principles. If you are meeting relativity for the
first time, the natural path is to read this volume's notebooks ([§4.1](crisis-and-postulates.ipynb)
through [§4.5](four-momentum-energy.ipynb)) first and then return to
[§3.12](../03-electrodynamics/relativistic-maxwell.ipynb), which develops just enough relativity inline to
stand on its own but is far richer once the full story is in hand.

The capstone also returns to a discrepancy you uncovered long before. In Volumes I
and II you found, with your own code, that an isolated Kepler orbit closes exactly
while any departure from the inverse-square law makes it precess — and that Mercury
carries a leftover advance no Newtonian effect explains. The general-relativity
capstone ([§4.8](gr-capstone.ipynb)) computes that residual from the curvature of spacetime and lands on
the observed $43''$ per century, closing a thread that runs the length of the course.

Work the notebooks in order. The volume is short by the standards of this course
and unusually self-contained, but each notebook leans on the one before, and the
whole point of relativity is that it is a single idea followed without flinching
to its conclusions.
