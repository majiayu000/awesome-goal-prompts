from __future__ import annotations

import re

from lint_goal_terms import (
    COMPACT_SECTIONS,
    FULL_SECTIONS,
    GENERIC_CONTEXT_PHRASES,
    GENERIC_DONE_PHRASES,
    GENERIC_VERIFY_PHRASES,
    GOAL_ACTION_TERMS,
    LINK_OR_NAVIGATION_TERMS,
    READ_ONLY_REPORT_TERMS,
)


def lower_text(text: str) -> str:
    return text.lower()


def contains_any(text: str, terms: list[str]) -> bool:
    lowered = lower_text(text)
    return any(term.lower() in lowered for term in terms)


def contains_all(text: str, terms: list[str]) -> bool:
    lowered = lower_text(text)
    return all(term.lower() in lowered for term in terms)


def unique_ordered(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def section_positions(text: str) -> dict[str, int]:
    return positions_for(text, FULL_SECTIONS)


def positions_for(text: str, sections: list[str]) -> dict[str, int]:
    lowered = lower_text(text)
    return {section: lowered.find(section.lower()) for section in sections}


def extract_section(text: str, section: str, sections: list[str] | None = None) -> str:
    positions = positions_for(text, sections or FULL_SECTIONS)
    start = positions.get(section, -1)
    if start < 0:
        return ""
    start += len(section)
    later_positions = [
        pos
        for name, pos in positions.items()
        if pos > start and name != section
    ]
    end = min(later_positions) if later_positions else len(text)
    return text[start:end].strip()


def has_read_only_boundary(text: str) -> bool:
    return contains_any(
        text,
        [
            "read-only",
            "do not edit files",
            "do not modify",
            "changed files: `none`",
            "changed files: none",
        ],
    )


def is_compact_goal(text: str) -> bool:
    lowered = lower_text(text)
    return "/goal" in lowered and all(
        section.lower() in lowered for section in COMPACT_SECTIONS
    )


def recommends_blacklist_only(text: str) -> bool:
    lowered = lower_text(text)
    if "blacklist-only" not in lowered and "blacklist only" not in lowered:
        return False
    avoidance_terms = [
        "do not rely on blacklist",
        "do not use blacklist",
        "do not use blacklist-only",
        "not rely on blacklist",
        "avoid blacklist",
        "avoid blacklist-only",
        "instead of blacklist",
        "not blacklist-only",
        "never rely on blacklist",
    ]
    return not any(term in lowered for term in avoidance_terms)


def has_link_or_navigation_context(text: str) -> bool:
    return contains_any(text, LINK_OR_NAVIGATION_TERMS)


def is_investigation_context(text: str) -> bool:
    lowered = lower_text(text)
    if contains_any(lowered, ["root cause", "debug", "why ", "empty state"]):
        return True
    if contains_any(lowered, ["investigate", "diagnose", "diagnosis", "diagnoses"]):
        fault_terms = [
            "bug",
            "crash",
            "error",
            "exception",
            "failing",
            "failure",
            "broken",
            "empty state",
        ]
        report_terms = [
            term for term in READ_ONLY_REPORT_TERMS
            if term not in {"report", "assessment"}
        ]
        return contains_any(lowered, fault_terms) and not contains_any(
            lowered, report_terms
        )
    return False


def has_concrete_context(context: str) -> bool:
    lowered = lower_text(context)
    if contains_any(lowered, GENERIC_CONTEXT_PHRASES) and len(lowered.split()) < 30:
        return False
    concrete_patterns = [
        r"`[^`]+`",
        r"\b[A-Za-z0-9_.-]+\.(md|py|js|ts|tsx|jsx|json|toml|yml|yaml|html|css|go|rs|java|rb|php)\b",
        r"\b(issue|pr|pull request)\s*#?\d+\b",
        r"\bhttps?://",
        r"\b(test|lint|build|typecheck|pytest|npm|pnpm|yarn|cargo|go test|node --check)\b",
        r"\b(log|screenshot|trace|stack|baseline|report|workflow)\b",
    ]
    return any(re.search(pattern, context, re.IGNORECASE) for pattern in concrete_patterns)


def is_generic_done_when(done_when: str) -> bool:
    stripped = " ".join(done_when.lower().strip(" .:-`").split())
    if stripped in GENERIC_DONE_PHRASES:
        return True
    return len(stripped.split()) <= 5 and contains_any(stripped, GENERIC_DONE_PHRASES)


def is_generic_verify(verify: str) -> bool:
    stripped = " ".join(verify.lower().strip(" .:-`").split())
    if stripped in GENERIC_VERIFY_PHRASES:
        return True
    if len(stripped.split()) <= 6 and contains_any(stripped, GENERIC_VERIFY_PHRASES):
        return True
    return False


def has_accountable_output(output: str) -> bool:
    return (
        contains_any(output, ["changed files", "changed file", "modified files"])
        and contains_any(output, ["verification output", "verification result", "evidence"])
        and contains_any(
            output,
            [
                "remaining risk",
                "remaining risks",
                "follow-up",
                "followup",
                "next action",
                "blocker",
                "uncertainty",
            ],
        )
    )


def looks_like_backlog_goal(goal: str) -> bool:
    lowered = lower_text(goal)
    if contains_any(lowered, ["backlog", "everything", "all bugs", "all issues"]):
        return True
    action_count = sum(
        1 for term in GOAL_ACTION_TERMS if re.search(rf"\b{re.escape(term)}\b", lowered)
    )
    has_many_connectors = lowered.count(",") >= 2 or lowered.count(" and ") >= 2
    return action_count >= 3 and has_many_connectors
