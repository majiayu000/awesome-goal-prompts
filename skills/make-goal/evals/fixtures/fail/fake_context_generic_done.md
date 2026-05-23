/goal
GOAL:
Fix the app.

CONTEXT:
- Read relevant files.

CONSTRAINTS:
- Do not weaken tests.

DONE WHEN:
- It works.

VERIFY:
- Run tests.

OUTPUT:
- Changed files and summary.

STOP RULES:
- Stop on secrets, production credentials, or destructive operations.
- Stop after three failed attempts on the same symptom.
