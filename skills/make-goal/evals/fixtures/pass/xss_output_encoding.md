/goal
GOAL:
Fix an XSS risk in Markdown rendering by replacing unsafe `innerHTML` usage with safe DOM construction or output encoding.

CONTEXT:
- Read `docs/entry-renderer.js`, `docs/app.js`, and the existing browser smoke test notes before editing.
- Use the current rendering behavior as the baseline.

CONSTRAINTS:
- Do not introduce unsafe HTML sinks, `eval`, shell string execution, or string-built queries.
- Preserve keyboard behavior and copy/verify controls.
- Verification integrity: do not weaken or bypass tests, assertions, lint, typecheck, validation, generated-output checks, screenshots, or external blockers to make the goal pass; fix the root cause or report the blocker.

DONE WHEN:
- User-controlled Markdown no longer reaches `innerHTML` or another unsafe sink.
- Existing entry rendering behavior remains intact for safe content.

VERIFY:
- Run `node --check docs/app.js`.
- Capture a browser smoke result or test result that exercises malicious Markdown and normal Markdown.

OUTPUT:
- Changed files, unsafe sink removed, verification output, and remaining risk.

STOP RULES:
- Stop if the fix requires changing trusted content policy or product rendering semantics.
- Stop on secrets, production credentials, destructive operations, or repository settings changes.
- Stop after three failed attempts on the same rendering failure.
