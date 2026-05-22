# Pattern Selection

The awesome-goal-prompts catalog separates source-backed examples from seed patterns. Preserve that boundary.

## Source-Backed

Use a source-backed pattern when a close match exists and credibility matters.

Source-backed means:

- It is tied to a public URL and a concrete task, example, or usage rule.
- It has source metadata such as `source_name`, `source_url`, `source_type`, and `evidence`.
- The goal contract is rewritten as a reusable task contract; it is not copied verbatim from the source.

Do not claim source-backed status unless source metadata exists.

Common source types include:

- `official-goal`
- `official-workflow`
- `official-agent-task`
- `third-party-tutorial`
- `third-party-review`
- `third-party-project`
- `x-post`
- `public-forum`
- `github-issue`
- `github-pr`
- `github-discussion`
- `tool-readme`
- `video-summary`

## Seed

Use a seed pattern when no source-backed pattern fits but a reusable shape is useful.

Seed means:

- It is a reusable catalog pattern.
- It is not presented as collected from X, GitHub, docs, a tutorial, or a named author.
- It can later be promoted to source-backed only by adding real source metadata to the existing entry, not by duplicating it.

## Selection Procedure

1. Identify the user's task type and risk: fix, build, review, read-only investigation, migration, CI, security, data, frontend, docs, or plan.
2. Check `source-backed-index.md` for a close source-backed shape.
3. If no close source-backed pattern exists, check `seed-patterns-index.md`.
4. Adapt the shape to the user's real repository files, commands, constraints, and evidence.
5. Do not leave catalog placeholders such as generic `npm test` if the user provided a better local command.
6. If no pattern fits, use the base contract shape and make assumptions explicit.

## Do Not

- Do not copy a catalog prompt unchanged when the user's repository has different files or commands.
- Do not treat recipe filters as prompt templates.
- Do not invent a source URL, source type, category, or evidence phrase.
- Do not let pattern matching override the user's explicit constraints.
- Do not use a broad seed when a more specific source-backed pattern matches.
