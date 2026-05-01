# Barba-CV Roadmap (Public Spec Repository)

This repository focuses on the **open Barba-CV specification**: schema, principles, and examples.

## Target line: v1.3

The v1.3 line is focused on implementation clarity and compatibility discipline (not service-layer features).

### v1.3 goals

1. Clarify schema semantics and field-level guidance.
2. Expand representative example payloads (including senior technical and non-linear career paths).
3. Improve versioning/changelog visibility for implementers.
4. Publish a compliance validator specification (contract + certification workflow draft).

## v1.3 implementation phases

### Phase 1 — Versioning transparency (in progress)
- Add machine-readable and human-readable release notes/changelog.
- Add explicit compatibility policy for `barba_cv_version`.
- Document migration expectations from legacy v1-style payloads.

### Phase 2 — Schema semantics hardening
- Document field intent, nullability, and optionality rules.
- Add field-level examples for ambiguous sections (`meta`, project achievements, skills buckets).
- Align naming/compatibility notes for legacy keys (e.g. `projects_achievements_extracts`).

### Phase 3 — Representative examples
- Add at least:
  - senior technical profile,
  - career-switch profile,
  - minimal valid payload,
  - validator edge-case payloads.
- Ensure all examples validate against current schema.

### Phase 4 — Validator specification
- Define public validator contract (inputs/outputs, error structure).
- Define compliance levels (schema-valid, compatibility-valid, recommended-quality).
- Draft certification process for ecosystem implementers.

## Validator status

A public **compliance validator** is planned to help implementers verify whether payloads are Barba-CV compatible.

Current status:
- JSON Schema validation is available via `schema/barba-cv.schema.json`.
- Certification workflow and official validator process are not yet finalized in this repository.

## Scope boundary

Barba-CV remains a **vendor-neutral standard**.

Parsing engines, normalization pipelines, and commercial processing services may use Barba-CV, but are intentionally out of scope for this repository.

A separate public service-layer repository exists at:
- https://github.com/lgb-sas/mcp-nantua
