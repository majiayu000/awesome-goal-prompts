#!/usr/bin/env python3
"""Validate source TOML files before regeneration.

Checks invariants that the generator alone does not enforce, so contributors
get an actionable error before CI runs. Reads only data/source/*.toml.
"""

from __future__ import annotations

import sys
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "data" / "source"

SOURCE_TYPES = {
    "official-goal",
    "official-workflow",
    "official-agent-task",
    "third-party-tutorial",
    "third-party-review",
    "third-party-project",
    "x-post",
    "public-forum",
    "github-issue",
    "github-pr",
    "github-discussion",
    "tool-readme",
    "video-summary",
}

VALID_ORIGINS = {"seed", "source-backed"}
VALID_DIFFICULTIES = {"intermediate", "advanced"}


def fail(messages: list[str]) -> None:
    sys.stderr.write("data validation failed:\n")
    for message in messages:
        sys.stderr.write(f"  - {message}\n")
    sys.exit(1)


def load_toml(path: Path, key: str) -> list[dict] | dict:
    with path.open("rb") as fh:
        data = tomllib.load(fh)
    if key not in data:
        return []
    return data[key]


def validate_categories(categories: dict[str, dict]) -> list[str]:
    errors: list[str] = []
    for name, meta in categories.items():
        if not isinstance(meta.get("context"), str) or not meta["context"]:
            errors.append(f"category '{name}': missing or empty 'context'")
        if not isinstance(meta.get("inspect"), str) or not meta["inspect"]:
            errors.append(f"category '{name}': missing or empty 'inspect'")
        difficulty = meta.get("difficulty")
        if difficulty not in VALID_DIFFICULTIES:
            errors.append(f"category '{name}': difficulty must be one of {sorted(VALID_DIFFICULTIES)}, got {difficulty!r}")
        constraints = meta.get("constraints")
        if not isinstance(constraints, list):
            errors.append(f"category '{name}': constraints must be a list")
    return errors


def validate_entries(entries: list[dict], categories: dict[str, dict]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    required_seed = ("id", "category", "title", "intent", "verify", "origin")
    required_sourced = required_seed + ("source_url", "source_name", "source_type", "evidence")

    for entry in entries:
        entry_id = entry.get("id", "<missing-id>")
        origin = entry.get("origin")

        if entry_id in seen_ids:
            errors.append(f"duplicate id: {entry_id}")
        seen_ids.add(entry_id)

        if origin not in VALID_ORIGINS:
            errors.append(f"entry '{entry_id}': origin must be one of {sorted(VALID_ORIGINS)}, got {origin!r}")
            continue

        required = required_sourced if origin == "source-backed" else required_seed
        for field in required:
            value = entry.get(field)
            if not isinstance(value, str) or not value:
                errors.append(f"entry '{entry_id}': missing or empty required field '{field}'")

        category = entry.get("category")
        if isinstance(category, str) and category not in categories:
            errors.append(f"entry '{entry_id}': category '{category}' not declared in categories.toml")

        if origin == "source-backed":
            source_url = entry.get("source_url")
            if isinstance(source_url, str) and not (source_url.startswith("http://") or source_url.startswith("https://")):
                errors.append(f"entry '{entry_id}': source_url must start with http:// or https://, got {source_url!r}")
            source_type = entry.get("source_type")
            if isinstance(source_type, str) and source_type not in SOURCE_TYPES:
                errors.append(f"entry '{entry_id}': source_type '{source_type}' not in SOURCES.md whitelist")

    return errors


def validate_recipes(recipes: list[dict], categories: dict[str, dict]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()
    valid_origins = VALID_ORIGINS | {"all"}
    for recipe in recipes:
        rid = recipe.get("id", "<missing-id>")
        if rid in seen_ids:
            errors.append(f"duplicate recipe id: {rid}")
        seen_ids.add(rid)
        for field in ("id", "label", "label_zh", "query", "category", "origin"):
            value = recipe.get(field)
            if not isinstance(value, str):
                errors.append(f"recipe '{rid}': missing or non-string field '{field}'")
        category = recipe.get("category")
        if isinstance(category, str) and category != "all" and category not in categories:
            errors.append(f"recipe '{rid}': category '{category}' not declared in categories.toml")
        origin = recipe.get("origin")
        if isinstance(origin, str) and origin not in valid_origins:
            errors.append(f"recipe '{rid}': origin must be one of {sorted(valid_origins)}, got {origin!r}")
    return errors


def main() -> None:
    categories = load_toml(SOURCE_DIR / "categories.toml", "categories")
    entries = load_toml(SOURCE_DIR / "entries.toml", "entries")
    recipes = load_toml(SOURCE_DIR / "recipes.toml", "recipes")

    errors: list[str] = []
    errors += validate_categories(categories)
    errors += validate_entries(entries, categories)
    errors += validate_recipes(recipes, categories)

    if errors:
        fail(errors)

    print(f"data validation ok ({len(entries)} entries, {len(recipes)} recipes, {len(categories)} categories)")


if __name__ == "__main__":
    main()
