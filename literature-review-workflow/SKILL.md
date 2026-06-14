---
name: literature-review-workflow
description: "Plan and execute an end-to-end literature review workflow: define scope, build and screen a paper corpus, classify papers into a stable taxonomy, extract evidence into comparison matrices, audit claims and citations, and prepare review deliverable content. Use when the user asks to survey recent papers, write a literature review, compare methods, do paper-by-paper review maintenance, prepare review-deck content, choose a research direction from papers, or repair Zotero review PDF attachments so course/research review PDFs are stored attachments for cross-device Zotero/WebDAV sync instead of absolute linked files."
---

# Literature Review Workflow

Trigger note: Use when the user asks to do a literature review, survey papers,
compare methods, build a reading list, maintain review notes, or update a
review deck. Examples include `做个文献综述`, `survey recent papers on force
control`, `compare methods in this area`, `literature review`, `帮我调研一下这个方向`,

## Purpose

Use this skill according to its frontmatter description.

Keep this `SKILL.md` as a concise routing and execution entrypoint. Do not load
long examples, command catalogs, detailed checklists, or edge-case policy until
the current task needs them.

## Workflow

1. Confirm the user request matches this skill's frontmatter description.
2. Bind the concrete target: source file, artifact, repo, device, document,
   dataset, or user-facing deliverable.
3. Use the smallest relevant workflow from this entrypoint first.
4. Load `references/entrypoint-details.md` when the task needs detailed
   procedures, examples, command recipes, acceptance criteria, or one of the
   detailed sections listed below.
5. Preserve local owner boundaries: route to a narrower skill or repo-specific
   workflow when the detailed reference indicates a more specific owner.

## Detailed Reference

Read `references/entrypoint-details.md` for:

- Overview
- Trigger Conditions
- Canonical Workflow
- User-Specific Review Rules
- Bundled Resources
- Quick Start
- Guardrails
- Validation And Checkpoints

## Validation

- Use the skill-specific validation or acceptance checks from the detailed
  reference before declaring completion.
- When editing this skill, run `quick_validate.py` on the skill directory and
  verify all referenced files still exist.
