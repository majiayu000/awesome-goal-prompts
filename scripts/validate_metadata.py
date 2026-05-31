#!/usr/bin/env python3
"""Validate generated catalog metadata against docs/examples.json.

The JSON-LD ItemList is intentionally scoped to source-backed entries. Seed
patterns are counted in Dataset and social metadata, but not listed as primary
evidence-backed contracts.
"""

from __future__ import annotations

import json
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

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


class IndexMetadataParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: dict[str, str] = {}
        self.title = ""
        self.json_ld_scripts: list[str] = []
        self._capturing_title = False
        self._capturing_json_ld = False
        self._script_chunks: list[str] = []
        self._title_chunks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        if tag == "meta":
            key = attributes.get("property") or attributes.get("name")
            content = attributes.get("content")
            if key and content is not None:
                self.meta[key] = content
        if tag == "script" and attributes.get("type") == "application/ld+json":
            self._capturing_json_ld = True
            self._script_chunks = []
        if tag == "title":
            self._capturing_title = True
            self._title_chunks = []

    def handle_data(self, data: str) -> None:
        if self._capturing_title:
            self._title_chunks.append(data)
        if self._capturing_json_ld:
            self._script_chunks.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title" and self._capturing_title:
            self.title = "".join(self._title_chunks).strip()
            self._capturing_title = False
            self._title_chunks = []
        if tag == "script" and self._capturing_json_ld:
            self.json_ld_scripts.append("".join(self._script_chunks).strip())
            self._capturing_json_ld = False
            self._script_chunks = []


def fail(message: str) -> None:
    raise SystemExit(message)


def assert_equal(label: str, actual: object, expected: object) -> None:
    if actual != expected:
        fail(f"{label} mismatch: expected {expected!r}, got {actual!r}")


def find_graph_node(graph: list[Any], node_type: str) -> dict[str, Any]:
    for node in graph:
        if isinstance(node, dict) and node.get("@type") == node_type:
            return node
    fail(f"JSON-LD missing {node_type} node")


def main() -> None:
    entries = json.loads((ROOT / "docs" / "examples.json").read_text(encoding="utf-8"))
    if not isinstance(entries, list):
        fail("docs/examples.json must contain a list")

    source_entries = [entry for entry in entries if entry.get("origin") == "source-backed"]
    source_count = len(source_entries)
    seed_count = len(entries) - source_count

    parser = IndexMetadataParser()
    parser.feed((ROOT / "docs" / "index.html").read_text(encoding="utf-8"))

    assert_equal("title", parser.title, SITE_TITLE)
    assert_equal("description", parser.meta.get("description"), SITE_DESCRIPTION)
    assert_equal("og:title", parser.meta.get("og:title"), SITE_TITLE)
    assert_equal("twitter:title", parser.meta.get("twitter:title"), SITE_TITLE)
    assert_equal("og:description", parser.meta.get("og:description"), SITE_DESCRIPTION)
    assert_equal("twitter:description", parser.meta.get("twitter:description"), SITE_DESCRIPTION)
    assert_equal("og:image:alt", parser.meta.get("og:image:alt"), SITE_IMAGE_ALT)
    assert_equal("twitter:image:alt", parser.meta.get("twitter:image:alt"), SITE_IMAGE_ALT)

    assert_equal("JSON-LD script count", len(parser.json_ld_scripts), 1)
    payload = json.loads(parser.json_ld_scripts[0])
    graph = payload.get("@graph")
    if not isinstance(graph, list):
        fail("JSON-LD @graph must be a list")

    dataset = find_graph_node(graph, "Dataset")
    website = find_graph_node(graph, "WebSite")
    item_list = find_graph_node(graph, "ItemList")
    assert_equal("WebSite name", website.get("name"), SITE_TITLE)
    assert_equal("WebSite description", website.get("description"), SITE_DESCRIPTION)
    assert_equal("Dataset description", dataset.get("description"), DATASET_DESCRIPTION)
    assert_equal(
        "Source-backed ItemList name",
        item_list.get("name"),
        "Source-Backed Goal Prompt Contracts",
    )
    assert_equal(
        "Source-backed ItemList numberOfItems",
        item_list.get("numberOfItems"),
        source_count,
    )
    assert_equal(
        "Source-backed ItemList description",
        item_list.get("description"),
        ITEMLIST_DESCRIPTION,
    )

    items = item_list.get("itemListElement")
    if not isinstance(items, list):
        fail("Source-backed ItemList itemListElement must be a list")
    assert_equal("Source-backed ItemList item count", len(items), source_count)

    for position, (entry, item) in enumerate(zip(source_entries, items), start=1):
        if not isinstance(item, dict):
            fail(f"Source-backed ItemList item {position} must be an object")
        expected_url = (
            f"{SITE_URL}goals/{entry['slug']}.html"
            if position <= STATIC_CONTRACT_URL_COUNT
            else f"{SITE_URL}#{entry['slug']}"
        )
        assert_equal(
            f"Source-backed ItemList item {position} position",
            item.get("position"),
            position,
        )
        assert_equal(
            f"Source-backed ItemList item {position} url",
            item.get("url"),
            expected_url,
        )
        assert_equal(
            f"Source-backed ItemList item {position} name",
            item.get("name"),
            entry.get("title"),
        )
        assert_equal(
            f"Source-backed ItemList item {position} description",
            item.get("description"),
            entry.get("intent"),
        )

    print(f"metadata validation ok ({source_count} source-backed, {seed_count} seed patterns)")


if __name__ == "__main__":
    main()
