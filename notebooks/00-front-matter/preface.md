# Preface

**Elementary Computational Physics** is a free companion course for anyone learning theoretical physics
who actually wants to *compute* something: to turn the equations on the page into something that runs,
plots, animates, and just looks elegant. This course was borne out of my idea to finally have a
compendium of exercises – and moderately challenging ones at that! – whose focus was not pen(cil) and
paper, but rather the computer.

Each notebook reviews the essential theory, then puts it to work in a sequence of exercises. You
implement the physics yourself, visualise it, and finish by **validating** the result against something
independent: a conserved quantity, an analytic limit, a known spectrum, a symmetry. Nothing here asks
you to trust a number you cannot check.

The sequence of topics in the course (more or less) follows Wolfgang Nolting's *Theoretical Physics*
series (Vols. 1–6) — elementary and analytical mechanics, electrodynamics, thermodynamics and special
relativity, quantum mechanics, and statistical mechanics. The exercises are written in that spirit and
ordering, but the explanations, code, and figures here are original work; this companion does not
reproduce the textbooks and is no substitute for them nor for full lectures themselves. Where a full
derivation belongs in a book, the notebooks point you there.

The course is now complete, and its shape is worth a sentence. A short **Prologue** opens it — one
gentle notebook that works a single question (how long does a pendulum take to swing?) at three levels
of honesty, so you meet the course's whole method before any formalism. A short **Volume 0 —
Foundations** then precedes the physics: the mathematical and computational tools every later notebook
relies on, beginning with floating-point arithmetic and numerical error. Seven physics volumes follow,
from projectile motion to quantum statistical mechanics; Volume VII carries an optional **Coda** — a
three-notebook gateway to many-body formalism (second quantization, Green's functions, linear response)
for those who want it, skippable without loss. And the course closes with an **Epilogue**: four
notebooks that gather what no single volume owns — one system seen seven ways, one principle behind
every dynamical law, the universality that makes microscopic details wash out at criticality, and,
last, an honest account of how a course with no laboratory and no oracle knew its answers were right —
followed by a one-page Afterword.

One promise, made here and kept on the last page: every number you compute in this course will be
approximate — the very first notebook shows that the computer cannot even represent (1 + ε) − 1 — and
the course's single deepest aim is that you learn to say, and to *show*, exactly how approximate. The
habits that deliver on it appear on every page: results computed more than one way and required to
agree; errors separated into their named sources rather than lumped; failures staged deliberately,
because knowing the shape of a wrong answer is how you recognise a right one; and a curriculum built to
be complete and minimal, where anything borrowed early is derived in full later — every forward
reference named, and every one kept.

## How to use these notebooks

- **Read the theory section first**, then work the exercises in order — each builds on the last.
- **Run everything.** The notebooks are meant to be executed and modified; change a parameter and watch
  what happens.
- **Don't skip the validation cells.** They are the point: they tell you whether your physics is right.
- **New to computational work?** Start with the Prologue — it is the course in miniature, and it
  explains the notebook machinery as you go. If you are comfortable already, you may skip straight to
  Volume 0.
- **Optional material is marked.** Volume VII's Coda and a handful of capstones are flagged optional;
  the core course never depends on them.
- Animations are pre-rendered so they play anywhere, even on the static website. A few notebooks offer
  live, interactive versions — launch those on Binder or Colab with the rocket button.

## Conventions

Code style, figure aesthetics, and the validation helpers are shared across every notebook (the `ecp`
package), so the series reads as one coherent work. Notebook prose is licensed under CC BY 4.0 and the
code under MIT. Exercise solutions are maintained by the author and are not distributed with the
notebooks; the validation cells are your feedback.

## A note on how this course was written

This course was written in collaboration with a generative AI assistant (Anthropic's Claude), and I
say so plainly, because the course's whole subject is honesty about method. The conception and the
curriculum are mine: the arc from a swinging pendulum to quantum statistical mechanics, the pedagogy
that carries it — the rendezvous method, the error budgets, the validation gates, the staged failures —
and the detailed per-notebook briefs, worked out number by number, from which every page was built. The
assistant drafted prose and code to those specifications, tirelessly and well; I reviewed, corrected,
and approved every page, and the final word on every one of them is a human's. And in the spirit of
everything above, neither author was taken on trust: every result in the course is validated against
something independent — a conserved quantity, an analytic limit, a known spectrum — precisely so that
you never have to take anyone's word, human or machine, for a single number here.

*— Raymond Amador*

```{raw} html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "Elementary Computational Physics",
  "description": "An interactive course from classical mechanics to quantum and statistical mechanics, taught with Python.",
  "url": "https://ramador.me/elementary-computational-physics-public/",
  "inLanguage": "en",
  "isAccessibleForFree": true,
  "teaches": [
    "computational physics",
    "classical mechanics",
    "quantum mechanics",
    "statistical mechanics",
    "Python"
  ],
  "provider": {
    "@type": "Person",
    "name": "Raymond Amador",
    "url": "https://ramador.me/"
  }
}
</script>
```
