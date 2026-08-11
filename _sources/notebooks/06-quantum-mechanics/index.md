# Volume VI — Quantum Mechanics

Classical physics, in all its forms, rested on a single quiet assumption: that the
world has a definite state, and physics is the work of finding it. A pendulum has a
definite position and momentum; a charge sits at a definite point; a gas of
$10^{23}$ molecules has a definite microstate even when we can only ever track its
statistics. Quantum mechanics breaks with this completely. It does not say we are
*ignorant* of the underlying state — it says there is no such state to be ignorant
of. In its place stands a new kind of object, a vector of complex numbers, and the
only questions we are permitted to ask of it return **probabilities**, computed from
**amplitudes** that add, and interfere, and become definite only when measured. The
world, at its base, is not made of definite things. It is made of amplitudes.

The single idea on which the entire theory rests is this: a quantum state is a unit
vector — more precisely a **ray**, since an overall phase carries no physics — in a
complex inner-product space, a **Hilbert space**. The inner product of two states is
a complex number, a probability *amplitude*, and the square of its magnitude is a
probability. That the scalars are **complex** rather than real is not a bookkeeping
convenience; it is the whole source of interference, the one phenomenon with no
classical shadow. Learn to compute in the complex Hilbert space and you can compute,
quite literally, all of quantum mechanics — because every postulate of the theory is
a statement of linear algebra on that space.

## A mathematical arsenal before the physics

So this volume opens, as Volumes 0 and V did before it, not with physics but with
its mathematics. The opening movement — its **Movement 0** — builds the complex
linear algebra the theory is written in, cleanly and for its own sake: complex
vector spaces and inner products ([§6.1](complex-vector-spaces.ipynb)), the operators that act on them and the
spectral theorem that diagonalizes them ([§6.2](operators-spectral-theorem.ipynb)), and the Dirac notation that makes the
whole apparatus weightless ([§6.3](dirac-notation-spectral-decomposition.ipynb)). This is the same lesson, taught now a third time.
When a subject leans on a distinctive toolkit, forge the toolkit first, so that the
physics is never interrupted to stop and learn a technique. The mathematics of
quantum mechanics is linear algebra over the complex numbers, and it is no generic
preliminary to be skimmed: an observable *is* a Hermitian operator, a measurement
outcome *is* an eigenvalue, a symmetry *is* a unitary transformation, and the
dynamics *is* a one-parameter group of them. Master the arsenal, and the postulates
read almost like a translation.

One distinction runs through the whole volume like a spine, and it appears already
in the first notebook: the difference between a **global** phase, which is
physically meaningless, and a **relative** phase within a superposition, which is
everything. It is why physical states are rays and not vectors, why interference
exists at all, and — for a single qubit — the difference between the radius of the
Bloch sphere and the point upon it. A reader who feels that distinction in [§6.1](complex-vector-spaces.ipynb)
already holds the key to most of what makes quantum mechanics strange.

## Where this volume sits

Quantum mechanics inherits directly from the mathematical language built in Volume
V. The expectation value $\langle A\rangle$, the uncertainty $\Delta A$, the
insistence that probabilities sum to one — these were forged there, deliberately in
the form and notation that quantum physics uses, precisely so that they would be in
hand here. We organize the curriculum by dependency and computational kinship rather
than by tradition. Classical statistical mechanics stood alone as Volume V, built on
no quantum input at all. Quantum mechanics is built here, in Volume VI, on the
complex Hilbert space. And the quantum statistics that genuinely *requires* both —
the photon gas, the degenerate electron gas, Bose–Einstein condensation — waits for
Volume VII, when the two halves are finally brought together.

After Movement 0 has laid the arena, the physics proper begins: the postulates and
the Born rule, where an amplitude squared becomes a measurement probability; time
evolution and the Schrödinger equation; the uncertainty principle, grown from an
inequality met in the very first notebook; and the exactly-solvable systems —
the well, the barrier, the oscillator, the hydrogen atom — whose spectra and states
we will compute rather than merely quote. Work the notebooks in order; the arsenal
is genuinely used, not decorative, and every later notebook computes in the space
built here.

Two codas stand after the capstone. Volume III introduced the vector potential as
bookkeeping and promised, three times over, that quantum mechanics would make its
gauge structure physical. [§6.28](aharonov-bohm.ipynb) keeps that promise: the
Aharonov–Bohm effect, the flux-threaded ring, and the $h/2e$ quantum of the
superconducting ring, computed from the machinery this volume built. And
[§6.29](scattering-3d.ipynb) takes scattering into three dimensions, where the
experiments that mapped the subatomic world actually live: partial waves and
phase shifts, the optical theorem verified to eight decimals, Born's
approximation caught working and failing, a Breit–Wigner resonance, and the
quantum transparency of Ramsauer's argon.
