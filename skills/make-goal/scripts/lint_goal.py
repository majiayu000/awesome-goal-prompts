#!/usr/bin/env python3
"""Lint make-goal outputs."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from lint_goal_engine import lint
from lint_goal_model import Check
from lint_goal_terms import PROFILE_NAMES


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
