# Workflow Templates

Use these templates when the review starts from scratch or when the current notes are messy.

## 1. Scope Note

```md
# Scope

Topic:

Review question:

Time window:

Primary venues:

Excluded lines:

Deliverable:

Decision needed at the end:
```

## 2. Corpus Log

Use TSV or Markdown with these columns:

| ID | Paper | Year | Venue | Role | Top-level class | Method tags | Canonical version | Why kept |
|---|---|---:|---|---|---|---|---|---|

Role values:

- `anchor`
- `supporting`
- `background`
- `exclude`

## 3. Taxonomy Note

```md
# Final taxonomy

## Class 1
- Primary objective:
- Typical control object:
- Representative papers:
- Method tags:

## Class 2
- Primary objective:
- Typical control object:
- Representative papers:
- Method tags:
```

## 4. Comparison Matrix

Use these columns for anchor papers:

| Paper | Primary objective | Adapted quantity / control output | Sensing | Theory story | Environment assumptions | Hardware evidence | Relevance to my platform |
|---|---|---|---|---|---|---|---|

## 5. Source Log

Track every strong statement that appears in the final deliverable:

| Location | Statement | Source | Type | Verified |
|---|---|---|---|---|

`Type` should be one of:

- `paper claim`
- `author synthesis`
- `metadata`

## 6. Slide Outline

Keep the main deck short.

Default outline:

1. title
2. final taxonomy
3. mind map / field map
4. class A method structure
5. class A anchor papers
6. class B method structure
7. class B anchor papers
8. cross-class comparison
9. candidate directions
10. venues / corpus summary
11. discussion points
12+. references / backup

## 7. Review Audit Checklist

Use this before delivery:

1. Top-level classes are defined by primary objective.
2. Every anchor paper appears in the corpus log, matrix, and source log.
3. Every venue/year entry for anchors is checked.
4. Every factual claim in the deck or report has a source.
5. Every synthesis statement is clearly synthesis.
6. The final direction section follows from the comparison matrix.
7. If the review is in slides, crowded slides were split rather than compressed.
8. Final deliverable voice is user-authored rather than assistant-authored.
9. Written reviews use neutral authorial prose by default; spoken notes use first-person user voice only when needed.
