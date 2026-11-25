import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LINT = ROOT / "conformance-kit/validators/profile_lint.py"
GOOD = ROOT / "examples/loyalty-agent/profile.json"


def run(doc):
    tmp = Path("/tmp/_profile_case.json")
    tmp.write_text(json.dumps(doc))
    return subprocess.run([sys.executable, str(LINT), str(tmp)], capture_output=True, text=True)


def test_valid_example_passes():
    r = subprocess.run([sys.executable, str(LINT), str(GOOD)], capture_output=True, text=True)
    assert r.returncode == 0, r.stderr


def test_non_agentic_above_l2_fails():
    doc = json.load(open(GOOD))
    doc["classification"]["agency_class"] = "Non-Agentic AI"
    doc["classification"]["autonomy_level"] = "L4"
    r = run(doc)
    assert r.returncode == 1 and "cannot exceed L2" in r.stderr


def test_high_impact_at_l1_fails():
    doc = json.load(open(GOOD))
    doc["security"]["impact_radius"] = "High"
    doc["classification"]["autonomy_level"] = "L1"
    r = run(doc)
    assert r.returncode == 1 and "structural inconsistency" in r.stderr


def test_bad_skill_id_fails():
    doc = json.load(open(GOOD))
    doc["skills"][0]["id"] = "OASF-3015"
    r = run(doc)
    assert r.returncode == 1 and "bad skill id" in r.stderr


def test_unbound_core_task_fails():
    doc = json.load(open(GOOD))
    doc["core_tasks"].append("Orphan task")
    r = run(doc)
    assert r.returncode == 1 and "no skill bound" in r.stderr
