"""Shared policy for generated static goal contract pages."""

from __future__ import annotations

from typing import Any


STATIC_CONTRACT_POLICY = "all-source-backed"


def is_static_contract_entry(entry: dict[str, Any]) -> bool:
    """Return whether an entry should have a generated static goal page."""
    return entry.get("origin") == "source-backed"


def static_contract_entries(entries: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Select entries covered by the static-page policy, preserving catalog order."""
    return [entry for entry in entries if is_static_contract_entry(entry)]


def static_contract_path(entry: dict[str, Any]) -> str | None:
    """Return the generated static page path for an entry, when covered."""
    if not is_static_contract_entry(entry):
        return None
    return f"goals/{entry['slug']}.html"


def static_contract_slugs(entries: list[dict[str, Any]]) -> list[str]:
    """Return static-page slugs in the same order as the catalog."""
    return [str(entry["slug"]) for entry in static_contract_entries(entries)]
