"""Shared policy for generated static goal contract pages."""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any


STATIC_CONTRACT_POLICY = "all-source-backed"

# Same allowlist as docs/app.js static_path: goals/[a-z0-9-]+.html
SAFE_SLUG_PATTERN = re.compile(r"^[a-z0-9-]+$")


def is_safe_slug(slug: str) -> bool:
    """Return whether slug is a safe single-segment id (no path separators)."""
    return isinstance(slug, str) and bool(SAFE_SLUG_PATTERN.fullmatch(slug))


def safe_output_path(output_dir: Path, slug: str, suffix: str = ".html") -> Path:
    """Resolve output_dir / f\"{slug}{suffix}\" and require it stay inside output_dir.

    Raises ValueError for unsafe slugs or any path that escapes the output directory
    (``..``, absolute paths, or other separators).
    """
    if not is_safe_slug(slug):
        raise ValueError(f"unsafe static contract slug: {slug!r}")

    resolved_dir = output_dir.resolve()
    candidate = (resolved_dir / f"{slug}{suffix}").resolve()
    try:
        candidate.relative_to(resolved_dir)
    except ValueError as exc:
        raise ValueError(
            f"static contract path escapes output dir: slug={slug!r} path={candidate}"
        ) from exc
    return candidate


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
