# Catalog Health

## Summary

- Total entries: 351
- Source-backed entries: 151
- Seed entries: 200
- Categories: 32
- Search eval cases: 33/33 passing
- Source-backed entries missing evidence summaries: 0
- Source-backed entries missing provenance fields: 0

## Category Coverage

| Category | Source-backed | Total | Coverage |
| --- | --- | --- | --- |
| accessibility | 1 | 13 | 8% |
| ai-evals | 2 | 12 | 17% |
| ai-ops | 2 | 12 | 17% |
| backend-api | 3 | 15 | 20% |
| backend-data | 3 | 13 | 23% |
| backlog | 3 | 3 | 100% |
| cli | 2 | 2 | 100% |
| data-analytics | 2 | 12 | 17% |
| data-eng | 2 | 12 | 17% |
| design | 2 | 14 | 14% |
| devops-ci | 2 | 12 | 17% |
| devops-runtime | 1 | 11 | 9% |
| docs | 7 | 19 | 37% |
| frontend | 6 | 18 | 33% |
| goal-maintenance | 15 | 15 | 100% |
| greenfield-build | 1 | 1 | 100% |
| investigation | 4 | 4 | 100% |
| maintenance | 2 | 2 | 100% |
| migration | 9 | 9 | 100% |
| mobile | 2 | 14 | 14% |
| orchestration | 4 | 4 | 100% |
| performance | 7 | 19 | 37% |
| product | 3 | 15 | 20% |
| prompt-optimization | 5 | 5 | 100% |
| prototype | 3 | 3 | 100% |
| qa | 2 | 14 | 14% |
| refactor | 3 | 3 | 100% |
| research | 6 | 6 | 100% |
| security-appsec | 3 | 13 | 23% |
| security-ops | 1 | 11 | 9% |
| testing | 22 | 22 | 100% |
| workflow | 21 | 23 | 91% |

## Source Types

| Source type | Count |
| --- | --- |
| github-discussion | 1 |
| github-issue | 7 |
| github-pr | 3 |
| none | 200 |
| official-agent-task | 37 |
| official-goal | 17 |
| official-workflow | 8 |
| public-forum | 11 |
| third-party-project | 8 |
| third-party-review | 3 |
| third-party-tutorial | 23 |
| tool-readme | 17 |
| video-summary | 2 |
| x-post | 14 |

## Search Evaluation

| Query | Expected | Rank | Required | Status |
| --- | --- | --- | --- | --- |
| auth tests fail lint red | claude-auth-tests-lint | 1 | top 1 | pass |
| auth lint | claude-auth-tests-lint | 1 | top 3 | pass |
| database migration schema | claude-dev-database-migration | 1 | top 3 | pass |
| a11y wcag accessibility | github-accessibility-html-wcag | 1 | top 3 | pass |
| agent evals trace grading | openai-agent-trace-evals | 1 | top 3 | pass |
| agent tracing observability | openai-agent-tracing-observability | 1 | top 3 | pass |
| security guardrails tool calls | openai-tool-guardrails-appsec | 1 | top 3 | pass |
| backend api integration tests | openhands-api-integration-tests | 1 | top 3 | pass |
| mobile github issue agent | github-mobile-agent-task-handoff | 1 | top 3 | pass |
| remote agent server smoke | openhands-remote-agent-server-smoke | 1 | top 3 | pass |
| docs quickstart onboarding | docs-quickstart | 1 | top 5 | pass |
| feature flag percentage react hook | openhands-feature-flag-system | 1 | top 3 | pass |
| checkout crash root cause regression | openhands-checkout-crash-regression | 1 | top 3 | pass |
| slow query log optimization report | openhands-slow-query-optimization | 1 | top 3 | pass |
| semantic merge repair dag conflict planner | deadreckon-semantic-merge-repair | 1 | top 3 | pass |
| daily priority progress status | goal-agent-daily-priority-loop | 1 | top 3 | pass |
| sparc payment processing | claude-flow-sparc-payment-plan | 1 | top 3 | pass |
| okr measurable key results scoring guardrails | claude-recipes-okr-development | 1 | top 3 | pass |
| clinical research ai safety | clinical-research-ai-safety-boundary | 1 | top 3 | pass |
| legacy stack migration compatibility checkpoints rollback | openai-code-migration-checkpoints | 1 | top 3 | pass |
| difficult task eval driven improvement loop artifact score | openai-difficult-task-eval-loop | 1 | top 3 | pass |
| promptfoo eval suite target adapter seed cases assertions | openai-promptfoo-eval-suite | 1 | top 3 | pass |
| expo react native app expo router expo go | openai-expo-react-native-app | 1 | top 3 | pass |
| agent friendly cli companion skill command surface | openai-agent-friendly-cli-skill | 1 | top 3 | pass |
| define goal measurable evidence scope stop condition | openai-define-goal-quality-bar | 1 | top 3 | pass |
| audit friendly goal objective scope done when stop if | goal-builder-audit-friendly-template | 1 | top 3 | pass |
| copilot fleet parallel test suite subagents | github-copilot-fleet-parallel-test-suite | 1 | top 3 | pass |
| innerHTML xss unsafe rendering fix | github-copilot-xss-innerhtml-fix | 1 | top 3 | pass |
| checkout p95 latency benchmark correctness suite | halmob-checkout-p95-goal | 1 | top 3 | pass |
| voice e2e scenarios anti pattern fences goal | tecton-codex-voice-e2e-contract | 1 | top 3 | pass |
| copilot usage metrics dashboard api export reconciliation | github-copilot-usage-metrics-reconciliation | 1 | top 3 | pass |
| design tokens figma agent context layout md | layout-design-system-context-export | 1 | top 3 | pass |
| long horizon one goal roadmap state protocol phase specs | github-supergoal-artifact-backed-phase-runner | 1 | top 3 | pass |

## Maintenance Notes

- Prefer adding real source-backed examples to categories with low coverage before adding more seed patterns.
- Keep search evals aligned with natural user phrases, not only exact titles.
- Do not promote seed entries to source-backed without a public URL and evidence phrase.
