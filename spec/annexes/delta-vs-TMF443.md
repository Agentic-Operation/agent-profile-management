# Delta annex — Spec-443 vs TMF443 v1.0.0

Spec-443 = TMF443 v1.0.0 (alpha) + the extensions below. Everything else is carried over unchanged.

| Spec-443 location | Extension | TMF443 origin | Class | Rationale |
|---|---|---|---|---|
| Front Matter › Identity & Integrity | companion refs renamed `spec444_bootstrap_ref` / `spec445_agent_card_ref` (were `tmf444_bootstrap_ref` / `tmf445_agent_card_ref`) | TMF443 Front Matter › Companion Artifacts | [M] | align pointer names with Spec-44X |
| §3.1 | Learning Module entries reference Model Management Authority `model_id` + `version` | TMF443 §3.1 (no model ref) | [M-cond: Learning Module present] | model lineage for autonomy cases |
| §6.4 | machine-readable `topology` block (swarm/hierarchy/pipeline, members, per-agent autonomy) | TMF443 §6 (narrative only) | [M-cond: posture ≠ Solo] | swarm/hierarchical management needs a declarative topology |
| §9.2 | learning-metric rows reference `model_id` + `version` | TMF443 §9.2 | [R] | drift metrics join to authority records |
| §10.1a | per-environment prerequisites table | TMF443 §10.1 | [M-cond: mobility = Cross-Environment] | multi-environment rollout support |
| §10.4 | per-environment autonomy-certificate scope (`autonomyCaseRef` per environment) | TMF443 §10.4 | [M-cond: autonomy ≥ L3 and Cross-Environment] | impact radius can differ per environment |

Carried-over fixes noted for upstream TM Forum: worked-example version consistency, single canonical
skillDiscovery URI (fixed in Spec-445), and informative-until-GA conformance caveat retained.
