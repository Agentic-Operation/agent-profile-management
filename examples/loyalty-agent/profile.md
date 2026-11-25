# Worked example — Loyalty Management Agent (Spec-443 profile instance)

Machine-readable instance: [`profile.json`](profile.json) (validated against `schemas/profile.schema.json`).
Companions: Spec-444 bootstrap
([agent-bootstrap-management](https://github.com/Agentic-Operation/agent-bootstrap-management/blob/main/examples/loyalty-agent/bootstrap.yaml)),
Spec-445 card
([agent-discovery-card](https://github.com/Agentic-Operation/agent-discovery-card/blob/main/examples/loyalty-agent/card.json)).

- **Identity:** id `loyalty-management-agent-v1`, uuid `9e3b2f5d-4a8c-4f6e-8b1d-7c9a2e5f3b6d`,
  version `1.0.0-stable`, Sigstore integrity wrapper — identical in all three artifacts (cross-check C1–C6).
- **Classification:** L3 Consultant / Agentic AI / Utility-Based Learning / Worker Agent /
  Cross-Environment / ODA-Adjacent.
- **Executive summary:** shift from transactional point-tracking to predictive relationship
  management; three outcomes: retention +15–25%, revenue/member +8–12%, campaign setup −70% (§9.3 rows).
- **Capabilities:** 4 core tasks, 7 skills (`TMF-OASF 3015/3016/3020/3021/2046/2051`, `TMF-GB1033 F-1842`).
- **Coordination:** participates in a hierarchy under `campaign-orchestrator-agent-v1` via A2A JSON-RPC;
  variables `DAILY_REDEMPTION_BUDGET`, `MEMBER_CONSENT_FLAG`; topology block in §6.4 ([EXT]).
- **Security:** OAuth 2.0/OIDC; impact radius Medium; 3 ODP-EL embargoes + 3 burdens.
- **Learning models ([EXT]):** `churn-scorer@2.3.1`, `ltv-predictor@1.7.0` — resolved via the Model
  Management Authority in the Spec-444 `model_bindings`.
- **Per-environment prerequisites ([EXT] §10.1a):** dev ≥90% identity-graph coverage, stage ≥95%,
  prod ≥95% + clean consent audit.
