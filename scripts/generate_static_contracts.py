#!/usr/bin/env python3
"""
混合渲染 SEO 方案 - 静态 Goal Contract 页面生成器

用法：
    python scripts/generate_static_contracts.py --output docs/goals

特点：
- 优先选择 source-backed（有真实来源）的 contracts
- 生成干净、SEO 友好的静态 HTML
- 默认生成所有 source-backed contracts
- 自动生成 sitemap 片段（可选）
"""

import argparse
import html
import json
from pathlib import Path
from string import Template
from typing import Any
from urllib.parse import urlparse

from static_contract_policy import static_contract_entries

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / "data" / "examples.json"
TEMPLATE_FILE = ROOT / "templates" / "static_goal.html"
OUTPUT_DIR = ROOT / "docs" / "goals"

def clean_text(text: str | None) -> str:
    if not text:
        return ""
    return html.escape(str(text), quote=True)


def require_http_url(url: str | None, field_name: str = "source_url") -> str:
    if not url:
        raise ValueError(f"{field_name} is required")
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ValueError(f"{field_name} must be an absolute http(s) URL: {url!r}")
    return clean_text(url)


def generate_source_badge(entry: dict[str, Any]) -> str:
    if entry.get("source_name") and entry.get("source_url"):
        return f'<span class="badge">来源：{clean_text(entry["source_name"])}</span>'
    if entry.get("origin") == "seed":
        return '<span class="badge">Seed Pattern</span>'
    return ""


def generate_source_section(entry: dict[str, Any]) -> str:
    if not entry.get("source_url"):
        return ""
    url = require_http_url(entry["source_url"])
    name = clean_text(entry.get("source_name") or url)
    evidence = clean_text(entry.get("evidence_summary") or entry.get("evidence") or "")

    html = f"""
  <div class="section">
    <h2>来源与证据</h2>
    <div class="source">
      <p><strong>原始来源：</strong> <a href="{url}" target="_blank" rel="noopener">{name}</a></p>
      {f"<p><strong>证据摘要：</strong> {evidence}</p>" if evidence else ""}
    </div>
  </div>
"""
    return html


def render_page(entry: dict[str, Any], template: Template) -> str:
    slug = clean_text(entry["slug"])
    title = clean_text(entry["title"])
    intent = clean_text(entry["intent"])
    prompt = clean_text(entry.get("prompt", "").strip())
    difficulty = clean_text(entry.get("difficulty", "unknown"))
    category = clean_text(entry.get("category", "general"))

    source_badge = generate_source_badge(entry)
    source_section = generate_source_section(entry)

    return template.substitute(
        title=title,
        intent=intent,
        slug=slug,
        prompt=prompt,
        difficulty=difficulty,
        category=category,
        source_badge=source_badge,
        source_section=source_section,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="生成静态 SEO 友好的 Goal Contract 页面")
    parser.add_argument("--limit", type=int, default=None, help="最多生成多少个 source-backed 页面（默认全部）")
    parser.add_argument("--output", type=str, default=str(OUTPUT_DIR), help="输出目录")
    parser.add_argument("--sitemap", action="store_true", help="同时生成 sitemap 片段")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 加载数据
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        entries: list[dict[str, Any]] = json.load(f)

    selected_entries = static_contract_entries(entries)
    if args.limit is not None:
        selected_entries = selected_entries[: args.limit]
    expected_files = {f"{entry['slug']}.html" for entry in selected_entries}

    # 加载模板
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = Template(f.read())

    for stale_path in sorted(output_dir.glob("*.html")):
        if stale_path.name not in expected_files:
            stale_path.unlink()
            print(f"✓ Removed stale: goals/{stale_path.name}")

    generated = []

    for entry in selected_entries:
        slug = entry["slug"]
        html = render_page(entry, template)

        out_path = output_dir / f"{slug}.html"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(html)

        generated.append(slug)
        print(f"✓ Generated: goals/{slug}.html")

    print(f"\n完成！共生成 {len(generated)} 个静态页面 → {output_dir}")

    if args.sitemap:
        sitemap_path = output_dir / "sitemap-goals.xml"
        with open(sitemap_path, "w", encoding="utf-8") as f:
            f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
            f.write('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
            for slug in generated:
                f.write(f"  <url>\n")
                f.write(f"    <loc>https://majiayu000.github.io/awesome-goal-prompts/goals/{slug}.html</loc>\n")
                f.write(f"    <lastmod>2026-05-29</lastmod>\n")
                f.write(f"    <changefreq>monthly</changefreq>\n")
                f.write(f"    <priority>0.7</priority>\n")
                f.write(f"  </url>\n")
            f.write("</urlset>\n")
        print(f"✓ Sitemap 片段已生成: {sitemap_path}")


if __name__ == "__main__":
    main()
