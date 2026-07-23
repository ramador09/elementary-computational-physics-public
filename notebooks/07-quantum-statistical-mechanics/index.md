# Volume VII — Quantum Statistical Mechanics

This is the volume where the two halves of the course finally meet. Volume V built
statistical mechanics on a deliberately classical foundation: count the microstates,
weight them by $e^{-\beta E}$, and let the large numbers do the rest. Volume VI built
quantum mechanics: the state is a ray in a complex Hilbert space, the observables are
Hermitian operators, and the world hands back eigenvalues with probabilities.
Quantum statistical mechanics is what happens when the counting of Volume V is done
over the states of Volume VI — when the "microstate" being weighted is an energy
eigenstate, the sum over configurations becomes a trace, and the density matrix of
6.26 acquires the temperature it was always waiting for:

$$
\rho \;=\; \frac{e^{-\beta H}}{Z},\qquad Z=\operatorname{Tr}\,e^{-\beta H}.
$$

## The promises this volume keeps

Volume V and Volume VI both made promises that only this volume can keep,
and keeping them is the volume's plot. The three occupancy statistics of 5.1 —
Maxwell–Boltzmann, Bose–Einstein, Fermi–Dirac — were counted there as combinatorics
and left waiting for physics. The Gibbs $1/N!$ of 5.6, inserted by hand to rescue
extensivity, and the constant $h$ in the phase-space measure, inserted to make the
entropy dimensionless, are both quantum imports: indistinguishability and $\hbar$ are
facts about quantum states, not classical conveniences, and the Sackur–Tetrode
entropy becomes a derived result rather than a fitted one. The freezing-out of
rotational and vibrational modes, flagged in Volume V as an unexplained failure of
equipartition, is the discreteness of quantum spectra meeting $k_BT$. And beyond the
promises lie the volume's own landmarks: the photon gas and the Planck law, the
degenerate electron gas that holds up white dwarfs and sets the properties of every
metal, and Bose–Einstein condensation — a phase transition driven by counting alone.

## A mathematical arsenal before the physics

Like Volumes 0, V, and VI before it, this volume opens with its mathematics — a
**Movement 0** that forges the toolkit once, properly, so the physics is never
interrupted to learn a technique. Here the toolkit is the analysis of functions of a
complex variable, and it earns its place twice over. The integrals that carry all of
quantum statistics — the Bose and Fermi integrals, the Sommerfeld expansion, the
Matsubara frequency sums — live naturally in the complex plane, wrapped around branch
cuts and poles. And the response of matter to probes obeys relations
(Kramers–Kronig) that are nothing but theorems about analytic functions, with
causality as the hypothesis.

The movement runs in three notebooks. **7.1** builds the core machinery — analyticity
and the Cauchy–Riemann equations, branch cuts, contour integration, Cauchy's theorem
and integral formula, Laurent series, poles, and the residue theorem — and puts it to work
immediately on the classic families of real integrals. **7.2** points the machine at
physics: principal values and Sokhotski–Plemelj, the Kramers–Kronig relations,
Matsubara sums, and the method of steepest descent (which re-derives, at last, the
Stirling formula that Volume V leaned on). **7.3** assembles the statistical toolkit
itself: densities of states, the Gamma and zeta functions and the polylogarithms, the
Bose and Fermi integrals, and the Sommerfeld expansion.

One editorial note, recorded deliberately. Elsewhere the course teaches a complete
*minimal* curriculum — each tool built exactly when needed and to the depth needed.
This movement is the exception: complex analysis is presented in full, Cauchy–Riemann
equations and all, because the subject is too important — to physics and to the
mathematical education of anyone doing physics — to be issued on a need-to-know
basis. It is a detour that is not one.

## Where this volume sits

Volume VII presumes both of its parents: the ensemble machinery, Legendre structure,
and large-$N$ instincts of Volume V, and the Hilbert-space mechanics — spectra,
traces, density matrices — of Volume VI. It inherits their shared probability
language ($\langle A\rangle$, $\Delta A$, $\sum p = 1$) that Volume V forged
deliberately in the form quantum mechanics would need. What it returns is the physics
of matter in bulk as it actually is: quantum, thermal, and calculable.

## Coda (optional): The Many-Body Gateway

After the arc closes with 7.22, three notebooks (7.23–7.25) sit outside it: second
quantization, Green's functions, and linear response. Nothing in this volume depends
on them; everything in them depends on what the volume built. They were once the
course's optional gateway — they are now its doorway: Volume VIII, which follows,
speaks their language throughout, and its many-body movement (8.13–8.17) assumes
them outright.
