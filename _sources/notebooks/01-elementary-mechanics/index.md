# Volume I — Elementary Mechanics

Mechanics is the backbone of physics. Everyone meets it first, and almost no one
meets it last: it keeps coming back, in disguises, for the rest of one's
education. This volume takes the mechanics you already know and runs it through a
computer, which turns out to be less a matter of "checking the answer" than of
*seeing* what the closed-form solutions quietly hide. A driven pendulum slips
into chaos. An almost-Kepler orbit precesses no matter how you tune it. A
careless integrator leaks energy one timestep at a time.

We start where textbooks start: projectiles, pendulums, orbits, coupled
oscillators — but we never stop at the equation of motion. Each notebook
integrates it, plots it, animates it where motion is the point, and validates the
result against something we can independently trust. The recurring lesson is that
a numerical answer is a claim, and a claim deserves a check. The final notebook on
integrators makes that lesson explicit, showing how the *geometry* of a method,
not merely its order, decides whether your solar system survives a million orbits.

The mathematics is assumed familiar; the novelty is the computational vantage
point and the insistence on verification. If you have had a first mechanics course
and can read a differential equation without flinching, you are ready. Along the
way you will pick up the machinery the rest of the course leans on: adaptive
integrators, phase portraits, Lyapunov exponents, and the habit of asking not just
"what is the answer" but "why should I believe it."

The volume ends by cashing in every one of those habits at once: [§1.8](solar-system.ipynb)
puts the real solar system — all eight planets, NASA's masses and orbits — into the
computer, races the symplectic integrator of [§1.6](integrators.ipynb) against an
adaptive one for a thousand years, and closes with a measurement of Mercury's
perihelion precession that Volume IV will pick up where Newton leaves off.

Work the notebooks in order; each assumes the tools (and the habits!) of the ones
before it.

One thread is worth following on your own. In [§1.4](kepler-orbits.ipynb) the two-body orbit closes
exactly, its perihelion fixed; in [§2.4](../02-classical-mechanics/central-force.ipynb) the smallest departure from the
inverse-square law sets that perihelion turning, at a rate you can predict; and in the
general-relativity capstone of Volume IV, Mercury's leftover precession — the part no
Newtonian gravity explains — becomes one of relativity's first triumphs. That is a
discovery you make with your own code, not a fact handed down.
