from __future__ import annotations

from lint_goal_model import Check
from lint_goal_text import (
    contains_all,
    contains_any,
    has_link_or_navigation_context,
    has_read_only_boundary,
    is_investigation_context,
    lower_text,
    recommends_blacklist_only,
)


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
            "dry-run" in lower_text(text),
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
            contains_all(text, ["production", "destructive"])
            and contains_any(text, ["stop", "do not"]),
            "Data or migration goals must block unsafe production or destructive work.",
        ),
    ]


def check_security_xss(text: str) -> list[Check]:
    link_context = has_link_or_navigation_context(text)
    return [
        Check(
            "requires_protocol_allowlist",
            "error",
            (not link_context)
            or contains_any(text, ["protocol allowlist", "protocol whitelist", "allowlist"]),
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
            contains_any(
                text,
                ["innerhtml", "unsafe html", "unsafe sink", "href", "window.open", "location.href"],
            ),
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
            contains_any(
                text,
                [
                    "scope fuse",
                    "multiple independent pr-sized changes",
                    "follow-up prs",
                    "smallest launch-readiness pass",
                ],
            ),
            "Launch/readiness goals should include a scope fuse for multiple independent PR-sized changes.",
        ),
        Check(
            "external_outcomes_not_guaranteed",
            "error",
            contains_any(
                text,
                ["not guaranteed", "external outcome", "do not claim", "do not imply", "advisory"],
            ),
            "Launch/readiness goals should not guarantee external outcomes such as trending, ranking, traffic, or approval.",
        ),
        Check(
            "manual_platform_steps",
            "error",
            contains_any(
                text,
                ["manual", "owner approval", "repository settings", "settings access", "exact steps"],
            ),
            "Platform or repository settings that require owner access should be documented as manual steps or blockers.",
        ),
    ]


def check_clarify(text: str) -> list[Check]:
    return [
        Check(
            "asks_for_primary_goal",
            "error",
            contains_any(
                text,
                ["primary goal", "one finish line", "what is the one", "single improvement goal"],
            ),
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
            "/goal\ngoal:" not in lower_text(text) and "stop rules:" not in lower_text(text),
            "Clarify-first responses should not emit a full goal contract.",
        ),
    ]
