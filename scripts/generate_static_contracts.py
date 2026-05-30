#!/usr/bin/env python3
"""
混合渲染 SEO 方案 - 静态 Goal Contract 页面生成器

用法：
    python scripts/generate_static_contracts.py --limit 20 --output docs/goals

特点：
- 优先选择 source-backed（有真实来源）的 contracts
- 生成干净、SEO 友好的静态 HTML
- 可控制生成数量（先做最重要的）
- 自动生成 sitemap 片段（可选）
"""

import argparse
import json
import os
import re
from pathlib import Path
from string import Template
from typing import Any

ROOT = Path(__file__).parent.parent
DATA_FILE = ROOT / "data" / "examples.json"
TEMPLATE_FILE = ROOT / "templates" / "static_goal.html"
OUTPUT_DIR = ROOT / "docs" / "goals"

# 优先级排序：有真实来源的排在前面
def score_entry(entry: dict[str, Any]) -> int:
    score = 0
    if entry.get("source_url"):
        score += 100
    if entry.get("source_name"):
        score += 50
    if entry.get("origin") != "seed":
        score += 30
    if entry.get("difficulty") in ("intermediate", "advanced"):
        score += 10
    return score


def clean_text(text: str | None) -> str:
    if not text:
        return ""
    # 简单转义 HTML
    text = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return text


def generate_source_badge(entry: dict[str, Any]) -> str:
    if entry.get("source_name") and entry.get("source_url"):
        return f'<span class="badge">来源：{clean_text(entry["source_name"])}</span>'
    if entry.get("origin") == "seed":
        return '<span class="badge">Seed Pattern</span>'
    return ""


def generate_source_section(entry: dict[str, Any]) -> str:
    if not entry.get("source_url"):
        return ""
    url = clean_text(entry["source_url"])
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
    slug = entry["slug"]
    title = clean_text(entry["title"])
    intent = clean_text(entry["intent"])
    prompt = entry.get("prompt", "").strip()
    difficulty = entry.get("difficulty", "unknown")
    category = entry.get("category", "general")

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


def main():
    parser = argparse.ArgumentParser(description="生成静态 SEO 友好的 Goal Contract 页面")
    parser.add_argument("--limit", type=int, default=30, help="最多生成多少个页面（默认 30）")
    parser.add_argument("--output", type=str, default=str(OUTPUT_DIR), help="输出目录")
    parser.add_argument("--sitemap", action="store_true", help="同时生成 sitemap 片段")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    # 加载数据
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        entries: list[dict[str, Any]] = json.load(f)

    # 排序：优先 source-backed
    entries.sort(key=score_entry, reverse=True)

    # 加载模板
    with open(TEMPLATE_FILE, "r", encoding="utf-8") as f:
        template = Template(f.read())

    generated = []

    for entry in entries[: args.limit]:
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
