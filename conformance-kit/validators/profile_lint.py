#!/usr/bin/env python3
"""Spec-443 profile linter — CI stage 2 validator (stdlib + jsonschema optional).

Usage: profile_lint.py <profile.json> [more.json ...]
Exit 0 = conformant; exit 1 = violations listed on stderr.
"""
import json
import re
import sys

SKILL_ID = re.compile(r"^(TMF-OASF [0-9]+|TMF-GB1033 F-[0-9]+|EXTENSION-[A-Za-z0-9-]+)$")
UUID_V4 = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$", re.I)
LEVELS = ["L1", "L2", "L3", "L4", "L5"]


def lint(doc, errors):
    ident = ["id", "uuid", "version", "provider"]
    for k in ident:
        if k not in doc:
            errors.append(f"identity: missing {k}")
    if "uuid" in doc and not UUID_V4.match(doc["uuid"]):
        errors.append("identity: uuid is not UUID v4")
    if "content_identifier_cid" in doc and not re.match(r"^sha256:[a-f0-9]{64}$", doc["content_identifier_cid"]):
        errors.append("identity: content_identifier_cid must be sha256:<64 hex>")

    c = doc.get("classification", {})
    lvl = c.get("autonomy_level")
    if lvl not in LEVELS:
        errors.append("classification: autonomy_level must be L1..L5")
    if c.get("agency_class") == "Non-Agentic AI" and lvl in ("L3", "L4", "L5"):
        errors.append("classification: Non-Agentic AI cannot exceed L2")
    if c.get("automation_role") == "Orchestrator Agent":
        if doc.get("coordination", {}).get("posture") != "Orchestrates other agents":
            errors.append("classification: Orchestrator Agent requires coordination posture 'Orchestrates other agents'")
    sec = doc.get("security", {})
    if sec.get("impact_radius") == "High" and lvl == "L1":
        errors.append("security: impact_radius High at L1 is a structural inconsistency")
    if lvl in ("L3", "L4", "L5"):
        if not sec.get("deontic_embargoes") or not sec.get("deontic_burdens"):
            errors.append("security: >=1 embargo and >=1 burden required at L3+ (ODP-EL tokens)")

    tasks = set(doc.get("core_tasks", []))
    skills = doc.get("skills", [])
    bound = set()
    for s in skills:
        if not SKILL_ID.match(s.get("id", "")):
            errors.append(f"skills: bad skill id {s.get('id')!r} (TMF prefix is part of the ID)")
        if s.get("bound_core_task") not in tasks:
            errors.append(f"skills: {s.get('id')} bound to unknown core task {s.get('bound_core_task')!r}")
        bound.add(s.get("bound_core_task"))
    for t in tasks:
        if t not in bound:
            errors.append(f"core_tasks: task {t!r} has no skill bound")

    outs = doc.get("executive_summary_outcomes", [])
    if len(outs) != 3:
        errors.append("executive_summary_outcomes: exactly 3 outcomes required")

    lm = doc.get("components", {}).get("learning_module", {})
    if lm.get("present") and not doc.get("learning_metrics"):
        errors.append("learning: Learning Module present but no learning_metrics")
    for m in doc.get("learning_metrics", []):
        if "model_id" not in m or "model_version" not in m:
            errors.append(f"learning: metric {m.get('metric')!r} missing model_id/model_version [EXT]")

    coord = doc.get("coordination", {})
    if coord.get("posture") not in (None, "Solo") and "topology" not in coord:
        errors.append("coordination: non-Solo posture requires topology block [EXT §6.4]")
    if coord.get("posture") == "Solo":
        pass
    topo = coord.get("topology")
    if topo:
        if topo.get("pattern") == "hierarchy" and not topo.get("orchestrator"):
            errors.append("topology: hierarchy requires orchestrator")
        if c.get("automation_role") == "Orchestrator Agent" and topo.get("pattern") != "hierarchy":
            errors.append("topology: Orchestrator Agent should declare a hierarchy")

    if c.get("mobility") == "Cross-Environment" and not doc.get("environment_prerequisites"):
        errors.append("deployment: Cross-Environment mobility requires environment_prerequisites [EXT §10.1a]")
    if lvl in ("L3", "L4", "L5") and not doc.get("maintenance", {}).get("autonomy_case_ref"):
        errors.append("maintenance: autonomy_case_ref required at L3+")


def validate_schema(doc, path, errors):
    try:
        import jsonschema
        schema = json.load(open(path.rsplit("/", 1)[0] + "/../../schemas/profile.schema.json"))
        jsonschema.validate(doc, schema)
    except ImportError:
        pass
    except Exception as e:  # noqa: BLE001
        errors.append(f"schema: {e}")


def main():
    paths = sys.argv[1:]
    if not paths:
        print(__doc__)
        return 2
    failed = False
    for p in paths:
        errors = []
        doc = json.load(open(p))
        lint(doc, errors)
        validate_schema(doc, p, errors)
        if errors:
            failed = True
            for e in errors:
                print(f"{p}: {e}", file=sys.stderr)
        else:
            print(f"{p}: OK")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
