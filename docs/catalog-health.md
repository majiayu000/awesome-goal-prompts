# Catalog Health

## Summary

- Total entries: 327
- Source-backed entries: 127
- Seed entries: 200
- Categories: 32
- Search eval cases: 25/25 passing
- Source-backed entries missing evidence summaries: 0
- Source-backed entries missing provenance fields: 0

## Category Coverage

| Category | Source-backed | Total | Coverage |
| --- | --- | --- | --- |
| accessibility | 1 | 13 | 8% |
| ai-evals | 2 | 12 | 17% |
| ai-ops | 1 | 11 | 9% |
| backend-api | 3 | 15 | 20% |
| backend-data | 2 | 12 | 17% |
| backlog | 3 | 3 | 100% |
| cli | 2 | 2 | 100% |
| data-analytics | 1 | 11 | 9% |
| data-eng | 2 | 12 | 17% |
| design | 1 | 13 | 8% |
| devops-ci | 1 | 11 | 9% |
| devops-runtime | 1 | 11 | 9% |
| docs | 5 | 17 | 29% |
| frontend | 6 | 18 | 33% |
| goal-maintenance | 13 | 13 | 100% |
| greenfield-build | 1 | 1 | 100% |
| investigation | 4 | 4 | 100% |
| maintenance | 2 | 2 | 100% |
| migration | 9 | 9 | 100% |
| mobile | 2 | 14 | 14% |
| orchestration | 3 | 3 | 100% |
| performance | 6 | 18 | 33% |
| product | 3 | 15 | 20% |
| prompt-optimization | 4 | 4 | 100% |
| prototype | 3 | 3 | 100% |
| qa | 1 | 13 | 8% |
| refactor | 2 | 2 | 100% |
| research | 4 | 4 | 100% |
| security-appsec | 2 | 12 | 17% |
| security-ops | 1 | 11 | 9% |
| testing | 20 | 20 | 100% |
| workflow | 16 | 18 | 89% |

## Source Types

| Source type | Count |
| --- | --- |
| github-discussion | 1 |
| github-issue | 7 |
| github-pr | 3 |
| none | 200 |
| official-agent-task | 27 |
| official-goal | 17 |
| official-workflow | 5 |
| public-forum | 10 |
| third-party-project | 7 |
| third-party-review | 2 |
| third-party-tutorial | 21 |
| tool-readme | 11 |
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

## Maintenance Notes

- Prefer adding real source-backed examples to categories with low coverage before adding more seed patterns.
- Keep search evals aligned with natural user phrases, not only exact titles.
- Do not promote seed entries to source-backed without a public URL and evidence phrase.
