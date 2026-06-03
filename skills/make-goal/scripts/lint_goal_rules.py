from __future__ import annotations

from lint_goal_model import Check
from lint_goal_terms import COMPACT_SECTIONS, FULL_SECTIONS, VAGUE_PHRASES
from lint_goal_text import (
    contains_any,
    contains_all,
    extract_section,
    has_accountable_output,
    has_concrete_context,
    is_generic_done_when,
    is_generic_verify,
    lower_text,
    looks_like_backlog_goal,
    positions_for,
    section_positions,
)


def check_contract_shape(text: str) -> list[Check]:
    checks: list[Check] = []
    checks.append(
        Check(
            "has_goal_command",
            "error",
            "/goal" in lower_text(text),
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
    present_positions = [
        positions[section] for section in FULL_SECTIONS if positions[section] >= 0
    ]
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
    checks.append(
        Check(
            "sections_nonempty",
            "error",
            not missing and not empty_sections,
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
            contains_any(
                verify,
                [
                    "run ",
                    "capture",
                    "fresh",
                    "current session",
                    "screenshot",
                    "report",
                    "inspect",
                    "if verification cannot run",
                    "stop and report",
                ],
            ),
            "VERIFY should require fresh command output, report, screenshot, inspection, or an explicit blocker.",
        )
    )
    output = extract_section(text, "OUTPUT:")
    checks.append(
        Check(
            "output_reports_accountability",
            "error",
            has_accountable_output(output),
            "OUTPUT should require changed files, verification/evidence, and remaining risk, follow-up, blocker, or uncertainty.",
            output[:220],
        )
    )
    stop_rules = extract_section(text, "STOP RULES:")
    checks.append(
        Check(
            "stop_rules_cover_high_risk_blockers",
            "error",
            contains_all(stop_rules, ["secrets", "production"])
            and contains_any(stop_rules, ["destructive", "credentials"]),
            "STOP RULES should cover secrets, production access, credentials, or destructive operations.",
            stop_rules[:220],
        )
    )
    checks.append(
        Check(
            "stop_rules_cover_repeated_failures",
            "error",
            contains_any(
                stop_rules,
                ["three failed", "3 failed", "three attempts", "3 attempts"],
            ),
            "STOP RULES should stop after repeated failed attempts on the same symptom.",
            stop_rules[:220],
        )
    )
    checks.append(
        Check(
            "protects_verification_integrity",
            "warn",
            "verification integrity:" in lower_text(text),
            "Goals with implementation or verification work should include the canonical Verification integrity constraint.",
        )
    )
    return checks


def check_compact_shape(text: str) -> list[Check]:
    checks: list[Check] = []
    lowered = lower_text(text)
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
    present_positions = [
        positions[section] for section in COMPACT_SECTIONS if positions[section] >= 0
    ]
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
        if positions.get(section, -1) >= 0
        and not extract_section(text, section, COMPACT_SECTIONS)
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
    goal_line = next(
        (line for line in text.splitlines() if line.lower().startswith("/goal")),
        "",
    )
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
            contains_any(
                extract_section(text, "Verify with:", COMPACT_SECTIONS),
                ["run ", "command", "report", "screenshot", "evidence", "test", "lint", "verify"],
            ),
            "Compact goals should name verification evidence.",
        )
    )
    checks.append(
        Check(
            "compact_stop_rules_present",
            "error",
            contains_any(
                extract_section(text, "Stop if:", COMPACT_SECTIONS),
                ["missing", "destructive", "production", "three failed", "3 failed", "unclear"],
            ),
            "Compact goals should include meaningful stop conditions.",
        )
    )
    final_output = extract_section(text, "Final output:", COMPACT_SECTIONS)
    checks.append(
        Check(
            "compact_output_reports_accountability",
            "error",
            has_accountable_output(final_output),
            "Compact final output should require changed files, verification/evidence, and remaining risk, follow-up, blocker, or uncertainty.",
            final_output[:220],
        )
    )
    return checks
