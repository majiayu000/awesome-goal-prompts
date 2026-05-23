/goal
GOAL:
Complete a launch-readiness pass for GitHub Trending.

CONTEXT:
- Read `README.md`, `docs/index.html`, and `.github/workflows/catalog.yml`.

CONSTRAINTS:
- Do not claim GitHub Trending is guaranteed.
- Do not weaken tests.

DONE WHEN:
- README, GitHub Pages, metadata, issue hygiene, share copy, and repo settings are all complete.

VERIFY:
- Run `python3 scripts/validate_data.py`.
- Capture browser screenshots.

OUTPUT:
- Changed files, verification output, and manual repository settings steps.

STOP RULES:
- Stop on secrets, production credentials, destructive operations, or repository settings requiring owner approval.
- Stop after three failed attempts on the same symptom.
