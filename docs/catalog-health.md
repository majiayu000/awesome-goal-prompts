# Catalog Health

Generated on: 2026-05-15

## Summary

- Total entries: 293
- Source-backed entries: 93
- Seed entries: 200
- Categories: 32
- Search eval cases: 11/11 passing
- Source-backed entries missing evidence summaries: 0
- Source-backed entries missing provenance fields: 0

## Category Coverage

| Category | Source-backed | Total | Coverage |
| --- | --- | --- | --- |
| accessibility | 1 | 13 | 8% |
| ai-evals | 1 | 11 | 9% |
| ai-ops | 1 | 11 | 9% |
| backend-api | 1 | 13 | 8% |
| backend-data | 1 | 11 | 9% |
| backlog | 3 | 3 | 100% |
| cli | 1 | 1 | 100% |
| data-analytics | 1 | 11 | 9% |
| data-eng | 1 | 11 | 9% |
| design | 1 | 13 | 8% |
| devops-ci | 1 | 11 | 9% |
| devops-runtime | 1 | 11 | 9% |
| docs | 3 | 15 | 20% |
| frontend | 6 | 18 | 33% |
| goal-maintenance | 9 | 9 | 100% |
| greenfield-build | 1 | 1 | 100% |
| investigation | 2 | 2 | 100% |
| maintenance | 2 | 2 | 100% |
| migration | 8 | 8 | 100% |
| mobile | 1 | 13 | 8% |
| orchestration | 1 | 1 | 100% |
| performance | 3 | 15 | 20% |
| product | 1 | 13 | 8% |
| prompt-optimization | 3 | 3 | 100% |
| prototype | 3 | 3 | 100% |
| qa | 1 | 13 | 8% |
| refactor | 2 | 2 | 100% |
| research | 3 | 3 | 100% |
| security-appsec | 1 | 11 | 9% |
| security-ops | 1 | 11 | 9% |
| testing | 19 | 19 | 100% |
| workflow | 9 | 11 | 82% |

## Source Types

| Source type | Count |
| --- | --- |
| github-discussion | 1 |
| github-issue | 7 |
| github-pr | 3 |
| none | 200 |
| official-agent-task | 12 |
| official-goal | 17 |
| official-workflow | 5 |
| public-forum | 10 |
| third-party-project | 3 |
| third-party-review | 2 |
| third-party-tutorial | 20 |
| tool-readme | 3 |
| video-summary | 2 |
| x-post | 8 |

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

## Maintenance Notes

- Prefer adding real source-backed examples to categories with low coverage before adding more seed patterns.
- Keep search evals aligned with natural user phrases, not only exact titles.
- Do not promote seed entries to source-backed without a public URL and evidence phrase.
