# Volume II — Analytical Mechanics

If Volume I was mechanics as Newton would recognise it (forces, trajectories,
things pushing on other things), this volume is mechanics rewritten in the
language that the rest of physics actually speaks. Lagrangians and Hamiltonians
are not just slicker bookkeeping for the same problems; they are the bridge from
"what force acts here" to "what quantity is conserved, and why," and from there
to quantum mechanics, field theory, and statistical mechanics, all of which
inherit this machinery wholesale.

We build it computationally and concretely. SymPy derives the equations of motion
from a single scalar $L = T - V$ so we can trust them, and once that crank is
built we never derive an equation of motion by hand again. Noether's theorem is
made to *earn* its conservation laws numerically, and phase space becomes
something we watch a distribution flow through, its area preserved, rather than
merely assert. Along the way the showpieces are real physics with real surprises:
the central-force orbit that refuses to close, the cross-section that cannot tell
attraction from repulsion, the rigid body that tumbles when spun about its middle
axis, the cycloid down which every bead arrives at the same instant.

This volume assumes Volume I's comfort with integrating dynamics, and it leans on
Volume 0's linear algebra the moment the normal-mode problem turns into an
eigenvalue problem. It rewards the reader with a unifying view: by the end,
"symmetry," "conservation," and "stability" stop being three separate words and
become three faces of the same computation. The Euler–Lagrange engine built in
the first notebook resurfaces in nearly every one that follows.

The central-force machinery of [§2.4](central-force.ipynb) is also where you uncover a genuine
puzzle. Any departure from the inverse-square law turns a planet's perihelion, and
Mercury carries a stubborn advance that no Newtonian accounting can remove. You meet
the mechanism here, with your own integrator; the general-relativity capstone of
Volume IV supplies the missing piece, closing a thread that began with the perfectly
closed Kepler orbit of Volume I.

The volume's last word belongs to honesty: after [§2.10](hamilton-jacobi.ipynb)
perfects the integrable picture, [§2.11](nonlinear-chaos.ipynb) shows what the
generic case actually looks like — tori breaking, period-doublings converging on
a universal constant you measure yourself, and deterministic motion that must be
described statistically. It is the hinge on which mechanics turns toward
Volume V.
