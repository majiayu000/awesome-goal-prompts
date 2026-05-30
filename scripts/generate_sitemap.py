#!/usr/bin/env python3
"""Regenerate sitemap.xml so lastmod reflects real git commit dates.

Outputs:
  docs/sitemap.xml          full sitemap (home, docs, goals pages, SPA anchors)
  docs/goals/sitemap-goals.xml   goals pages only
"""
import datetime
import json
import subprocess
from pathlib import Path

BASE_URL = "https://majiayu000.github.io/awesome-goal-prompts/"
ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
GOALS_DIR = DOCS_DIR / "goals"
EXAMPLES_JSON = DOCS_DIR / "examples.json"
SITEMAP_PATH = DOCS_DIR / "sitemap.xml"
GOALS_SITEMAP_PATH = GOALS_DIR / "sitemap-goals.xml"

HREFLANGS = ("en", "zh", "x-default")


def git_last_modified(rel_path: str) -> str:
    """Return the last git commit date (YYYY-MM-DD) for rel_path.

    Falls back to today's date when the file has no git history or the
    command fails. Uses array args (no shell) per SEC-01.
    """
    today = datetime.date.today().isoformat()
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", rel_path],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
    except (OSError, subprocess.SubprocessError):
        return today
    if result.returncode != 0:
        return today
    date = result.stdout.strip()
    return date if date else today


def build_url_block(loc: str, lastmod: str, changefreq: str,
                    priority: str, alternates: str = "") -> str:
    """Render one <url> element."""
    return (
        "  <url>\n"
        f"    <loc>{loc}</loc>\n"
        f"    <lastmod>{lastmod}</lastmod>\n"
        f"    <changefreq>{changefreq}</changefreq>\n"
        f"    <priority>{priority}</priority>\n"
        f"{alternates}"
        "  </url>\n"
    )


def build_alternates(path: str) -> str:
    """Render xhtml:link hreflang alternates for a localized page."""
    rows = []
    for lang in HREFLANGS:
        href = f"{BASE_URL}{path}"
        if lang != "x-default":
            sep = "&" if "?" in path else "?"
            href = f"{BASE_URL}{path}{sep}lang={lang}"
        rows.append(
            f'    <xhtml:link rel="alternate" hreflang="{lang}" href="{href}"/>\n'
        )
    return "".join(rows)


def collect_localized_blocks() -> list[str]:
    """Home + docs.html with hreflang alternates."""
    home_mod = git_last_modified("docs/index.html")
    docs_mod = git_last_modified("docs/docs.html")
    return [
        build_url_block(
            BASE_URL, home_mod, "weekly", "1.0", build_alternates("")
        ),
        build_url_block(
            f"{BASE_URL}docs.html", docs_mod, "monthly", "0.8",
            build_alternates("docs.html"),
        ),
    ]


def collect_goals_blocks() -> list[str]:
    """One <url> per docs/goals/*.html, sorted by slug."""
    blocks = []
    for html in sorted(GOALS_DIR.glob("*.html")):
        slug = html.stem
        mod = git_last_modified(f"docs/goals/{html.name}")
        loc = f"{BASE_URL}goals/{slug}.html"
        blocks.append(build_url_block(loc, mod, "monthly", "0.7"))
    return blocks


def collect_anchor_blocks() -> list[str]:
    """SPA anchors /#<slug> from examples.json, sharing its commit date."""
    anchor_mod = git_last_modified("docs/examples.json")
    with open(EXAMPLES_JSON, encoding="utf-8") as fh:
        entries = json.load(fh)
    blocks = []
    for entry in entries:
        loc = f"{BASE_URL}#{entry['slug']}"
        blocks.append(build_url_block(loc, anchor_mod, "monthly", "0.5"))
    return blocks


def render_urlset(blocks: list[str]) -> str:
    """Wrap url blocks in an xhtml-aware urlset document."""
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"\n'
        '        xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
        f"{''.join(blocks)}"
        "</urlset>\n"
    )


def main() -> None:
    localized = collect_localized_blocks()
    goals = collect_goals_blocks()
    anchors = collect_anchor_blocks()

    full = render_urlset(localized + goals + anchors)
    with open(SITEMAP_PATH, "w", encoding="utf-8") as fh:
        fh.write(full)

    goals_only = render_urlset(goals)
    with open(GOALS_SITEMAP_PATH, "w", encoding="utf-8") as fh:
        fh.write(goals_only)

    print(f"sitemap.xml: {len(localized) + len(goals) + len(anchors)} urls")
    print(f"sitemap-goals.xml: {len(goals)} urls")


if __name__ == "__main__":
    main()
