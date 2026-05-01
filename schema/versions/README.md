# Barba-CV schema version archive

This directory stores historical schema/version artifacts for compatibility and migration work.

## Layout

- `v1.2/`
  - `barba-cv.schema.json` — archived snapshot of current 1.2 schema line.
- `v1.0/`
  - legacy baseline artifacts used before formal 1.2 schema hardening.

## Notes

- v1.2 is the current formalized schema line.
- v1.0 is preserved for migration tooling and backward-compatibility analysis.
- Future lines should add a new subdirectory per version and include either:
  - a formal schema file, or
  - explicit archival notes when only raw templates/examples are available.
