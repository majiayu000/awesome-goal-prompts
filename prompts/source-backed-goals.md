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
<a id="x-interview-driven-goal-prompt-generator"></a>
- [Interview-Driven Goal Prompt Generator](goal-examples.md#x-interview-driven-goal-prompt-generator) - Use a meta prompt to interview the user with clarifying questions until 'done' can be expressed in specific, measurable, verifiable terms, then output a high-quality structured /goal prompt.
<a id="github-noninteractive-goal-creation"></a>
- [Non-Interactive Goal Creation](goal-examples.md#github-noninteractive-goal-creation) - Create and confirm an active goal during non-interactive Codex execution before continuing.
<a id="github-goalbuddy-workspace"></a>
- [Prep A Goal Workspace](goal-examples.md#github-goalbuddy-workspace) - Prepare a goal workspace with board, notes, receipts, and an exact `/goal` command.
<a id="github-claude-long-goal-template"></a>
- [Long Goal With Constraints](goal-examples.md#github-claude-long-goal-template) - Use a longer goal template with repo path, constraints, plan pointer, and execution order.
<a id="deadreckon-coherence-closure"></a>
- [User-Facing Coherence Closure](goal-examples.md#deadreckon-coherence-closure) - Finish a coherence pass so CLI help, docs, JSON/plain output, colors, prompts, flags, and next-action grammar stay aligned.
<a id="x-three-questions-goal-framework"></a>
- [Three Questions Goal Framework](goal-examples.md#x-three-questions-goal-framework) - Write higher quality goals by explicitly answering three core questions: what needs to be done, how success will be measured, and what is off-limits.
<a id="x-explicit-stop-rules-goal-loops"></a>
- [Explicit Stop Rules for Goal Loops](goal-examples.md#x-explicit-stop-rules-goal-loops) - Prevent infinite loops, cost overruns, and unsafe behavior in autonomous /goal executions by defining clear, explicit stop conditions and escalation rules.
<a id="x-dual-model-evaluator-goal-loop"></a>
- [Dual-Model Evaluator Loop for Goals](goal-examples.md#x-dual-model-evaluator-goal-loop) - Run long /goal sessions reliably and cost-effectively by using a strong worker model for execution paired with a cheap fast evaluator model (typically Haiku) that periodically judges progress against the goal criteria and decides whether to continue or stop.
<a id="x-claude-md-goal-workflow"></a>
- [CLAUDE.md + Goal Workflow](goal-examples.md#x-claude-md-goal-workflow) - Combine a persistent project-level CLAUDE.md (or AGENTS.md) file containing rules, standards, and context with /goal commands so long-running autonomous agent work stays aligned with repository-specific constraints and learned lessons.
<a id="x-goal-ledger"></a>
- [Goal Ledger for Long-Running Runs](goal-examples.md#x-goal-ledger) - Maintain a live, browser-viewable HTML progress ledger during extended /goal executions to provide visibility, persistent memory, decision logging, and self-reflection, reducing drift in long autonomous sessions.
<a id="github-supergoal-artifact-backed-phase-runner"></a>
- [Artifact-Backed Phase Runner](goal-examples.md#github-supergoal-artifact-backed-phase-runner) - Run a long-horizon task from one short /goal by storing the roadmap, state, protocol, and phase specs on disk, then auditing final deliverables against the original plan.
<a id="github-copilot-well-scoped-agent-issue"></a>
- [Well-Scoped Agent Issue](goal-examples.md#github-copilot-well-scoped-agent-issue) - Turn a backlog item into a coding-agent-ready issue with a clear problem statement, acceptance criteria, file directions, and test expectations.
<a id="github-copilot-plan-before-pr"></a>
- [Research And Plan Before PR](goal-examples.md#github-copilot-plan-before-pr) - Have an agent research the repository, create an implementation plan, and iterate on a branch before deciding whether to open a pull request.
<a id="codex-goalcraft-six-field-contract"></a>
- [Goalcraft Six-Field Contract Spine](goal-examples.md#codex-goalcraft-six-field-contract) - Write any /goal as a compact, evidence-first, thread-scoped completion contract with explicit outcome, verification surface, constraints, boundaries, iteration policy, and blocked stop conditions instead of vague effort descriptions.
<a id="chinese-v2ex-grillme-strong-goal-contract"></a>
- [Strong Verifiable Goal Contract After Alignment Interview](goal-examples.md#chinese-v2ex-grillme-strong-goal-contract) - After a structured alignment interview, produce a binding /goal contract with explicit success evidence, hard constraints, file boundaries, iteration strategy, and blocking/escape handling so a Ralph-loop or native /goal agent can run autonomously until evidence-based completion.
<a id="simi-codex-acceptance-stop"></a>
- [Codex Acceptance-Criteria Stop](goal-examples.md#simi-codex-acceptance-stop) - Put explicit acceptance and stopping criteria directly in the agent task so it stops when the condition is met instead of running open-ended.
<a id="sunilpai-oracle-definition-of-done"></a>
- [Oracle Definition Of Done](goal-examples.md#sunilpai-oracle-definition-of-done) - Define an oracle — the concrete checks (tests, edge cases, benchmarks, static checks) that decide success — before running the agent task.
<a id="aimaker-goal-finish-line-evidence"></a>
- [Goal Finish Line Built From Evidence](goal-examples.md#aimaker-goal-finish-line-evidence) - Write the /goal finish line as an outcome plus success criteria built from evidence, not vibes, so the agent knows when it is truly done.

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
<a id="goal-md-fitness-dual-score-loop"></a>
- [Fitness Function Dual-Score Improvement Loop](goal-examples.md#goal-md-fitness-dual-score-loop) - For goals without natural scalar metric (docs quality, code health, consistency), construct an explicit runnable fitness function plus dual-score (outcome + instrument quality guard) and drive an improvement loop with iterations.jsonl ledger until converge criteria.

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
<a id="github-copilot-playwright-instructions"></a>
- [Playwright Test Instructions](goal-examples.md#github-copilot-playwright-instructions) - Create path-specific Playwright instructions that enforce stable locators, isolated tests, explicit assertions, cross-browser coverage, and CI behavior.
<a id="tecton-codex-voice-e2e-contract"></a>
- [Voice E2E Goal Contract](goal-examples.md#tecton-codex-voice-e2e-contract) - Run a long-horizon Codex goal against a TypeScript voice system using a reading list, working rules, concrete done-when criteria, and anti-pattern fences.

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
<a id="github-copilot-repository-instructions"></a>
- [Repository Agent Instructions](goal-examples.md#github-copilot-repository-instructions) - Add repository-level agent instructions that document project structure, build/test/validate commands, coding standards, and documentation expectations.
<a id="github-copilot-doc-code-sync"></a>
- [Documentation Matches Code](goal-examples.md#github-copilot-doc-code-sync) - Update stale API or function documentation so parameters, behavior, examples, thrown errors, and links match the current implementation.

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
<a id="github-copilot-cross-cutting-logging"></a>
- [Centralize Cross-Cutting Logging](goal-examples.md#github-copilot-cross-cutting-logging) - Centralize scattered logging, validation, security, or error-handling behavior without changing the core business behavior of the services.
<a id="fowler-structured-prompt-refactor"></a>
- [Structured-Prompt-Driven Refactor](goal-examples.md#fowler-structured-prompt-refactor) - Keep the spec or prompt and the code in sync during a refactor; when reality diverges, fix the prompt or spec first, then update the code.
<a id="openai-community-refactor-stop-conditions"></a>
- [Refactor Until Stop Conditions Met](goal-examples.md#openai-community-refactor-stop-conditions) - Let the agent iterate on a refactor continually until one of several predefined stop conditions is met, resolving blockers so each run works longer.

### security-ops
<a id="explainx-npm-audit-clean"></a>
- [NPM Audit Clean Remediation](goal-examples.md#explainx-npm-audit-clean) - Patch npm audit vulnerabilities without breaking tests or public APIs.
<a id="addyosmani-dependency-audit-triage"></a>
- [Dependency Audit Triage Boundaries](goal-examples.md#addyosmani-dependency-audit-triage) - Triage dependency audit results with explicit boundaries: audits only find known advisories, so verify before trusting a package and never commit secrets.

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
<a id="halmob-checkout-p95-goal"></a>
- [Checkout P95 Latency Goal](goal-examples.md#halmob-checkout-p95-goal) - Reduce checkout p95 latency below a numeric target while keeping the correctness suite green and logging each experiment.

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
<a id="github-copilot-usage-metrics-reconciliation"></a>
- [Copilot Usage Metrics Reconciliation](goal-examples.md#github-copilot-usage-metrics-reconciliation) - Reconcile Copilot dashboard, API, and export metrics before reporting agent adoption or pull-request impact trends.

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
<a id="github-copilot-research-architecture-report"></a>
- [Cited Architecture Research Report](goal-examples.md#github-copilot-research-architecture-report) - Produce a saved, cited Markdown architecture report after inspecting the local codebase, relevant repositories, and web sources.
<a id="halmob-research-reproduction-goal"></a>
- [Evidence-Backed Research Reproduction](goal-examples.md#halmob-research-reproduction-goal) - Reproduce a paper or research result as far as local materials allow while separating confirmed findings, approximate reconstructions, blocked claims, and remaining uncertainty.

### maintenance
<a id="apidog-repo-maintenance-audit"></a>
- [Repo Maintenance Audit](goal-examples.md#apidog-repo-maintenance-audit) - Find dead code, unused dependencies, and stale files, then produce a PR-ready justification list.
<a id="theaidaily-clean-worktree-budget"></a>
- [Clean Worktree File Budget](goal-examples.md#theaidaily-clean-worktree-budget) - Keep the worktree clean and enforce a source file size budget.

### devops-ci
<a id="explainx-ci-pipeline-green"></a>
- [CI Pipeline Green](goal-examples.md#explainx-ci-pipeline-green) - Repair CI test, lint, typecheck, and security scan failures until checks pass.
<a id="github-copilot-autopilot-ci-repair"></a>
- [Bounded Autopilot CI Repair](goal-examples.md#github-copilot-autopilot-ci-repair) - Run a bounded autonomous CI repair after plan acceptance, with explicit continuation limits, permissions, validation commands, and blocker reporting.

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
<a id="goal-builder-audit-friendly-template"></a>
- [Audit-Friendly Goal Template](goal-examples.md#goal-builder-audit-friendly-template) - Rewrite a vague /goal into a mappable contract with objective, scope, constraints, done-when evidence, stop rules, and token budget.
<a id="goal-ledger-html-resume-incomplete-hatch"></a>
- [Single-File HTML Goal Ledger with Resume Block and Structured Incomplete Escape](goal-examples.md#goal-ledger-html-resume-incomplete-hatch) - Maintain one canonical browser-viewable implementation-notes.html containing Resume Here block, inline progressEvents timeline, and explicit [incomplete]/[blocked] states with full reason/proof/impact so long-running /goal can safely pause and resume across compaction or handoff without drift.

### qa
<a id="x-qa-engineer-simulation"></a>
- [QA Engineer Simulation](goal-examples.md#x-qa-engineer-simulation) - Use `/goal` as a quality loop until tests pass and lint is clean.
<a id="github-copilot-cli-agentic-review"></a>
- [Terminal Agentic Code Review](goal-examples.md#github-copilot-cli-agentic-review) - Review a diff from the terminal with a scoped prompt, path, or file pattern, inspect suggested commands, and apply or reject findings before commit.
<a id="developersdigest-skill-exit-criteria"></a>
- [Agent Skill Exit Criteria](goal-examples.md#developersdigest-skill-exit-criteria) - Require exit criteria and a change report (files changed, commands run, commands not run, open risks) before an agent task counts as done.

### orchestration
<a id="hn-dag-agent-dispatch"></a>
- [DAG Agent Dispatch](goal-examples.md#hn-dag-agent-dispatch) - Split a goal into a dependency graph and dispatch independent agents into isolated worktrees.
<a id="deadreckon-semantic-merge-repair"></a>
- [DAG-Aware Semantic Merge Repair](goal-examples.md#deadreckon-semantic-merge-repair) - Make orchestration merge failures repairable by using plan DAG context, conflict bundles, planner-mediated repair, and bounded retry.
<a id="deadreckon-orchestration-eventbus"></a>
- [Plan EventBus Live UX](goal-examples.md#deadreckon-orchestration-eventbus) - Unify plan, fork, merge, and orchestrate around shared builders and a live plan event stream.
<a id="github-copilot-fleet-parallel-test-suite"></a>
- [Fleet Parallel Test Suite](goal-examples.md#github-copilot-fleet-parallel-test-suite) - Break a large test expansion into independent subtasks that subagents can execute in parallel while the orchestrator manages dependencies and final integration.

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
<a id="github-copilot-deadlock-minimization"></a>
- [Deadlock-Minimizing Transaction Rewrite](goal-examples.md#github-copilot-deadlock-minimization) - Rewrite transaction ordering and locking to reduce deadlock risk without adverse performance or data-integrity regressions.

### accessibility
<a id="github-accessibility-html-wcag"></a>
- [HTML WCAG Instruction Audit](goal-examples.md#github-accessibility-html-wcag) - Audit HTML changes against WCAG guidance and prove the Lighthouse accessibility audit passes.

### design
<a id="claude-reference-layout-design"></a>
- [Reference Layout Match](goal-examples.md#claude-reference-layout-design) - Build a settings page that follows an existing profile page layout instead of inventing a new pattern.
<a id="layout-design-system-context-export"></a>
- [Design System Context Export](goal-examples.md#layout-design-system-context-export) - Extract design tokens, components, and visual patterns into agent-readable context so generated UI follows the product design system.

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
<a id="goal-builder-openspec-rerank-provider"></a>
- [OpenSpec Rerank Provider Goal](goal-examples.md#goal-builder-openspec-rerank-provider) - Implement an OpenSpec feature change exactly as specified, adding a new rerank provider with contract tests, integration coverage, docs, and changelog evidence.

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
<a id="github-copilot-xss-innerhtml-fix"></a>
- [Unsafe innerHTML XSS Fix](goal-examples.md#github-copilot-xss-innerhtml-fix) - Find and fix XSS caused by unsafe innerHTML rendering while preserving the user-visible text and adding a regression guard.
<a id="simonroses-security-do-not-list"></a>
- [Security Do-NOT Constraint List](goal-examples.md#simonroses-security-do-not-list) - Build a growing Do-NOT constraint list from every security issue found in AI-generated code, and include it in future security prompts.
