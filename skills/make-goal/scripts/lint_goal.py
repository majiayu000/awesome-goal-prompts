#!/usr/bin/env python3
"""Lint make-goal outputs.

This script checks deterministic properties that are easy to regress:
required goal sections, fresh verification language, stop rules, and
profile-specific safety requirements for read-only, data migration, XSS, and
clarify-first outputs.
"""

from __future__ import annotations

import argparse
import json
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

VAGUE_PHRASES = [
    "make it better",
    "fix everything",
    "do whatever it takes",
    "keep going until perfect",
    "improve the codebase",
    "use your best judgment",
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


def section_positions(text: str) -> dict[str, int]:
    lowered = normalize(text)
    return {section: lowered.find(section.lower()) for section in FULL_SECTIONS}


def extract_section(text: str, section: str) -> str:
    positions = section_positions(text)
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


def infer_profile(text: str) -> str:
    lowered = normalize(text)
    if "/goal" not in lowered and contains_any(lowered, ["primary goal", "one finish line", "what is the one"]):
        return "clarify"
    if contains_any(lowered, ["xss", "user-provided link", "javascript:", "innerhtml", "unsafe html"]):
        return "security-xss"
    if contains_any(lowered, ["production database", "unique index", "users.email", "migration", "ddl"]):
        return "data-migration"
    if contains_any(lowered, ["read-only", "do not edit files", "changed files: `none`", "changed files: none"]):
        return "read-only"
    return "general"


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
    ordered = present_positions == sorted(present_positions)
    checks.append(
        Check(
            "sections_in_order",
            "error",
            ordered,
            "Full goal sections should appear in the standard order.",
        )
    )
    empty_sections = [
        section
        for section in FULL_SECTIONS
        if positions.get(section, -1) >= 0 and not extract_section(text, section)
    ]
    checks.append(
        Check(
            "sections_nonempty",
            "error",
            not empty_sections,
            "Each full goal section should contain concrete content.",
            ", ".join(empty_sections) if empty_sections else "all present sections have content",
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
            "verify_requires_fresh_evidence",
            "error",
            contains_any(extract_section(text, "VERIFY:"), ["run ", "capture", "fresh", "current session", "screenshot", "report", "inspect", "if verification cannot run", "stop and report"]),
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
            "protects_test_integrity",
            "warn",
            contains_any(text, ["do not weaken tests", "do not delete assertions", "test integrity", "do not weaken lint"]),
            "Goal should protect tests and assertions when implementation or verification is involved.",
        )
    )
    return checks


def check_read_only(text: str) -> list[Check]:
    return [
        Check(
            "read_only_boundary",
            "error",
            contains_any(text, ["read-only", "do not edit files", "do not modify", "changed files: `none`", "changed files: none"]),
            "Read-only goals must explicitly forbid edits.",
        ),
        Check(
            "no_patch_instruction",
            "error",
            not contains_any(text, ["apply a fix", "patch the code", "edit implementation"]),
            "Read-only goals must not instruct the agent to patch implementation code.",
        ),
        Check(
            "root_cause_evidence",
            "error",
            contains_all(text, ["root cause", "evidence"]),
            "Read-only investigation goals should require a root-cause report with evidence.",
        ),
    ]


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
    return [
        Check(
            "requires_protocol_allowlist",
            "error",
            contains_any(text, ["protocol allowlist", "protocol whitelist", "allowlist"]),
            "XSS link goals must require protocol allowlist validation.",
        ),
        Check(
            "rejects_blacklist_only",
            "error",
            contains_any(text, ["do not rely on blacklist", "not rely on blacklist", "blacklist-only", "allowlist"]),
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
    selected = infer_profile(text) if profile == "auto" else profile
    checks: list[Check] = []
    if selected == "clarify":
        checks.extend(check_clarify(text))
        return selected, checks
    checks.extend(check_contract_shape(text))
    if selected == "read-only":
        checks.extend(check_read_only(text))
    elif selected == "data-migration":
        checks.extend(check_data_migration(text))
    elif selected == "security-xss":
        checks.extend(check_security_xss(text))
    elif selected != "general":
        raise SystemExit(f"unknown profile: {selected}")
    return selected, checks


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
        choices=["auto", "general", "read-only", "data-migration", "security-xss", "clarify"],
        default="auto",
        help="Lint profile. auto infers from the file content.",
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
