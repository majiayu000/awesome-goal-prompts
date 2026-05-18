# Changelog

## v0.1.1 - 2026-05-18

Post-launch catalog polish and maintainer workflow hardening.

- Added localized in-site documentation pages and Chinese catalog health output.
- Added sitemap, robots metadata, structured data, and share-preview assets for the GitHub Pages catalog.
- Improved README search wording for Claude Code, Codex, Cursor, Gemini CLI, and coding-agent discovery.
- Switched the project license to CC0 1.0 Universal.
- Added GitHub issue templates for new contracts and bug reports.
- Externalized catalog source data into `data/source/*.toml` and marked generated README regions.
- Added source-data validation before regeneration, including source type, URL scheme, category, recipe, difficulty, and duplicate-ID checks.
- Kept the catalog at 293 task contracts with 93 source-backed examples and 11/11 search evaluation cases passing.

## v0.1.0 - 2026-05-15

Initial public release.

- Published a searchable GitHub Pages catalog for `/goal` task contracts.
- Curated 293 task contracts across engineering, product, documentation, testing, security, AI ops, and agent workflow categories.
- Added 93 source-backed examples with public URLs, provenance classes, evidence phrases, and generated evidence summaries.
- Added reusable full and compact `/goal` templates.
- Added a writing guide for turning vague requests into verifiable goal contracts.
- Added data-driven start-here recipes for common user entry points.
- Added catalog health reporting for source-backed coverage, source type distribution, and search evaluation.
- Added CI quality gates for catalog generation, search evaluation, JavaScript syntax, generated-file drift, and whitespace checks.

## Earlier Development

- Built the initial awesome-list structure.
- Added provenance fields for source-backed examples.
- Added the GitHub Pages browser UI.
- Refined search ranking, source badges, verification display, and prompt adaptation controls.
