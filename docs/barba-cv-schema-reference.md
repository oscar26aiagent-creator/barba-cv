# Barba-CV Schema Reference (Human-Readable)

This document explains Barba-CV payload fields for implementers and AI systems.

## 1) Version marker

### `barba_cv_version` (required)
- Type: `string`
- Current stable line: `"1.2"`
- Purpose: declares payload compatibility line.

---

## 2) Core profile sections

### `personal_info`
Candidate identity/contact block.

Common fields:
- `first_name`, `middle_name`, `last_name`
- `date_of_birth` (free-form date string for compatibility)
- `driving_licenses` (array)
- `address`, `contact`, `links`

Notes:
- date fields are intentionally flexible text to avoid rejecting operational payloads.
- link aliases from legacy payloads should be normalized where possible (e.g., `X/twitter` -> `twitter`).

### `profile_summary`
Free-text profile paragraph.

### `position_sought`
Array of role/target-position strings.

### `experiences`
Array of employment entries.
Typical fields: `organization`, `role_title`, `location`, `start_date`, `end_date`, `tasks`, `achievements`.

### `education`
Array of education entries.

### `skills`
Grouped buckets:
- `it_skills`
- `hard_skills`
- `soft_skills`

Recommendation:
- Prefer object entries with at least `name`, optional `level`, `category`, `keywords`.

### `certifications`
Array of certification records.

### `languages`
Array of language records (`language`, `level`, optional certificates).

### `interests`
Array of interest strings.

### `project_achievements`
Canonical array for structured project/achievement extracts.

Migration note:
- Legacy key `projects_achievements_extracts` should map to `project_achievements` during migration.

---

## 3) Metadata block

### `meta` (recommended)
Operational and extraction metadata.

Examples:
- `cv_uuid`, `cv_title`
- `parsing_errors`
- `ats_processed`
- `processor_engine`
- provenance timestamps (`parsed_at`, `ingested_at`, `embedded_at`)
- source traces (`source_original_text`, `source_ats_revised_text`, `original_filename`, `source_format`)
- `extraction_confidence_overall`

Optionality notes:
- most fields are optional and may be null/empty depending on source system.

Migration note:
- In legacy v1 payloads, `parsing_errors` may exist at root; in 1.2 it belongs under `meta.parsing_errors`.

---

## 4) Extensions

### `extensions`
Vendor/system-specific fields outside the core spec.

Rules:
- Keep core interoperability fields in canonical keys.
- Use `extensions` for non-standard additions.

---

## 5) Date flexibility policy

Barba-CV intentionally permits flexible date strings (e.g., year-only, month-year, full date).

Reason:
- real CV data is heterogeneous;
- strict date formats can cause avoidable ingestion failures.

Implementers may normalize dates downstream but should preserve original information.

---

## 6) Migration summary (v1 -> v1.2)

Typical migration tasks:
1. Add `barba_cv_version: "1.2"`.
2. Move root-level parser metadata under `meta`.
3. Map `projects_achievements_extracts` -> `project_achievements`.
4. Normalize known legacy aliases (e.g., social links).
5. Preserve unknown legacy fields under `extensions.legacy_fields` if needed.

See converter utility:
- `scripts/convert_v1_to_v12.py`
