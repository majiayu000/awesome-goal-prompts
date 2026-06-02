# Growth Playbook

Use this as a one-week measurement plan for making awesome-goal-prompts easier to discover and contribute to. External outcomes are tracked, not guaranteed.

## Target Audiences

- Coding-agent users who need rescue contracts when an agent drifts, loops, or weakens verification.
- Maintainers who want source-backed examples for common repo tasks, CI failures, migrations, and security reviews.
- Contributors who can turn public docs, GitHub issues, forum threads, or tool READMEs into verifiable `/goal` catalog entries.

## Shareable Entry Points

| Entry point | What to share | Success signal |
| --- | --- | --- |
| Rescue prompts | `README.md` "Start With Ten Rescue Prompts" and `prompts/source-backed-goals.md` | Visitors copy a prompt or open a static goal page. |
| make-goal skill | `skills/make-goal/` plus `skills/make-goal/references/catalog-contribution.md` | Contributors submit source-backed entries with provenance fields. |
| Catalog search | https://majiayu000.github.io/awesome-goal-prompts/ | Search queries retrieve expected entries and users browse source-backed examples first. |

## One-Week Measurement

| Signal | Type | How to measure | Week-one target |
| --- | --- | --- | --- |
| GitHub Pages visits and referrers | Leading | GitHub repository traffic and Pages analytics if available | Directional increase after sharing; no fixed traffic guarantee. |
| Catalog search health | Leading | `python3 scripts/evaluate_search.py` | All eval cases pass after catalog changes. |
| Source-backed coverage | Leading | `python3 scripts/generate_catalog_health.py` and `docs/catalog-health.md` | Source-backed count rises without missing provenance fields. |
| Contributor PRs merged | Leading | GitHub PR list for source-backed entries or docs improvements | At least one reviewed PR path is clear and reproducible. |
| README contribution clicks | Leading | GitHub traffic for `CONTRIBUTING.md`, `docs/how-to-write-goals.md`, and `skills/make-goal/` | More views than baseline if GitHub exposes file traffic. |
| Stars | Lagging | GitHub repository stars | Track trend only; do not use as a completion criterion. |

## Manual Repo Settings Checklist

- Add or review repository topics such as `codex`, `claude-code`, `cursor`, `coding-agents`, `prompts`, and `goal`.
- Set a social preview image that shows the searchable catalog, not only the README title.
- Consider enabling GitHub Discussions for source suggestions and duplicate checks.
- Draft an awesome-list submission only after the source-backed catalog and contribution path are stable.
- Prepare social hooks around rescue prompts, the make-goal skill, and catalog search; do not promise stars, trending, ranking, or approval.

## Review Cadence

After one week, compare leading signals to the baseline, inspect failed or low-rank search queries, and choose the next smallest PR: more thin-category entries, a Chinese README slice, or additional search eval cases.
