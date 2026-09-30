#!/usr/bin/env python3
"""Regenerate sitemaps containing canonical, separately addressable pages.

Outputs:
  docs/sitemap.xml          full sitemap (home, docs, goals pages)
  docs/goals/sitemap-goals.xml   goals pages only
"""
from pathlib import Path

BASE_URL = "https://majiayu000.github.io/awesome-goal-prompts/"
ROOT = Path(__file__).resolve().parents[1]
DOCS_DIR = ROOT / "docs"
GOALS_DIR = DOCS_DIR / "goals"
SITEMAP_PATH = DOCS_DIR / "sitemap.xml"
GOALS_SITEMAP_PATH = GOALS_DIR / "sitemap-goals.xml"

HREFLANGS = ("en", "zh", "x-default")


def build_url_block(loc: str, changefreq: str,
                    priority: str, alternates: str = "") -> str:
    """Render one <url> element."""
    return (
        "  <url>\n"
        f"    <loc>{loc}</loc>\n"
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
    return [
        build_url_block(
            BASE_URL, "weekly", "1.0", build_alternates("")
        ),
        build_url_block(
            f"{BASE_URL}docs.html", "monthly", "0.8",
            build_alternates("docs.html"),
        ),
    ]


def collect_goals_blocks() -> list[str]:
    """One <url> per docs/goals/*.html, sorted by slug."""
    blocks = []
    for html in sorted(GOALS_DIR.glob("*.html")):
        slug = html.stem
        loc = f"{BASE_URL}goals/{slug}.html"
        blocks.append(build_url_block(loc, "monthly", "0.7"))
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

    full = render_urlset(localized + goals)
    with open(SITEMAP_PATH, "w", encoding="utf-8") as fh:
        fh.write(full)

    goals_only = render_urlset(goals)
    with open(GOALS_SITEMAP_PATH, "w", encoding="utf-8") as fh:
        fh.write(goals_only)

    print(f"sitemap.xml: {len(localized) + len(goals)} urls")
    print(f"sitemap-goals.xml: {len(goals)} urls")


if __name__ == "__main__":
    main()
