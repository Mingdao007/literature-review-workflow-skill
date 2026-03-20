#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


SCOPE = """# Scope

Topic:

Review question:

Time window:

Primary venues:

Excluded lines:

Deliverable:

Decision needed at the end:
"""


TAXONOMY = """# Final taxonomy

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
"""


SYNTHESIS = """# Synthesis

## What each class solves well

## What each class assumes

## What each class does not solve

## Candidate directions
"""


SOURCES = """# Source log

| Location | Statement | Source | Type | Verified |
|---|---|---|---|---|
"""


OUTLINE = """# Slide outline

1. title
2. final taxonomy
3. field map
4. class A method structure
5. class A anchors
6. class B method structure
7. class B anchors
8. cross-class comparison
9. candidate directions
10. discussion
11+. references / backup
"""


CORPUS_TSV = (
    "id\tpaper\tyear\tvenue\trole\ttop_level_class\tmethod_tags\tcanonical_version\twhy_kept\n"
)


MATRIX_TSV = (
    "paper\tprimary_objective\tadapted_quantity_or_output\tsensing\ttheory_story\t"
    "environment_assumptions\thardware_evidence\trelevance_to_platform\n"
)


def write_if_missing(path: Path, content: str, force: bool) -> None:
    if path.exists() and not force:
        return
    path.write_text(content, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Create a scaffold for a literature review workspace."
    )
    parser.add_argument("target_dir", help="Target directory for the review workspace")
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing scaffold files",
    )
    args = parser.parse_args()

    target = Path(args.target_dir).expanduser().resolve()
    target.mkdir(parents=True, exist_ok=True)
    (target / "slides").mkdir(exist_ok=True)
    (target / "figures").mkdir(exist_ok=True)

    write_if_missing(target / "00_scope.md", SCOPE, args.force)
    write_if_missing(target / "01_corpus.tsv", CORPUS_TSV, args.force)
    write_if_missing(target / "02_taxonomy.md", TAXONOMY, args.force)
    write_if_missing(target / "03_comparison_matrix.tsv", MATRIX_TSV, args.force)
    write_if_missing(target / "04_synthesis.md", SYNTHESIS, args.force)
    write_if_missing(target / "05_sources.md", SOURCES, args.force)
    write_if_missing(target / "slides" / "outline.md", OUTLINE, args.force)

    print(f"Initialized literature review workspace at: {target}")


if __name__ == "__main__":
    main()
