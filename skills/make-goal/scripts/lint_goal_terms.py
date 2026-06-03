from __future__ import annotations


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
