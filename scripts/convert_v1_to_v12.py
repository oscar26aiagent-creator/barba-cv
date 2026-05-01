#!/usr/bin/env python3
"""Convert legacy Barba-CV v1-style payloads to v1.2-compatible shape.

Usage:
  python scripts/convert_v1_to_v12.py input.json output.json

Notes:
- Non-destructive: unknown fields are preserved under `extensions.legacy_fields`.
- Best-effort migration: keeps flexibility for real-world payload variance.
"""
from __future__ import annotations

import json
import sys
from copy import deepcopy
from pathlib import Path


def as_obj(v):
    return v if isinstance(v, dict) else {}


def ensure_list(v):
    if v is None:
        return []
    return v if isinstance(v, list) else [v]


def normalize_links(links: dict) -> dict:
    out = deepcopy(links)
    if "X/twitter" in out and "twitter" not in out:
        out["twitter"] = out.pop("X/twitter")
    if "other_socials" not in out:
        out["other_socials"] = []
    return out


def normalize_skills(skills: dict) -> dict:
    out = {}
    for bucket in ("it_skills", "hard_skills", "soft_skills"):
        vals = ensure_list(skills.get(bucket, []))
        normalized = []
        for item in vals:
            if isinstance(item, str):
                normalized.append({"name": item, "level": "", "category": "", "keywords": []})
            elif isinstance(item, dict):
                obj = deepcopy(item)
                obj.setdefault("name", "")
                obj.setdefault("level", "")
                obj.setdefault("category", "")
                obj.setdefault("keywords", [])
                normalized.append(obj)
        out[bucket] = normalized
    return out


def normalize_project_achievements(payload: dict) -> list:
    if "project_achievements" in payload:
        return ensure_list(payload.get("project_achievements"))
    if "projects_achievements_extracts" in payload:
        return ensure_list(payload.get("projects_achievements_extracts"))
    return []


def move_root_parsing_errors_to_meta(payload: dict, meta: dict) -> None:
    if "parsing_errors" in payload and "parsing_errors" not in meta:
        meta["parsing_errors"] = ensure_list(payload.get("parsing_errors"))


def convert(v1_payload: dict) -> dict:
    src = deepcopy(v1_payload)
    out = {}

    # Core version marker
    out["barba_cv_version"] = "1.2"

    # Root sections kept compatible
    for key in [
        "personal_info",
        "profile_summary",
        "position_sought",
        "experiences",
        "education",
        "certifications",
        "languages",
        "interests",
    ]:
        if key in src:
            out[key] = deepcopy(src[key])

    # personal_info normalization
    pi = as_obj(out.get("personal_info", {}))
    if "Middle_name" in pi and "middle_name" not in pi:
        pi["middle_name"] = pi.pop("Middle_name")
    links = as_obj(pi.get("links", {}))
    if links:
        pi["links"] = normalize_links(links)
    out["personal_info"] = pi

    # skills normalization
    out["skills"] = normalize_skills(as_obj(src.get("skills", {})))

    # project achievements alias mapping
    out["project_achievements"] = normalize_project_achievements(src)

    # meta construction
    meta = as_obj(src.get("meta", {}))
    move_root_parsing_errors_to_meta(src, meta)
    meta.setdefault("parsing_errors", [])
    out["meta"] = meta

    # extensions passthrough
    out["extensions"] = as_obj(src.get("extensions", {}))

    # Preserve unknown legacy root fields for auditability
    known = {
        "barba_cv_version",
        "personal_info",
        "profile_summary",
        "position_sought",
        "experiences",
        "education",
        "skills",
        "certifications",
        "languages",
        "interests",
        "project_achievements",
        "projects_achievements_extracts",
        "meta",
        "extensions",
        "parsing_errors",
    }
    legacy = {k: deepcopy(v) for k, v in src.items() if k not in known}
    if legacy:
        out["extensions"].setdefault("legacy_fields", legacy)

    return out


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python scripts/convert_v1_to_v12.py input.json output.json", file=sys.stderr)
        return 2

    inp = Path(sys.argv[1])
    outp = Path(sys.argv[2])

    data = json.loads(inp.read_text(encoding="utf-8"))
    converted = convert(data)

    outp.parent.mkdir(parents=True, exist_ok=True)
    outp.write_text(json.dumps(converted, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Converted {inp} -> {outp}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
