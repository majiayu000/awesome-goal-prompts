# Launch Kit

Use this file as prepared launch copy. Adjust the links only if the repository or Pages URL changes.

## Primary Links

- GitHub: https://github.com/majiayu000/awesome-goal-prompts
- Live catalog: https://majiayu000.github.io/awesome-goal-prompts/
- Catalog health: https://github.com/majiayu000/awesome-goal-prompts/blob/main/docs/catalog-health.md

## Visual Assets

- Catalog browser screenshot: `docs/assets/catalog-browser.png`
- Contract detail screenshot: `docs/assets/auth-contract.png`

## One-Line Positioning

Awesome Goal Prompts is a searchable, source-backed catalog of runnable `/goal` task contracts for coding agents.

## X Post

I built Awesome Goal Prompts: a searchable catalog of runnable `/goal` task contracts for coding agents.

The problem: most prompt lists are vibes.

This one keeps the contract:

- one goal
- real context
- hard constraints
- done-when criteria
- verification commands
- stop rules
- source-backed provenance where available

Current state:

- 293 task contracts
- 93 source-backed examples
- GitHub Pages search UI
- start-here recipes
- copy/adapt controls
- catalog health report
- CI search evaluation

Use it when you want Codex, Claude Code, Hermes, or another coding agent to do real work without drifting into scope creep.

GitHub: https://github.com/majiayu000/awesome-goal-prompts
Live catalog: https://majiayu000.github.io/awesome-goal-prompts/

## X Thread

1/ I built Awesome Goal Prompts: a searchable catalog of runnable `/goal` task contracts for coding agents.

Most prompt lists are catchy. They are not operational.

This repo treats a goal as a contract.

2/ The contract shape:

- GOAL
- CONTEXT
- CONSTRAINTS
- DONE WHEN
- VERIFY
- OUTPUT
- STOP RULES

That is the difference between “fix the app” and a task an agent can actually finish.

3/ Current catalog:

- 293 task contracts
- 93 source-backed examples
- 32 categories
- official docs, GitHub issues/PRs, tutorials, forums, videos, and tool READMEs
- seed patterns clearly labeled as seed, not fake citations

4/ The live UI includes:

- search
- category browsing
- source type badges
- verification commands
- evidence summaries
- start-here recipes
- adapt-and-copy controls

5/ It also has quality gates:

- generated catalog data
- catalog health report
- search eval cases
- CI that fails on generated-file drift
- CI that checks JS syntax and search quality

6/ Example use cases:

- auth tests + lint red
- database migration safety
- agent trace observability
- API integration tests
- accessibility audit
- security guardrails
- mobile agent handoff

7/ The point is not to collect more prompts.

The point is to make long-running coding-agent work auditable:

- where did the prompt come from?
- what should it inspect?
- what must not change?
- how do we prove completion?
- when should the agent stop?

8/ GitHub:
https://github.com/majiayu000/awesome-goal-prompts

Live catalog:
https://majiayu000.github.io/awesome-goal-prompts/

## Hacker News Title Options

- Show HN: Awesome Goal Prompts, a source-backed catalog of coding-agent task contracts
- Show HN: I built a searchable catalog of runnable /goal prompts for coding agents
- Show HN: Goal prompts as verifiable task contracts, not prompt vibes

## Hacker News Body

I built Awesome Goal Prompts, a searchable catalog of `/goal` task contracts for coding agents like Codex, Claude Code, Hermes, and similar tools.

The motivation is that most prompt lists are hard to trust. They contain catchy phrasing, but not enough context, constraints, verification, or stop rules for long-running coding-agent work.

This repo treats a goal as a runnable contract:

- one measurable goal
- context the agent must inspect
- hard constraints and non-goals
- done-when criteria
- verification commands or artifacts
- stop rules for uncertainty, secrets, destructive operations, or repeated failed fixes

Current state:

- 293 task contracts
- 93 source-backed examples with public URLs and evidence summaries
- searchable GitHub Pages UI
- start-here recipes
- copy/adapt controls
- generated catalog health report
- search evaluation in CI

GitHub: https://github.com/majiayu000/awesome-goal-prompts
Live catalog: https://majiayu000.github.io/awesome-goal-prompts/

I am interested in examples of real goal-style prompts from public docs, issues, PRs, tutorials, forum posts, or READMEs.

## Reddit / Discord Short Post

I made a source-backed catalog of `/goal` prompts for coding agents.

It is not just a prompt dump. Each contract includes context, constraints, done-when, verification, output expectations, and stop rules. Source-backed examples include public URLs and evidence summaries; seed examples are clearly labeled.

Useful if you run Codex, Claude Code, Hermes, or similar agents on long-running tasks and want less scope drift.

GitHub: https://github.com/majiayu000/awesome-goal-prompts
Live catalog: https://majiayu000.github.io/awesome-goal-prompts/

## Launch Checklist

- Confirm latest `main` has green Catalog quality CI.
- Confirm GitHub Pages deploy is green.
- Confirm README screenshot renders on GitHub.
- Publish X post or thread.
- Submit to Hacker News with a Show HN title.
- Share in relevant Claude Code, Codex, and coding-agent communities.
- Ask early users for missing real source-backed examples rather than generic prompt ideas.
