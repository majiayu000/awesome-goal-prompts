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
SITE_URL = "https://majiayu000.github.io/awesome-goal-prompts/"
SITE_TITLE = "Awesome Goal Prompts - /goal contracts for coding agents"
SITE_DESCRIPTION = "300+ runnable /goal contracts for Codex, Claude Code, Cursor, and other coding agents."
SITE_IMAGE_ALT = "Awesome Goal Prompts - searchable goal contracts for coding agents."
DATASET_DESCRIPTION = (
    "A searchable catalog of runnable /goal task contracts for coding agents, "
    "with source-backed examples and reusable seed patterns."
)
ITEMLIST_DESCRIPTION = "Source-backed task contracts in the primary catalog."
STATIC_CONTRACT_URL_COUNT = 25
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


def build_markdown(entries: list[dict[str, str | None]], title: str, description: list[str]) -> str:
    lines = [
        f"# {title}",
        "",
        *description,
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


def build_index_markdown(entries: list[dict[str, str | None]], title: str, description: list[str]) -> str:
    lines = [f"# {title}", "", *description, "", "## Index", ""]
    for category, category_entries in by_category(entries).items():
        lines.append(f"### {category}")
        for entry in category_entries:
            lines.append(f'<a id="{entry["slug"]}"></a>')
            lines.append(
                f"- [{entry['title']}](goal-examples.md#{entry['slug']}) - {entry['intent']}"
            )
        lines.append("")
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
    seed = len(entries) - source_backed
    body = (
        f"The public catalog starts with **{source_backed}** source-backed examples drawn from "
        "official docs, public GitHub threads, tutorials, forum posts, and tool READMEs. "
        f"The other **{seed}** reusable seed patterns are kept in "
        "[Seed Patterns](prompts/seed-patterns.md) so they do not dilute provenance-backed examples."
    )
    return f"\n{body}\n"


def build_catalog_section(entries: list[dict[str, str | None]]) -> str:
    lines: list[str] = []
    source_entries = [entry for entry in entries if entry["origin"] == "source-backed"]
    for category, category_entries in by_category(source_entries).items():
        lines.append(f"### {category}")
        for entry in category_entries:
            lines.append(
                f"- [{entry['title']}](prompts/source-backed-goals.md#{entry['slug']}) - {entry['intent']}"
            )
        lines.append("")
    body = "\n".join(lines).rstrip()
    return f"\n{body}\n"


def build_total_section(entries: list[dict[str, str | None]]) -> str:
    bucket = max(100, (len(entries) // 100) * 100)
    return f"**{bucket}+**"


def build_json_ld(entries: list[dict[str, str | None]]) -> str:
    source_entries = [entry for entry in entries if entry["origin"] == "source-backed"]
    source_backed = len(source_entries)
    creator = {"@type": "Person", "name": "majiayu000", "url": "https://github.com/majiayu000"}
    keywords = [
        "coding agents",
        "prompt engineering",
        "AI agents",
        "Claude Code",
        "Codex",
        "Hermes",
        "task contracts",
        "goal prompts",
    ]

    def item_url(index: int, entry: dict[str, str | None]) -> str:
        if index <= STATIC_CONTRACT_URL_COUNT:
            return f"{SITE_URL}goals/{entry['slug']}.html"
        return f"{SITE_URL}#{entry['slug']}"

    graph = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "WebSite",
                "@id": f"{SITE_URL}#website",
                "url": SITE_URL,
                "name": SITE_TITLE,
                "description": SITE_DESCRIPTION,
                "inLanguage": ["en", "zh-CN"],
                "publisher": creator,
                "potentialAction": {
                    "@type": "SearchAction",
                    "target": f"{SITE_URL}?q={{search_term_string}}",
                    "query-input": "required name=search_term_string",
                },
            },
            {
                "@type": "Dataset",
                "@id": f"{SITE_URL}#dataset",
                "name": "Awesome Goal Prompts",
                "alternateName": "The Contract Codex",
                "description": DATASET_DESCRIPTION,
                "url": SITE_URL,
                "keywords": keywords,
                "license": "https://github.com/majiayu000/awesome-goal-prompts/blob/main/LICENSE",
                "isAccessibleForFree": True,
                "creator": creator,
                "codeRepository": "https://github.com/majiayu000/awesome-goal-prompts",
                "version": "0.1.2",
                "inLanguage": ["en", "zh-CN"],
            },
            {
                "@type": "ItemList",
                "@id": f"{SITE_URL}#contracts",
                "name": "Source-Backed Goal Prompt Contracts",
                "description": ITEMLIST_DESCRIPTION,
                "numberOfItems": source_backed,
                "itemListOrder": "https://schema.org/ItemListOrderAscending",
                # Keep the linked ItemList scoped to evidence-backed catalog entries;
                # seed patterns are counted in Dataset metadata but omitted here.
                "itemListElement": [
                    {
                        "@type": "ListItem", "position": index, "url": item_url(index, entry),
                        "name": entry["title"], "description": entry["intent"],
                    }
                    for index, entry in enumerate(source_entries, start=1)
                ],
            },
        ],
    }
    return json.dumps(graph, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")


def update_static_metadata(entries: list[dict[str, str | None]]) -> None:
    index_path = ROOT / "docs" / "index.html"
    index_text = index_path.read_text(encoding="utf-8")
    replacements = {
        r'<meta name="description" content="[^"]*">': (
            f'<meta name="description" content="{SITE_DESCRIPTION}">'
        ),
        r"<title>.*?</title>": (
            f"<title>{SITE_TITLE}</title>"
        ),
        r'<meta property="og:title" content="[^"]*">': (
            f'<meta property="og:title" content="{SITE_TITLE}">'
        ),
        r'<meta property="og:description" content="[^"]*">': (
            f'<meta property="og:description" content="{SITE_DESCRIPTION}">'
        ),
        r'<meta property="og:image:alt" content="[^"]*">': (
            f'<meta property="og:image:alt" content="{SITE_IMAGE_ALT}">'
        ),
        r'<meta name="twitter:title" content="[^"]*">': (
            f'<meta name="twitter:title" content="{SITE_TITLE}">'
        ),
        r'<meta name="twitter:description" content="[^"]*">': (
            f'<meta name="twitter:description" content="{SITE_DESCRIPTION}">'
        ),
        r'<meta name="twitter:image:alt" content="[^"]*">': (
            f'<meta name="twitter:image:alt" content="{SITE_IMAGE_ALT}">'
        ),
        r'<script type="application/ld\+json">.*?</script>': (
            f'<script type="application/ld+json">{build_json_ld(entries)}</script>'
        ),
    }
    for pattern, replacement in replacements.items():
        index_text, count = re.subn(pattern, replacement, index_text, count=1, flags=re.DOTALL)
        if count != 1:
            raise SystemExit(f"failed to update docs/index.html metadata for pattern: {pattern}")
    index_path.write_text(index_text, encoding="utf-8")

    docs_path = ROOT / "docs" / "docs.html"
    docs_text = docs_path.read_text(encoding="utf-8")
    docs_text, count = re.subn(
        r'<meta property="og:image:alt" content="[^"]*">',
        f'<meta property="og:image:alt" content="{SITE_IMAGE_ALT}">',
        docs_text,
        count=1,
    )
    if count != 1:
        raise SystemExit("failed to update docs/docs.html image alt metadata")
    docs_path.write_text(docs_text, encoding="utf-8")


def main() -> None:
    categories = load_categories()
    recipes = load_recipes()
    entries = load_entries(categories)
    for entry in entries:
        entry["prompt"] = prompt_for(entry, categories)

    (ROOT / "prompts").mkdir(exist_ok=True)
    (ROOT / "data").mkdir(exist_ok=True)
    (ROOT / "docs").mkdir(exist_ok=True)
    common_description = [
        "Each example is a complete `/goal` task contract. Replace placeholder commands, paths, and project names with your repository's real values before running.",
        "",
        "These examples intentionally use only the documented `/goal <goal>` form. They do not rely on unofficial subcommands.",
    ]
    source_entries = [entry for entry in entries if entry["origin"] == "source-backed"]
    seed_entries = [entry for entry in entries if entry["origin"] == "seed"]
    (ROOT / "prompts" / "goal-examples.md").write_text(
        build_markdown(entries, "Goal Prompt Examples", common_description),
        encoding="utf-8",
    )
    (ROOT / "prompts" / "source-backed-goals.md").write_text(
        build_index_markdown(
            source_entries,
            "Source-Backed Goal Contracts",
            ["These source-backed contracts are the primary catalog. Follow each link for the full prompt body in the complete archive."],
        ),
        encoding="utf-8",
    )
    (ROOT / "prompts" / "seed-patterns.md").write_text(
        build_index_markdown(
            seed_entries,
            "Seed Goal Patterns",
            ["These reusable patterns are not presented as collected from public sources. Prefer source-backed contracts first when credibility matters."],
        ),
        encoding="utf-8",
    )
    examples_json = json.dumps(entries, indent=2, ensure_ascii=True) + "\n"
    recipes_json = json.dumps(recipes, indent=2, ensure_ascii=True) + "\n"
    (ROOT / "data" / "examples.json").write_text(examples_json, encoding="utf-8")
    (ROOT / "docs" / "examples.json").write_text(examples_json, encoding="utf-8")
    (ROOT / "data" / "recipes.json").write_text(recipes_json, encoding="utf-8")
    (ROOT / "docs" / "recipes.json").write_text(recipes_json, encoding="utf-8")
    update_static_metadata(entries)

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
