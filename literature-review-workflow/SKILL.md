---
name: literature-review-workflow
description: "Plan and execute an end-to-end literature review workflow: define scope, build and screen a paper corpus, classify papers into a stable taxonomy, extract evidence into comparison matrices, audit claims and citations, and prepare review deliverable content. Use when the user asks to survey recent papers, write a literature review, compare methods, do paper-by-paper review maintenance, prepare review-deck content, or choose a research direction from papers."
---

Trigger note: Use when the user asks to do a literature review, survey papers,
compare methods, build a reading list, maintain review notes, or update a
review deck. Examples include `做个文献综述`, `survey recent papers on force
control`, `compare methods in this area`, `literature review`, `帮我调研一下这个方向`,
`按 paper-by-paper 重写`, and `维护 review deck`.

# Literature Review Workflow

## Overview

Use this skill to run a full literature review from corpus building to prepared deliverable content.

This skill owns the review pipeline upstream of deck authoring.

When the final artifact is a slide deck:
- use this skill to lock scope, taxonomy, anchors, matrices, and review outline
- hand off final deck authoring to `academic-presentation`

Default outputs:

1. scope note
2. corpus log
3. taxonomy
4. comparison matrix
5. synthesis / gap note
6. source log
7. prepared final-deliverable content or deck handoff package

For this user:

- converse in Chinese
- internal written reviews default to Chinese unless the user explicitly fixes another language or the existing artifact language is already fixed
- keep wording concise
- prefer tables, matrices, timelines, and diagrams over long prose
- for robot contact-control reviews, prefer `force-first` and `compliance-first` as the default top-level split unless the user overrides it
- treat edge papers as `supporting`, `adjacent`, or `exclude`; do not force them into the mainline taxonomy
- ready-to-send reviews are user-authored deliverables: the author and default speaker are the user, not the assistant
- written reviews default to neutral authorial prose such as `本文聚焦...`, `更合理的判断是...`; do not default to assistant-self-reference such as `我建议`
- speaker notes or oral scripts default to first-person user voice only when the deliverable is explicitly meant to be spoken
- avoid AI-smelling phrases in final deliverables such as `reviewer synthesis`, `as an AI`, `I searched`, `for the current user`, or process filler that exposes workflow rather than content

## Trigger Conditions

Use this skill when the user asks to:

- do a literature review or survey
- read recent papers in a field
- compare methods across papers
- build a taxonomy
- maintain paper-by-paper review notes or paper-by-paper explanation artifacts
- prepare a group-meeting or advisor-meeting review deck
- choose a research direction from papers

Do not use this skill for:

- single-paper explanation only
- Zotero library maintenance only
- pure slide design work with no review workflow

## Canonical Workflow

### 1. Lock the review question

Write a short scope note before classifying papers.

Always pin:

- topic
- review question
- time window
- main venues
- excluded lines
- deliverable type
- decision to be made at the end

If the user already fixed these, record them and continue.

### 2. Build the working corpus

Start from the strongest local sources first:

- existing review notes
- local `~/Zotero/storage` attachments
- local PDF text cache such as `.zotero-ft-cache`
- Zotero / Zotero MCP for structured metadata or when local attachments are not
  found

Use web lookup only when a fact is time-sensitive or unstable, such as:

- latest year
- venue
- DOI
- arXiv vs final publication status

Keep one canonical record per paper.
If the same work appears as preprint + journal/conference version, keep the formal version as canonical unless the user wants the preprint specifically.

### 3. Screen before synthesis

For each paper, mark one of:

- `anchor`
- `supporting`
- `adjacent`
- `background`
- `exclude`

Keep anchors small and intentional.
The top-line taxonomy and final deck should be driven by anchor papers, not by every collected reference.
If a paper is interesting but not control-structure-central, mark it `adjacent` instead of forcing it into the mainline split.

### 4. Build the taxonomy

Choose top-level classes by primary objective, not by buzzwords.

Default rule:

- use `2-4` top-level classes
- assign each anchor paper to exactly one top-level class
- treat labels such as `learning`, `diffusion`, `safe`, `RL`, `hybrid`, `passivity`, `policy` as method tags unless the user explicitly wants them as top-level classes

For robot contact-control reviews where the user has not fixed another scheme, use this default:

- `Force-first contact control`
- `Compliance-first interaction shaping`

Apply the split by primary objective:

- `Force-first`: explicit force target, force tracking, force-position hybrid control, unified force-impedance formulations
- `Compliance-first`: contact behavior shaping, variable impedance, adaptive compliance, virtual elasto-plastic interaction, indirect force objectives

Do not keep edge policy-learning papers in the mainline split unless their core contribution is a control law or control structure.

For the current user, when the review has already converged to the force/compliance split, prefer this stable internal structure instead of inventing fresh subtrees:

- `Force-first`
  - `Force tracking on impedance/admittance backbone`
  - `Hybrid / unified force-impedance framework`
  - `Adaptive / robust force regulation`
  - `Specialized applications and impact-contact`
  - keep `background` only as a note or bridge, not as a peer category

- `Compliance-first`
  - `Passive compliance`
    - acknowledge it
    - mark it `excluded` when the active-control line is the real scope
  - `Active compliance control`
    - `Standard impedance/admittance family`
      - `VIC: stability / passivity`
      - `VIC: task-structured shaping`
      - `Learned tuning on standard compliant backbones`
    - `Extended impedance family`
      - `Constitutive innovation`

A taxonomy is acceptable only if each class answers:

- what is optimized first
- what the controller is allowed to adapt
- what guarantee or evidence supports it

### 5. Extract evidence into a matrix

For each anchor paper, record at least:

- primary objective
- control output / adapted quantity
- sensing used
- theory story
- environment assumptions
- hardware evidence
- relevance to the user's platform

Separate:

- `paper claim`
- `author synthesis`

Do not blur them.

### 6. Synthesize the field

For each class, state:

- what problem it solves well
- what it assumes
- what it does not solve
- where it is promising for the user's project

The end state should be a defensible shortlist of candidate directions, not a pile of paper summaries.

### 7. Draft the deliverable

For written reviews:

- open with the final taxonomy
- then compare anchor papers
- then state gaps and candidate directions
- keep editable review source and work files in the normal local research or course workspace; when Zotero `Reviews` handling is in scope, mirror only the final PDF into Zotero and do not place `.tex`, `.md`, `.bib`, build folders, render checks, or other source artifacts there
- before every user-visible iteration report on review or report deliverables, run `python3 ~/.codex/skills/ai-detect/scripts/scan_ai_smell.py <file>` on the edited `.tex` / `.md` source files, keep only high-confidence findings after human review, and rerun once after any wording fix
- when the review has a rendered PDF artifact, run [$visual-deliverable-check](/Users/andyl/.codex/skills/visual-deliverable-check/SKILL.md) before reporting the artifact as ready

For slides:

- prepare the classification, comparison logic, citations, and outline first
- hand off final slide authoring to `academic-presentation`
- one idea per slide
- no process narration such as “how I searched” unless the user asks for it
- default to a minimal title page: keep the main title plus one short course/topic line unless the user explicitly wants author, institution, or subtitle metadata
- when a scope slide is needed, avoid AI-sounding setup labels such as `Working scope` or `Mainline corpus`; prefer one or two direct human sentences
- use in-body citations on content slides
- if citations become dense, add one or more dedicated reference slides
- prioritize readable spacing and balanced whitespace over a fixed font-size rule
- prefer flowcharts, mind maps, tables, and short comparison cards
- use human academic slide titles; avoid placeholder or AI-sounding headings such as `Final split`
- keep method labels and paper titles readable; avoid unexplained abbreviations on content slides
- on reference slides, use `author + year + full paper title`; venue is optional but must be consistent if included
- if both Beamer and PPTX are maintained, keep slide order and content synchronized
- compile only the requested artifacts; if the user only asks to update PPTX content, do not rebuild LaTeX, and if the user only asks to rebuild LaTeX, do not auto-export PPTX
- do not surface internal workflow markers such as Zotero collection names, internal reading IDs like `F1` / `C1`, or “current collection” wording in advisor-facing deck copy
- if a paper title appears on a content slide, use the full paper title in Title Case and append a compact tag such as `25TRO` without parentheses when space allows
- ordinary slide titles should stay in sentence case unless the slide title itself is a full paper title
- prefer flat bullet points and one point per line over dense prose paragraphs
- if a structure slide becomes crowded, split the slide before shrinking the font aggressively
- when a paper genuinely serves more than one mechanism line, keep one primary line placement and at most a light secondary-relevance cue; do not duplicate it as another main anchor page
- for slide-iteration QA, check the rendered PDF pages themselves; do not treat successful compilation or log cleanliness as sufficient evidence that the visual layout is acceptable
- use [$visual-deliverable-check](/Users/andyl/.codex/skills/visual-deliverable-check/SKILL.md) as the default final visual gate for rendered review decks
- treat the slide outline, citations, and evidence matrix as the source package for `academic-presentation`
- before every user-visible iteration report on deck or source-log deliverables, run `python3 ~/.codex/skills/ai-detect/scripts/scan_ai_smell.py <file>` on the edited deck-authoring or log source files, not on `.pptx` or rendered images; if high-risk wording is found, revise and rerun before handoff

### 8. Audit before handoff

Check all of these:

1. every factual claim is traceable to a source
2. every synthesis claim is clearly the author's synthesis
3. venue/year/DOI are checked for anchor papers
4. taxonomy is consistent across notes, slides, and source logs
5. no slide is carrying process filler or AI-style meta text
6. deliverable tone is concise and human
7. no placeholder titles, machineish headings, or unexplained shorthand remain in the final deck
8. references are formatted consistently across all reference slides
9. if a dual-format deck exists, the active PPTX source and LaTeX source are content-synchronized
10. every edited review/report/deck/source-log authoring source passed an `ai-detect` scan after the latest text revision
11. the user-visible iteration report ends with a short `ai-detect` status line when the deliverable is report-class

## User-Specific Review Rules

Apply these defaults unless the user overrides them:

- recent papers are the main body; classics stay in background or backup
- titles should sound like normal human academic titles, not placeholders
- for slide decks, if a slide looks crowded, split it; do not compress the font first
- when comparing methods, prefer the user's research question over generic taxonomies
- for robot force/contact control, keep the mainline review hardcore: control-law and control-structure papers stay in scope; edge policy papers stay adjacent or excluded
- internal review notes and report deliverables default to Chinese unless the user or existing artifact language fixes English
- reference formatting should be uniform; full paper titles are preferred over shorthand
- intermediate build clutter should stay outside the final deliverable folder when possible
- when the user has already fixed a mature taxonomy, update existing review artifacts to that taxonomy instead of inventing a new split each time
- for advisor-facing review decks, speak about the field and the method structure, not about Zotero, collections, or internal bookkeeping
- in final deliverables, the user is the first responsible author and default first speaker; never write as if the assistant is the author
- when a deliverable needs a viewpoint sentence, prefer neutral formulations like `本文主张...`, `当前阶段更合理的选择是...`, or `这里更值得优先考虑...`
- if a working matrix needs a synthesis column, call it `author synthesis` or `作者综合判断`; do not surface `reviewer synthesis` in the final deliverable
- for report-class iteration updates to the user, append exactly one short `ai-detect` status line after the substantive update; do not dump raw scanner output unless the user explicitly asks for findings

## Bundled Resources

- `references/workflow-templates.md`
- `scripts/init_review_workspace.py`

Read `references/workflow-templates.md` when starting a new review or when you need templates for the corpus log, matrix, source log, or slide outline.

Use `scripts/init_review_workspace.py` when the user wants a clean review workspace scaffold on disk.

## Quick Start

If the user wants a new workspace, run:

```bash
python3 ~/.codex/skills/literature-review-workflow/scripts/init_review_workspace.py <target_dir>
```

Then fill the scaffold in this order:

1. `00_scope.md`
2. `01_corpus.tsv`
3. `02_taxonomy.md`
4. `03_comparison_matrix.tsv`
5. `04_synthesis.md`
6. `05_sources.md`
7. `slides/outline.md`

## Guardrails

- Do not classify before reading the actual anchor papers.
- Do not force every collected paper into the final taxonomy.
- Do not treat practical guardrails as formal guarantees.
- Do not leave citation status ambiguous for anchor papers.
- Do not let the mainline deck drift into generic `foundation model`, `VLA`, or `policy` survey territory unless the user explicitly expands scope.


## Validation And Checkpoints

- Before final handoff, validate the requested artifact or decision against this skill's output contract and report the verification result explicitly.
- Before any local mutation, pass the recoverability gate: create a rollback point when the change is reversible, and request confirmation when backup cannot cover the risk.
- Use an explicit checkpoint when required input is missing, tool evidence conflicts, or repeated attempts fail; wait for approval or route to the named owner instead of guessing.
- For multi-session work, update a progress or HANDOFF artifact with current state, verified result, and next executable step.
- For L1/default-triggered work, if the path fails or becomes ambiguous, stop the default route, state the failure, and provide recovery options instead of expanding scope silently.
