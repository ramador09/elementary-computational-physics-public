# Volume VIII — Electronic Structure and Many-Body Matter

Volume VII ended with quantum statistics and, in its Coda, the language of many
bodies; this volume is where that language earns its keep. Everything before it
treated the quantum mechanics of one particle, or the statistics of many that
ignore each other. But the matter on every desk — the silicon
in the machine running this page, the metal in its frame — is neither: it is
$10^{23}$ electrons interacting through the Coulomb force, and the single problem
"solve the many-electron Schrödinger equation" has consumed more computer cycles than
any other question science asks. This volume is about the ideas that make that
problem tractable, built and tested one approximation at a time.

## An exact laboratory, then honest approximations

The volume's method is its signature. Early on we construct a system small enough to
solve *exactly* — two interacting electrons on a grid — and from then on every
approximation the field actually uses is judged against exact numbers we computed
ourselves. Hartree–Fock is derived, coded, and measured against the exact answer; its
error acquires a name (correlation) and a number. Density-functional theory is built
from the Hohenberg–Kohn theorems up through a working Kohn–Sham code, and the exact
exchange-correlation potential — usually a phrase in a review article — is computed
outright by inverting the exact density. When the local-density approximation errs,
we do not report that it errs: we measure by how much, and we trace the failure to
the exact conditions it violates. The band-gap problem, the self-interaction error,
the derivative discontinuity: each is a computation here, not a warning.

## Four movements

**The many-electron problem** (8.1–8.4) states the problem honestly — the
Born–Oppenheimer separation, the wall of exponential cost, the exact laboratory —
and takes mean-field theory as far as it goes, from Hartree–Fock atoms to the
homogeneous electron gas whose exchange energy will power everything after.

**Density-functional theory** (8.5–8.8) is the reigning answer: Thomas–Fermi as the
prototype, the Hohenberg–Kohn theorems run as computations, the Kohn–Sham
construction as a working radial code, and the exact conditions — piecewise
linearity, the derivative discontinuity — that separate the exact functional from
the approximations in daily use.

**Electrons in crystals** (8.9–8.12) moves to solids: tight binding through
graphene's Dirac cones, plane waves and pseudopotentials, the empirical
pseudopotential band structures of real silicon and gallium arsenide, and the
geometry of Bloch states — Berry phases, Wannier functions, and the SSH model's
topological edge states — that a modern electronic-structure course cannot omit.

**Beyond the mean field** (8.13–8.17) is where the volume earns its subtitle: the
Hubbard model diagonalized exactly, spectral functions and the GW approximation
tested against exact answers, optical absorption and excitons, time-dependent DFT
propagated in real time against the exact laboratory, and — closing the volume and
the course's physics — the BCS theory of superconductivity, electrons doing
something no single electron can.

## Provenance

This volume follows the shape of the electronic-structure education I received at
Humboldt-Universität zu Berlin: Claudia Draxl's density-functional theory course,
and Pasquale Pavone's electronic-structure theory and theoretical solid-state
physics courses, whose problem sets I solved as a student and whose spirit — theory
stated precisely, then made concrete — these notebooks try to honour. The exercises
here are original, written for this course's computational format, but their themes
descend from those courses and from the standard literature: Martin's *Electronic
Structure*, Parr and Yang, Giustino's *Materials Modelling using Density-Functional
Theory*, and the primary papers cited notebook by notebook. The worked literature
example of the fourth movement — quasiparticle and excitonic corrections for the
photocathode materials Na₂KSb and NaK₂Sb — is my own MSc thesis (Humboldt-Universität
zu Berlin, 2019, supervised by Caterina Cocchi).

Readers who want the production-code counterpart of this volume — the same physics
driven through CP2K and Quantum ESPRESSO rather than built from scratch — will find
it in the companion course [Molecular and Materials
Modelling](https://ramador09.github.io/molecular-materials-modelling-public/); the
two are cross-referenced where they meet, most directly at the silicon band
structure.
