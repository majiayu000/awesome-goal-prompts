#!/usr/bin/env python3
"""Generate a catalog health report for maintainers."""

from __future__ import annotations

import json
from collections import Counter, defaultdict
from pathlib import Path

from catalog_search import ranked


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def table(headers: list[str], rows: list[list[str]]) -> list[str]:
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]
    lines.extend("| " + " | ".join(row) + " |" for row in rows)
    return lines


def main() -> None:
    entries = load_json(ROOT / "data" / "examples.json")
    cases = load_json(ROOT / "data" / "search-eval-cases.json")
    total = len(entries)
    source_backed = [entry for entry in entries if entry["origin"] == "source-backed"]
    by_origin = Counter(entry["origin"] for entry in entries)
    by_type = Counter(entry.get("source_type") or "none" for entry in entries)
    by_category: dict[str, dict[str, int]] = defaultdict(lambda: {"total": 0, "source-backed": 0})

    for entry in entries:
        by_category[entry["category"]]["total"] += 1
        if entry["origin"] == "source-backed":
            by_category[entry["category"]]["source-backed"] += 1

    category_rows = []
    for category in sorted(by_category):
        values = by_category[category]
        total_for_category = values["total"]
        sourced = values["source-backed"]
        coverage = f"{(sourced / total_for_category) * 100:.0f}%"
        category_rows.append([category, str(sourced), str(total_for_category), coverage])

    source_type_rows = [[source_type, str(count)] for source_type, count in sorted(by_type.items())]

    eval_rows = []
    eval_failures = 0
    for case in cases:
        results = ranked(entries, case["query"])
        ids = [entry["id"] for entry in results]
        expected = case["expected"]
        max_rank = int(case.get("max_rank", 3))
        rank = ids.index(expected) + 1 if expected in ids else None
        passed = rank is not None and rank <= max_rank
        if not passed:
            eval_failures += 1
        eval_rows.append([
            case["query"],
            expected,
            str(rank or "missing"),
            f"top {max_rank}",
            "pass" if passed else "fail",
        ])

    short_evidence = [
        entry["id"]
        for entry in source_backed
        if not entry.get("evidence_summary")
    ]
    missing_source_fields = [
        entry["id"]
        for entry in source_backed
        if not all(entry.get(field) for field in ["source_name", "source_url", "source_type", "evidence", "evidence_summary"])
    ]

    lines = [
        "# Catalog Health",
        "",
        "## Summary",
        "",
        f"- Total entries: {total}",
        f"- Source-backed entries: {len(source_backed)}",
        f"- Seed entries: {by_origin.get('seed', 0)}",
        f"- Categories: {len(by_category)}",
        f"- Search eval cases: {len(cases) - eval_failures}/{len(cases)} passing",
        f"- Source-backed entries missing evidence summaries: {len(short_evidence)}",
        f"- Source-backed entries missing provenance fields: {len(missing_source_fields)}",
        "",
        "## Category Coverage",
        "",
        *table(["Category", "Source-backed", "Total", "Coverage"], category_rows),
        "",
        "## Source Types",
        "",
        *table(["Source type", "Count"], source_type_rows),
        "",
        "## Search Evaluation",
        "",
        *table(["Query", "Expected", "Rank", "Required", "Status"], eval_rows),
        "",
        "## Maintenance Notes",
        "",
        "- Prefer adding real source-backed examples to categories with low coverage before adding more seed patterns.",
        "- Keep search evals aligned with natural user phrases, not only exact titles.",
        "- Do not promote seed entries to source-backed without a public URL and evidence phrase.",
        "",
    ]

    (ROOT / "docs" / "catalog-health.md").write_text("\n".join(lines), encoding="utf-8")
    print("generated catalog health")


if __name__ == "__main__":
    main()
