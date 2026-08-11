# Meditations

*A short word, before any physics, on what it means to compute in this particular decade — and why this
course is built the way it is.*

## The thing the machine now does

There was a time, not long ago, when a working scientist spent a real fraction of each day in a kind of
low-grade archaeology: hunting a forum thread for the exact `matplotlib` incantation, misremembering the
argument order of a `scipy` routine, reconstructing from scratch the loop they had written a hundred times
before. That labor is over. A capable language model now produces correct, idiomatic scientific Python
faster than any of us can type it, and it does so across a surface far wider than any single person keeps
in their head. It is worth saying plainly, at the outset of a course that will ask you to write a great
deal of code: for most of the code most scientists write, the machine is now better at the writing than
you are. Not more careful — better at the act of production. This is not a threat to be managed or a
temptation to be resisted. It is simply the ground we now stand on, and a course that pretended otherwise
would be lying to you on its first page.

So we will not pretend. We will assume, throughout, that you have a competent assistant at your elbow and
that you use it — to draft the plotting boilerplate, to recall the routine you have forgotten, to turn a
sentence of intent into a first draft of a function. This course is not a rearguard action against that.
It is an argument about what is left for you to do once the typing is no longer the hard part — and it
turns out that what is left is nearly everything that ever mattered.

## What the machine does not do

Recall is cheap now. Judgment is not, and it never was. The machine will hand you code that runs, reads
beautifully, and is quietly, catastrophically wrong: a fit that reports success while sitting in a garbage
local minimum; an integrator handed to it by habit when a different one was called for; an array silently
aliased so that a later line mutates something you thought was safe; a computation that "worked" while
losing every digit of accuracy you cared about. The model cannot see these, because it cannot see the
answer — it has no idea what your system is supposed to do, whether energy ought to be conserved here,
whether that cross-section can physically be negative, whether the number it just produced is absurd. Only
you can hold the code up against the physics and ask whether it is telling the truth. That act — the
holding-up, the asking — is the whole of this course, and it is the one thing the machine has made *more*
urgent rather than less, because it has never been easier to generate a plausible wrong answer at scale
and ship it unexamined.

There is a subtler loss the machine has, too, and it is the one that quietly separates people who can
compute from people who cannot. The machine is superb at your *known* unknowns — you know sparse matrices
exist, you ask how to use them, it tells you. It is nearly useless for your *unknown* unknowns. If you
have never heard of a sparse solver, you will write the dense one, it will run a hundred times too slowly,
and the model will help you write that slow code beautifully, because it answered the question you asked
and you did not know to ask a better one. The prompt is framed by what you already know exists, and so the
map of the territory — the sense of what is out there, what problem each tool solves, where the roads
run — remains stubbornly yours to carry. This is why we will still teach you the shape of the scientific
Python ecosystem, not the contents of its every drawer. You do not need to memorize what is in the
toolbox. You very much need to know the toolbox exists and roughly what each tool is for, because that
knowledge is exactly the thing that converts an unknown unknown into a question the machine can finally
answer.

## Recognition, not recall

From this a single design principle follows, and it governs every notebook in this course. There are two
kinds of knowing. One is *recall*: producing the exact call from memory — the fifteen keyword arguments,
the precise signature, the method name spelled correctly. The other is *recognition*: reading
`minimize(f, x0, method='L-BFGS-B', jac=grad)` and understanding it on sight — that there is a
minimizer, that it takes a function and a starting guess, that the method names an algorithm and `jac`
supplies the gradient. Recall is expensive to acquire, quick to decay, and the machine now owns it
completely. Recognition is cheap, durable, and must live in your head, because it is what lets you read
generated code at speed and catch it when it drifts. The old scientific-Python course was deep on recall
and shallow on judgment. This one inverts the axis: we teach the stratum of each library that lives
permanently in your working memory — the concepts, the idioms, the map — and we let the assistant supply
the stratum that lives in its context window, the exact call, which it tracks through version churn far
better than you ever will. When we teach `broadcasting`, the goal is that you can *predict* what a shape
mismatch will do, not that you can recite the rules; when we name `einsum`, the goal is that you know it
exists and what problem it solves, not that you have memorized its grammar. Familiarity is not the enemy
of judgment — it is the substrate judgment is built on. You cannot spot a wrong broadcast without a model
of a right one. But the substrate is smaller, and more conceptual, and more permanent, than the old
courses believed.

## What you will still write by hand, and why

If the machine writes the code, why write any of it yourself? Because for one specific kind of code, the
writing *is* the understanding, and there is no other door in. When this course asks you to implement the
core of a method — the symplectic step, the Metropolis update, the eigensolver's inner loop — it is not
testing whether you can produce lines the assistant could produce faster. It is using the act of writing
as the only reliable way to *understand* what the method does, because a method you have built by hand is
a method whose failures you can later recognize in someone else's code — or the machine's. Those cells
will be marked, and they are few, and they are the ones that matter. Everywhere else — the plotting, the
file handling, the parameter sweep, the scaffolding around the idea — you should feel free to delegate,
because typing those builds nothing, and pretending otherwise is a superstition, not a pedagogy. The
skill this course builds is not blank-page fluency from memory; that was always the rare case in real
scientific work. The skill is the actual working loop of modern computation — generate, read, modify,
verify — and we train it directly, by having you read code critically, predict what it will do before it
runs, modify it toward correctness, and check the result against something you trust. You build the
ability to write well through the discipline of reading well, which is, if you think about it, how one
learns to write anything.

## The instrument

What all of this is building, underneath the physics, is a single instrument, and it is the only thing
worth carrying out of this course. Not the `coth`, not the instanton, not the exponent that two lattices
share — those you can always regenerate. The instrument is a calibrated distrust: the reflex to compute a
thing more than one way and demand the ways agree, to separate an error into its named sources rather than
lump them into a shrug, to check every result — yours or the machine's — against a fact you already hold,
and to know, within a stated tolerance, exactly how far to trust the number in front of you. That reflex
is what makes a scientist in an age when code is cheap and correctness is dear. The machine has made the
production of answers nearly free. It has done nothing at all to make them *true*. Closing that gap —
between an answer that runs and an answer that is right — is the work that remains, and it is entirely
yours. This course is a long apprenticeship in that one skill, conducted on the most beautiful problems we
could find. The physics is the occasion. The judgment is the point.

*Now, gently, to a pendulum.*
