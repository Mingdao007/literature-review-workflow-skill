# Literature Review Workflow Skill

Portable end-to-end literature review skill for scope setting, corpus building, taxonomy design, evidence extraction, and review deliverable preparation.

## What Ships

- installable skill: [`literature-review-workflow`](./literature-review-workflow)
- bundled public references: [`literature-review-workflow/references/`](./literature-review-workflow/references)
- bundled helper scripts: [`literature-review-workflow/scripts/`](./literature-review-workflow/scripts)

## Install / Use

- `Codex App`: install the skill from this repo path `literature-review-workflow`
- GitHub install target:
  - repo: `<owner>/literature-review-workflow-skill`
  - path: `literature-review-workflow`
- Restart `Codex App` after installation so the new skill is discovered.

## Coverage

- scope note, corpus log, taxonomy, and comparison-matrix workflow
- anchor-paper driven synthesis before report or deck authoring
- structured templates for review notes, source logs, and slide outlines

## Trigger Examples

- `Run a literature review on this topic.`
- `Build a taxonomy and comparison matrix for these papers.`
- `Prepare review-ready content from a paper corpus.`

## Non-Trigger Examples

- `Explain only one paper section.`
- `Only clean my bibliography database.`
- `Design slide visuals without doing the review workflow.`

## Privacy Boundary

This public repository keeps the workflow generic and reusable.

- User-specific defaults and local note conventions are rewritten into generic public defaults.
- The public package does not depend on private memory files or local reference-manager setup.

## Repository Layout

- `literature-review-workflow/`: installable `Codex App` skill
- `literature-review-workflow/references/`: bundled public references
- `literature-review-workflow/scripts/`: bundled public scripts
- `CHANGELOG.md`: release history
- `LICENSE`: `MIT`

Chinese:

- [README.zh-CN.md](./README.zh-CN.md)
