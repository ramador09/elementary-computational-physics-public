# How This Course Was Made

The [Meditations](meditations.md) argue that you should compute with an
assistant at your elbow, and that what remains yours is the judgment. It would
be a poor kind of hypocrisy to make that argument without saying how this course
was itself produced. So, plainly:

## What the assistant did

The notebooks were drafted with **Claude Code** (Anthropic's Claude models,
2025–2026). The assistance was substantial, and covered drafting notebook prose
and exercise text from an agreed design; writing implementation code, figures
and validation checks; building the surrounding machinery — the style,
cross-reference, figure and manifest gates, the continuous-integration pipeline,
the typeset PDF build; and systematic review passes over finished volumes,
several of which found real errors in earlier drafts.

## What I did

I set the course's design, its sequence and its scope, chose what each notebook
must teach and what would count as a convincing check of it, decided which
explanations were good enough to keep and rejected a great many that were not,
and supplied the physics. Where a passage makes a claim about physics or about
numerical behaviour, I am responsible for it being true. Errors that remain are
mine.

## What the machines check

The course's central claim is not about who wrote it. It is that **no
quantitative claim in the prose is unchecked.** All 155 notebooks execute end to
end on every change, and their 2,225 validation calls each compare a computed
result against something the calculation did not assume — a conserved quantity,
a limiting case, an analytic solution, a second method. If a number in the text
drifts from what the code produces, the build fails and the page does not
update.

That is what makes an AI-assisted physics course trustworthy further than its
production process alone would warrant. A fluent, confident, wrong paragraph is
the characteristic failure of these tools, and prose review catches it
unreliably. An executable check does not care how fluent the claim was.

It is also incomplete, and worth being honest about the shape of the gap. A gate
tests what someone thought to test. The review passes that found errors here
found most of them in the prose *around* the numbers — an explanation of why a
correct result held that was itself wrong, a check that could not have failed, a
figure caption describing something the figure did not show. Those needed a
reader. The instrument the Meditations describe — the calibrated distrust — is
exactly what the writing of this course required, and it is not automatable
either.

## Citing and reuse

Cite this course as given in `CITATION.cff`. Text is CC BY 4.0 and code is MIT;
adapt either freely, including for teaching.
