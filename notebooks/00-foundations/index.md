# Volume 0 — Mathematical & Computational Foundations

Everything has to start somewhere. Before we can
trust a single simulated orbit or a single quantum energy level, we need the
instruments that produce them, and an honest measure of what those instruments
can and cannot do. In this spirit, the present volume works through floating-point reality,
root-finding, numerical integration and differentiation, linear systems and the
singular value decomposition, the fast Fourier transform, and the ODE solvers
that drive everything afterward. It is familiar mathematics seen from an
unfamiliar angle: not the theorems, which we have met probably *ad nauseam* already, but rather *what it costs to
actually compute with them*, which is to say what each idea breaks into, rounds
off to, or quietly reveals once it runs on a real machine.

There is a single thread holding the volume together. Every later
energy-conservation check, every adaptive integrator, every normal-mode
diagonalisation, and every spectrum you will read stands on something built here:
the tolerance that replaces `==`, the factorization that replaces the inverse,
the convergence order that decides ten samples from ten thousand. Lay the
foundation well and the physics volumes spend it without ever having to stop and
re-derive it.

The material is genuinely second- and third-year ground, and it is pitched to a
reader who already knows it as mathematics — a peer, not a pupil. The novelty is
purely the computational vantage point and the insistence on verification: a new
look at the familiar, in which a quantity you can write in closed form becomes a
question of how faithfully a finite machine can return it.

Each notebook also seeks to be forward thinking, with references to deferred treatments of the course material
so indicated. The root-finder built here is the engine for the transcendental energy levels of
quantum mechanics; the eigenproblem becomes every normal mode in Volumes I and
II; the SVD's low-rank truncation is, almost verbatim, the tensor-network
compression of many-body physics; and the ODE solvers are simply *how* all of
mechanics and electrodynamics get integrated. Work the notebooks in order; later
volumes assume the numerical habits (and the tolerance-based validation
discipline!) established here.

One body of mathematics is deliberately absent here: probability and statistics. They
are not generic preliminaries but the working language of statistical mechanics, and we
develop them there, in the statistical-mechanics volumes, from simple combinatorics
through the counting of microstates, at the depth that subject demands. This is the same
arsenal-first principle the volume applies to numerics: build each toolkit where it is
used, not before.

A confession from my side. "Mathematical and Computational Foundations"
sounds reassuringly gentle: the sort of warm-up chapter you might skim on the way
to the real physics. A more honest title would be something like "Elements of
Numerical Analysis and Linear Algebra," because that is, in fact, what this
volume is: floating-point error analysis, the conditioning of linear systems,
the singular value decomposition, the convergence orders of quadrature and
Runge–Kutta schemes, the stability of stiff solvers. None of that is what one
usually files under "foundations" in the soothing sense of the word, and indeed there are bound to be
some topics in the present Volume, from which most anyone could hopefully learn something.

I have kept the gentler name on purpose. The material here genuinely is
foundational (everything in the later volumes stands on it), and I would rather
not present this Volume with a title that reads like a graduate numerics qualifier
before one has actually seen directly how these tools pay for themselves. So: if the
name undersells the contents, consider it a friendly deception. The contents
will speak for themselves soon enough.
