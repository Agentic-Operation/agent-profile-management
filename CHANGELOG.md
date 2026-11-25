# Changelog

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions follow SemVer.

## [Unreleased]

### Added

- Phase 0 communication package: triad overview, audience one-pagers, model management authority
  overview, glossary, FAQ, conformance cheat sheet, worked-example walkthrough, references index,
  architecture diagrams (mermaid).
- Repo scaffolding: `docs/`, `spec/`, `schemas/`, `examples/`, `conformance-kit/`, `api/`, `tools/`,
  `integrations/`, `user-tools/`, `tests/`, GitHub templates and docs-lint workflow, pre-commit config.

### Added (Phase 1)

- `spec/SPEC-443.md` normative draft v1.0.0-alpha with extensions (§6.4 topology, §3.1/§9.2 model refs,
  §10.1a per-environment prerequisites, §10.4 per-env autonomy scope) + annexes
  (delta-vs-TMF443, cross-check-manifest C1–C20, self-check).
- `schemas/profile.schema.json`; worked example `examples/loyalty-agent/profile.{md,json}`.
- `conformance-kit/`: `profile_lint.py`, `crosscheck.py`, pytest suite, CI gate template; active
  `.github/workflows/ci-gate.yml`.
- `api/openapi/profile-api.yaml` (publication & validation API).

### Added (Phase 2)

- `tools/cli/spec443.py`: lint / publish / status / report CLI against the profile API
  (`api/openapi/profile-api.yaml`); lint always runs locally via `profile_lint.py` first.
- CI: ci-gate runs profile_lint + CLI lint; new `cross-triad` job runs crosscheck.py across sibling repos.
