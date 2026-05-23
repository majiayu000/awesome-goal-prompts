#!/usr/bin/env python3
"""Lint make-goal outputs.

This script checks deterministic properties that are easy to regress:
required goal sections, fresh verification language, stop rules, and
profile-specific safety requirements for read-only, data migration, XSS,
launch-readiness, and clarify-first outputs.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from pathlib import Path


FULL_SECTIONS = [
    "GOAL:",
    "CONTEXT:",
    "CONSTRAINTS:",
    "DONE WHEN:",
    "VERIFY:",
    "OUTPUT:",
    "STOP RULES:",
]

COMPACT_SECTIONS = [
    "Read first:",
    "Constraints:",
    "Done when:",
    "Verify with:",
    "Stop if:",
    "Final output:",
]

VAGUE_PHRASES = [
    "make it better",
    "fix everything",
    "do whatever it takes",
    "keep going until perfect",
    "improve the codebase",
    "use your best judgment",
]

PROFILE_NAMES = [
    "general",
    "compact",
    "read-only",
    "data-migration",
    "security-xss",
    "launch-readiness",
    "clarify",
]

GENERIC_CONTEXT_PHRASES = [
    "read relevant files",
    "inspect the repo",
    "read the codebase",
    "look around",
    "understand the project",
]

GENERIC_DONE_PHRASES = [
    "it works",
    "works",
    "done",
    "complete",
    "completed",
    "fixed",
    "all good",
]

GENERIC_VERIFY_PHRASES = [
    "run tests",
    "run the tests",
    "test it",
    "verify it works",
    "make sure it works",
]

GOAL_ACTION_TERMS = [
    "fix",
    "add",
    "refactor",
    "redesign",
    "migrate",
    "deploy",
    "rewrite",
    "optimize",
    "build",
    "implement",
    "update",
    "document",
]

LINK_OR_NAVIGATION_TERMS = [
    "user-provided link",
    "user provided link",
    "href",
    "src",
    "url",
    "link",
    "javascript:",
    "window.open",
    "location.href",
    "navigation",
]

INVESTIGATION_TERMS = [
    "debug",
    "root cause",
    "why ",
    "empty state",
]

READ_ONLY_REPORT_TERMS = [
    "readiness",
    "growth",
    "launch",
    "review",
    "assessment",
    "report",
    "plan",
    "strategy",
]


@dataclass
class Check:
    id: str
    severity: str
    passed: bool
    message: str
    evidence: str = ""


def normalize(text: str) -> str:
    return text.lower()


def contains_any(text: str, terms: list[str]) -> bool:
    lowered = normalize(text)
    return any(term.lower() in lowered for term in terms)


def contains_all(text: str, terms: list[str]) -> bool:
    lowered = normalize(text)
    return all(term.lower() in lowered for term in terms)


def unique(items: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for item in items:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


def section_positions(text: str) -> dict[str, int]:
    lowered = normalize(text)
    return {section: lowered.find(section.lower()) for section in FULL_SECTIONS}


def positions_for(text: str, sections: list[str]) -> dict[str, int]:
    lowered = normalize(text)
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
    return contains_any(text, ["read-only", "do not edit files", "do not modify", "changed files: `none`", "changed files: none"])


def is_compact_goal(text: str) -> bool:
    lowered = normalize(text)
    return "/goal" in lowered and all(section.lower() in lowered for section in COMPACT_SECTIONS)


def recommends_blacklist_only(text: str) -> bool:
    lowered = normalize(text)
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
    lowered = normalize(text)
    if contains_any(lowered, ["root cause", "debug", "why ", "empty state"]):
        return True
    if contains_any(lowered, ["investigate", "diagnose", "diagnosis", "diagnoses"]):
        fault_terms = ["bug", "crash", "error", "exception", "failing", "failure", "broken", "empty state"]
        report_terms = [term for term in READ_ONLY_REPORT_TERMS if term not in {"report", "assessment"}]
        return contains_any(lowered, fault_terms) and not contains_any(lowered, report_terms)
    return False


def has_concrete_context(context: str) -> bool:
    lowered = normalize(context)
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


def looks_like_backlog_goal(goal: str) -> bool:
    lowered = normalize(goal)
    if contains_any(lowered, ["backlog", "everything", "all bugs", "all issues"]):
        return True
    action_count = sum(1 for term in GOAL_ACTION_TERMS if re.search(rf"\b{re.escape(term)}\b", lowered))
    has_many_connectors = lowered.count(",") >= 2 or lowered.count(" and ") >= 2
    return action_count >= 3 and has_many_connectors


def infer_profiles(text: str) -> list[str]:
    lowered = normalize(text)
    if "/goal" not in lowered and contains_any(lowered, ["primary goal", "one finish line", "what is the one"]):
        return ["clarify"]

    profiles: list[str] = []
    if is_compact_goal(lowered):
        profiles.append("compact")
    else:
        profiles.append("general")

    if contains_any(lowered, ["production database", "unique index", "users.email", "migration", "ddl"]):
        profiles.append("data-migration")
    if contains_any(lowered, ["xss", "innerhtml", "unsafe html"]) and (
        has_link_or_navigation_context(lowered) or contains_any(lowered, ["innerhtml", "unsafe html", "unsafe sink"])
    ):
        profiles.append("security-xss")
    if has_read_only_boundary(lowered):
        profiles.append("read-only")
    if contains_any(lowered, ["launch-readiness", "launch readiness", "release-prep", "release prep", "trending", "roadmap"]):
        profiles.append("launch-readiness")
    return unique(profiles)


def parse_profiles(profile: str) -> list[str]:
    if profile == "auto":
        return ["auto"]
    profiles = [part.strip() for part in profile.split(",") if part.strip()]
    unknown = [name for name in profiles if name not in PROFILE_NAMES]
    if unknown:
        raise SystemExit(f"unknown profile: {', '.join(unknown)}")
    if "clarify" in profiles and len(profiles) > 1:
        raise SystemExit("clarify cannot be combined with other profiles")
    if "general" in profiles and "compact" in profiles:
        raise SystemExit("general and compact cannot be combined")
    if "general" not in profiles and "compact" not in profiles and "clarify" not in profiles:
        profiles.insert(0, "general")
    return unique(profiles)


def check_contract_shape(text: str) -> list[Check]:
    checks: list[Check] = []
    checks.append(
        Check(
            "has_goal_command",
            "error",
            "/goal" in normalize(text),
            "Goal contracts should include the /goal command.",
        )
    )
    positions = section_positions(text)
    missing = [section for section, pos in positions.items() if pos < 0]
    checks.append(
        Check(
            "has_full_goal_sections",
            "error",
            not missing,
            "Full goal must include GOAL, CONTEXT, CONSTRAINTS, DONE WHEN, VERIFY, OUTPUT, and STOP RULES.",
            ", ".join(missing) if missing else "all sections present",
        )
    )
    present_positions = [positions[section] for section in FULL_SECTIONS if positions[section] >= 0]
    ordered = not missing and present_positions == sorted(present_positions)
    checks.append(
        Check(
            "sections_in_order",
            "error",
            ordered,
            "Full goal sections should appear in the standard order.",
            "cannot check order until all sections are present" if missing else "",
        )
    )
    empty_sections = [
        section
        for section in FULL_SECTIONS
        if positions.get(section, -1) >= 0 and not extract_section(text, section)
    ]
    nonempty = not missing and not empty_sections
    checks.append(
        Check(
            "sections_nonempty",
            "error",
            nonempty,
            "Each full goal section should contain concrete content.",
            (
                "missing: " + ", ".join(missing)
                if missing
                else ", ".join(empty_sections)
                if empty_sections
                else "all present sections have content"
            ),
        )
    )
    goal = extract_section(text, "GOAL:")
    checks.append(
        Check(
            "goal_not_vague",
            "error",
            not contains_any(goal, VAGUE_PHRASES),
            "GOAL must not use vague improvement language.",
            goal[:180],
        )
    )
    checks.append(
        Check(
            "goal_not_backlog",
            "error",
            not looks_like_backlog_goal(goal),
            "GOAL should describe one primary objective, not several independent backlog items.",
            goal[:180],
        )
    )
    context = extract_section(text, "CONTEXT:")
    checks.append(
        Check(
            "context_has_concrete_sources",
            "error",
            has_concrete_context(context),
            "CONTEXT should name concrete files, issues, logs, commands, screenshots, URLs, or baselines.",
            context[:220],
        )
    )
    done_when = extract_section(text, "DONE WHEN:")
    checks.append(
        Check(
            "done_when_not_generic",
            "error",
            not is_generic_done_when(done_when),
            "DONE WHEN should be mechanically checkable, not a generic completion phrase.",
            done_when[:180],
        )
    )
    verify = extract_section(text, "VERIFY:")
    checks.append(
        Check(
            "verify_not_generic",
            "error",
            not is_generic_verify(verify),
            "VERIFY should name a concrete command, report, screenshot, artifact, or exact blocker.",
            verify[:180],
        )
    )
    checks.append(
        Check(
            "verify_requires_fresh_evidence",
            "error",
            contains_any(verify, ["run ", "capture", "fresh", "current session", "screenshot", "report", "inspect", "if verification cannot run", "stop and report"]),
            "VERIFY should require fresh command output, report, screenshot, inspection, or an explicit blocker.",
        )
    )
    stop_rules = extract_section(text, "STOP RULES:")
    checks.append(
        Check(
            "stop_rules_cover_high_risk_blockers",
            "error",
            contains_all(stop_rules, ["secrets", "production"]) and contains_any(stop_rules, ["destructive", "credentials"]),
            "STOP RULES should cover secrets, production access, credentials, or destructive operations.",
            stop_rules[:220],
        )
    )
    checks.append(
        Check(
            "stop_rules_cover_repeated_failures",
            "error",
            contains_any(stop_rules, ["three failed", "3 failed", "three attempts", "3 attempts"]),
            "STOP RULES should stop after repeated failed attempts on the same symptom.",
            stop_rules[:220],
        )
    )
    checks.append(
        Check(
            "protects_verification_integrity",
            "warn",
            "verification integrity:" in normalize(text),
            "Goals with implementation or verification work should include the canonical Verification integrity constraint.",
        )
    )
    return checks


def check_compact_shape(text: str) -> list[Check]:
    checks: list[Check] = []
    lowered = normalize(text)
    checks.append(
        Check(
            "has_goal_command",
            "error",
            "/goal" in lowered,
            "Compact goals should include the /goal command.",
        )
    )
    positions = positions_for(text, COMPACT_SECTIONS)
    missing = [section for section, pos in positions.items() if pos < 0]
    checks.append(
        Check(
            "has_compact_sections",
            "error",
            not missing,
            "Compact goals must include Read first, Constraints, Done when, Verify with, Stop if, and Final output.",
            ", ".join(missing) if missing else "all compact sections present",
        )
    )
    present_positions = [positions[section] for section in COMPACT_SECTIONS if positions[section] >= 0]
    checks.append(
        Check(
            "compact_sections_in_order",
            "error",
            not missing and present_positions == sorted(present_positions),
            "Compact goal sections should appear in the standard order.",
            "cannot check order until all compact sections are present" if missing else "",
        )
    )
    empty_sections = [
        section
        for section in COMPACT_SECTIONS
        if positions.get(section, -1) >= 0 and not extract_section(text, section, COMPACT_SECTIONS)
    ]
    checks.append(
        Check(
            "compact_sections_nonempty",
            "error",
            not missing and not empty_sections,
            "Each compact goal section should contain concrete content.",
            (
                "missing: " + ", ".join(missing)
                if missing
                else ", ".join(empty_sections)
                if empty_sections
                else "all compact sections have content"
            ),
        )
    )
    goal_line = next((line for line in text.splitlines() if line.lower().startswith("/goal")), "")
    checks.append(
        Check(
            "goal_not_vague",
            "error",
            bool(goal_line.strip()) and not contains_any(goal_line, VAGUE_PHRASES),
            "Compact /goal line must contain a specific measurable goal.",
            goal_line[:180],
        )
    )
    checks.append(
        Check(
            "compact_verify_present",
            "error",
            contains_any(extract_section(text, "Verify with:", COMPACT_SECTIONS), ["run ", "command", "report", "screenshot", "evidence", "test", "lint", "verify"]),
            "Compact goals should name verification evidence.",
        )
    )
    checks.append(
        Check(
            "compact_stop_rules_present",
            "error",
            contains_any(extract_section(text, "Stop if:", COMPACT_SECTIONS), ["missing", "destructive", "production", "three failed", "3 failed", "unclear"]),
            "Compact goals should include meaningful stop conditions.",
        )
    )
    return checks


def check_read_only(text: str) -> list[Check]:
    requires_root_cause = is_investigation_context(text)
    checks = [
        Check(
            "read_only_boundary",
            "error",
            has_read_only_boundary(text),
            "Read-only goals must explicitly forbid edits.",
        ),
        Check(
            "no_patch_instruction",
            "error",
            not contains_any(text, ["apply a fix", "patch the code", "edit implementation"]),
            "Read-only goals must not instruct the agent to patch implementation code.",
        ),
        Check(
            "read_only_requires_evidence",
            "error",
            contains_any(text, ["evidence", "findings", "report", "assessment", "summary"]),
            "Read-only goals should require evidence, findings, a report, or an assessment.",
        ),
    ]
    checks.append(
        Check(
            "root_cause_evidence",
            "error",
            (not requires_root_cause) or contains_all(text, ["root cause", "evidence"]),
            "Read-only investigation/debug goals should require a root-cause report with evidence.",
            "not an investigation/debug goal" if not requires_root_cause else "",
        )
    )
    return checks


def check_data_migration(text: str) -> list[Check]:
    return [
        Check(
            "requires_dry_run",
            "error",
            "dry-run" in normalize(text),
            "Data or migration goals must explicitly include the literal term dry-run.",
        ),
        Check(
            "requires_rollback_or_recovery",
            "error",
            contains_any(text, ["rollback", "forward-only recovery", "forward-fix", "recovery"]),
            "Data or migration goals must include rollback or recovery evidence.",
        ),
        Check(
            "requires_integrity_evidence",
            "error",
            contains_any(text, ["row count", "row-count", "checksum", "duplicate"]),
            "Data or migration goals must require integrity evidence such as row counts, checksums, or duplicate reports.",
        ),
        Check(
            "blocks_unsafe_production_work",
            "error",
            contains_all(text, ["production", "destructive"]) and contains_any(text, ["stop", "do not"]),
            "Data or migration goals must block unsafe production or destructive work.",
        ),
    ]


def check_security_xss(text: str) -> list[Check]:
    link_context = has_link_or_navigation_context(text)
    return [
        Check(
            "requires_protocol_allowlist",
            "error",
            (not link_context) or contains_any(text, ["protocol allowlist", "protocol whitelist", "allowlist"]),
            "Link or navigation XSS goals must require protocol allowlist validation.",
            "not a link/navigation XSS goal" if not link_context else "",
        ),
        Check(
            "rejects_blacklist_only",
            "error",
            not recommends_blacklist_only(text),
            "XSS link goals should avoid blacklist-only validation.",
        ),
        Check(
            "mentions_unsafe_sinks",
            "error",
            contains_any(text, ["innerhtml", "unsafe html", "unsafe sink", "href", "window.open", "location.href"]),
            "XSS link goals should mention unsafe HTML or navigation sinks.",
        ),
        Check(
            "requires_browser_or_test_evidence",
            "error",
            contains_any(text, ["browser", "playwright", "smoke", "test"]),
            "XSS link goals should require tests or browser smoke evidence.",
        ),
    ]


def check_launch_readiness(text: str) -> list[Check]:
    return [
        Check(
            "launch_scope_fuse",
            "error",
            contains_any(text, ["scope fuse", "multiple independent pr-sized changes", "follow-up prs", "smallest launch-readiness pass"]),
            "Launch/readiness goals should include a scope fuse for multiple independent PR-sized changes.",
        ),
        Check(
            "external_outcomes_not_guaranteed",
            "error",
            contains_any(text, ["not guaranteed", "external outcome", "do not claim", "do not imply", "advisory"]),
            "Launch/readiness goals should not guarantee external outcomes such as trending, ranking, traffic, or approval.",
        ),
        Check(
            "manual_platform_steps",
            "error",
            contains_any(text, ["manual", "owner approval", "repository settings", "settings access", "exact steps"]),
            "Platform or repository settings that require owner access should be documented as manual steps or blockers.",
        ),
    ]


def check_clarify(text: str) -> list[Check]:
    return [
        Check(
            "asks_for_primary_goal",
            "error",
            contains_any(text, ["primary goal", "one finish line", "what is the one", "single improvement goal"]),
            "Clarify-first responses should ask for the primary goal or finish line.",
        ),
        Check(
            "asks_for_context",
            "error",
            contains_any(text, ["files", "issue", "logs", "context", "screenshot"]),
            "Clarify-first responses should ask for real context.",
        ),
        Check(
            "asks_for_done_or_verify",
            "error",
            contains_any(text, ["done", "verify", "completion", "proves", "evidence"]),
            "Clarify-first responses should ask what proves completion.",
        ),
        Check(
            "does_not_emit_full_goal",
            "error",
            "/goal\ngoal:" not in normalize(text) and "stop rules:" not in normalize(text),
            "Clarify-first responses should not emit a full goal contract.",
        ),
    ]


def lint(text: str, profile: str) -> tuple[str, list[Check]]:
    selected_profiles = infer_profiles(text) if profile == "auto" else parse_profiles(profile)
    checks: list[Check] = []
    if "clarify" in selected_profiles:
        checks.extend(check_clarify(text))
        return "+".join(selected_profiles), checks
    if "compact" in selected_profiles:
        checks.extend(check_compact_shape(text))
    else:
        checks.extend(check_contract_shape(text))
    if "read-only" in selected_profiles:
        checks.extend(check_read_only(text))
    if "data-migration" in selected_profiles:
        checks.extend(check_data_migration(text))
    if "security-xss" in selected_profiles:
        checks.extend(check_security_xss(text))
    if "launch-readiness" in selected_profiles:
        checks.extend(check_launch_readiness(text))
    return "+".join(selected_profiles), checks


def print_text(path: Path, profile: str, checks: list[Check]) -> None:
    failed_errors = [check for check in checks if not check.passed and check.severity == "error"]
    failed_warnings = [check for check in checks if not check.passed and check.severity == "warn"]
    if failed_errors:
        status = "FAIL"
    elif failed_warnings:
        status = "PASS_WITH_WARNINGS"
    else:
        status = "PASS"
    print(f"{status} {path} profile={profile}")
    for check in checks:
        mark = "ok" if check.passed else check.severity
        print(f"- [{mark}] {check.id}: {check.message}")
        if check.evidence and not check.passed:
            print(f"  evidence: {check.evidence}")
    clean = len(checks) - len(failed_errors) - len(failed_warnings)
    print(f"summary: {clean}/{len(checks)} checks clean, errors={len(failed_errors)}, warnings={len(failed_warnings)}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Lint make-goal output files.")
    parser.add_argument("path", type=Path, help="Markdown/text file to lint")
    parser.add_argument(
        "--profile",
        default="auto",
        help=(
            "Lint profile. Use auto, one profile, or comma-separated profiles "
            f"from: {', '.join(PROFILE_NAMES)}."
        ),
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text")
    parser.add_argument("--strict-warnings", action="store_true", help="Treat warnings as failures")
    args = parser.parse_args()

    text = args.path.read_text(encoding="utf-8")
    selected_profile, checks = lint(text, args.profile)
    failed_errors = [check for check in checks if not check.passed and check.severity == "error"]
    failed_warnings = [check for check in checks if not check.passed and check.severity == "warn"]

    if args.json:
        print(
            json.dumps(
                {
                    "path": str(args.path),
                    "profile": selected_profile,
                    "passed": not failed_errors and not (args.strict_warnings and failed_warnings),
                    "checks": [asdict(check) for check in checks],
                },
                indent=2,
            )
        )
    else:
        print_text(args.path, selected_profile, checks)

    if failed_errors or (args.strict_warnings and failed_warnings):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
