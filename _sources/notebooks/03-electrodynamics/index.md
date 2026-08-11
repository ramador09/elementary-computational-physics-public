# Volume III — Classical Electrodynamics

Electrodynamics is the first great unification in physics, and it is worth
pausing on how unlikely that was. Electricity and magnetism arrived as separate
curiosities: amber that attracts dust, lodestones that point north. Light was a
third thing entirely, the business of optics. That all three are the same
phenomenon, governed by four equations that fit on a coffee mug, is not obvious
from the outside. This volume is the story of how they fold into one.

We build it in the order the physics discloses itself. We begin with a single
charge and the inverse-square law, which looks reassuringly like the gravity of
Volume I (it is no accident that they share a form). From there the field acquires
a potential, the potential obeys Laplace's and Poisson's equations, and we meet
the computational heart of the volume: solving those equations on a grid, by
relaxation, when no closed form exists. Then currents, magnetic fields, induction,
and the moment where Maxwell adds one term for consistency and the equations
suddenly predict light. By the end we reach the capstone, where the whole edifice
is rewritten in a single relativistic object and electricity and magnetism are
revealed as two views of one field, seen from different frames.

There is a name for what we are really learning here. In Landau and Lifshitz's
framing this whole subject is *the classical theory of fields*, and
electrodynamics is its forerunning and richest classical example: a physics not of
particles pulling on one another across a distance, but of a field that fills space
and obeys *local* equations at every point. The volume assembles those equations
one at a time, beginning with the very first, $\nabla\cdot\mathbf E=\rho/\varepsilon_0$
([§3.3](gauss-law.ipynb)), which ties the field to its source right where the source sits.
They accumulate until they close into Maxwell's four, and the relativistic capstone
then shows them to be a single law in spacetime. Keeping that arc in view, each new
field equation a local law, the set of them the real content, is the best way to
read the volume.

Computationally this volume asks something new of us. Mechanics was the world of
the initial-value problem: give the state now, integrate forward. Electrostatics is
the world of the boundary-value problem: fix the conditions on the walls, and solve
for the field that fills the room. These need different tools, and we build them as
they arise: numerical vector calculus introduced alongside the physics that needs
it, relaxation solvers for the field equations, special functions for the
symmetries that admit them, and the linear algebra and Fourier methods of Volume 0
fulfilled at last. The driven RLC circuit even turns out to be the damped, driven
oscillator of [§1.2](../01-elementary-mechanics/damped-driven-pendulum.ipynb) wearing different clothes (the same resonance, relabelled!).

We assume the vector calculus and the first encounter with E&M that a German
second- or third-year has already had. The mathematics, as ever, is familiar; the
novelty is the computational vantage point and the insistence that every field we
draw be one we actually solved for. Work the notebooks in order: the volume is long
by design, because electrodynamics rewards being seen whole rather than in pieces.

One note on the capstone. [§3.12](relativistic-maxwell.ipynb) belongs here as the summit of electrodynamics,
but it leans on special relativity. If you are meeting relativity for the first time,
you may prefer to read Volume IV's special-relativity notebooks ([§4.1](../04-special-relativity/crisis-and-postulates.ipynb)–[§4.5](../04-special-relativity/four-momentum-energy.ipynb)) first and
return to [§3.12](relativistic-maxwell.ipynb) afterwards; we develop just enough relativity inline for it to stand on
its own, but the fuller story is in Volume IV.

The volume does not stop at the capstone. What follows is longer than a coda and
is best read as a second half, in which the fields we have built are put inside
matter and the methods we have been quoting are finally derived.

The first pair lives where most fields actually do: inside matter.
[§3.13](fields-in-matter.ipynb) works both halves of the story — bound charges
summed into the polarized sphere's exact interior field, a permittivity-jump
relaxation solver benchmarked against the dielectric sphere, Clausius–Mossotti
pricing argon's permittivity from one atom, the magnetized cylinder unmasked as
a solenoid, and the mean-field hysteresis that turns response into memory.
The second takes the waves of [§3.8](maxwell-waves.ipynb) to the optics bench:
[§3.14](wave-optics.ipynb) computes diffraction as the Fourier transform it is —
Young's fringes and the Airy resolution limit matched to their closed forms, the
Fresnel number's arc from shadow to far field, the Arago spot that decided the
wave theory in 1818, and a lens revealed as an analog Fourier transformer.

Then the medium itself becomes the subject, in the order the physics discloses
it. [§3.15](waves-in-media.ipynb) asks what a wave does once it is *inside*
something and what happens where two somethings meet: the driven oscillator of
[§1.2](../01-elementary-mechanics/damped-driven-pendulum.ipynb) relocated inside
an atom and summed into a permittivity, absorption and the skin depth, the plasma
frequency that decides why metals shine and why the ionosphere returns AM but not
FM, and then Snell, Fresnel, Brewster and total internal reflection derived rather
than quoted. [§3.16](anisotropic-dielectrics.ipynb) then removes the assumption
almost every earlier notebook made without saying so — that a medium responds the
same way in every direction. The permittivity becomes a tensor in its own right, a
thing defined by how it transforms; the electric displacement stops being parallel
to the field, exactly as angular momentum stopped being parallel to angular
velocity in [§2.6](../02-classical-mechanics/rigid-body.ipynb); and Neumann's
principle turns crystal symmetry into a component count, which makes the optical
isotropy of cubic crystals a theorem rather than a coincidence.
[§3.17](crystal-optics.ipynb) then sends light through the crystal and watches
what that costs: two waves for every direction, an ordinary index that ignores
direction and an extraordinary one that does not, a ray that walks away from its
own wave normal — which is the non-parallel **D** and **E** of the previous
notebook, seen on an optical bench — and the wave plates that all of this makes
possible.

The volume ends by going back for something it left behind. Three notebooks —
[§3.4](laplace-poisson.ipynb), [§3.5](multipole-expansion.ipynb) and
[§3.9](waveguides-cavities.ipynb) — graded their solvers against series they
quoted rather than derived, and each said so at the time.
[§3.18](separation-of-variables.ipynb) derives them, and the separation
constant turns out to be an eigenvalue of a Sturm–Liouville operator: one piece of
mathematics that, run three times without modification, produces the box series in
Cartesian coordinates, the multipole moments in spherical ones, and the cavity
frequencies from three per-axis problems whose constants simply add. It closes
where the method fails, on the Gibbs overshoot that will not go away.
