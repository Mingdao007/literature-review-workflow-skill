---
name: review
description: "Write any concept-review or comparison-review as a user-authored deliverable. Use when the user asks to write a review of a concept, method family, simulator, framework, or comparison topic, and the output should read like the user's own concise academic review rather than an assistant-generated report."
---

# Review Subskill

Use this subskill under `literature-review-workflow` when the final product is a review-oriented deliverable rather than only corpus management.

## Core contract

- The author is the user.
- The default first responsible person is the user.
- The default speaker is the user when the deliverable is spoken.
- Never write as if the assistant is the author, reviewer, or speaker.

## Voice rules

- For written reviews:
  - default to neutral authorial prose such as `本文聚焦...`, `更合理的判断是...`, `当前阶段更适合...`
  - avoid assistant-self-reference such as `我建议`, `我会把`, `作为 reviewer`, `this review by the assistant`
- For speaker notes or oral scripts:
  - use first-person user voice when the output is explicitly meant to be spoken
  - do not mix neutral paper prose and assistant voice in the same deliverable

## Anti-AI-smell rules

- Do not expose workflow narration such as `I searched`, `I collected`, `the current user`, `reviewer synthesis`, or tool/process filler.
- Prefer direct claims over meta claims.
- Prefer short evidence-backed comparisons over padded transitions.
- Use human academic titles, not placeholder or machineish headings.

## Iteration gate

- For every user-visible iteration of a review deliverable, run `python3 ~/.codex/skills/ai-detect/scripts/scan_ai_smell.py <file>` on the edited authoring source first.
- Prioritize the actual authoring source, e.g. `.tex` or `.md`, not the generated `.pdf`.
- Keep only high-confidence findings after human review.
- If the scan finds high-risk wording and the text is revised, rerun `ai-detect` at least once before reporting the iteration as updated.
- If the review is rendered to PDF, run [$visual-deliverable-check](/Users/andyl/.codex/skills/visual-deliverable-check/SKILL.md) before reporting the artifact as ready.
- End the user-visible iteration update with one short status line: `ai-detect：已检查，无高风险 AI 味残留。` or `ai-detect：已检查，并已修正高风险措辞后再输出。`

## Synthesis labeling

- In working notes and source logs, use `paper claim` and `author synthesis`.
- In the final review, do not surface internal labels unless the user explicitly asks for an audit-style document.
- When a conclusion is your synthesis, write the conclusion directly in the user's authorial voice.

## Defaults for this user

- Internal review deliverables default to Chinese.
- Technical terms keep English on first mention.
- Prefer tables, comparison matrices, and short conclusion paragraphs over long prose blocks.
- If the topic is a comparison review, end with:
  1. main recommendation for the current stage
  2. one backup / second workbench
  3. one watchlist item if the field contains an immature but important direction

## Minimal checklist before handoff

1. Does the deliverable read as if the user wrote it?
2. Is every stance sentence in neutral authorial prose or explicit user-speaking prose?
3. Did all assistant-authored phrasing get removed?
4. Did any `reviewer synthesis` wording leak into the final deliverable?
5. Does the close answer the actual decision question instead of narrating process?
6. Did the latest authoring source pass the `ai-detect` iteration gate before handoff?
