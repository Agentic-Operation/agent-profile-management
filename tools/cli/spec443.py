#!/usr/bin/env python3
"""spec443 CLI — lint / publish / status for Spec-443 agent profiles.

Subcommands:
  lint    <profile.json>              schema + structural rules (profile_lint)
  publish <profile.json> [--api URL] lint + POST to the profile API (api/openapi/profile-api.yaml)
  status  <id> <Draft|In Review|Approved|Deprecated> [--api URL]   PATCH /profiles/{id}/status
  report  <id> [--api URL]            GET conformance report (incl. triad cross-check status)
"""
import argparse
import json
import subprocess
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "conformance-kit" / "validators" / "profile_lint.py"


def api(method, url, obj=None):
    data = json.dumps(obj).encode() if obj is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req) as r:
            return r.status, json.loads(r.read())
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read())


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("lint"); p.add_argument("profile")
    p = sub.add_parser("publish"); p.add_argument("profile"); p.add_argument("--api", default="http://localhost:8080/v1")
    p = sub.add_parser("status"); p.add_argument("id"); p.add_argument("status"); p.add_argument("--api", default="http://localhost:8080/v1")
    p = sub.add_parser("report"); p.add_argument("id"); p.add_argument("--api", default="http://localhost:8080/v1")
    a = ap.parse_args()

    if a.cmd == "lint":
        return subprocess.run([sys.executable, str(VALIDATOR), a.profile]).returncode
    if a.cmd == "publish":
        r = subprocess.run([sys.executable, str(VALIDATOR), a.profile])
        if r.returncode != 0:
            return r.returncode
        code, resp = api("POST", f"{a.api}/profiles", json.load(open(a.profile)))
        print(json.dumps(resp))
        return 0 if code == 201 else 1
    if a.cmd == "status":
        code, resp = api("PATCH", f"{a.api}/profiles/{a.id}/status", {"status": a.status})
        print(json.dumps(resp))
        return 0 if code == 200 else 1
    if a.cmd == "report":
        code, resp = api("GET", f"{a.api}/profiles/{a.id}/conformance-report")
        print(json.dumps(resp, indent=2))
        return 0 if code == 200 else 1


if __name__ == "__main__":
    sys.exit(main() or 0)
