#!/usr/bin/env python3
"""Generate the curated `/goal` example catalog.

Source data lives in `data/source/*.toml`. This script renders the published
artifacts (catalog JSON, the long catalog markdown, and the generated regions
of README.md). Edit the TOML data, not the generated outputs.
"""

from __future__ import annotations

import json
import re
import tomllib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DIR = ROOT / "data" / "source"


def load_categories() -> dict[str, dict[str, object]]:
    with (SOURCE_DIR / "categories.toml").open("rb") as fh:
        return tomllib.load(fh)["categories"]


def load_recipes() -> list[dict[str, str]]:
    with (SOURCE_DIR / "recipes.toml").open("rb") as fh:
        return tomllib.load(fh)["recipes"]


def load_entries(categories: dict[str, dict[str, object]]) -> list[dict[str, str | None]]:
    with (SOURCE_DIR / "entries.toml").open("rb") as fh:
        raw_entries = tomllib.load(fh)["entries"]
    entries: list[dict[str, str | None]] = []
    for raw in raw_entries:
        category = raw["category"]
        if category not in categories:
            raise SystemExit(f"unknown category in entries.toml: {category}")
        slug = raw["id"]
        origin = raw["origin"]
        source_url = raw.get("source_url")
        source_name = raw.get("source_name")
        source_type = raw.get("source_type")
        evidence = raw.get("evidence")
        evidence_summary_value = None
        if origin == "source-backed":
            if not (source_url and source_name and source_type and evidence):
                raise SystemExit(f"source-backed entry missing required fields: {slug}")
            evidence_summary_value = evidence_summary(source_name, source_type, evidence, raw["verify"])
        entries.append(
            {
                "id": slug,
                "slug": slug,
                "category": category,
                "title": raw["title"],
                "intent": raw["intent"],
                "verify": raw["verify"],
                "difficulty": str(categories[category]["difficulty"]),
                "origin": origin,
                "source_url": source_url,
                "source_name": source_name,
                "source_type": source_type,
                "evidence": evidence,
                "evidence_summary": evidence_summary_value,
            }
        )
    slugs = [str(entry["slug"]) for entry in entries]
    if len(slugs) != len(set(slugs)):
        duplicates = sorted({slug for slug in slugs if slugs.count(slug) > 1})
        raise SystemExit(f"duplicate slugs: {', '.join(duplicates)}")
    return entries


def evidence_summary(source_name: str, source_type: str, evidence: str, verify: str) -> str:
    return f"{evidence}; source: {source_name}; type: {source_type}; verification: {verify}"


def constraints_for(category: str, categories: dict[str, dict[str, object]]) -> list[str]:
    base = [
        "Keep the scope limited to this goal; do not expand into unrelated cleanup.",
        "Do not weaken tests, delete assertions, or mask errors to make verification pass.",
        "Respect the repository's AGENTS.md/CLAUDE.md instructions and existing patterns.",
    ]
    category_specific = categories[category].get("constraints", [])
    return base + list(category_specific)  # type: ignore[arg-type]


def prompt_for(entry: dict[str, str | None], categories: dict[str, dict[str, object]]) -> str:
    category = str(entry["category"])
    category_data = categories[category]
    context_label = str(category_data["context"])
    inspect_scope = str(category_data["inspect"])
    constraints = "\n".join(f"- {item}" for item in constraints_for(category, categories))
    return f"""/goal
GOAL:
Complete {entry["title"]} for {context_label}: {entry["intent"]}

CONTEXT:
- Before editing, read the nearest AGENTS.md/CLAUDE.md, current issue or PLAN.md, and any failing logs already in the repo.
- Inspect {inspect_scope}.
- Establish a baseline by running or locating evidence for: `{entry["verify"]}`.

CONSTRAINTS:
{constraints}

DONE WHEN:
- The implementation or documentation directly satisfies: {entry["intent"]}
- The verification command or evidence path succeeds: `{entry["verify"]}`.
- The final diff is scoped to the relevant files and has no unrelated formatting churn.

VERIFY:
- Run `{entry["verify"]}` or the closest repo-local equivalent if the exact command is not available.
- Capture before/after evidence for the behavior, metric, report, or artifact involved.
- If verification cannot run locally, stop and report the missing dependency instead of guessing success.

OUTPUT:
- Summarize changed files, key decisions, verification output, and remaining risks.
- Include any follow-up that is required for production rollout or human review.

STOP RULES:
- Pause if secrets, production access, stakeholder decisions, or destructive data operations are required.
- Pause after three failed fix attempts on the same symptom and challenge the root-cause hypothesis.
- Do not mark the goal complete until the current repository state has been audited against DONE WHEN."""


def by_category(entries: list[dict[str, str | None]]) -> dict[str, list[dict[str, str | None]]]:
    grouped: dict[str, list[dict[str, str | None]]] = {}
    for entry in entries:
        grouped.setdefault(str(entry["category"]), []).append(entry)
    return grouped


def source_line(entry: dict[str, str | None]) -> str | None:
    if entry.get("source_url") and entry.get("source_name"):
        parts = [f"- Source: [{entry['source_name']}]({entry['source_url']})"]
        if entry.get("source_type"):
            parts.append(f"- Source type: `{entry['source_type']}`")
        if entry.get("evidence"):
            parts.append(f"- Evidence: {entry['evidence']}")
        if entry.get("evidence_summary"):
            parts.append(f"- Evidence summary: {entry['evidence_summary']}")
        return "\n".join(parts)
    return None


def build_markdown(entries: list[dict[str, str | None]]) -> str:
    lines = [
        "# Goal Prompt Examples",
        "",
        "Each example is a complete `/goal` task contract. Replace placeholder commands, paths, and project names with your repository's real values before running.",
        "",
        "These examples intentionally use only the documented `/goal <goal>` form. They do not rely on unofficial subcommands.",
        "",
        "## Index",
        "",
    ]
    for category, category_entries in by_category(entries).items():
        lines.append(f"### {category}")
        for entry in category_entries:
            suffix = " Source-backed." if entry["origin"] == "source-backed" else ""
            lines.append(f"- [{entry['title']}](#{entry['slug']}) - {entry['intent']}{suffix}")
        lines.append("")
    lines.append("## Examples")
    lines.append("")
    for entry in entries:
        source = source_line(entry)
        lines.extend(
            [
                f'<a id="{entry["slug"]}"></a>',
                f"### {entry['title']}",
                "",
                f"- Category: `{entry['category']}`",
                f"- Difficulty: `{entry['difficulty']}`",
                f"- Origin: `{entry['origin']}`",
                f"- Intent: {entry['intent']}",
                f"- Verification: `{entry['verify']}`",
            ]
        )
        if source:
            lines.append(source)
        lines.extend(
            [
                "",
                "```text",
                str(entry["prompt"]),
                "```",
                "",
            ]
        )
    return "\n".join(lines).rstrip() + "\n"


MARKER_PATTERN = re.compile(
    r"<!-- generated:(\w+)-start -->(.*?)<!-- generated:\1-end -->",
    re.DOTALL,
)


def replace_markers(text: str, sections: dict[str, str]) -> str:
    seen: set[str] = set()

    def substitute(match: re.Match[str]) -> str:
        name = match.group(1)
        seen.add(name)
        if name not in sections:
            raise SystemExit(f"README contains unknown generated marker: {name}")
        return f"<!-- generated:{name}-start -->{sections[name]}<!-- generated:{name}-end -->"

    result = MARKER_PATTERN.sub(substitute, text)
    missing = set(sections) - seen
    if missing:
        raise SystemExit(f"README missing markers: {', '.join(sorted(missing))}")
    return result


def build_stats_section(entries: list[dict[str, str | None]]) -> str:
    source_backed = sum(1 for entry in entries if entry["origin"] == "source-backed")
    body = (
        f"Of those, **{source_backed}** are source-backed examples drawn from "
        "official docs, public GitHub threads, tutorials, forum posts, and tool "
        "READMEs; the rest are reusable seed patterns."
    )
    return f"\n{body}\n"


def build_catalog_section(entries: list[dict[str, str | None]]) -> str:
    lines: list[str] = []
    for category, category_entries in by_category(entries).items():
        lines.append(f"### {category}")
        for entry in category_entries:
            marker = " _(source-backed)_" if entry["origin"] == "source-backed" else ""
            lines.append(
                f"- [{entry['title']}](prompts/goal-examples.md#{entry['slug']}) - {entry['intent']}{marker}"
            )
        lines.append("")
    body = "\n".join(lines).rstrip()
    return f"\n{body}\n"


def build_total_section(entries: list[dict[str, str | None]]) -> str:
    return f"**{len(entries)}**"


def main() -> None:
    categories = load_categories()
    recipes = load_recipes()
    entries = load_entries(categories)
    for entry in entries:
        entry["prompt"] = prompt_for(entry, categories)

    (ROOT / "prompts").mkdir(exist_ok=True)
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "docs").mkdir(exist_ok=True)
    (ROOT / "prompts" / "goal-examples.md").write_text(build_markdown(entries), encoding="utf-8")
    examples_json = json.dumps(entries, indent=2, ensure_ascii=True) + "\n"
    recipes_json = json.dumps(recipes, indent=2, ensure_ascii=True) + "\n"
    (ROOT / "data" / "examples.json").write_text(examples_json, encoding="utf-8")
    (ROOT / "docs" / "examples.json").write_text(examples_json, encoding="utf-8")
    (ROOT / "data" / "recipes.json").write_text(recipes_json, encoding="utf-8")
    (ROOT / "docs" / "recipes.json").write_text(recipes_json, encoding="utf-8")

    readme_path = ROOT / "README.md"
    readme_text = readme_path.read_text(encoding="utf-8")
    readme_text = replace_markers(
        readme_text,
        {
            "total": build_total_section(entries),
            "stats": build_stats_section(entries),
            "catalog": build_catalog_section(entries),
        },
    )
    readme_path.write_text(readme_text, encoding="utf-8")

    print(f"generated goal catalog ({len(entries)} entries, {len(recipes)} recipes)")


if __name__ == "__main__":
    main()
