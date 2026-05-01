# Barba-CV Versioning and Compatibility Policy

## Scope
This policy applies to the Barba-CV **data specification** (schema + docs + examples) in this repository.

## Version field
- Payload version is carried by: `barba_cv_version`.
- Current stable line: `1.2`.
- Next target line: `1.3` (unreleased).

## Compatibility intent
Barba-CV prioritizes implementer stability:

1. **No silent breaking changes** within a published minor line.
2. New guidance fields should be introduced as optional first whenever possible.
3. Legacy key behavior must be documented before deprecation/removal.

## Change categories

### Patch-level documentation updates
- Clarifications, wording improvements, examples.
- No schema-compatibility impact expected.

### Minor-line evolution (e.g., 1.2 → 1.3)
- May introduce new optional structures or clearer normative guidance.
- Any compatibility-sensitive changes must include migration notes.

### Breaking changes
- Must be explicitly announced.
- Must include migration guide and deprecation window guidance.

## Migration expectations for 1.3
Planned expectations (subject to final acceptance):

- Keep v1.2 payloads valid for baseline schema checks.
- Provide mapping guidance for legacy names (e.g., `projects_achievements_extracts` to canonical forms).
- Add validator compliance levels so implementers can separate strict schema validity from recommended quality.

## Release-note contract
Each release line should provide:
- what changed,
- compatibility impact,
- migration steps (if any),
- validator implications.

See `docs/changelog.md` and `docs/roadmap.md`.
