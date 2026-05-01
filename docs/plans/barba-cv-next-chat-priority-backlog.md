# Barba-CV — Priority Backlog for Next Chat

Canonical source: this file captures the user-approved backlog for immediate execution planning.

## A) Versioning and previous schema versions

Implement explicit previous-version archive structure:

```text
schema/
  barba-cv.schema.json
  versions/
    v1.0/
      barba-cv.schema.json
    v1.2/
      barba-cv.schema.json
```

Decisions to finalize:
- Whether v1.0 is formalized retroactively as schema, or archived as raw example/template only.
- README must state latest stable + previous versions.

Status: **Not implemented yet**.

---

## B) Feedback and contribution workflow

Define explicit contribution/feedback paths:
- Report issues
- Suggest fields
- Request new sections
- Report edge cases

Likely implementation:
- GitHub Issues
- Issue templates:
  - feature request
  - schema change
  - bug report

Status: **Needs structuring**.

---

## C) Roadmap v1.3 updates (roadmap only, not schema yet)

Add planned sections to roadmap:
1. `events`
   - exhibitions, conferences, panels, TV, podcasts, concerts, public/professional appearances
2. `publications`
   - books, articles, scientific papers, reports, white papers, studies

Target file: `docs/roadmap.md` (canonical roadmap location to be unified).

Status: **Not done**.

---

## D) Barba-CV 1.0 -> 1.2 conversion utility (priority)

Need a migration utility (Python) for old payloads to 1.2:
- Field renaming
- Move metadata into `meta`
- Add `barba_cv_version`
- Normalize keys
- Preserve backward compatibility

Reason:
- 1.2 formalized, legacy v1 payloads still exist.
- Migration path required for practical adoption.

Status: **Priority technical step, not started**.

---

## E) `docs/barba-cv-schema-reference.md`

Create full human-readable schema reference:
- Field-by-field explanation
- Examples
- Optionality notes
- Date flexibility notes
- Migration notes from v1

Audience:
- Developers
- AI systems
- Standards credibility

Status: **Still needed**.

---

## F) README / docs polishing

Cleanup checklist:
- Verify cross-links
- Verify consistency with latest schema
- Verify docs mention SchemaStore availability
- Add usage example with `$schema` reference
- Consider README section: “Available in SchemaStore”

Status: **Partially done, needs pass**.

---

## G) Developer adoption phase (next major phase)

Current state (mostly done):
- Specification visibility
- Documentation baseline
- Release baseline
- Schema registration baseline

Immediate adoption tasks:
- Practical tooling
- Converter
- Copy-paste examples
- Reference implementations

Later (not immediate):
- dev.to / HN / Reddit outreach

Guiding principle:
- Don’t oversell, don’t push too early.
- Make spec truly usable first.
