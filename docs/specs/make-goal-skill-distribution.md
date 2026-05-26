# Make Goal Skill Distribution Spec

Status: Proposed
Date: 2026-05-26
Owner: majiayu000

## Summary

Package the existing `skills/make-goal` workflow as an installable Codex skill distribution while preserving this repository's primary value: a source-backed `/goal` contract catalog with deterministic data, search, and skill quality gates.

This spec is informed by a review of `Kappaemme-git/codex-mvp-goal-skill` at commit `81f9c51`. The useful pattern is the distribution shape: a small npm package with a CLI installer that copies a bundled skill directory into `~/.codex/skills/<name>`. The content model and quality bar should stay local to `awesome-goal-prompts`.

## Problem

The repository already has a mature `make-goal` skill:

- `skills/make-goal/SKILL.md`
- deterministic linter and evals in `skills/make-goal/scripts/`
- catalog references in `skills/make-goal/references/`
- CI coverage through `.github/workflows/catalog.yml`

Users can browse and copy contracts from the site, but there is no first-class install path for using `make-goal` directly in Codex. That leaves a gap between "search the catalog" and "use this as a local workflow".

## Goals

- Add a one-command local install path for `skills/make-goal`.
- Keep the installer simple, auditable, and offline after package download.
- Make the package name, CLI names, and install target explicit.
- Add README and docs guidance that treats the skill as a companion to the catalog, not a replacement for it.
- Add launch or demo notes that show how to test the skill without weakening catalog quality requirements.
- Preserve all current catalog validation, search eval, metadata, and skill fixture checks.

## Non-Goals

- Do not rewrite `skills/make-goal/SKILL.md` into an MVP-specific workflow.
- Do not add a generic "ask exactly three questions" rule that conflicts with `execute_direct`, `plan_first`, and `clarify_first` routing.
- Do not add external service calls, telemetry, auth, or remote installs.
- Do not hand-edit generated catalog files.
- Do not publish to npm as part of the first implementation PR unless explicitly requested after review.

## Proposed Package Shape

Add a small npm package at the repository root:

- `package.json`
- `bin/codex-make-goal-skill.js`
- package files: `bin`, `skills/make-goal`, `README.md`, `LICENSE`

Recommended npm package name:

- `codex-make-goal-skill`

Recommended CLI aliases:

- `codex-make-goal-skill`
- `make-goal-skill`

Default install target:

```text
~/.codex/skills/make-goal
```

CLI options:

- `--target <dir>`: install into a custom skill directory.
- `--force`: overwrite an existing target directory.
- `--dry-run`: print the source and target paths without writing.
- `--help`: print usage.

Installer behavior:

- Resolve the bundled skill source from the package directory.
- Verify `skills/make-goal/SKILL.md` exists before writing.
- Refuse to overwrite an existing target unless `--force` is passed.
- Copy files recursively with Node filesystem APIs.
- Print the installed path and a short restart note.
- Exit non-zero on missing source, existing target without `--force`, or copy failure.

## Documentation Changes

Add a short install section to the hand-maintained README introduction:

```sh
npx codex-make-goal-skill
```

The copy should say:

- the site remains the searchable catalog;
- the skill is for generating, tightening, or reviewing a local `/goal`;
- source-backed and seed boundaries still apply;
- validation remains `python3 scripts/validate_data.py`, `python3 scripts/evaluate_search.py`, and `python3 skills/make-goal/scripts/run_evals.py`.

Add a launch kit:

- `skills/make-goal/references/test-and-launch.md`
- include 2 or 3 demo prompts;
- include a short recording flow;
- include the exact local eval command;
- keep social copy optional and factual.

## Acceptance Criteria

Implementation is complete when:

- `npx codex-make-goal-skill --dry-run` prints the intended target without writing files.
- A local package command installs `skills/make-goal` into a disposable target directory.
- Re-running without `--force` fails if the target exists.
- Re-running with `--force` replaces the disposable target.
- The installed directory contains `SKILL.md`, `references/`, `scripts/`, and `evals/`.
- README explains the install path without changing generated catalog sections.
- The launch kit exists and points to current verification commands.
- `python3 scripts/validate_data.py` passes.
- `python3 scripts/evaluate_search.py` passes.
- `python3 skills/make-goal/scripts/run_evals.py` passes.
- `node --check bin/codex-make-goal-skill.js` passes.
- `npm pack --dry-run` or equivalent package inspection shows only intended files.

## Risks And Controls

- Package drift: include `skills/make-goal` directly from the repo package files instead of duplicating the skill under a second directory.
- Accidental generated-file edits: keep implementation changes outside generated catalog outputs unless generators are run intentionally.
- Unsafe overwrite: default to refusing existing targets and require `--force`.
- Mispositioning: README should present the package as an installable companion workflow, not as a smaller replacement for the catalog.
- Premature publish: first PR should prove package shape locally; npm publishing remains a separate manual step.

## Suggested Issue Checklist

- [ ] Add root package metadata and CLI installer.
- [ ] Add installer tests or shell smoke commands using a disposable target.
- [ ] Add README install section outside generated regions.
- [ ] Add `skills/make-goal/references/test-and-launch.md`.
- [ ] Run catalog validators, search evals, skill evals, Node syntax check, and npm pack dry-run.
- [ ] Decide separately whether to publish `codex-make-goal-skill` to npm.
