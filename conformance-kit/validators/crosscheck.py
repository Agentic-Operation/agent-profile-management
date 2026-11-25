#!/usr/bin/env python3
"""Triad cross-check validator (Spec-443/444/445 join keys; manifest: spec/annexes/cross-check-manifest.md).

Usage: crosscheck.py --profile profile.json --bootstrap bootstrap.yaml --card card.json
Exit 0 = all joins pass.
"""
import argparse
import json
import sys


def load(path):
    if path.endswith((".yaml", ".yml")):
        import yaml
        return yaml.safe_load(open(path))
    return json.load(open(path))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--profile", required=True)
    ap.add_argument("--bootstrap", required=True)
    ap.add_argument("--card", required=True)
    a = ap.parse_args()
    p, b, c = load(a.profile), load(a.bootstrap), load(a.card)
    bp = (b.get("bootstrap_profile") or b)
    errors = []

    def eq(name, x, y):
        if x != y:
            errors.append(f"{name}: {x!r} != {y!r}")

    eq("C1 id", p.get("id"), bp.get("id", "").replace("-bootstrap", "") if bp.get("id") else p.get("id"))
    eq("C2 uuid", p.get("uuid"), bp.get("uuid"))
    eq("C2 card uuid", p.get("uuid"), c.get("uuid"))
    eq("C3 version", p.get("version"), c.get("version"))
    eq("C4 provider", p.get("provider"), (c.get("provider") or {}).get("organization"))

    p_skills = {s["id"] for s in p.get("skills", [])}
    b_skills = {s["skill_id"] for s in bp.get("skill_bindings", [])}
    c_skills = {s["id"] for s in c.get("skills", [])}
    if not p_skills <= b_skills:
        errors.append(f"C7 skills in profile missing from bootstrap: {p_skills - b_skills}")
    if not p_skills <= c_skills:
        errors.append(f"C7 skills in profile missing from card: {p_skills - c_skills}")

    proto = p.get("coordination", {}).get("protocol")
    if proto and proto not in bp.get("protocol_handlers", {}):
        errors.append(f"C10 protocol {proto} not in bootstrap protocol_handlers")
    cc = c.get("coordination", {})
    if proto and cc.get("coordinationProtocol") != proto:
        errors.append(f"C10 card coordinationProtocol {cc.get('coordinationProtocol')} != profile {proto}")

    sec = p.get("security", {})
    if sec.get("impact_radius", "").lower() != c.get("impactRadius"):
        errors.append("C15 impactRadius mismatch")
    auth = sec.get("auth_scheme", "")
    schemes = c.get("authentication", {}).get("schemes", [])
    if "OAuth" in auth and not set(schemes) & {"oauth2_oidc", "keycloak"}:
        errors.append("C13 auth mismatch: profile OAuth2/OIDC but card schemes " + str(schemes))

    lvl = p.get("classification", {}).get("autonomy_level")
    if lvl in ("L3", "L4", "L5") and not c.get("autonomyCaseRef"):
        errors.append("C17 autonomyCaseRef required at L3+")

    envs = {e["environment"] for e in p.get("environment_prerequisites", [])}
    card_envs = set()
    for ext in c.get("extensions", []):
        if "environment-instances" in (ext.get("uri") or ""):
            card_envs = {e.get("environment") for e in ext.get("params", {}).get("environments", [])}
    if envs and card_envs and not envs <= card_envs:
        errors.append(f"C20 environment names mismatch: profile {envs} vs card {card_envs}")

    if errors:
        for e in errors:
            print("FAIL " + e, file=sys.stderr)
        return 1
    print("crosscheck: all joins pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
