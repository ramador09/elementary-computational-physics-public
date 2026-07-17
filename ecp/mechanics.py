"""Reusable analytical-mechanics helpers for Volume II.

These functions were developed and reused across the Volume II notebooks
(Lagrangian/Hamiltonian dynamics, central forces, small oscillations) and have
stable interfaces, so they live here and are imported rather than redefined in
each notebook, the same way :mod:`ecp.validate` and :mod:`ecp.draw` work.

    from ecp import mechanics

Symbolic helpers use a canonical time symbol :data:`t`. A notebook's own
``sp.symbols("t")`` is the *same* SymPy symbol (equality is by name), so
coordinates built in a notebook differentiate correctly here with no special
handling.
"""

import numpy as np
import sympy as sp
from scipy.linalg import eigh
from scipy.optimize import brentq

# Canonical time symbol. ``sp.symbols("t")`` in a notebook compares equal to
# this, so Functions of t built anywhere differentiate consistently.
t = sp.symbols("t")


# --------------------------------------------------------------------------- #
# Symbolic Lagrangian / Hamiltonian mechanics (reused across 2.1, 2.2, 2.3, 2.7)
# --------------------------------------------------------------------------- #
def euler_lagrange(L, coords, t=t):
    """Solve the Euler–Lagrange equations of a Lagrangian.

    For each generalised coordinate the Euler–Lagrange equation
    $\\tfrac{d}{dt}(\\partial L/\\partial\\dot q)-\\partial L/\\partial q=0$ is the
    equation of motion that makes the action stationary; here we form that set and
    solve it symbolically for the accelerations, the bridge from a Lagrangian to a
    numerically integrable system.

    Parameters
    ----------
    L : sympy.Expr
        The Lagrangian, a SymPy expression in the coordinates, their time
        derivatives, and ``t``.
    coords : sequence of sympy.Function
        The generalised coordinates, each a SymPy ``Function`` of ``t``.
    t : sympy.Symbol, optional
        The time symbol (defaults to the module's canonical :data:`t`).

    Returns
    -------
    dict
        Mapping ``{q.diff(t, 2): expression}`` giving each second derivative in
        terms of the coordinates and velocities.
    """
    eqs = [sp.diff(sp.diff(L, sp.diff(q, t)), t) - sp.diff(L, q) for q in coords]
    accs = [sp.diff(q, t, 2) for q in coords]
    return sp.solve(eqs, accs, dict=True)[0]


def hamilton_rhs(H, qs, ps):
    """Build the ODE right-hand side for Hamilton's equations.

    Hamilton's equations $\\dot q=\\partial H/\\partial p$, $\\dot p=-\\partial
    H/\\partial q$ recast the dynamics as a first-order flow on phase space; this
    lambdifies them into a callable suitable for ``scipy.integrate.solve_ivp``.

    Parameters
    ----------
    H : sympy.Expr
        The Hamiltonian, already carrying numeric parameter values, in the symbols
        ``qs`` and ``ps``.
    qs, ps : sequence of sympy.Symbol
        Equal-length lists of the canonical coordinate and momentum symbols.

    Returns
    -------
    callable
        ``rhs(t, y)`` taking the block state ``y = [q0, …, q_{n-1}, p0, …, p_{n-1}]``
        and returning its time derivative as a NumPy array.
    """
    n = len(qs)
    syms = list(qs) + list(ps)
    qdot_f = [sp.lambdify(syms, sp.diff(H, p), "numpy") for p in ps]
    pdot_f = [sp.lambdify(syms, -sp.diff(H, q), "numpy") for q in qs]

    def rhs(_t, y):
        args = list(y)
        dy = np.empty_like(np.asarray(y, dtype=float))
        for i in range(n):
            dy[i] = qdot_f[i](*args)
            dy[n + i] = pdot_f[i](*args)
        return dy

    return rhs


def poisson(f, g, qs, ps):
    """Symbolic Poisson bracket of two phase-space functions.

    The Poisson bracket $\\{f,g\\}=\\sum_i(\\partial_{q_i}f\\,\\partial_{p_i}g-
    \\partial_{p_i}f\\,\\partial_{q_i}g)$ is the classical algebra of observables:
    $\\{f,H\\}=0$ marks $f$ as a constant of the motion, and brackets generate
    canonical transformations.

    Parameters
    ----------
    f, g : sympy.Expr
        The two phase-space functions.
    qs, ps : sequence of sympy.Symbol
        The canonical coordinate and momentum symbols.

    Returns
    -------
    sympy.Expr
        The bracket ``{f, g}`` (simplify it to read off a vanishing result).
    """
    return sum(
        sp.diff(f, q) * sp.diff(g, p) - sp.diff(f, p) * sp.diff(g, q)
        for q, p in zip(qs, ps)
    )


def linearize(L, coords, equilibrium, t=t):
    """Mass and stiffness matrices of a Lagrangian about an equilibrium.

    Expanding a natural Lagrangian $L=T-V$ to second order about an equilibrium
    gives $T=\\tfrac12\\dot{\\mathbf q}^\\top M\\dot{\\mathbf q}$ and
    $V=\\tfrac12\\mathbf q^\\top K\\mathbf q$; the matrices $M$ (inertia) and $K$
    (stiffness) are the input to the small-oscillation eigenproblem
    (:func:`normal_modes`).

    Parameters
    ----------
    L : sympy.Expr
        The Lagrangian in the coordinates, their velocities, and ``t``.
    coords : sequence of sympy.Function
        The generalised coordinates (Functions of ``t``).
    equilibrium : sequence of float or sympy.Expr
        The coordinate values $q_{0,i}$ at the equilibrium about which to expand.
    t : sympy.Symbol, optional
        The time symbol (defaults to :data:`t`).

    Returns
    -------
    M, K : sympy.Matrix
        The symbolic mass matrix ``M_ij = ∂²L/∂q̇_i∂q̇_j`` and stiffness matrix
        ``K_ij = -∂²L/∂q_i∂q_j``, both evaluated at the equilibrium with all
        velocities set to zero.
    """
    n = len(coords)
    qdots = [sp.diff(q, t) for q in coords]
    at_eq = {qd: 0 for qd in qdots}
    at_eq.update({coords[i]: equilibrium[i] for i in range(n)})
    M = sp.zeros(n, n)
    K = sp.zeros(n, n)
    for i in range(n):
        for j in range(n):
            M[i, j] = sp.simplify(sp.diff(L, qdots[i], qdots[j]).subs(at_eq))
            K[i, j] = sp.simplify(-sp.diff(L, coords[i], coords[j]).subs(at_eq))
    return M, K


def normal_modes(M, K):
    """Solve the small-oscillation generalised eigenproblem ``K v = ω² M v``.

    The normal modes diagonalise the mass and stiffness matrices simultaneously:
    each eigenvalue is a squared normal frequency and each eigenvector a mode shape
    in which every coordinate oscillates in lockstep. A negative eigenvalue means
    an imaginary frequency, the signature of an unstable (inverted) direction.

    Parameters
    ----------
    M : array_like
        Symmetric positive-definite mass matrix (``n × n``).
    K : array_like
        Symmetric stiffness matrix (``n × n``).

    Returns
    -------
    omega_sq : numpy.ndarray
        The squared normal-mode frequencies in ascending order.
    V : numpy.ndarray
        Matrix whose columns are the corresponding **M-orthonormal** mode shapes
        ($V^\\top M V = I$).
    """
    M = np.asarray(M, dtype=float)
    K = np.asarray(K, dtype=float)
    omega_sq, V = eigh(K, M)
    return omega_sq, V


# --------------------------------------------------------------------------- #
# Central-force radial machinery (reused in 2.4, 2.5)
# --------------------------------------------------------------------------- #
def effective_potential_1d(r, L, V, mu=1.0):
    """One-dimensional radial effective potential of a central-force problem.

    Conservation of angular momentum reduces a central-force orbit to 1-D motion
    in $V_{\\rm eff}(r)=V(r)+L^2/2\\mu r^2$; the added centrifugal term is the
    angular-momentum barrier that keeps a nonzero-$L$ orbit away from the origin
    and sets the turning points.

    Parameters
    ----------
    r : float or numpy.ndarray
        Radius (or array of radii) at which to evaluate.
    L : float
        Angular momentum.
    V : callable
        The genuine potential ``V(r)``.
    mu : float, optional
        Reduced mass (default ``1.0``, i.e. reduced units).

    Returns
    -------
    float or numpy.ndarray
        The effective potential at ``r``, matching the shape of ``r``.
    """
    return V(r) + L**2 / (2.0 * mu * r**2)


# --------------------------------------------------------------------------- #
# Root-finding utility (the fix for the recurring bracket bug: 2.4, 2.9)
# --------------------------------------------------------------------------- #
def bracketed_roots(f, a, b, n=2000):
    """All real roots of a function on an interval, brackets discovered not guessed.

    Scans the interval for sign changes and refines each with Brent's method. This
    is the robust replacement for hand-chosen brackets that silently miss a root or
    straddle two of them, the recurring failure in turning-point and Lagrange-point
    searches.

    Parameters
    ----------
    f : callable
        Scalar function ``f(x)``; may be vectorised (a fast path evaluates the
        whole scan at once) but need not be.
    a, b : float
        Endpoints of the search interval ``[a, b]``.
    n : int, optional
        Number of subintervals to scan for sign changes (default ``2000``).

    Returns
    -------
    numpy.ndarray
        The sorted real roots found on ``[a, b]`` (possibly empty).
    """
    xs = np.linspace(a, b, n + 1)
    try:  # fast path: a vectorised (NumPy) f evaluates on the whole scan at once
        fs = np.asarray(f(xs), dtype=float)
        if fs.shape != xs.shape:
            raise TypeError
    except (TypeError, ValueError):  # scalar-only f: evaluate pointwise
        fs = np.array([float(f(x)) for x in xs])
    roots = []
    for i in np.where(np.diff(np.sign(fs)) != 0)[0]:
        try:
            roots.append(brentq(f, xs[i], xs[i + 1]))
        except ValueError:
            # endpoint exactly zero, or no genuine sign change: skip
            continue
    return np.sort(np.array(roots))


def turning_points(E, Veff, r_lo, r_hi, n=2000):
    """Radial turning points of a central-force orbit at energy ``E``.

    The turning points are the radii where the radial kinetic energy vanishes,
    $E=V_{\\rm eff}(r)$: a bound orbit has two (peri- and apoapsis) and an unbound
    one has a single innermost approach. They are the roots of $E-V_{\\rm eff}(r)$,
    found with :func:`bracketed_roots`.

    Parameters
    ----------
    E : float
        Orbit energy.
    Veff : callable
        The effective potential ``Veff(r)`` (e.g. from
        :func:`effective_potential_1d`).
    r_lo, r_hi : float
        Radial search bounds.
    n : int, optional
        Number of scan subintervals (default ``2000``).

    Returns
    -------
    numpy.ndarray
        The sorted turning-point radii on ``[r_lo, r_hi]``.
    """
    return bracketed_roots(lambda r: E - Veff(r), r_lo, r_hi, n)
