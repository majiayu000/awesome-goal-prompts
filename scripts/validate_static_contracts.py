#!/usr/bin/env python3
"""Validate static contract page rendering safety."""

from pathlib import Path
from string import Template

import generate_static_contracts


ROOT = Path(__file__).resolve().parents[1]


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def render(entry: dict[str, str]) -> str:
    template = Template((ROOT / "templates" / "static_goal.html").read_text(encoding="utf-8"))
    return generate_static_contracts.render_page(entry, template)


def main() -> None:
    base_entry = {
        "slug": "static-render-safety",
        "title": 'Static "Render" <Safety>',
        "intent": 'Ensure prompt text cannot break attributes or HTML <tags>.',
        "prompt": '</pre><script>alert(1)</script><pre><img src=x onerror=alert(1)>',
        "difficulty": "intermediate",
        "category": "security-appsec",
        "origin": "source-backed",
        "source_name": 'Example "Source"',
        "source_url": "https://example.com/path?q=1&ok=true",
        "evidence_summary": "Synthetic safety fixture <not a catalog entry>.",
    }

    page = render(base_entry)
    require("</pre><script>alert(1)</script><pre>" not in page, "prompt closed <pre> and injected script")
    require("<img src=x onerror=alert(1)>" not in page, "prompt injected raw HTML")
    require("&lt;/pre&gt;&lt;script&gt;alert(1)&lt;/script&gt;&lt;pre&gt;" in page, "prompt was not HTML-escaped")
    require("Static &quot;Render&quot; &lt;Safety&gt;" in page, "title was not attribute/text escaped")
    require("https://example.com/path?q=1&amp;ok=true" in page, "safe URL was not escaped for HTML")

    bad_url_entry = dict(base_entry)
    bad_url_entry["source_url"] = "javascript:alert(1)"
    try:
        render(bad_url_entry)
    except ValueError as exc:
        require("source_url must be an absolute http(s) URL" in str(exc), "unexpected unsafe URL error")
    else:
        raise AssertionError("unsafe source_url did not fail")

    print("static contract rendering validation ok")


if __name__ == "__main__":
    main()
