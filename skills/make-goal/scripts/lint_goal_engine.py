from __future__ import annotations

from lint_goal_model import Check
from lint_goal_profiles import (
    check_clarify,
    check_data_migration,
    check_launch_readiness,
    check_read_only,
    check_security_xss,
)
from lint_goal_rules import check_compact_shape, check_contract_shape
from lint_goal_terms import PROFILE_NAMES
from lint_goal_text import (
    contains_any,
    has_link_or_navigation_context,
    has_read_only_boundary,
    is_compact_goal,
    lower_text,
    unique_ordered,
)


def infer_profiles(text: str) -> list[str]:
    lowered = lower_text(text)
    if "/goal" not in lowered and contains_any(
        lowered, ["primary goal", "one finish line", "what is the one"]
    ):
        return ["clarify"]

    profiles: list[str] = ["compact" if is_compact_goal(lowered) else "general"]
    if contains_any(
        lowered, ["production database", "unique index", "users.email", "migration", "ddl"]
    ):
        profiles.append("data-migration")
    if contains_any(lowered, ["xss", "innerhtml", "unsafe html"]) and (
        has_link_or_navigation_context(lowered)
        or contains_any(lowered, ["innerhtml", "unsafe html", "unsafe sink"])
    ):
        profiles.append("security-xss")
    if has_read_only_boundary(lowered):
        profiles.append("read-only")
    if contains_any(
        lowered,
        ["launch-readiness", "launch readiness", "release-prep", "release prep", "trending", "roadmap"],
    ):
        profiles.append("launch-readiness")
    return unique_ordered(profiles)


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
    return unique_ordered(profiles)


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
