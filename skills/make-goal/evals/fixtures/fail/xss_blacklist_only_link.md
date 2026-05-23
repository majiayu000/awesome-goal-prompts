/goal
GOAL:
Fix a frontend XSS risk from user-provided links.

CONTEXT:
- Read `docs/entry-renderer.js`, `docs/app.js`, and the link rendering tests.

CONSTRAINTS:
- Use blacklist-only validation for `javascript:` links.
- Do not weaken tests.

DONE WHEN:
- User-provided links are filtered.

VERIFY:
- Run `node --check docs/app.js`.
- Run the link rendering test.

OUTPUT:
- Changed files and verification output.

STOP RULES:
- Stop on secrets, production credentials, or destructive operations.
- Stop after three failed attempts on the same symptom.
