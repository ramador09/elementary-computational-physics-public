# Volume V — Classical Statistical Mechanics

There is a moment in physics where the questions change shape. Until now we have
followed single objects: a pendulum, a charge, a particle near a black hole, each
with its own definite trajectory we could compute and plot. Statistical mechanics
asks a different kind of question. What happens when there are $10^{23}$ of them?
We can no longer track each one, and — this is the surprising part — we no longer
need to. Out of the chaos of unimaginably many particles, sharp and reliable laws
emerge: temperature, pressure, entropy, the direction of time itself. The bridge
from the microscopic to the macroscopic is built out of **counting**, and that is
where this volume begins.

## A mathematical equipping before the physics

This volume opens not with physics but with three notebooks of mathematics —
counting ([§5.1](counting.ipynb)), probability ([§5.2](probability.ipynb)), and the large-$N$ limit ([§5.3](large-n-limit.ipynb)) — and that choice
is deliberate. It is the same lesson Volume 0 taught for numerics, applied again:
when a subject leans on a distinctive mathematical toolkit, it is worth building
that toolkit first, cleanly and for its own sake, so that the physics is never
interrupted to stop and learn a technique. The mathematics of statistical mechanics
is combinatorics and probability, and they are not generic preliminaries to be
skimmed. They are the working language of the subject. A microstate count *is* a
combinatorial enumeration; an equilibrium *is* a most-probable distribution; an
average *is* an expectation value. Learn to count configurations well, and the
physics of Boltzmann, Gibbs, and Planck becomes almost a matter of reading the
counts aloud.

So think of these opening notebooks as an *Auf- und Ausrüstung* — an equipping and
an outfitting, a deliberate, unhurried pause to forge and sharpen the tools before
the campaign. They are taught entirely in the form and notation physics uses:
expectation as the quantum-mechanical $\langle A\rangle$, variance as the
uncertainty $\Delta A$, distributions as the multiplicities of physical systems.
We include only the mathematics that quantum and statistical physics actually
spend, at the depth the physics demands — and leave the apparatus of data-analysis
statistics, which belongs to a different subject, aside. This is the mathematical
language of quantum and statistical physics, taught from the ground up, and it
equips not only the rest of this volume but the quantum mechanics of Volume VI as
well.

One idea runs like a spine through the three opening notebooks, so watch for it:
the distinction between **distinguishable and indistinguishable** objects. Whether
the things you are counting carry identities or not changes the count, and that
single combinatorial fork — three different ways to drop balls into boxes — turns
out to be the entire difference between classical particles, the bosons that make
up a beam of light, and the fermions that make up matter. A reader who can count
poker hands and stars-and-bars correctly already holds, without knowing it yet, the
key to the three quantum statistics.

## Where this volume sits, and a deliberate break

The traditional German curriculum — Nolting's among them — bundles thermodynamics
and statistical mechanics with special relativity in a single fourth volume, and
then treats quantum statistics much later. We organize differently, by dependency
and computational kinship rather than by tradition. Special relativity stood alone
as Volume IV. Here, classical statistical mechanics and thermodynamics form Volume
V, built on no quantum input at all; the computationally heavy heart of the subject
— Monte Carlo, molecular dynamics, the Ising model — needs none. And the quantum
statistics that genuinely *requires* quantum mechanics — the photon gas, the
degenerate electron gas, Bose–Einstein condensation — waits for Volume VII, after
quantum mechanics has been built in Volume VI.

The cost of this choice is honest: classical and quantum statistical mechanics sit
in non-adjacent volumes, and the through-line between them must be carried by
cross-reference rather than by mere proximity. We pay it willingly, because the
reward is that each subject is met when its tools are actually in hand. The
distinguishability spine introduced in [§5.1](counting.ipynb) is exactly the thread that will be
picked up again in Volume VII, where the three counts finally become three gases.

A note on what "thermodynamics" means here. We do not present it as a separate,
axiomatic science of heat handed down from the nineteenth century. We let it
**emerge**. Entropy will appear as the logarithm of a number of microstates,
temperature as a derivative of that, the laws of thermodynamics as theorems about
overwhelmingly probable behaviour. The macroscopic world is what the microscopic
world looks like when there is too much of it to track — and counting is how we
make that precise.

After the three-notebook arsenal, the physics proper begins (kinetic theory,
ensembles, Monte Carlo, the Ising model, thermodynamic cycles) from [§5.4](microstates-entropy-temperature.ipynb) onward.
Work the notebooks in order; the arsenal is genuinely used, not decorative, and
every later notebook reaches back into it.

A closing suite extends the volume past its finale. [§5.12](kinetic-theory.ipynb)
finally puts the collisions themselves on stage — mean free paths, an
event-driven hard-disk gas, the transport coefficients, and the effusion
physics that once separated isotopes; [§5.13](random-walks.ipynb) gives
the random walk the systematic treatment its cameos deserved: from coin flips
to the diffusion equation, first passages, Pólya's drunkard, and the polymer
that swells because it may not cross itself; [§5.14](heat-engines.ipynb)
spends the whole apparatus on the subject thermodynamics was invented for —
Carnot's bound earned leg by leg, the Otto cycle in the driveway, the heat-pump
bargain, and the endoreversible square root that out-predicts Carnot on real
power plants; and [§5.15](van-der-waals.ipynb) takes the promised step beyond
the ideal gas, where two small corrections conjure a liquid: Maxwell's
equal-area coexistence, a latent heat honoring Clausius–Clapeyron, mean-field
critical exponents measured from our own dome, and the corresponding-states
vote of five real fluids.
