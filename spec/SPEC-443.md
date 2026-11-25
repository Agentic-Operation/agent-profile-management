# Spec-443 — AI Agent Profile (normative draft v1.0.0-alpha)

**Status:** Draft. **Base:** TM Forum TMF443 AI Agent Profile Template v1.0.0 (alpha) — this document
is TMF443 plus the extensions listed in `annexes/delta-vs-TMF443.md` (marked **[EXT]** below).
**Authority precedence:** IG1412 prevails for the L1–L5 autonomy framework and the 8-component agent
model; Spec-443 prevails for its own extensions.

A Spec-443 **profile** is the human-readable contract of one AI agent: what it is, what it may do,
under what constraints. Machine companions: Spec-444 bootstrap (onboard) and Spec-445 card (source).

## Front Matter

### Document Identification [M]

- **Cover block [M]:** title `"{Agent Profile Name}: AI Agent Profile"`, document identifier, version +
  effective date, owner/authoring team + contact, status (`Draft / In Review / Approved / Deprecated`),
  self-declared conformance class.
- **Identity & Integrity [M]:** `id` (slug, registry key), `name`, `uuid` (UUID v4),
  `content_identifier_cid` (`sha256:...`, required for production-bound),
  `version` (semver + stability tag), `provider`,
  `integrity_wrapper{signature_type, issuer, transparency_log}` (mandatory in regulated environments).
  These MUST match the corresponding fields in the Spec-444 bootstrap and Spec-445 card byte-for-byte.
- **Classification [M]** — six orthogonal axes:
  - `autonomy_level`: L1–L5 (IG1412; L1 Operator … L5 Observer). Non-Agentic AI cannot exceed L2.
  - `agency_class`: `Agentic AI` | `Non-Agentic AI`. Agentic AI requires active (non-stub) Learning,
    Reasoning & Decision-Making, and Planning modules in §3.1.
  - `intelligence_class`: `Simple Reflex | Model-Based Reflex | Goal-Based | Utility-Based | Learning | Utility-Based Learning`.
  - `automation_role`: `Worker Agent | Planner Agent | Orchestrator Agent` (Orchestrator requires §6.1 posture "Orchestrates").
  - `mobility`: `Static | Single-Environment | Cross-Environment`.
  - `oda_relationship`: `Standalone | Agentified ODA Component | ODA-Adjacent`.
- **Companion artifacts [M]:** `spec444_bootstrap_ref`, `spec445_agent_card_ref` (URL or CID; TBD+date
  allowed at draft, required for GA). Pointers are bidirectional — a one-way pointer is non-conformant.

### Conformance Clause [M]

Classes: **[M]** mandatory (absent/placeholder ⇒ non-conformant), **[R]** recommended (absent without
justification in §10.3 ⇒ flagged), **[O]** optional, **[M-cond]** mandatory when the named condition
holds. Section-header class = section presence; per-field classes in each section's Field Conformance
table. Conformance = all [M] sections present + all [M] fields populated + [M-cond] populated when its
condition holds + all cross-check joins pass (`annexes/cross-check-manifest.md`).

Per-section mapping: Front Matter [M]; §1–§8 [M]; §9 [R]; §10 [R] (with §10.4 maintenance mandatory).

### Executive Summary [M]

One narrative paragraph (150–250 words) naming the agent, its `autonomy_level` with user role, the
"shift" vs the prior approach — plus **exactly three** measurable outcomes (baseline → target), each
mapping 1:1 to a §9.3 row.

## §1 Business Context & Applications [M]

1.1 Impact areas (2–5; ≥1 lifecycle-stage, ≥1 operational-excellence, each a business-process effect);
1.2 Stakeholders table (3–6 rows; Role | Relationship ∈ Owner/Operator/Consumer/Auditor/Integrator |
Primary Concern); 1.3 Business drivers (3–5 sentences, ≥1 external pressure).

## §2 Scope & Assumptions [M]

2.1 In scope (4–10 responsibilities, each a specific action/state with eTOM L2/L3 mapping; cross-map to
ODA Components if `oda_relationship = Agentified ODA Component`); 2.2 Out of scope (4–10 exclusions,
each naming the alternative owner); 2.3 Assumptions (3–8, each testable: "Assumed: X. If violated: Y").

## §3 Operational Architecture [M]

3.1 Component decomposition — all 8 IG1412 §5.5 components addressed (Persona/Role mandatory; every
"No" justified); **[EXT]** each Learning Module entry MUST reference the bound model in the Model
Management Authority by `model_id` + `version` (see Spec-444 `model_bindings`); 3.2 sub-function
coverage (IG1412 vocabulary; non-IG1412 sub-functions marked `EXTENSION` + one-sentence description);
3.3 memory hierarchy (working / short-term / long-term / archival — technology, retention, latency per
layer); 3.4 control flow & runtime (`execution_engine` named from open-agent-spec/wayflow/langgraph/
crewai/autogen/custom; `logic_structure` ∈ DAG | State Machine | HTN | Other; trigger model; learning
agents need feedback edges); 3.5 interface table (Interface | Dir | Counterparty | Protocol | Data
contract; agent counterparties name the agent or its Spec-443 ref; TM Forum Open APIs cited with version).

## §4 Core Business Capabilities [M]

4.1 Core tasks (3–10, single-sentence business outcomes, consistent with §2.1); 4.2 Skills bindings
(table: Bound Core Task | Skill Name | Skill ID | Description | Source Taxonomy). Skill ID =
`TMF-OASF <number>` | `TMF-GB1033 <id>` | `EXTENSION-<proposed-id>` — the TMF prefix is part of the ID
(string-equality join with Spec-444 §2 and Spec-445 §5). Every core task has ≥1 skill; every skill is
bound to exactly one core task; `source_taxonomy` ∈ OASF Skill Taxonomy | GB1033 Functional Framework |
eTOM | TM Forum Custom | EXTENSION.

## §5 Data Ecosystem & Integration [M]

5.1 Critical data inputs (Data Entity | Source system of record | Refresh cadence quantified | Quality
SLA | SID ref); 5.2 Integration touchpoints (System | Interaction type ∈ Synchronous Request /
Asynchronous Event / Batch / File Drop | Protocol | Open API ref | Failure mode); 5.3 Infrastructure
(scale QPS, latency P50/P95/P99, RTO/RPO with graceful-degradation vs hard-failure distinction,
transport/storage security).

## §6 Coordination & Multi-Agent Behavior [M]

6.1 Coordination posture ∈ `Solo | Participates as a member of a multi-agent system | Orchestrates other
agents`, with the coordination protocol named (A2A JSON-RPC 2.0 / REP / WoA / MCP / custom);
6.2 Coordination variables (name, type, scope, publisher, consumer, update frequency — publisher and
consumer explicit); 6.3 Sensitivity signals — conditional "If [condition], I will [action]" rules,
aligned with `autonomy_level` (L5 looser than L2).

### 6.4 Topology (machine-readable) [EXT] [M-cond: posture ≠ Solo]

```yaml
topology:
  pattern: swarm | hierarchy | pipeline
  orchestrator: "<agent id or uuid>"        # required when pattern = hierarchy
  members:
    - agent_id: "..."                        # Spec-443 id or uuid of a peer
      role: worker | planner | orchestrator
      protocol: a2a_jsonrpc | rep | wo_a | mcp
      autonomy_level: L1..L5                 # per-agent; a mesh has no single level
  coordination_variables: [names from 6.2]
  sensitivity_signals_ref: "section 6.3"
```

Cross-checks: `orchestrator` requires `automation_role: Orchestrator Agent`; every `members[].agent_id`
SHOULD resolve to a published Spec-445 card; Spec-445 carries the same topology in `coordination.topology_ref`.

## §7 User Experience & Interaction Model [M]

7.1 Interaction surfaces (actor, surface type, purpose, affordances; operator surfaces reflect the
autonomy level — L3 consultation hooks, L4 approval flows, L5 observation; no advertised-but-unbuilt
surfaces); 7.2 Discovery & invocation (`discovery_primitive{well_known_path, media_type}`,
`invocation_interface{method, base_url, invoke_path}`, `handshake_protocol` ∈ A2A JSON-RPC 2.0 / MCP /
custom, `protocol_envelope`, `ontology_alignment`) — must be consistent with the Spec-445 card fields.

## §8 Security, Trust & Governance [M]

8.1 Deontic constraints — ODP-EL tokens: embargoes (prohibited) + burdens (obligations); ≥1 of each at
L3+; 8.2 Risk mapping (NIST AI RMF adversarial categories AI 100-1 / AI 100-3 / AAI00x or declared
extension; Risk ID | Description | Mitigation | Status); 8.3 Authentication (`auth_scheme` ∈ OAuth 2.0 /
OIDC | mTLS | API Key | Custom); 8.4 Impact radius ∈ Low | Medium | High — High constrains autonomy
(High at L1 is a structural inconsistency); justification names the specific irreversible effects.

## §9 Performance Metrics & Business Outcomes Baseline [R]

9.1 Operational (Metric | Baseline | Target | Method | Cadence); 9.2 Learning — **[EXT]** each row
references the evaluated model via `model_id` + `version` from the Model Management Authority (drift
cadence feeds §10.4); named benchmarks cite version; MUI target named. A declared Learning Module
without 9.2 rows is a structural inconsistency; 9.3 Business impact — each of the three executive
summary outcomes appears exactly once, explicit cross-reference.

## §10 Deployment Considerations & Known Limitations [R] (§10.4 [M])

10.1 Deployment prerequisites (each testable pre-deploy); **[EXT]** 10.1a Per-environment prerequisites —
a table (Environment | Prerequisite | Verification) since `mobility: Cross-Environment` agents must state
what differs per environment; 10.2 Known limitations ("Limitation: X. Workaround: Y/N"); 10.3 Deviation
register (Section | Deviation | Justification | Approval | Date); 10.4 Maintenance & documentation —
`maintenance_plan` (incl. drift-assessment cadence if Learning Module; **[EXT]** per-environment
autonomy-certificate scope — `autonomyCaseRef` may differ per environment), `technical_manual`,
`api_spec`, `autonomy_case_ref` (required at L3+), `last_updated` ISO 8601.

## Annexes

- `annexes/delta-vs-TMF443.md` — every [EXT] mapped to its TMF443 origin section.
- `annexes/cross-check-manifest.md` — mechanical joins to Spec-444 / Spec-445.
- `annexes/self-check.md` — pre-submission checklist.
- Worked example: `../examples/loyalty-agent/profile.md` (+ machine-readable `profile.json`).
