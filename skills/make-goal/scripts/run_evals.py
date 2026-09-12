#!/usr/bin/env python3
"""Run deterministic make-goal eval fixtures.

The skill still needs human or model review for semantic quality. These evals
only guard regressions that should be mechanically catchable: section shape,
profile safety checks, and known negative cases.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from lint_goal_engine import lint
from lint_goal_model import Check


SKILL_ROOT = Path(__file__).resolve().parents[1]
EVALS_DIR = SKILL_ROOT / "evals"
EVALS_PATH = EVALS_DIR / "evals.json"


@dataclass
class CaseResult:
    name: str
    passed: bool
    detail: str


def resolve_fixture_path(file_value: str) -> Path:
    """Resolve a fixture path under EVALS_DIR, constrained to SKILL_ROOT.

    Absolute paths are rejected. Relative paths are joined under EVALS_DIR,
    resolved, and must remain inside the skill package root so intentional
    references like ``../SKILL.md`` stay valid while traversal outside the
    skill fails closed before any file read.
    """
    if not isinstance(file_value, str) or not file_value.strip():
        raise ValueError("fixture file path must be a non-empty string")
    raw = Path(file_value)
    if raw.is_absolute():
        raise ValueError(f"fixture file path must be relative, got absolute: {file_value!r}")
    resolved = (EVALS_DIR / raw).resolve()
    skill_root = SKILL_ROOT.resolve()
    if not resolved.is_relative_to(skill_root):
        raise ValueError(
            f"fixture file path escapes skill root {skill_root}: {file_value!r} -> {resolved}"
        )
    return resolved


def assertion_passes(text: str, assertion: dict[str, Any]) -> bool:
    kind = assertion["type"]
    values = assertion.get("values", [])
    if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
        raise ValueError(f"assertion {assertion.get('name', '<unnamed>')} values must be strings")
    lowered = text.lower()
    lowered_values = [value.lower() for value in values]
    if kind == "contains_all":
        return all(value in lowered for value in lowered_values)
    if kind == "contains_any":
        return any(value in lowered for value in lowered_values)
    if kind == "not_contains_any":
        return not any(value in lowered for value in lowered_values)
    raise ValueError(f"unknown assertion type: {kind}")


def validate_prompt_eval_specs(data: dict[str, Any]) -> list[CaseResult]:
    results: list[CaseResult] = []
    for item in data.get("evals", []):
        name = f"prompt-spec:{item.get('id', '<missing-id>')}"
        assertions = item.get("assertions", [])
        missing = [
            field
            for field in ["id", "prompt", "expected_output", "files", "assertions"]
            if field not in item
        ]
        bad_assertions = [
            assertion.get("name", "<unnamed>")
            for assertion in assertions
            if assertion.get("type") not in {"contains_all", "contains_any", "not_contains_any"}
            or not isinstance(assertion.get("values"), list)
        ]
        if missing or bad_assertions:
            detail = []
            if missing:
                detail.append(f"missing fields: {', '.join(missing)}")
            if bad_assertions:
                detail.append(f"bad assertions: {', '.join(bad_assertions)}")
            results.append(CaseResult(name, False, "; ".join(detail)))
        else:
            results.append(CaseResult(name, True, f"{len(assertions)} assertions defined"))
    return results


def run_skill_contract_check(case: dict[str, Any]) -> CaseResult:
    case_id = case["id"]
    path = resolve_fixture_path(case["file"])
    text = path.read_text(encoding="utf-8")
    assertion_failures = [
        assertion["name"]
        for assertion in case.get("assertions", [])
        if not assertion_passes(text, assertion)
    ]
    passed = not assertion_failures
    detail = f"{len(case.get('assertions', []))} assertions checked"
    if assertion_failures:
        detail += f" assertion_failures={','.join(assertion_failures)}"
    return CaseResult(f"skill-contract:{case_id}", passed, detail)


def lint_passed(checks: list[Check], strict_warnings: bool) -> bool:
    failed_errors = [check for check in checks if not check.passed and check.severity == "error"]
    failed_warnings = [check for check in checks if not check.passed and check.severity == "warn"]
    return not failed_errors and not (strict_warnings and failed_warnings)


def run_fixture(case: dict[str, Any]) -> CaseResult:
    case_id = case["id"]
    path = resolve_fixture_path(case["file"])
    text = path.read_text(encoding="utf-8")
    profile = case.get("profile", "auto")
    strict_warnings = bool(case.get("strict_warnings", False))
    expected_lint_pass = bool(case.get("expected_lint_pass", True))
    selected_profile, checks = lint(text, profile)
    actual_lint_pass = lint_passed(checks, strict_warnings)
    assertion_failures = [
        assertion["name"]
        for assertion in case.get("assertions", [])
        if not assertion_passes(text, assertion)
    ]
    failed_checks = [
        check.id
        for check in checks
        if not check.passed and (check.severity == "error" or strict_warnings)
    ]
    passed = actual_lint_pass == expected_lint_pass and not assertion_failures
    detail = (
        f"profile={selected_profile} expected_lint_pass={expected_lint_pass} "
        f"actual_lint_pass={actual_lint_pass}"
    )
    if failed_checks:
        detail += f" failed_checks={','.join(failed_checks)}"
    if assertion_failures:
        detail += f" assertion_failures={','.join(assertion_failures)}"
    return CaseResult(f"fixture:{case_id}", passed, detail)


def _expect_resolve_rejection(file_value: str, *, label: str) -> None:
    """Assert resolve_fixture_path rejects before any read_text occurs."""
    try:
        resolve_fixture_path(file_value)
    except ValueError:
        return
    raise AssertionError(f"{label}: expected ValueError for {file_value!r} before read_text")


def self_check_fixture_path_resolver() -> list[CaseResult]:
    """Negative unit assertions for absolute and skill-root escape paths."""
    results: list[CaseResult] = []

    try:
        _expect_resolve_rejection("/etc/hosts", label="absolute-path")
        results.append(CaseResult("path-safety:reject-absolute", True, "absolute path rejected"))
    except AssertionError as exc:
        results.append(CaseResult("path-safety:reject-absolute", False, str(exc)))

    try:
        _expect_resolve_rejection("../../../README.md", label="escape-skill-root")
        results.append(
            CaseResult("path-safety:reject-escape", True, "path escaping skill root rejected")
        )
    except AssertionError as exc:
        results.append(CaseResult("path-safety:reject-escape", False, str(exc)))

    try:
        allowed = resolve_fixture_path("../SKILL.md")
        if not allowed.is_relative_to(SKILL_ROOT.resolve()):
            raise AssertionError(f"../SKILL.md resolved outside skill root: {allowed}")
        if allowed.name != "SKILL.md":
            raise AssertionError(f"expected SKILL.md, got {allowed}")
        results.append(CaseResult("path-safety:allow-skill-md", True, f"resolved {allowed}"))
    except (AssertionError, ValueError) as exc:
        results.append(CaseResult("path-safety:allow-skill-md", False, str(exc)))

    return results


def main() -> int:
    data = json.loads(EVALS_PATH.read_text(encoding="utf-8"))
    results = self_check_fixture_path_resolver()
    results.extend(validate_prompt_eval_specs(data))
    for case in data.get("skill_contract_checks", []):
        results.append(run_skill_contract_check(case))
    for case in data.get("fixture_cases", []):
        results.append(run_fixture(case))

    failures = [result for result in results if not result.passed]
    for result in results:
        status = "PASS" if result.passed else "FAIL"
        print(f"{status} {result.name} - {result.detail}")

    print(f"summary: {len(results) - len(failures)}/{len(results)} eval checks passed")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
