#!/usr/bin/env python3
"""Guard the public Pages docs surface against old/private content."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PUBLIC_SURFACE_FILES = [
    DOCS / "index.html",
    DOCS / "app.js",
    DOCS / "docs.html",
    DOCS / "docs-page.js",
    DOCS / "how-to-write-goals.md",
    DOCS / "how-to-write-goals.zh.md",
]

COMMUNITY_COPY = [
    "Community X",
    "\u793e\u533a X",
    "\u793e\u533a\u5e16\u5b50",
]

REMOVED_DOC_ENTRIES = [
    'id: "schema"',
    'id: "catalog-health"',
    "Data Schema",
    "Catalog Health",
    "\u6570\u636e\u7ed3\u6784",
    "\u76ee\u5f55\u5065\u5eb7\u62a5\u544a",
    "catalog schema",
    "checking catalog quality",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def docs_config_ids(text: str) -> list[str]:
    match = re.search(r"const docs = \[(.*?)\];", text, flags=re.S)
    if not match:
        return []
    return re.findall(r'\bid:\s*"([^"]+)"', match.group(1))


def main() -> None:
    failures: list[str] = []

    missing = [str(path.relative_to(ROOT)) for path in PUBLIC_SURFACE_FILES if not path.exists()]
    require(not missing, f"missing public surface files: {', '.join(missing)}", failures)
    if missing:
        raise SystemExit("\n".join(failures))

    public_text = {path: read(path) for path in PUBLIC_SURFACE_FILES}

    for path, text in public_text.items():
        for token in COMMUNITY_COPY:
            require(
                token not in text,
                f"{path.relative_to(ROOT)} still contains public docs copy token {token!r}",
                failures,
            )

    app_js = public_text[DOCS / "app.js"]
    require(
        "\u793a\u4f8b\u53ea\u7528\u6765\u770b\u7ed3\u6784" in app_js,
        "docs/app.js is missing the revised Chinese guide copy",
        failures,
    )

    docs_page = public_text[DOCS / "docs-page.js"]
    docs_html = public_text[DOCS / "docs.html"]
    docs_ids = docs_config_ids(docs_page)
    require(
        docs_ids == ["how-to-write"],
        f"docs-page.js should expose only ['how-to-write'], got {docs_ids!r}",
        failures,
    )
    require(
        'title_zh: "\u5982\u4f55\u5199\u597d /goal"' in docs_page,
        "docs-page.js is missing the Chinese guide title",
        failures,
    )
    require(
        "docs.find((doc) => doc.id === hash) || docs[0]" in docs_page,
        "old/unknown docs hashes must fall back to the first guide",
        failures,
    )
    require(
        "docs.find((item) => item.id === id) || docs[0]" in docs_page,
        "unknown selected docs must fall back to the first guide",
        failures,
    )

    for token in REMOVED_DOC_ENTRIES:
        require(token not in docs_page, f"docs-page.js still exposes {token!r}", failures)
        require(token not in docs_html, f"docs.html still exposes {token!r}", failures)

    require(
        "docs-ledger" not in docs_html and "docs-count" not in docs_html,
        "docs.html should not render multi-document statistics",
        failures,
    )
    require(
        not (DOCS / "launch-kit.md").exists(),
        "docs/launch-kit.md must stay absent so GitHub Pages returns 404",
        failures,
    )

    if failures:
        print("Public docs surface check failed:")
        for failure in failures:
            print(f"- {failure}")
        raise SystemExit(1)

    print("PASS public docs surface:")
    print("- homepage guide copy has no Community/X copy")
    print("- docs browser exposes only how-to-write")
    print("- schema and catalog-health are not exposed on docs.html")
    print("- old docs hashes fall back to the guide")
    print("- docs/launch-kit.md is absent")


if __name__ == "__main__":
    main()
