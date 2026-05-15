"""Shared catalog search scoring used by the site QA scripts."""

from __future__ import annotations

import re
from typing import Any


QUERY_ALIASES = {
    "a11y": ["accessibility", "a11y", "wcag"],
    "agent": ["agent", "agents", "codex", "claude", "hermes"],
    "api": ["api", "endpoint", "route", "contract"],
    "auth": ["auth", "authentication", "authorization", "authz", "login", "permission"],
    "bug": ["bug", "fix", "repair", "failure", "failing", "error", "regression"],
    "ci": ["ci", "workflow", "actions", "pipeline", "check"],
    "database": ["database", "db", "schema", "migration", "sql"],
    "docs": ["docs", "documentation", "readme", "guide", "runbook"],
    "evals": ["eval", "evals", "evaluation", "grading", "score"],
    "fail": ["fail", "fails", "failing", "failure", "red", "error", "repair", "fix", "pass", "clean"],
    "flaky": ["flaky", "unstable", "race", "intermittent"],
    "guardrails": ["guardrail", "guardrails", "safety", "policy", "security"],
    "lint": ["lint", "eslint", "ruff", "format", "typecheck", "typescript"],
    "migration": ["migration", "migrate", "port", "upgrade", "compatibility", "schema"],
    "mobile": ["mobile", "ios", "android", "github mobile"],
    "onboarding": ["onboarding", "quickstart", "docs", "guide", "contributor"],
    "red": ["red", "failing", "failure", "error", "lint", "test", "clean"],
    "refactor": ["refactor", "cleanup", "split", "standardize"],
    "security": ["security", "auth", "authorization", "injection", "xss", "csrf", "ssrf", "secret", "guardrails"],
    "tests": ["test", "tests", "testing", "suite", "vitest", "pytest", "playwright", "coverage"],
    "trace": ["trace", "tracing", "span", "spans", "observability"],
    "typescript": ["typescript", "ts", "typecheck", "eslint"],
    "安全": ["security", "auth", "authorization", "injection", "xss", "csrf", "ssrf", "secret"],
    "鉴权": ["auth", "authentication", "authorization", "authz", "login", "permission"],
    "登录": ["auth", "login", "permission"],
    "迁移": ["migration", "migrate", "port", "upgrade", "compatibility"],
    "测试": ["test", "tests", "testing", "suite", "vitest", "pytest", "playwright", "coverage"],
    "失败": ["fail", "fails", "failing", "failure", "red", "error", "repair", "fix"],
    "报错": ["fail", "error", "failure", "bug", "fix"],
    "文档": ["docs", "documentation", "readme", "guide", "runbook"],
    "前端": ["frontend", "ui", "css", "react", "component"],
    "后端": ["backend", "api", "endpoint", "route", "data"],
    "性能": ["performance", "perf", "latency", "speed", "benchmark"],
    "移动端": ["mobile", "ios", "android", "responsive"],
    "工作流": ["workflow", "pipeline", "actions", "ci"],
    "命令行": ["cli", "command", "terminal"],
    "重构": ["refactor", "cleanup", "split", "standardize"],
}


def normalize(value: Any) -> str:
    return str(value or "").lower()


def tokenize(value: str) -> list[str]:
    return [token for token in re.split(r"[^\w+.#/-]+", normalize(value), flags=re.UNICODE) if token]


def unique(values: list[str]) -> list[str]:
    return sorted(set(values))


def query_terms(query: str) -> list[list[str]]:
    groups = []
    for token in tokenize(query):
        variants = [token, *QUERY_ALIASES.get(token, [])]
        for alias, expanded in QUERY_ALIASES.items():
            if not alias.isascii() and alias in token:
                variants.extend(expanded)
        groups.append(unique(variants))
    return groups


def searchable_text(entry: dict[str, Any]) -> str:
    return " ".join(
        normalize(entry.get(field))
        for field in [
            "title",
            "intent",
            "category",
            "difficulty",
            "origin",
            "verify",
            "source_name",
            "source_type",
            "evidence",
            "evidence_summary",
            "prompt",
        ]
    )


def term_matches(text: str, variants: list[str]) -> bool:
    return any(variant in text for variant in variants)


def search_score(entry: dict[str, Any], query: str) -> int:
    if not query:
        return 1
    text = searchable_text(entry)
    groups = query_terms(query)
    if not groups:
        return 1
    if not all(term_matches(text, group) for group in groups):
        return 0

    score = 10
    title = normalize(entry.get("title"))
    intent = normalize(entry.get("intent"))
    verify = normalize(entry.get("verify"))
    evidence = normalize(f"{entry.get('evidence') or ''} {entry.get('evidence_summary') or ''}")
    for group in groups:
        if term_matches(title, group):
            score += 5
        if term_matches(intent, group):
            score += 4
        if term_matches(verify, group):
            score += 3
        if term_matches(evidence, group):
            score += 2
    if entry.get("origin") == "source-backed":
        score += 3
    if entry.get("source_type") == "official-goal":
        score += 4
    return score


def ranked(entries: list[dict[str, Any]], query: str) -> list[dict[str, Any]]:
    indexed = list(enumerate(entries))
    scored = [
        (search_score(entry, query), index, entry)
        for index, entry in indexed
    ]
    return [
        entry
        for score, _index, entry in sorted(scored, key=lambda item: (-item[0], item[1]))
        if score > 0
    ]
