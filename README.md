# Awesome Goal Prompts — Coding Agent Rescue Contracts

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Catalog quality](https://github.com/majiayu000/awesome-goal-prompts/actions/workflows/catalog.yml/badge.svg)](https://github.com/majiayu000/awesome-goal-prompts/actions/workflows/catalog.yml)
[![Pages](https://github.com/majiayu000/awesome-goal-prompts/actions/workflows/pages.yml/badge.svg)](https://github.com/majiayu000/awesome-goal-prompts/actions/workflows/pages.yml)
[![Release](https://img.shields.io/github/v/release/majiayu000/awesome-goal-prompts)](https://github.com/majiayu000/awesome-goal-prompts/releases/latest)
[![License: CC0-1.0](https://img.shields.io/badge/License-CC0--1.0-lightgrey.svg)](LICENSE)

When Claude Code, Codex, Cursor, or another coding agent starts making broad edits, paste a contract that says exactly what to inspect, what not to touch, how to verify, and when to stop.

This repo keeps <!-- generated:total-start -->**300+**<!-- generated:total-end --> runnable `/goal` contracts for engineering work. Start with the provenance-backed rescue prompts below; use seed patterns only when you need a raw shape to adapt.

**Search the full catalog:** https://majiayu000.github.io/awesome-goal-prompts/

A good goal is not a wish. It is a runnable contract: one goal, enough context to inspect, hard constraints, verifiable completion, and stop rules for uncertainty or risk. This repo turns that contract shape into a catalog you can search, inspect, adapt, and copy.

<!-- generated:stats-start -->
The public catalog starts with **151** source-backed examples drawn from official docs, public GitHub threads, tutorials, forum posts, and tool READMEs. The other **200** reusable seed patterns are kept in [Seed Patterns](prompts/seed-patterns.md) so they do not dilute provenance-backed examples.
<!-- generated:stats-end -->

![Awesome Goal Prompts — searchable prompt catalog for Claude Code, Codex, and Cursor coding agents](docs/assets/catalog-browser.png)

## Try It In 60 Seconds

1. **Open the searchable catalog** at https://majiayu000.github.io/awesome-goal-prompts/, or pick any contract straight from this README.
2. **Copy the full `/goal` contract text** — the whole block, including `GOAL`, `CONTEXT`, `CONSTRAINTS`, `DONE WHEN`, `VERIFY`, `OUTPUT`, and `STOP RULES`.
3. **Paste it to your coding agent** (Claude Code, Codex, or Cursor) and let it run.

First example — [Auth Tests And Lint Clean](prompts/source-backed-goals.md#claude-auth-tests-lint): use it when your auth tests and lint are both red and "fix auth" keeps inviting API churn.

**Expected outcome:** the agent keeps working until the auth tests pass and lint is clean, then stops only after pasting the passing command output as evidence. If it cannot reach that state, the stop rules tell it to report instead of editing further.

## Contribute A Goal In 5 Minutes

1. Find a thin category or missing rescue pattern in the [catalog browser](https://majiayu000.github.io/awesome-goal-prompts/) or [catalog health report](docs/catalog-health.md).
2. Draft the contract with [skills/make-goal/](skills/make-goal/) and its [catalog contribution reference](skills/make-goal/references/catalog-contribution.md).
3. Add the entry through [CONTRIBUTING.md](CONTRIBUTING.md): edit `data/source/entries.toml`, keep public provenance for source-backed examples, regenerate, and run the validation commands.

## Why This Exists

Most prompt lists stop at catchy instructions. This catalog is for the moment after an agent starts drifting: the task is real, the repo has constraints, and "try harder" is not enough. Each contract gives the agent a narrow job, required context, explicit boundaries, proof, and stop rules.

- **Source-backed where possible:** external examples keep a public URL, source type, evidence phrase, and generated evidence summary.
- **Runnable by design:** every prompt includes `GOAL`, `CONTEXT`, `CONSTRAINTS`, `DONE WHEN`, `VERIFY`, `OUTPUT`, and `STOP RULES`.
- **Search quality is tested:** representative user queries must retrieve the expected contract in CI.
- **Seed patterns are separated:** reusable patterns stay available, but the main catalog leads with source-backed contracts.

## Start With Ten Rescue Prompts

These are the front door. Each one is source-backed, tied to a common coding-agent failure mode, and links to the full copyable prompt.

| If the agent is failing at... | Copy this contract | Before | After |
| --- | --- | --- | --- |
| Auth tests and lint are both red | [Auth Tests And Lint Clean](prompts/source-backed-goals.md#claude-auth-tests-lint) | "Fix auth" invites API churn. | Auth behavior is preserved; tests and lint prove the fix. |
| CI has mixed test, lint, and typecheck failures | [CI Pipeline Green](prompts/source-backed-goals.md#explainx-ci-pipeline-green) | The agent chases one log line at a time. | Local and remote CI evidence define done. |
| A migration needs proof, not vibes | [Dev Database Migration Proof](prompts/source-backed-goals.md#claude-dev-database-migration) | The agent edits schema without rollback evidence. | Dev DB application and schema comparison are required. |
| A PR may have security bugs | [Security PR Review](prompts/source-backed-goals.md#openhands-security-pr-review) | Review comments stay generic. | File-level auth, injection, XSS, and secret risks are called out. |
| Checkout crashes from a stack trace | [Checkout Crash Regression Fix](prompts/source-backed-goals.md#openhands-checkout-crash-regression) | The agent patches the symptom. | Reproduction, root cause, fix, and regression test are all required. |
| Users see an empty billing state | [Billing Empty State Root Cause](prompts/source-backed-goals.md#reddit-billing-empty-state) | The agent rewrites pricing or webhooks. | The investigation is scoped to the empty-state cause. |
| A visual migration must not drift | [Visual Migration With Playwright](prompts/source-backed-goals.md#codex-visual-migration-playwright) | "Looks close" becomes the acceptance test. | Playwright checks preserve screen output. |
| Agent runs need traceability | [Agent Trace Observability](prompts/source-backed-goals.md#openai-agent-tracing-observability) | Tool calls and handoffs disappear in logs. | One representative run produces trace spans. |
| `npm audit` is red | [NPM Audit Clean Remediation](prompts/source-backed-goals.md#explainx-npm-audit-clean) | The agent upgrades packages blindly. | Audit and tests must both pass without public API breakage. |
| A plan may still have holes | [Review Plan Until No Gaps](prompts/source-backed-goals.md#github-review-plan-no-gaps) | The agent accepts the first plausible plan. | A fresh review must find no remaining gaps. |

The provenance-backed library stays below as the primary reference catalog.

## Contents

- [Try It In 60 Seconds](#try-it-in-60-seconds)
- [Contribute A Goal In 5 Minutes](#contribute-a-goal-in-5-minutes)
- [Why This Exists](#why-this-exists)
- [Start With Ten Rescue Prompts](#start-with-ten-rescue-prompts)
- [Source-Backed Catalog](#source-backed-catalog)
- [How To Write A Good Goal](#how-to-write-a-good-goal)
- [Catalog Health](#catalog-health)
- [Growth Playbook](#growth-playbook)
- [Templates](#templates)
- [Quality Bar](#quality-bar)
- [Sources And Caveats](#sources-and-caveats)
- [Contributing](#contributing)

## Source-Backed Catalog

The source-backed index lives in [prompts/source-backed-goals.md](prompts/source-backed-goals.md), and the searchable UI defaults to source-backed examples in the [GitHub Pages catalog](https://majiayu000.github.io/awesome-goal-prompts/).

Reusable patterns that are not backed by public sources live in [Seed Patterns](prompts/seed-patterns.md).

<!-- generated:catalog-start -->
### workflow
- [Verifiable End-State Contract](prompts/source-backed-goals.md#codex-verifiable-end-state) - Complete one goal only when a verifiable end state is met.
- [Four Files Walkthrough](prompts/source-backed-goals.md#hermes-four-files-walkthrough) - Create four note files across turns and verify each contains its number.
- [Meta Goal Prompt Generator](prompts/source-backed-goals.md#x-meta-goal-prompt-generator) - Ask the agent to inspect the session, repo, history, and docs before writing the actual `/goal` prompt.
- [AGENTS.md Goal Workflow](prompts/source-backed-goals.md#x-agentsmd-goal-workflow) - Use AGENTS.md rules together with `/goal` so long-running work keeps repo-specific constraints.
- [Plan-Then-Goal Execution](prompts/source-backed-goals.md#x-plan-then-goal-execution) - Use plan mode to define the work, then start a new goal session to implement the plan completely.
- [Measurable Goal Structure](prompts/source-backed-goals.md#x-measurable-goal-structure) - Write goals with a clear target, proof requirement, and explicit limits.
- [Interview-Driven Goal Prompt Generator](prompts/source-backed-goals.md#x-interview-driven-goal-prompt-generator) - Use a meta prompt to interview the user with clarifying questions until 'done' can be expressed in specific, measurable, verifiable terms, then output a high-quality structured /goal prompt.
- [Non-Interactive Goal Creation](prompts/source-backed-goals.md#github-noninteractive-goal-creation) - Create and confirm an active goal during non-interactive Codex execution before continuing.
- [Prep A Goal Workspace](prompts/source-backed-goals.md#github-goalbuddy-workspace) - Prepare a goal workspace with board, notes, receipts, and an exact `/goal` command.
- [Long Goal With Constraints](prompts/source-backed-goals.md#github-claude-long-goal-template) - Use a longer goal template with repo path, constraints, plan pointer, and execution order.
- [User-Facing Coherence Closure](prompts/source-backed-goals.md#deadreckon-coherence-closure) - Finish a coherence pass so CLI help, docs, JSON/plain output, colors, prompts, flags, and next-action grammar stay aligned.
- [Three Questions Goal Framework](prompts/source-backed-goals.md#x-three-questions-goal-framework) - Write higher quality goals by explicitly answering three core questions: what needs to be done, how success will be measured, and what is off-limits.
- [Explicit Stop Rules for Goal Loops](prompts/source-backed-goals.md#x-explicit-stop-rules-goal-loops) - Prevent infinite loops, cost overruns, and unsafe behavior in autonomous /goal executions by defining clear, explicit stop conditions and escalation rules.
- [Dual-Model Evaluator Loop for Goals](prompts/source-backed-goals.md#x-dual-model-evaluator-goal-loop) - Run long /goal sessions reliably and cost-effectively by using a strong worker model for execution paired with a cheap fast evaluator model (typically Haiku) that periodically judges progress against the goal criteria and decides whether to continue or stop.
- [CLAUDE.md + Goal Workflow](prompts/source-backed-goals.md#x-claude-md-goal-workflow) - Combine a persistent project-level CLAUDE.md (or AGENTS.md) file containing rules, standards, and context with /goal commands so long-running autonomous agent work stays aligned with repository-specific constraints and learned lessons.
- [Goal Ledger for Long-Running Runs](prompts/source-backed-goals.md#x-goal-ledger) - Maintain a live, browser-viewable HTML progress ledger during extended /goal executions to provide visibility, persistent memory, decision logging, and self-reflection, reducing drift in long autonomous sessions.
- [Artifact-Backed Phase Runner](prompts/source-backed-goals.md#github-supergoal-artifact-backed-phase-runner) - Run a long-horizon task from one short /goal by storing the roadmap, state, protocol, and phase specs on disk, then auditing final deliverables against the original plan.
- [Well-Scoped Agent Issue](prompts/source-backed-goals.md#github-copilot-well-scoped-agent-issue) - Turn a backlog item into a coding-agent-ready issue with a clear problem statement, acceptance criteria, file directions, and test expectations.
- [Research And Plan Before PR](prompts/source-backed-goals.md#github-copilot-plan-before-pr) - Have an agent research the repository, create an implementation plan, and iterate on a branch before deciding whether to open a pull request.
- [Goalcraft Six-Field Contract Spine](prompts/source-backed-goals.md#codex-goalcraft-six-field-contract) - Write any /goal as a compact, evidence-first, thread-scoped completion contract with explicit outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop conditions instead of vague effort descriptions.
- [Strong Verifiable Goal Contract After Alignment Interview](prompts/source-backed-goals.md#chinese-v2ex-grillme-strong-goal-contract) - After a structured alignment interview, produce a binding /goal contract with explicit success evidence, hard constraints, file boundaries, iteration strategy, and blocking/escape handling so a Ralph-loop or native /goal agent can run autonomously until evidence-based completion.

### migration
- [Visual Migration With Playwright](prompts/source-backed-goals.md#codex-visual-migration-playwright) - Migrate a project while preserving screen output and checking it with Playwright.
- [Feature Port With CI Green](prompts/source-backed-goals.md#hermes-feature-port-ci-green) - Port a feature from another repo, include tests, and get CI green.
- [Vue 2 To Vue 3 Visual And Unit Gate](prompts/source-backed-goals.md#qiita-vue2-vue3-visual-unit) - Migrate listed Vue screens and stop only when visual and unit tests pass.
- [Finish Migration Keep Tests Green](prompts/source-backed-goals.md#openai-slash-finish-migration) - Use `/goal` to complete a migration while keeping the relevant tests green.
- [Module API Migration](prompts/source-backed-goals.md#claude-module-api-migration) - Migrate a module to a new API while keeping call sites compiling and tests passing.
- [Moment To Day.js Migration](prompts/source-backed-goals.md#explainx-moment-dayjs-migration) - Replace Moment.js with Day.js while preserving date output across edge cases.
- [React 19 Migration](prompts/source-backed-goals.md#cursor-forum-react19-migration) - Migrate a project to React 19 and continue until the build passes.
- [Pydantic V1 To V2 Migration](prompts/source-backed-goals.md#github-pydantic-v2-migration) - Migrate a project from Pydantic v1 to v2 while preserving API behavior.
- [Code Migration Checkpoints](prompts/source-backed-goals.md#openai-code-migration-checkpoints) - Inventory legacy assumptions, map them to a target stack, and execute the migration through validated checkpoints.

### prototype
- [PLAN.md Milestone Prototype](prompts/source-backed-goals.md#codex-plan-milestone-prototype) - Implement a PLAN.md-driven prototype with tests at each milestone and browser verification.
- [Canvas Puzzle PLAN.md Prototype](prompts/source-backed-goals.md#qiita-canvas-puzzle-plan) - Implement PLAN.md milestones for a canvas puzzle prototype and prove e2e passes.
- [Rift Salvage Game Goal](prompts/source-backed-goals.md#video-rift-salvage-game) - Build a 2D combat game prototype with assets, combat, boss logic, and browser verification.

### prompt-optimization
- [Eval-Driven Prompt Optimization](prompts/source-backed-goals.md#codex-eval-prompt-optimization) - Optimize prompts against an eval suite until the target score or pass rate is reached.
- [Router Prompt Eval Score](prompts/source-backed-goals.md#qiita-router-eval-score) - Improve a router prompt against an eval directory until the result score reaches a target.
- [RAG Chat Flywheel](prompts/source-backed-goals.md#reddit-rag-chat-flywheel) - Iterate on code, tests, and metrics to improve a document-chat RAG system.
- [Difficult Task Eval Loop](prompts/source-backed-goals.md#openai-difficult-task-eval-loop) - Run a difficult task as an eval-driven improvement loop with one focused change, rerun scores, and direct artifact inspection each iteration.
- [Fitness Function Dual-Score Improvement Loop](prompts/source-backed-goals.md#goal-md-fitness-dual-score-loop) - For goals without natural scalar metric (docs quality, code health, consistency), construct an explicit runnable fitness function plus dual-score (outcome + instrument quality guard) and drive an improvement loop with iterations.jsonl ledger until converge criteria.

### testing
- [Auth Tests And Lint Clean](prompts/source-backed-goals.md#claude-auth-tests-lint) - Keep working until auth tests pass and the lint step is clean.
- [Ruff Clean Source Tree](prompts/source-backed-goals.md#hermes-ruff-src-clean) - Fix every lint error in src and prove ruff passes.
- [TypeScript ESLint Coverage Gate](prompts/source-backed-goals.md#explainx-typescript-eslint-coverage) - Resolve TypeScript errors, pass tests, clear ESLint warnings, and keep coverage above a threshold.
- [Fix Hermes CLI Tests](prompts/source-backed-goals.md#hermes-cli-tests-pass) - Fix failing Hermes CLI tests until the project test script passes.
- [Add Authentication Tests](prompts/source-backed-goals.md#google-jules-auth-tests) - Create unit tests for an authentication module in a Jules session.
- [Add UserService Unit Tests](prompts/source-backed-goals.md#openhands-userservice-tests) - Add unit tests for UserService and raise target coverage to the documented threshold.
- [Parallel Test Coverage Recovery](prompts/source-backed-goals.md#devin-parallel-coverage-recovery) - Find low-coverage modules and open separate test-improvement PRs for each module.
- [Single Vitest Case Fix](prompts/source-backed-goals.md#qiita-aochan-single-vitest-fix) - Fix a quiz application until one named Vitest case passes.
- [Full Quiz Test Recovery](prompts/source-backed-goals.md#qiita-aochan-full-vitest-recovery) - Repair the quiz app until the full Vitest suite exits cleanly.
- [Auth Coverage Lift](prompts/source-backed-goals.md#jdhodges-auth-coverage-lift) - Raise authentication code coverage from the documented baseline to the documented target within a scoped edit boundary.
- [Auth Test Repair Boundary](prompts/source-backed-goals.md#apidog-auth-test-repair) - Fix failing auth tests while preserving the documented file boundary.
- [Coverage Autoresearch Loop](prompts/source-backed-goals.md#udit-coverage-autoresearch) - Iterate on tests until coverage reaches the documented target.
- [Test And TypeScript Clean](prompts/source-backed-goals.md#theaidaily-test-typescript-clean) - Keep working until tests exit cleanly and TypeScript errors are gone.
- [Go Race Cleanup](prompts/source-backed-goals.md#cursor-forum-go-race-cleanup) - Eliminate data races detected by the Go race detector.
- [Tests And Lint Completion](prompts/source-backed-goals.md#x-tests-lint-completion) - Run a `/goal` loop until all tests pass and lint is clean.
- [Tests Pass And PR Ready](prompts/source-backed-goals.md#reddit-tests-pass-pr-ready) - Keep Claude Code working until tests pass and the PR is ready for review.
- [Flaky Auth Tests Goal](prompts/source-backed-goals.md#github-claude-goal-flaky-auth) - Use a Claude goal plugin example to find and fix flaky authentication tests.
- [Improve Benchmark Coverage](prompts/source-backed-goals.md#github-benchmark-coverage-goal) - Use `/goal` to improve benchmark coverage and persist the command in history.
- [Batch Fix Bugs](prompts/source-backed-goals.md#github-claude-batch-bugs) - Use a Claude Code goal to fix a numbered batch of bugs without looping on missing skills.
- [GOAP Coverage Target Plan](prompts/source-backed-goals.md#claude-flow-coverage-goap) - Raise test coverage with an explicit test pyramid across unit, integration, and end-to-end coverage targets.
- [Playwright Test Instructions](prompts/source-backed-goals.md#github-copilot-playwright-instructions) - Create path-specific Playwright instructions that enforce stable locators, isolated tests, explicit assertions, cross-browser coverage, and CI behavior.
- [Voice E2E Goal Contract](prompts/source-backed-goals.md#tecton-codex-voice-e2e-contract) - Run a long-horizon Codex goal against a TypeScript voice system using a reading list, working rules, concrete done-when criteria, and anti-pattern fences.

### docs
- [Weekly Changelog Coverage](prompts/source-backed-goals.md#claude-weekly-changelog) - Ensure CHANGELOG.md includes an entry for every PR merged this week.
- [Contributor README Rewrite](prompts/source-backed-goals.md#apidog-contributor-readme) - Rewrite README installation, run, test, and architecture guidance for new contributors.
- [Public API Docs Coverage](prompts/source-backed-goals.md#explainx-public-api-jsdoc) - Add JSDoc and examples for public functions while keeping documentation links valid.
- [Payment Retry Logic Diagram](prompts/source-backed-goals.md#claude-payment-retry-diagram) - Explain payment retry behavior as a browsable HTML page with a diagram for developer or support review.
- [Implementation Notes Decision Ledger](prompts/source-backed-goals.md#deadreckon-implementation-notes-ledger) - Keep live implementation notes and the final run decisions document aligned around decisions, deviations, tradeoffs, and open questions.
- [Repository Agent Instructions](prompts/source-backed-goals.md#github-copilot-repository-instructions) - Add repository-level agent instructions that document project structure, build/test/validate commands, coding standards, and documentation expectations.
- [Documentation Matches Code](prompts/source-backed-goals.md#github-copilot-doc-code-sync) - Update stale API or function documentation so parameters, behavior, examples, thrown errors, and links match the current implementation.

### investigation
- [Session Drift Report](prompts/source-backed-goals.md#hermes-session-drift-report) - Investigate session ID drift during mid-run compression and write a report.
- [Billing Empty State Root Cause](prompts/source-backed-goals.md#reddit-billing-empty-state) - Find why active subscriptions show an empty state without changing pricing or webhook code.
- [Checkout Crash Regression Fix](prompts/source-backed-goals.md#openhands-checkout-crash-regression) - Reproduce a checkout crash from a stack trace, identify the root cause, fix it, and add a regression test.
- [Build Log Failure Diagnosis](prompts/source-backed-goals.md#claude-build-log-diagnosis) - Use a provided build log to explain why the build fails and identify the smallest verified fix path.

### cli
- [EXIF Rename CLI](prompts/source-backed-goals.md#hermes-exif-rename-cli) - Build a small CLI that renames photos by EXIF date and test it on a photos folder.
- [Agent-Friendly CLI And Skill](prompts/source-backed-goals.md#openai-agent-friendly-cli-skill) - Create a composable CLI and companion skill so future agent tasks can search, read, download, or draft against a recurring source safely.

### refactor
- [Auth Dependency Injection Refactor](prompts/source-backed-goals.md#explainx-auth-di-refactor) - Refactor auth code to dependency injection while preserving tests, coverage, and public API.
- [Split Oversized File](prompts/source-backed-goals.md#claude-split-oversized-file) - Split an oversized source file into focused modules while preserving behavior.
- [Centralize Cross-Cutting Logging](prompts/source-backed-goals.md#github-copilot-cross-cutting-logging) - Centralize scattered logging, validation, security, or error-handling behavior without changing the core business behavior of the services.

### security-ops
- [NPM Audit Clean Remediation](prompts/source-backed-goals.md#explainx-npm-audit-clean) - Patch npm audit vulnerabilities without breaking tests or public APIs.

### performance
- [Lighthouse And Core Web Vitals Gate](prompts/source-backed-goals.md#explainx-lighthouse-core-web-vitals) - Improve Lighthouse and Core Web Vitals to explicit thresholds without regressions.
- [Bundle Size Reduction](prompts/source-backed-goals.md#udit-bundle-size-reduction) - Iteratively reduce bundle size below the documented threshold.
- [Benchmark Optimization](prompts/source-backed-goals.md#udit-benchmark-optimization) - Optimize performance against a benchmark command until the goal is reached.
- [Order Service Performance Review](prompts/source-backed-goals.md#openhands-orderservice-performance-review) - Inspect service code for N+1 queries, missing indexes, inefficient loops, missing caches, and unnecessary fetching.
- [Node Memory Leak Fix](prompts/source-backed-goals.md#openhands-node-memory-leak-fix) - Investigate a growing-memory Node.js process, isolate the leak source, fix it, and add monitoring for recurrence.
- [GOAP API Latency Reduction](prompts/source-backed-goals.md#claude-flow-api-latency-goap) - Reduce API latency by profiling current performance, optimizing database queries, adding caching, and improving code paths.
- [Checkout P95 Latency Goal](prompts/source-backed-goals.md#halmob-checkout-p95-goal) - Reduce checkout p95 latency below a numeric target while keeping the correctness suite green and logging each experiment.

### greenfield-build
- [Build Design Tool From Scratch](prompts/source-backed-goals.md#openai-long-horizon-design-tool) - Run a long-horizon Codex task to build a design tool with milestone verification.

### product
- [Design Doc Acceptance Complete](prompts/source-backed-goals.md#claude-design-doc-acceptance) - Implement a design document until every acceptance criterion is satisfied.
- [Feature Flag System](prompts/source-backed-goals.md#openhands-feature-flag-system) - Implement boolean, percentage, and user-based feature flags with service logic, API middleware, a React hook, docs, and tests.
- [OKR Development From Vague Priorities](prompts/source-backed-goals.md#claude-recipes-okr-development) - Turn vague strategic priorities into measurable OKRs with objectives, key results, alignment, scoring, guardrails, and a communication summary.

### backlog
- [Clear Labeled Issue Backlog](prompts/source-backed-goals.md#claude-clear-labeled-issues) - Work through a labeled issue queue until no matching issues remain.
- [Clear Trading App Backlog](prompts/source-backed-goals.md#reddit-trading-backlog-clearance) - Generate a roadmap backlog for a trading app and then clear it with goals.
- [Ship Backlog Features](prompts/source-backed-goals.md#reddit-ship-backlog-features) - Implement the feature list from BACKLOG.md until CI is green.

### data-analytics
- [Analyze Product Usage Patterns](prompts/source-backed-goals.md#cursor-usage-pattern-analysis) - Analyze product usage patterns between tab view and agent panels.
- [Copilot Usage Metrics Reconciliation](prompts/source-backed-goals.md#github-copilot-usage-metrics-reconciliation) - Reconcile Copilot dashboard, API, and export metrics before reporting agent adoption or pull-request impact trends.

### frontend
- [Fix Freezing Chart Tooltips](prompts/source-backed-goals.md#cursor-chart-tooltip-freeze) - Debug and fix chart tooltips that freeze on hover.
- [Improve Common Error Messages](prompts/source-backed-goals.md#github-copilot-error-messages) - Use a cloud coding agent to implement user-friendly messages for common errors.
- [Visual Feedback With Test Guard](prompts/source-backed-goals.md#qiita-aochan-visual-feedback) - Add correct and wrong answer visual feedback while keeping tests green.
- [Theme Toggle Persistence](prompts/source-backed-goals.md#apidog-theme-toggle) - Add a dark and light theme toggle that persists across refreshes.
- [Button Console Error Fix](prompts/source-backed-goals.md#hn-button-console-error-fix) - Use browser automation to click a button, inspect console errors, fix the issue, and prove it.
- [Next.js Chat History Sidebar](prompts/source-backed-goals.md#video-nextjs-chat-sidebar) - Replace a Next.js sidebar with chat history, then test, fix build issues, and push.

### research
- [Read-Only Font Match](prompts/source-backed-goals.md#jdhodges-read-only-font-match) - Research font matches in read-only mode and produce a report without purchasing or downloading assets.
- [Public Benchmark Table](prompts/source-backed-goals.md#apidog-benchmark-table) - Collect distinct public benchmarks and build a date-sorted comparison table.
- [Review Sentiment JSON Agent](prompts/source-backed-goals.md#hn-review-sentiment-json-agent) - Fetch reviews with browser automation, classify sentiment, and write structured JSON output.
- [Clinical Research AI Safety Boundary](prompts/source-backed-goals.md#clinical-research-ai-safety-boundary) - Review clinical research AI work with evidence-first boundaries so agents do not invent medical sources, expose private data, or turn research notes into patient-specific advice.
- [Cited Architecture Research Report](prompts/source-backed-goals.md#github-copilot-research-architecture-report) - Produce a saved, cited Markdown architecture report after inspecting the local codebase, relevant repositories, and web sources.
- [Evidence-Backed Research Reproduction](prompts/source-backed-goals.md#halmob-research-reproduction-goal) - Reproduce a paper or research result as far as local materials allow while separating confirmed findings, approximate reconstructions, blocked claims, and remaining uncertainty.

### maintenance
- [Repo Maintenance Audit](prompts/source-backed-goals.md#apidog-repo-maintenance-audit) - Find dead code, unused dependencies, and stale files, then produce a PR-ready justification list.
- [Clean Worktree File Budget](prompts/source-backed-goals.md#theaidaily-clean-worktree-budget) - Keep the worktree clean and enforce a source file size budget.

### devops-ci
- [CI Pipeline Green](prompts/source-backed-goals.md#explainx-ci-pipeline-green) - Repair CI test, lint, typecheck, and security scan failures until checks pass.
- [Bounded Autopilot CI Repair](prompts/source-backed-goals.md#github-copilot-autopilot-ci-repair) - Run a bounded autonomous CI repair after plan acceptance, with explicit continuation limits, permissions, validation commands, and blocker reporting.

### goal-maintenance
- [Goal Escape Hatch](prompts/source-backed-goals.md#x-goal-escape-hatch) - Add an explicit incomplete state for impossible subtasks so a goal loop can stop safely.
- [Goal-Forge Done-When Loop](prompts/source-backed-goals.md#x-goal-forge-done-when) - Write a GOAL.md-style contract where `done_when` controls completion instead of vague success claims.
- [Review Plan Until No Gaps](prompts/source-backed-goals.md#github-review-plan-no-gaps) - Loop on implementation-plan review until a fresh review finds no remaining gaps.
- [Long Task Until Verification](prompts/source-backed-goals.md#github-long-task-verification) - Continue a long-running task until final verification passes rather than stopping on partial progress.
- [Completion Audit Before Done](prompts/source-backed-goals.md#github-completion-audit-before-done) - Audit completion criteria before calling the goal complete.
- [Goal Permission Context Sync](prompts/source-backed-goals.md#github-goal-permission-context) - Ensure goal continuation uses the current permission context after approval mode changes.
- [Real CLI Goal Loop](prompts/source-backed-goals.md#github-hermes-real-cli-loop) - Verify a real CLI goal loop where the second judge round confirms completion.
- [Verify File Creation](prompts/source-backed-goals.md#github-hermes-file-verification) - Verify that a requested file was actually created instead of trusting the agent claim.
- [Queue Follow-Up Goals](prompts/source-backed-goals.md#github-hermes-goal-queue) - Promote queued follow-up goals: fix tests, run full tests, then produce coverage.
- [Daily Goal Priority Loop](prompts/source-backed-goals.md#goal-agent-daily-priority-loop) - Use a persistent goal profile to compute daily priorities, execute them, log progress, and refresh status across sessions.
- [Goal-Aligned Profile Optimization](prompts/source-backed-goals.md#goal-agent-profile-optimization) - Audit and update professional profiles against a stated goal while recording the resulting progress and gaps.
- [Content And Audience Engagement Loop](prompts/source-backed-goals.md#goal-agent-content-engagement-loop) - Generate goal-aligned content, publish or promote it, engage with target audience posts, and log the session outcome.
- [Define Goal Quality Bar](prompts/source-backed-goals.md#openai-define-goal-quality-bar) - Turn a fuzzy intention into a concrete measurable goal with evidence, scope boundaries, and honest stop conditions before creating it.
- [Audit-Friendly Goal Template](prompts/source-backed-goals.md#goal-builder-audit-friendly-template) - Rewrite a vague /goal into a mappable contract with objective, scope, constraints, done-when evidence, stop rules, and token budget.
- [Single-File HTML Goal Ledger with Resume Block and Structured Incomplete Escape](prompts/source-backed-goals.md#goal-ledger-html-resume-incomplete-hatch) - Maintain one canonical browser-viewable implementation-notes.html containing Resume Here block, inline progressEvents timeline, and explicit [incomplete]/[blocked] states with full reason/proof/impact so long-running /goal can safely pause and resume across compaction or handoff without drift.

### qa
- [QA Engineer Simulation](prompts/source-backed-goals.md#x-qa-engineer-simulation) - Use `/goal` as a quality loop until tests pass and lint is clean.
- [Terminal Agentic Code Review](prompts/source-backed-goals.md#github-copilot-cli-agentic-review) - Review a diff from the terminal with a scoped prompt, path, or file pattern, inspect suggested commands, and apply or reject findings before commit.

### orchestration
- [DAG Agent Dispatch](prompts/source-backed-goals.md#hn-dag-agent-dispatch) - Split a goal into a dependency graph and dispatch independent agents into isolated worktrees.
- [DAG-Aware Semantic Merge Repair](prompts/source-backed-goals.md#deadreckon-semantic-merge-repair) - Make orchestration merge failures repairable by using plan DAG context, conflict bundles, planner-mediated repair, and bounded retry.
- [Plan EventBus Live UX](prompts/source-backed-goals.md#deadreckon-orchestration-eventbus) - Unify plan, fork, merge, and orchestrate around shared builders and a live plan event stream.
- [Fleet Parallel Test Suite](prompts/source-backed-goals.md#github-copilot-fleet-parallel-test-suite) - Break a large test expansion into independent subtasks that subagents can execute in parallel while the orchestrator manages dependencies and final integration.

### backend-api
- [API Integration Tests](prompts/source-backed-goals.md#openhands-api-integration-tests) - Add end-to-end tests for product API endpoints with success and error cases.
- [User Preferences API](prompts/source-backed-goals.md#openhands-user-preferences-api) - Add GET, PUT, and PATCH endpoints for user preferences with validation, service logic, OpenAPI docs, and tests.
- [SPARC Payment Processing Plan](prompts/source-backed-goals.md#claude-flow-sparc-payment-plan) - Plan and implement payment processing through SPARC phases with requirements, pseudocode, architecture, TDD refinement, and integration.

### backend-data
- [Dev Database Migration Proof](prompts/source-backed-goals.md#claude-dev-database-migration) - Write a migration, run it against the dev database, and confirm the schema matches.
- [Slow Query Optimization Report](prompts/source-backed-goals.md#openhands-slow-query-optimization) - Analyze slow query logs, explain bottlenecks, recommend indexes or rewrites, and produce prioritized SQL changes.
- [Deadlock-Minimizing Transaction Rewrite](prompts/source-backed-goals.md#github-copilot-deadlock-minimization) - Rewrite transaction ordering and locking to reduce deadlock risk without adverse performance or data-integrity regressions.

### accessibility
- [HTML WCAG Instruction Audit](prompts/source-backed-goals.md#github-accessibility-html-wcag) - Audit HTML changes against WCAG guidance and prove the Lighthouse accessibility audit passes.

### design
- [Reference Layout Match](prompts/source-backed-goals.md#claude-reference-layout-design) - Build a settings page that follows an existing profile page layout instead of inventing a new pattern.
- [Design System Context Export](prompts/source-backed-goals.md#layout-design-system-context-export) - Extract design tokens, components, and visual patterns into agent-readable context so generated UI follows the product design system.

### mobile
- [Mobile Agent Task Handoff](prompts/source-backed-goals.md#github-mobile-agent-task-handoff) - Prepare and track a coding-agent task started from GitHub Mobile with review-ready evidence.
- [Expo React Native App Slice](prompts/source-backed-goals.md#openai-expo-react-native-app) - Build a working React Native app slice with Expo Router conventions, Expo-compatible packages, and native-feeling UI states.

### ai-evals
- [Trace-Graded Agent Regression](prompts/source-backed-goals.md#openai-agent-trace-evals) - Create trace-based evals that catch workflow regressions across tool calls and handoffs.
- [Promptfoo Eval Suite](prompts/source-backed-goals.md#openai-promptfoo-eval-suite) - Add a runnable Promptfoo eval suite for an AI application before changing production prompts or model behavior.

### ai-ops
- [Agent Trace Observability](prompts/source-backed-goals.md#openai-agent-tracing-observability) - Instrument agent runs so LLM generations, tool calls, handoffs, guardrails, and custom events are traceable.
- [OpenSpec Rerank Provider Goal](prompts/source-backed-goals.md#goal-builder-openspec-rerank-provider) - Implement an OpenSpec feature change exactly as specified, adding a new rerank provider with contract tests, integration coverage, docs, and changelog evidence.

### data-eng
- [CSV Processing Report](prompts/source-backed-goals.md#openhands-csv-processing-report) - Create a data processing script that validates CSV input and generates an analysis report.
- [Rate-Limited Web Scraper](prompts/source-backed-goals.md#openhands-rate-limited-web-scraper) - Build a scraper that extracts product data across paginated pages while respecting rate limits and logging progress.

### devops-runtime
- [Remote Agent Server Smoke](prompts/source-backed-goals.md#openhands-remote-agent-server-smoke) - Deploy an isolated remote agent server and prove event streaming, workspace access, and command execution work.

### security-appsec
- [Tool Guardrails For AppSec](prompts/source-backed-goals.md#openai-tool-guardrails-appsec) - Add tool guardrails around high-risk agent tool calls and stop unsafe input or output before execution continues.
- [Security PR Review](prompts/source-backed-goals.md#openhands-security-pr-review) - Review a pull request for input validation, authentication, injection, XSS, and secrets risks with file-level fixes.
- [Unsafe innerHTML XSS Fix](prompts/source-backed-goals.md#github-copilot-xss-innerhtml-fix) - Find and fix XSS caused by unsafe innerHTML rendering while preserving the user-visible text and adding a regression guard.
<!-- generated:catalog-end -->

## How To Write A Good Goal

Start with the tutorial: [How To Write A Good `/goal`](docs/how-to-write-goals.md).

The short version: write one measurable goal, point at the real context, add hard constraints, define `DONE WHEN`, require fresh verification, and give the agent explicit stop rules for uncertainty or risk.

## Catalog Health

The generated [catalog health report](docs/catalog-health.md) tracks source-backed coverage, source types, and search evaluation results.

## Growth Playbook

Use [docs/growth-playbook.md](docs/growth-playbook.md) to plan one-week contributor and traffic measurement. It separates leading signals such as catalog traffic, search eval health, and merged PRs from lagging indicators such as stars.

## Templates

- [Full template](templates/full-goal-template.md) for high-risk or multi-step work.
- [Compact template](templates/compact-goal-template.md) for routine work.
- [Structured JSON data](data/examples.json) for search, tooling, or site generation.
- [Start-here recipes](data/recipes.json) for common user entry points.
- [Data schema](docs/schema.md) for provenance fields and source types.

## Quality Bar

- One example should cover one measurable goal.
- The prompt must include verification that can run in a real repository or produce a concrete artifact.
- New externally sourced examples must include `source_name`, `source_url`, `source_type`, `evidence`, and generated `evidence_summary` in `data/examples.json`.
- Do not add undocumented slash-command behavior, fake tool capabilities, or examples copied from private/non-verifiable sources.

## Sources And Caveats

See [SOURCES.md](SOURCES.md) for public sources used by source-backed examples and notes about cross-tool differences.

This repository does not claim that `/goal` behaves identically across Codex, Claude Code, Hermes, or other tools.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before adding examples. Keep descriptions short, source-backed when based on external material, and scoped to verifiable engineering work.
