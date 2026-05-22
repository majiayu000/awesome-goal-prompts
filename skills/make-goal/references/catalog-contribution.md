# Catalog Contribution

Use this only when the user wants to add or update an entry in an awesome-goal-prompts style catalog.

## Source Files

Edit source data, not generated outputs.

- Add or update entries in `data/source/entries.toml`.
- Category metadata lives in `data/source/categories.toml`.
- Start-here recipes live in `data/source/recipes.toml`.
- Generated outputs include `README.md` generated regions, `data/examples.json`, `docs/examples.json`, `prompts/goal-examples.md`, `prompts/source-backed-goals.md`, `prompts/seed-patterns.md`, and catalog health docs.

## Entry Fields

Seed entry:

- `id`
- `category`
- `title`
- `intent`
- `verify`
- `origin = "seed"`

Source-backed entry:

- All seed fields.
- `source_name`
- `source_url`
- `source_type`
- `evidence`
- `origin = "source-backed"`

Generated fields such as `slug`, `difficulty`, `prompt`, and `evidence_summary` should not be hand-written in source TOML. `slug` follows `id`; `difficulty` comes from category metadata.

## Source Rules

`source-backed` means the entry is tied to a public URL and a concrete task, example, or usage rule. It does not mean the prompt text is copied verbatim.

`seed` means the entry is a reusable pattern. Do not present it as collected from X, GitHub, docs, or a named author.

If a seed later gets real public evidence, update the existing entry with source metadata instead of adding a duplicate.

## Quality Checklist

- The task has exactly one primary objective.
- The done condition is mechanically checkable or evidence-based.
- The constraints prevent scope creep.
- The verification does not depend on prior claims or stale logs.
- The stop rules cover missing secrets, missing production access, destructive data operations, and repeated failed fixes.
- Source-backed examples include a public URL, source type, evidence phrase, and generated evidence summary.
- Seed examples are not presented as external citations.

## Validation Commands

Run these from the catalog repository when contributing:

```bash
python3 scripts/validate_data.py
python3 scripts/generate_examples.py
python3 scripts/generate_catalog_health.py
python3 scripts/evaluate_search.py
node --check docs/app.js
git diff --check
```

CI should also check that generated files are committed by running `git diff --exit-code` after regeneration.
