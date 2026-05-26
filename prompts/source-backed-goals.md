# Source-Backed Goal Contracts

These source-backed contracts are the primary catalog. Follow each link for the full prompt body in the complete archive.

## Index

### workflow
<a id="codex-verifiable-end-state"></a>
- [Verifiable End-State Contract](goal-examples.md#codex-verifiable-end-state) - Complete one goal only when a verifiable end state is met.
<a id="hermes-four-files-walkthrough"></a>
- [Four Files Walkthrough](goal-examples.md#hermes-four-files-walkthrough) - Create four note files across turns and verify each contains its number.
<a id="x-meta-goal-prompt-generator"></a>
- [Meta Goal Prompt Generator](goal-examples.md#x-meta-goal-prompt-generator) - Ask the agent to inspect the session, repo, history, and docs before writing the actual `/goal` prompt.
<a id="x-agentsmd-goal-workflow"></a>
- [AGENTS.md Goal Workflow](goal-examples.md#x-agentsmd-goal-workflow) - Use AGENTS.md rules together with `/goal` so long-running work keeps repo-specific constraints.
<a id="x-plan-then-goal-execution"></a>
- [Plan-Then-Goal Execution](goal-examples.md#x-plan-then-goal-execution) - Use plan mode to define the work, then start a new goal session to implement the plan completely.
<a id="x-measurable-goal-structure"></a>
- [Measurable Goal Structure](goal-examples.md#x-measurable-goal-structure) - Write goals with a clear target, proof requirement, and explicit limits.
<a id="github-noninteractive-goal-creation"></a>
- [Non-Interactive Goal Creation](goal-examples.md#github-noninteractive-goal-creation) - Create and confirm an active goal during non-interactive Codex execution before continuing.
<a id="github-goalbuddy-workspace"></a>
- [Prep A Goal Workspace](goal-examples.md#github-goalbuddy-workspace) - Prepare a goal workspace with board, notes, receipts, and an exact `/goal` command.
<a id="github-claude-long-goal-template"></a>
- [Long Goal With Constraints](goal-examples.md#github-claude-long-goal-template) - Use a longer goal template with repo path, constraints, plan pointer, and execution order.
<a id="deadreckon-coherence-closure"></a>
- [User-Facing Coherence Closure](goal-examples.md#deadreckon-coherence-closure) - Finish a coherence pass so CLI help, docs, JSON/plain output, colors, prompts, flags, and next-action grammar stay aligned.

### migration
<a id="codex-visual-migration-playwright"></a>
- [Visual Migration With Playwright](goal-examples.md#codex-visual-migration-playwright) - Migrate a project while preserving screen output and checking it with Playwright.
<a id="hermes-feature-port-ci-green"></a>
- [Feature Port With CI Green](goal-examples.md#hermes-feature-port-ci-green) - Port a feature from another repo, include tests, and get CI green.
<a id="qiita-vue2-vue3-visual-unit"></a>
- [Vue 2 To Vue 3 Visual And Unit Gate](goal-examples.md#qiita-vue2-vue3-visual-unit) - Migrate listed Vue screens and stop only when visual and unit tests pass.
<a id="openai-slash-finish-migration"></a>
- [Finish Migration Keep Tests Green](goal-examples.md#openai-slash-finish-migration) - Use `/goal` to complete a migration while keeping the relevant tests green.
<a id="claude-module-api-migration"></a>
- [Module API Migration](goal-examples.md#claude-module-api-migration) - Migrate a module to a new API while keeping call sites compiling and tests passing.
<a id="explainx-moment-dayjs-migration"></a>
- [Moment To Day.js Migration](goal-examples.md#explainx-moment-dayjs-migration) - Replace Moment.js with Day.js while preserving date output across edge cases.
<a id="cursor-forum-react19-migration"></a>
- [React 19 Migration](goal-examples.md#cursor-forum-react19-migration) - Migrate a project to React 19 and continue until the build passes.
<a id="github-pydantic-v2-migration"></a>
- [Pydantic V1 To V2 Migration](goal-examples.md#github-pydantic-v2-migration) - Migrate a project from Pydantic v1 to v2 while preserving API behavior.
<a id="openai-code-migration-checkpoints"></a>
- [Code Migration Checkpoints](goal-examples.md#openai-code-migration-checkpoints) - Inventory legacy assumptions, map them to a target stack, and execute the migration through validated checkpoints.

### prototype
<a id="codex-plan-milestone-prototype"></a>
- [PLAN.md Milestone Prototype](goal-examples.md#codex-plan-milestone-prototype) - Implement a PLAN.md-driven prototype with tests at each milestone and browser verification.
<a id="qiita-canvas-puzzle-plan"></a>
- [Canvas Puzzle PLAN.md Prototype](goal-examples.md#qiita-canvas-puzzle-plan) - Implement PLAN.md milestones for a canvas puzzle prototype and prove e2e passes.
<a id="video-rift-salvage-game"></a>
- [Rift Salvage Game Goal](goal-examples.md#video-rift-salvage-game) - Build a 2D combat game prototype with assets, combat, boss logic, and browser verification.

### prompt-optimization
<a id="codex-eval-prompt-optimization"></a>
- [Eval-Driven Prompt Optimization](goal-examples.md#codex-eval-prompt-optimization) - Optimize prompts against an eval suite until the target score or pass rate is reached.
<a id="qiita-router-eval-score"></a>
- [Router Prompt Eval Score](goal-examples.md#qiita-router-eval-score) - Improve a router prompt against an eval directory until the result score reaches a target.
<a id="reddit-rag-chat-flywheel"></a>
- [RAG Chat Flywheel](goal-examples.md#reddit-rag-chat-flywheel) - Iterate on code, tests, and metrics to improve a document-chat RAG system.
<a id="openai-difficult-task-eval-loop"></a>
- [Difficult Task Eval Loop](goal-examples.md#openai-difficult-task-eval-loop) - Run a difficult task as an eval-driven improvement loop with one focused change, rerun scores, and direct artifact inspection each iteration.

### testing
<a id="claude-auth-tests-lint"></a>
- [Auth Tests And Lint Clean](goal-examples.md#claude-auth-tests-lint) - Keep working until auth tests pass and the lint step is clean.
<a id="hermes-ruff-src-clean"></a>
- [Ruff Clean Source Tree](goal-examples.md#hermes-ruff-src-clean) - Fix every lint error in src and prove ruff passes.
<a id="explainx-typescript-eslint-coverage"></a>
- [TypeScript ESLint Coverage Gate](goal-examples.md#explainx-typescript-eslint-coverage) - Resolve TypeScript errors, pass tests, clear ESLint warnings, and keep coverage above a threshold.
<a id="hermes-cli-tests-pass"></a>
- [Fix Hermes CLI Tests](goal-examples.md#hermes-cli-tests-pass) - Fix failing Hermes CLI tests until the project test script passes.
<a id="google-jules-auth-tests"></a>
- [Add Authentication Tests](goal-examples.md#google-jules-auth-tests) - Create unit tests for an authentication module in a Jules session.
<a id="openhands-userservice-tests"></a>
- [Add UserService Unit Tests](goal-examples.md#openhands-userservice-tests) - Add unit tests for UserService and raise target coverage to the documented threshold.
<a id="devin-parallel-coverage-recovery"></a>
- [Parallel Test Coverage Recovery](goal-examples.md#devin-parallel-coverage-recovery) - Find low-coverage modules and open separate test-improvement PRs for each module.
<a id="qiita-aochan-single-vitest-fix"></a>
- [Single Vitest Case Fix](goal-examples.md#qiita-aochan-single-vitest-fix) - Fix a quiz application until one named Vitest case passes.
<a id="qiita-aochan-full-vitest-recovery"></a>
- [Full Quiz Test Recovery](goal-examples.md#qiita-aochan-full-vitest-recovery) - Repair the quiz app until the full Vitest suite exits cleanly.
<a id="jdhodges-auth-coverage-lift"></a>
- [Auth Coverage Lift](goal-examples.md#jdhodges-auth-coverage-lift) - Raise authentication code coverage from the documented baseline to the documented target within a scoped edit boundary.
<a id="apidog-auth-test-repair"></a>
- [Auth Test Repair Boundary](goal-examples.md#apidog-auth-test-repair) - Fix failing auth tests while preserving the documented file boundary.
<a id="udit-coverage-autoresearch"></a>
- [Coverage Autoresearch Loop](goal-examples.md#udit-coverage-autoresearch) - Iterate on tests until coverage reaches the documented target.
<a id="theaidaily-test-typescript-clean"></a>
- [Test And TypeScript Clean](goal-examples.md#theaidaily-test-typescript-clean) - Keep working until tests exit cleanly and TypeScript errors are gone.
<a id="cursor-forum-go-race-cleanup"></a>
- [Go Race Cleanup](goal-examples.md#cursor-forum-go-race-cleanup) - Eliminate data races detected by the Go race detector.
<a id="x-tests-lint-completion"></a>
- [Tests And Lint Completion](goal-examples.md#x-tests-lint-completion) - Run a `/goal` loop until all tests pass and lint is clean.
<a id="reddit-tests-pass-pr-ready"></a>
- [Tests Pass And PR Ready](goal-examples.md#reddit-tests-pass-pr-ready) - Keep Claude Code working until tests pass and the PR is ready for review.
<a id="github-claude-goal-flaky-auth"></a>
- [Flaky Auth Tests Goal](goal-examples.md#github-claude-goal-flaky-auth) - Use a Claude goal plugin example to find and fix flaky authentication tests.
<a id="github-benchmark-coverage-goal"></a>
- [Improve Benchmark Coverage](goal-examples.md#github-benchmark-coverage-goal) - Use `/goal` to improve benchmark coverage and persist the command in history.
<a id="github-claude-batch-bugs"></a>
- [Batch Fix Bugs](goal-examples.md#github-claude-batch-bugs) - Use a Claude Code goal to fix a numbered batch of bugs without looping on missing skills.
<a id="claude-flow-coverage-goap"></a>
- [GOAP Coverage Target Plan](goal-examples.md#claude-flow-coverage-goap) - Raise test coverage with an explicit test pyramid across unit, integration, and end-to-end coverage targets.

### docs
<a id="claude-weekly-changelog"></a>
- [Weekly Changelog Coverage](goal-examples.md#claude-weekly-changelog) - Ensure CHANGELOG.md includes an entry for every PR merged this week.
<a id="apidog-contributor-readme"></a>
- [Contributor README Rewrite](goal-examples.md#apidog-contributor-readme) - Rewrite README installation, run, test, and architecture guidance for new contributors.
<a id="explainx-public-api-jsdoc"></a>
- [Public API Docs Coverage](goal-examples.md#explainx-public-api-jsdoc) - Add JSDoc and examples for public functions while keeping documentation links valid.
<a id="claude-payment-retry-diagram"></a>
- [Payment Retry Logic Diagram](goal-examples.md#claude-payment-retry-diagram) - Explain payment retry behavior as a browsable HTML page with a diagram for developer or support review.
<a id="deadreckon-implementation-notes-ledger"></a>
- [Implementation Notes Decision Ledger](goal-examples.md#deadreckon-implementation-notes-ledger) - Keep live implementation notes and the final run decisions document aligned around decisions, deviations, tradeoffs, and open questions.

### investigation
<a id="hermes-session-drift-report"></a>
- [Session Drift Report](goal-examples.md#hermes-session-drift-report) - Investigate session ID drift during mid-run compression and write a report.
<a id="reddit-billing-empty-state"></a>
- [Billing Empty State Root Cause](goal-examples.md#reddit-billing-empty-state) - Find why active subscriptions show an empty state without changing pricing or webhook code.
<a id="openhands-checkout-crash-regression"></a>
- [Checkout Crash Regression Fix](goal-examples.md#openhands-checkout-crash-regression) - Reproduce a checkout crash from a stack trace, identify the root cause, fix it, and add a regression test.
<a id="claude-build-log-diagnosis"></a>
- [Build Log Failure Diagnosis](goal-examples.md#claude-build-log-diagnosis) - Use a provided build log to explain why the build fails and identify the smallest verified fix path.

### cli
<a id="hermes-exif-rename-cli"></a>
- [EXIF Rename CLI](goal-examples.md#hermes-exif-rename-cli) - Build a small CLI that renames photos by EXIF date and test it on a photos folder.
<a id="openai-agent-friendly-cli-skill"></a>
- [Agent-Friendly CLI And Skill](goal-examples.md#openai-agent-friendly-cli-skill) - Create a composable CLI and companion skill so future agent tasks can search, read, download, or draft against a recurring source safely.

### refactor
<a id="explainx-auth-di-refactor"></a>
- [Auth Dependency Injection Refactor](goal-examples.md#explainx-auth-di-refactor) - Refactor auth code to dependency injection while preserving tests, coverage, and public API.
<a id="claude-split-oversized-file"></a>
- [Split Oversized File](goal-examples.md#claude-split-oversized-file) - Split an oversized source file into focused modules while preserving behavior.

### security-ops
<a id="explainx-npm-audit-clean"></a>
- [NPM Audit Clean Remediation](goal-examples.md#explainx-npm-audit-clean) - Patch npm audit vulnerabilities without breaking tests or public APIs.

### performance
<a id="explainx-lighthouse-core-web-vitals"></a>
- [Lighthouse And Core Web Vitals Gate](goal-examples.md#explainx-lighthouse-core-web-vitals) - Improve Lighthouse and Core Web Vitals to explicit thresholds without regressions.
<a id="udit-bundle-size-reduction"></a>
- [Bundle Size Reduction](goal-examples.md#udit-bundle-size-reduction) - Iteratively reduce bundle size below the documented threshold.
<a id="udit-benchmark-optimization"></a>
- [Benchmark Optimization](goal-examples.md#udit-benchmark-optimization) - Optimize performance against a benchmark command until the goal is reached.
<a id="openhands-orderservice-performance-review"></a>
- [Order Service Performance Review](goal-examples.md#openhands-orderservice-performance-review) - Inspect service code for N+1 queries, missing indexes, inefficient loops, missing caches, and unnecessary fetching.
<a id="openhands-node-memory-leak-fix"></a>
- [Node Memory Leak Fix](goal-examples.md#openhands-node-memory-leak-fix) - Investigate a growing-memory Node.js process, isolate the leak source, fix it, and add monitoring for recurrence.
<a id="claude-flow-api-latency-goap"></a>
- [GOAP API Latency Reduction](goal-examples.md#claude-flow-api-latency-goap) - Reduce API latency by profiling current performance, optimizing database queries, adding caching, and improving code paths.

### greenfield-build
<a id="openai-long-horizon-design-tool"></a>
- [Build Design Tool From Scratch](goal-examples.md#openai-long-horizon-design-tool) - Run a long-horizon Codex task to build a design tool with milestone verification.

### product
<a id="claude-design-doc-acceptance"></a>
- [Design Doc Acceptance Complete](goal-examples.md#claude-design-doc-acceptance) - Implement a design document until every acceptance criterion is satisfied.
<a id="openhands-feature-flag-system"></a>
- [Feature Flag System](goal-examples.md#openhands-feature-flag-system) - Implement boolean, percentage, and user-based feature flags with service logic, API middleware, a React hook, docs, and tests.
<a id="claude-recipes-okr-development"></a>
- [OKR Development From Vague Priorities](goal-examples.md#claude-recipes-okr-development) - Turn vague strategic priorities into measurable OKRs with objectives, key results, alignment, scoring, guardrails, and a communication summary.

### backlog
<a id="claude-clear-labeled-issues"></a>
- [Clear Labeled Issue Backlog](goal-examples.md#claude-clear-labeled-issues) - Work through a labeled issue queue until no matching issues remain.
<a id="reddit-trading-backlog-clearance"></a>
- [Clear Trading App Backlog](goal-examples.md#reddit-trading-backlog-clearance) - Generate a roadmap backlog for a trading app and then clear it with goals.
<a id="reddit-ship-backlog-features"></a>
- [Ship Backlog Features](goal-examples.md#reddit-ship-backlog-features) - Implement the feature list from BACKLOG.md until CI is green.

### data-analytics
<a id="cursor-usage-pattern-analysis"></a>
- [Analyze Product Usage Patterns](goal-examples.md#cursor-usage-pattern-analysis) - Analyze product usage patterns between tab view and agent panels.

### frontend
<a id="cursor-chart-tooltip-freeze"></a>
- [Fix Freezing Chart Tooltips](goal-examples.md#cursor-chart-tooltip-freeze) - Debug and fix chart tooltips that freeze on hover.
<a id="github-copilot-error-messages"></a>
- [Improve Common Error Messages](goal-examples.md#github-copilot-error-messages) - Use a cloud coding agent to implement user-friendly messages for common errors.
<a id="qiita-aochan-visual-feedback"></a>
- [Visual Feedback With Test Guard](goal-examples.md#qiita-aochan-visual-feedback) - Add correct and wrong answer visual feedback while keeping tests green.
<a id="apidog-theme-toggle"></a>
- [Theme Toggle Persistence](goal-examples.md#apidog-theme-toggle) - Add a dark and light theme toggle that persists across refreshes.
<a id="hn-button-console-error-fix"></a>
- [Button Console Error Fix](goal-examples.md#hn-button-console-error-fix) - Use browser automation to click a button, inspect console errors, fix the issue, and prove it.
<a id="video-nextjs-chat-sidebar"></a>
- [Next.js Chat History Sidebar](goal-examples.md#video-nextjs-chat-sidebar) - Replace a Next.js sidebar with chat history, then test, fix build issues, and push.

### research
<a id="jdhodges-read-only-font-match"></a>
- [Read-Only Font Match](goal-examples.md#jdhodges-read-only-font-match) - Research font matches in read-only mode and produce a report without purchasing or downloading assets.
<a id="apidog-benchmark-table"></a>
- [Public Benchmark Table](goal-examples.md#apidog-benchmark-table) - Collect distinct public benchmarks and build a date-sorted comparison table.
<a id="hn-review-sentiment-json-agent"></a>
- [Review Sentiment JSON Agent](goal-examples.md#hn-review-sentiment-json-agent) - Fetch reviews with browser automation, classify sentiment, and write structured JSON output.
<a id="clinical-research-ai-safety-boundary"></a>
- [Clinical Research AI Safety Boundary](goal-examples.md#clinical-research-ai-safety-boundary) - Review clinical research AI work with evidence-first boundaries so agents do not invent medical sources, expose private data, or turn research notes into patient-specific advice.

### maintenance
<a id="apidog-repo-maintenance-audit"></a>
- [Repo Maintenance Audit](goal-examples.md#apidog-repo-maintenance-audit) - Find dead code, unused dependencies, and stale files, then produce a PR-ready justification list.
<a id="theaidaily-clean-worktree-budget"></a>
- [Clean Worktree File Budget](goal-examples.md#theaidaily-clean-worktree-budget) - Keep the worktree clean and enforce a source file size budget.

### devops-ci
<a id="explainx-ci-pipeline-green"></a>
- [CI Pipeline Green](goal-examples.md#explainx-ci-pipeline-green) - Repair CI test, lint, typecheck, and security scan failures until checks pass.

### goal-maintenance
<a id="x-goal-escape-hatch"></a>
- [Goal Escape Hatch](goal-examples.md#x-goal-escape-hatch) - Add an explicit incomplete state for impossible subtasks so a goal loop can stop safely.
<a id="x-goal-forge-done-when"></a>
- [Goal-Forge Done-When Loop](goal-examples.md#x-goal-forge-done-when) - Write a GOAL.md-style contract where `done_when` controls completion instead of vague success claims.
<a id="github-review-plan-no-gaps"></a>
- [Review Plan Until No Gaps](goal-examples.md#github-review-plan-no-gaps) - Loop on implementation-plan review until a fresh review finds no remaining gaps.
<a id="github-long-task-verification"></a>
- [Long Task Until Verification](goal-examples.md#github-long-task-verification) - Continue a long-running task until final verification passes rather than stopping on partial progress.
<a id="github-completion-audit-before-done"></a>
- [Completion Audit Before Done](goal-examples.md#github-completion-audit-before-done) - Audit completion criteria before calling the goal complete.
<a id="github-goal-permission-context"></a>
- [Goal Permission Context Sync](goal-examples.md#github-goal-permission-context) - Ensure goal continuation uses the current permission context after approval mode changes.
<a id="github-hermes-real-cli-loop"></a>
- [Real CLI Goal Loop](goal-examples.md#github-hermes-real-cli-loop) - Verify a real CLI goal loop where the second judge round confirms completion.
<a id="github-hermes-file-verification"></a>
- [Verify File Creation](goal-examples.md#github-hermes-file-verification) - Verify that a requested file was actually created instead of trusting the agent claim.
<a id="github-hermes-goal-queue"></a>
- [Queue Follow-Up Goals](goal-examples.md#github-hermes-goal-queue) - Promote queued follow-up goals: fix tests, run full tests, then produce coverage.
<a id="goal-agent-daily-priority-loop"></a>
- [Daily Goal Priority Loop](goal-examples.md#goal-agent-daily-priority-loop) - Use a persistent goal profile to compute daily priorities, execute them, log progress, and refresh status across sessions.
<a id="goal-agent-profile-optimization"></a>
- [Goal-Aligned Profile Optimization](goal-examples.md#goal-agent-profile-optimization) - Audit and update professional profiles against a stated goal while recording the resulting progress and gaps.
<a id="goal-agent-content-engagement-loop"></a>
- [Content And Audience Engagement Loop](goal-examples.md#goal-agent-content-engagement-loop) - Generate goal-aligned content, publish or promote it, engage with target audience posts, and log the session outcome.
<a id="openai-define-goal-quality-bar"></a>
- [Define Goal Quality Bar](goal-examples.md#openai-define-goal-quality-bar) - Turn a fuzzy intention into a concrete measurable goal with evidence, scope boundaries, and honest stop conditions before creating it.

### qa
<a id="x-qa-engineer-simulation"></a>
- [QA Engineer Simulation](goal-examples.md#x-qa-engineer-simulation) - Use `/goal` as a quality loop until tests pass and lint is clean.

### orchestration
<a id="hn-dag-agent-dispatch"></a>
- [DAG Agent Dispatch](goal-examples.md#hn-dag-agent-dispatch) - Split a goal into a dependency graph and dispatch independent agents into isolated worktrees.
<a id="deadreckon-semantic-merge-repair"></a>
- [DAG-Aware Semantic Merge Repair](goal-examples.md#deadreckon-semantic-merge-repair) - Make orchestration merge failures repairable by using plan DAG context, conflict bundles, planner-mediated repair, and bounded retry.
<a id="deadreckon-orchestration-eventbus"></a>
- [Plan EventBus Live UX](goal-examples.md#deadreckon-orchestration-eventbus) - Unify plan, fork, merge, and orchestrate around shared builders and a live plan event stream.

### backend-api
<a id="openhands-api-integration-tests"></a>
- [API Integration Tests](goal-examples.md#openhands-api-integration-tests) - Add end-to-end tests for product API endpoints with success and error cases.
<a id="openhands-user-preferences-api"></a>
- [User Preferences API](goal-examples.md#openhands-user-preferences-api) - Add GET, PUT, and PATCH endpoints for user preferences with validation, service logic, OpenAPI docs, and tests.
<a id="claude-flow-sparc-payment-plan"></a>
- [SPARC Payment Processing Plan](goal-examples.md#claude-flow-sparc-payment-plan) - Plan and implement payment processing through SPARC phases with requirements, pseudocode, architecture, TDD refinement, and integration.

### backend-data
<a id="claude-dev-database-migration"></a>
- [Dev Database Migration Proof](goal-examples.md#claude-dev-database-migration) - Write a migration, run it against the dev database, and confirm the schema matches.
<a id="openhands-slow-query-optimization"></a>
- [Slow Query Optimization Report](goal-examples.md#openhands-slow-query-optimization) - Analyze slow query logs, explain bottlenecks, recommend indexes or rewrites, and produce prioritized SQL changes.

### accessibility
<a id="github-accessibility-html-wcag"></a>
- [HTML WCAG Instruction Audit](goal-examples.md#github-accessibility-html-wcag) - Audit HTML changes against WCAG guidance and prove the Lighthouse accessibility audit passes.

### design
<a id="claude-reference-layout-design"></a>
- [Reference Layout Match](goal-examples.md#claude-reference-layout-design) - Build a settings page that follows an existing profile page layout instead of inventing a new pattern.

### mobile
<a id="github-mobile-agent-task-handoff"></a>
- [Mobile Agent Task Handoff](goal-examples.md#github-mobile-agent-task-handoff) - Prepare and track a coding-agent task started from GitHub Mobile with review-ready evidence.
<a id="openai-expo-react-native-app"></a>
- [Expo React Native App Slice](goal-examples.md#openai-expo-react-native-app) - Build a working React Native app slice with Expo Router conventions, Expo-compatible packages, and native-feeling UI states.

### ai-evals
<a id="openai-agent-trace-evals"></a>
- [Trace-Graded Agent Regression](goal-examples.md#openai-agent-trace-evals) - Create trace-based evals that catch workflow regressions across tool calls and handoffs.
<a id="openai-promptfoo-eval-suite"></a>
- [Promptfoo Eval Suite](goal-examples.md#openai-promptfoo-eval-suite) - Add a runnable Promptfoo eval suite for an AI application before changing production prompts or model behavior.

### ai-ops
<a id="openai-agent-tracing-observability"></a>
- [Agent Trace Observability](goal-examples.md#openai-agent-tracing-observability) - Instrument agent runs so LLM generations, tool calls, handoffs, guardrails, and custom events are traceable.

### data-eng
<a id="openhands-csv-processing-report"></a>
- [CSV Processing Report](goal-examples.md#openhands-csv-processing-report) - Create a data processing script that validates CSV input and generates an analysis report.
<a id="openhands-rate-limited-web-scraper"></a>
- [Rate-Limited Web Scraper](goal-examples.md#openhands-rate-limited-web-scraper) - Build a scraper that extracts product data across paginated pages while respecting rate limits and logging progress.

### devops-runtime
<a id="openhands-remote-agent-server-smoke"></a>
- [Remote Agent Server Smoke](goal-examples.md#openhands-remote-agent-server-smoke) - Deploy an isolated remote agent server and prove event streaming, workspace access, and command execution work.

### security-appsec
<a id="openai-tool-guardrails-appsec"></a>
- [Tool Guardrails For AppSec](goal-examples.md#openai-tool-guardrails-appsec) - Add tool guardrails around high-risk agent tool calls and stop unsafe input or output before execution continues.
<a id="openhands-security-pr-review"></a>
- [Security PR Review](goal-examples.md#openhands-security-pr-review) - Review a pull request for input validation, authentication, injection, XSS, and secrets risks with file-level fixes.
