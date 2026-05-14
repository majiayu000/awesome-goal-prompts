# Contributing

Every example must be useful as a small task specification, not just a catchy prompt.

## Required Shape

Each prompt must include:

- `GOAL`: one objective, not a backlog
- `CONTEXT`: what the agent must inspect before acting
- `CONSTRAINTS`: boundaries, non-goals, and safety rules
- `DONE WHEN`: a measurable completion state
- `VERIFY`: exact command, artifact, report, or manual evidence
- `OUTPUT`: what the final report must contain
- `STOP RULES`: when to pause instead of guessing

If an example is based on a public post, documentation page, article, or repository, add:

- `source_name`: short human-readable source name
- `source_url`: canonical public URL
- `source_type`: one of the provenance classes in `SOURCES.md`
- `evidence`: a short phrase from, or tightly tied to, the public source
- `origin`: `source-backed`

If there is no verifiable public source, keep `origin` as `seed` and do not describe it as collected from X, GitHub, docs, or a named author.

## Quality Bar

Accept examples that:

- Have a real engineering scenario.
- Include deterministic verification where possible.
- Protect tests, data, secrets, user-visible behavior, and production systems.
- Teach a reusable pattern that is meaningfully different from existing examples.

Reject examples that:

- Say only "optimize the app", "fix all bugs", or "make it better".
- Ask the agent to weaken tests, swallow errors, invent contracts, or bypass auth.
- Require reading, printing, or hardcoding secrets.
- Ask for automatic merge, force push, or production deployment without explicit human approval.
- Differ from an existing example only by framework, language, or wording.

## De-Duplication Rules

- Same goal plus same verification is a duplicate.
- Keep at most three examples per theme: basic, complex, and high-risk.
- Prefer a more specific example over a broad one.
- Prefer examples with concrete verification over examples that rely only on subjective judgment.

## Review Checklist

- The task has exactly one primary objective.
- The done condition is mechanically checkable or evidence-based.
- The constraints prevent scope creep.
- The verification does not depend on prior claims or stale logs.
- The stop rules cover missing secrets, missing production access, destructive data operations, and repeated failed fixes.
- Source-backed examples include a public URL, source type, and evidence phrase.
- Seed examples are not presented as external citations.
