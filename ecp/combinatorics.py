"""Reusable combinatorics-and-distributions helpers for Volume V.

The Volume V analogue of :mod:`ecp.mechanics`: the schematics, distribution plots,
counting functions, and Monte Carlo simulators that the statistical-mechanics math
arsenal (5.1 counting, 5.2 probability, 5.3 large-$N$) and the physics notebooks share.
Two families live here:

* **Schematics** (``card``, ``hand``, ``die``, ``boxes``, ``sock_drawer``) draw the
  recognizable counting props on a Matplotlib axes, composing with :mod:`ecp.draw` for
  the collision-free label placer and the ``finish`` gate. Their inline glyphs (a card's
  rank, a die's pips) are drawn with ``ax.text`` and are *not* gate-checked; annotation
  labels added with :func:`ecp.draw.place_label` still route through the gate.
* **Counting and simulation** (``stars_bars``, ``count_statistics``, ``poker_rank``,
  ``simulate_poker``, ``draw_without_replacement``, ``distribution_bars``) turn the
  combinatorics into numbers and Monte Carlo checks.

Everything is deterministic given an explicit ``numpy.random.Generator`` (from
``numpy.random.default_rng``), so simulations reproduce exactly.
"""

import math
from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle

from . import draw
from .draw import ACCENT, INK, PANEL, SOFT

RED = "#c1121f"  # the red suits (hearts, diamonds)

SUIT_SYMBOL = {"S": "♠", "H": "♥", "D": "♦", "C": "♣"}
SUIT_COLOR = {"S": INK, "C": INK, "H": RED, "D": RED}
RANK_LABEL = {11: "J", 12: "Q", 13: "K", 14: "A", 1: "A"}


# ---------------------------------------------------------------------------
# Counting (pure functions)
# ---------------------------------------------------------------------------
def stars_bars(n, k):
    """The number of ways to place ``n`` indistinguishable balls into ``k`` boxes.

    The stars-and-bars count $C(n+k-1,\\,k-1)$: arrange $n$ stars and $k-1$ bars in a row,
    each arrangement being one distribution. This is the **Bose-Einstein** multiplicity of
    $n$ indistinguishable particles among $k$ states (Volume VII).

    Parameters
    ----------
    n : int
        Number of indistinguishable balls (particles).
    k : int
        Number of boxes (states).

    Returns
    -------
    int
        The exact count $C(n+k-1,\\,k-1)$.
    """
    return math.comb(n + k - 1, k - 1)


def count_statistics(n, k):
    """The three occupation counts for ``n`` objects in ``k`` states {eq}`eq-distinguishable`.

    The same physical setup counted three ways, the distinction that separates the quantum
    statistics (Volume VII):

    * ``"MB"`` (Maxwell-Boltzmann), distinguishable objects: $k^n$;
    * ``"BE"`` (Bose-Einstein), indistinguishable, any number per state: $C(n+k-1,\\,k-1)$;
    * ``"FD"`` (Fermi-Dirac), indistinguishable, at most one per state: $C(k,\\,n)$.

    Parameters
    ----------
    n : int
        Number of objects (particles).
    k : int
        Number of states (boxes).

    Returns
    -------
    dict
        ``{"MB": k**n, "BE": C(n+k-1, k-1), "FD": C(k, n)}``.
    """
    return {"MB": k**n, "BE": stars_bars(n, k), "FD": math.comb(k, n)}


# ---------------------------------------------------------------------------
# Monte Carlo simulators (deterministic given an explicit Generator)
# ---------------------------------------------------------------------------
def poker_rank(ranks, suits):
    """Classify a five-card poker hand into its category.

    Pure ranking by multiplicity: the rarer the hand, the smaller its count (Exercise 7).
    Aces are high ($14$) but also complete the low straight $A2345$.

    Parameters
    ----------
    ranks : sequence of int
        The five card ranks, $2$-$14$ (J=11, Q=12, K=13, A=14).
    suits : sequence of str
        The five suits, each one of ``"SHDC"``.

    Returns
    -------
    str
        One of ``"straight flush"``, ``"four of a kind"``, ``"full house"``, ``"flush"``,
        ``"straight"``, ``"three of a kind"``, ``"two pair"``, ``"one pair"``,
        ``"high card"``.
    """
    counts = sorted(Counter(ranks).values(), reverse=True)
    is_flush = len(set(suits)) == 1
    uniq = sorted(set(ranks))
    is_straight = len(uniq) == 5 and (uniq[-1] - uniq[0] == 4)
    if set(ranks) == {14, 2, 3, 4, 5}:  # the ace-low straight (wheel)
        is_straight = True
    if is_straight and is_flush:
        return "straight flush"
    if counts[0] == 4:
        return "four of a kind"
    if counts[0] == 3 and counts[1] == 2:
        return "full house"
    if is_flush:
        return "flush"
    if is_straight:
        return "straight"
    if counts[0] == 3:
        return "three of a kind"
    if counts[0] == 2 and counts[1] == 2:
        return "two pair"
    if counts[0] == 2:
        return "one pair"
    return "high card"


def simulate_poker(rng, n_deals):
    """Deal ``n_deals`` random five-card hands and tally the categories.

    A Monte Carlo check on the exact counts: deal from a 52-card deck without replacement
    with ``rng`` (a ``numpy.random.default_rng`` generator) and classify each hand with
    :func:`poker_rank`.

    Parameters
    ----------
    rng : numpy.random.Generator
        The random generator (from ``numpy.random.default_rng``).
    n_deals : int
        Number of hands to deal.

    Returns
    -------
    collections.Counter
        Category name to observed frequency.
    """
    ranks_deck = np.repeat(np.arange(2, 15), 4)
    suits_deck = np.tile(np.array(list("SHDC")), 13)
    tally = Counter()
    for _ in range(n_deals):
        idx = rng.choice(52, size=5, replace=False)
        tally[poker_rank(ranks_deck[idx], suits_deck[idx])] += 1
    return tally


def draw_without_replacement(rng, population, k, n_trials):
    """Draw ``k`` items without replacement, ``n_trials`` times, returning the draws.

    The Monte Carlo engine behind the sock-drawer and lottery counts: each trial picks
    ``k`` distinct items from ``population`` with ``rng`` (``numpy.random.default_rng``).

    Parameters
    ----------
    rng : numpy.random.Generator
        The random generator.
    population : array_like
        The items to draw from (e.g. an array of colour labels).
    k : int
        Number drawn per trial.
    n_trials : int
        Number of independent trials.

    Returns
    -------
    numpy.ndarray
        An ``(n_trials, k)`` array of drawn items.
    """
    population = np.asarray(population)
    out = np.empty((n_trials, k), dtype=population.dtype)
    for i in range(n_trials):
        out[i] = rng.choice(population, size=k, replace=False)
    return out


# ---------------------------------------------------------------------------
# Schematics (compose with ecp.draw; inline glyphs via ax.text, not gate-checked)
# ---------------------------------------------------------------------------
def card(ax, x, y, rank, suit, w=0.62, h=0.92, z=2):
    """Draw one playing card with its rank and suit, lower-left corner at ``(x, y)``.

    A rounded white card with the rank and suit glyph in the suit's colour (black for
    spades/clubs, red for hearts/diamonds). Composed by :func:`hand` into a poker hand.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to draw on.
    x, y : float
        Lower-left corner of the card.
    rank : int
        Card rank $2$-$14$ (J=11, Q=12, K=13, A=14).
    suit : str
        One of ``"SHDC"`` (spades, hearts, diamonds, clubs).
    w, h : float, optional
        Card width and height.
    z : int, optional
        Draw z-order (default ``2``).

    Returns
    -------
    None
        Draws the card onto ``ax`` in place.
    """
    label = RANK_LABEL.get(rank, str(rank))
    sym = SUIT_SYMBOL[suit]
    col = SUIT_COLOR[suit]
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.0,rounding_size=0.08",
            linewidth=1.3, edgecolor=INK, facecolor="white", zorder=z,
        )
    )
    # inline card glyphs are exempt from the collision gate (gid "_nocheck")
    ax.text(x + 0.13, y + h - 0.13, label, color=col, fontsize=11, ha="center", va="center", zorder=z + 1, fontweight="bold", gid="_nocheck")
    ax.text(x + 0.13, y + h - 0.32, sym, color=col, fontsize=10, ha="center", va="center", zorder=z + 1, gid="_nocheck")
    ax.text(x + w / 2, y + h / 2 - 0.05, sym, color=col, fontsize=20, ha="center", va="center", zorder=z + 1, gid="_nocheck")


def hand(ax, cards, x0=0.0, y=0.0, gap=0.16, w=0.62, h=0.92):
    """Draw a row of playing cards (a poker hand).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to draw on.
    cards : sequence of (int, str)
        The cards as ``(rank, suit)`` pairs.
    x0, y : float, optional
        Lower-left corner of the first card.
    gap : float, optional
        Horizontal gap between cards.
    w, h : float, optional
        Card width and height.

    Returns
    -------
    None
        Draws the hand onto ``ax`` in place.
    """
    for i, (rank, suit) in enumerate(cards):
        card(ax, x0 + i * (w + gap), y, rank, suit, w=w, h=h)


def die(ax, x, y, n, size=0.8, color=INK, z=2):
    """Draw one die face showing ``n`` pips, lower-left corner at ``(x, y)``.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to draw on.
    x, y : float
        Lower-left corner of the die.
    n : int
        Number of pips, $1$-$6$.
    size : float, optional
        Side length of the die (default ``0.8``).
    color : str, optional
        Pip and outline colour (default the series ink).
    z : int, optional
        Draw z-order (default ``2``).

    Returns
    -------
    None
        Draws the die onto ``ax`` in place.
    """
    ax.add_patch(
        FancyBboxPatch(
            (x, y), size, size, boxstyle="round,pad=0.0,rounding_size=0.12",
            linewidth=1.4, edgecolor=color, facecolor="white", zorder=z,
        )
    )
    a, b, c = 0.25, 0.5, 0.75  # pip grid positions (fractions of the side)
    layout = {
        1: [(b, b)],
        2: [(a, c), (c, a)],
        3: [(a, c), (b, b), (c, a)],
        4: [(a, a), (a, c), (c, a), (c, c)],
        5: [(a, a), (a, c), (b, b), (c, a), (c, c)],
        6: [(a, a), (a, b), (a, c), (c, a), (c, b), (c, c)],
    }
    for fx, fy in layout[n]:
        ax.add_patch(Circle((x + fx * size, y + fy * size), 0.06 * size, color=color, zorder=z + 1))


def boxes(ax, occupation, x0=0.0, y=0.0, box_w=0.9, box_h=1.0, ball_color=ACCENT, labels=True, z=2):
    """Draw ``k`` boxes in a row with balls inside, the occupation/ball-in-box schematic.

    The central schematic of the distinguishability spine: ``occupation`` gives, per box,
    either a count of plain balls (indistinguishable) or a list of labels (distinguishable,
    e.g. ``["A", "C"]``). Used for stars-and-bars and the three-statistics enumeration.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to draw on.
    occupation : sequence
        One entry per box: an ``int`` (that many unlabelled balls) or a sequence of
        short string labels (one labelled ball each).
    x0, y : float, optional
        Lower-left corner of the first box.
    box_w, box_h : float, optional
        Box width and height.
    ball_color : str, optional
        Ball fill colour (default the series accent).
    labels : bool, optional
        Whether to draw the labels inside distinguishable balls (default ``True``).
    z : int, optional
        Draw z-order (default ``2``).

    Returns
    -------
    None
        Draws the boxes and balls onto ``ax`` in place.
    """
    r = 0.16 * box_w
    for j, occ in enumerate(occupation):
        bx = x0 + j * box_w
        ax.add_patch(Rectangle((bx, y), box_w, box_h, fill=False, edgecolor=INK, lw=1.4, zorder=z))
        items = list(occ) if not isinstance(occ, (int, np.integer)) else [None] * int(occ)
        for m, item in enumerate(items):  # stack balls upward inside the box
            cy = y + 0.28 + m * (2.2 * r)
            cx = bx + box_w / 2
            ax.add_patch(Circle((cx, cy), r, facecolor=ball_color, edgecolor=INK, lw=0.8, zorder=z + 1))
            if item is not None and labels:
                ax.text(cx, cy, str(item), color="white", fontsize=8, ha="center", va="center", zorder=z + 2, fontweight="bold", gid="_nocheck")


def sock_drawer(ax, color_counts, x0=0.0, y=0.0, cols=4, z=2):
    """Draw a drawer of coloured socks, the without-replacement schematic.

    A rounded drawer outline holding ``color_counts`` socks (a mapping of colour to count),
    laid out in a small grid. The seed of occupation-number counting (drawing
    indistinguishable-within-colour objects without replacement).

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to draw on.
    color_counts : dict
        Mapping of Matplotlib colour to the number of socks of that colour.
    x0, y : float, optional
        Lower-left corner of the drawer.
    cols : int, optional
        Socks per row (default ``4``).
    z : int, optional
        Draw z-order (default ``2``).

    Returns
    -------
    None
        Draws the drawer onto ``ax`` in place.
    """
    socks = [c for c, n in color_counts.items() for _ in range(n)]
    rows = (len(socks) + cols - 1) // cols
    pad = 0.3
    w = cols * 0.55 + pad
    h = rows * 0.6 + pad
    ax.add_patch(
        FancyBboxPatch(
            (x0, y), w, h, boxstyle="round,pad=0.0,rounding_size=0.1",
            linewidth=1.6, edgecolor=INK, facecolor=PANEL, zorder=z,
        )
    )
    for i, c in enumerate(socks):
        r, col = divmod(i, cols)
        cx = x0 + pad / 2 + 0.275 + col * 0.55
        cy = y + h - pad / 2 - 0.3 - r * 0.6
        ax.add_patch(Circle((cx, cy), 0.2, facecolor=c, edgecolor=INK, lw=1.0, zorder=z + 1))


def distribution_bars(ax, labels, values, highlight=None, color=ACCENT, hi_color=RED, ylabel="probability"):
    """A labelled bar chart of a distribution (probabilities or counts).

    The standard distribution plot of the arsenal, for poker-hand probabilities, Monte Carlo
    frequencies, and occupation distributions. One bar may be highlighted.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes to draw on.
    labels : sequence of str
        The category labels (x-axis).
    values : array_like
        The bar heights.
    highlight : int or None, optional
        Index of a bar to draw in ``hi_color`` (default ``None``).
    color, hi_color : str, optional
        Default and highlight bar colours.
    ylabel : str, optional
        The y-axis label (default ``"probability"``).

    Returns
    -------
    matplotlib.container.BarContainer
        The drawn bars.
    """
    cols = [hi_color if (highlight is not None and i == highlight) else color for i in range(len(labels))]
    bars = ax.bar(range(len(labels)), values, color=cols, edgecolor=INK, linewidth=0.6)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels, rotation=35, ha="right", fontsize=8)
    ax.set_ylabel(ylabel)
    return bars
