/goal
GOAL:
Produce a read-only assessment of whether `docs/styles.css` matches the existing catalog typography and spacing conventions.

CONTEXT:
- Read `docs/styles.css`, `docs/index.html`, and `docs/assets/catalog-browser.png`.
- Compare against the current local first viewport screenshot if one exists.

CONSTRAINTS:
- This is read-only. Do not edit files, run formatters, or stage changes.
- Separate observed evidence from design preferences.

DONE WHEN:
- The final report lists typography and spacing findings with evidence and file references.
- Changed files are none.

VERIFY:
- Inspect the named files and report exact selectors or screenshot observations used as evidence.

OUTPUT:
- Findings, evidence, remaining uncertainty, and changed files: none.

STOP RULES:
- Stop on missing screenshots only for screenshot-specific claims; continue with file-based evidence.
- Stop after three failed attempts to locate a referenced selector.
- Stop if secrets, production access, credentials, or destructive operations are required.
