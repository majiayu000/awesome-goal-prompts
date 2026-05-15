#!/usr/bin/env python3
"""Evaluate catalog search quality against representative user queries."""

from __future__ import annotations

import json
from pathlib import Path

from catalog_search import ranked


ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> None:
    entries = load_json(ROOT / "data" / "examples.json")
    cases = load_json(ROOT / "data" / "search-eval-cases.json")
    failures: list[str] = []

    for case in cases:
        results = ranked(entries, case["query"])
        ids = [entry["id"] for entry in results]
        expected = case["expected"]
        max_rank = int(case.get("max_rank", 3))
        rank = ids.index(expected) + 1 if expected in ids else None
        top = ", ".join(ids[:5])
        if rank is None or rank > max_rank:
            failures.append(
                f"{case['query']!r}: expected {expected} within top {max_rank}, "
                f"got rank {rank or 'missing'}; top={top}"
            )
        else:
            print(f"PASS {case['query']!r}: {expected} rank {rank}; top={top}")

    if failures:
        print("\nSearch eval failures:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print(f"\n{len(cases)} search eval cases passed")


if __name__ == "__main__":
    main()
