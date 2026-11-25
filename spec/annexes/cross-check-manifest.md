# Cross-check manifest — Spec-443 ↔ Spec-444 ↔ Spec-445

Mechanical joins enforced by `conformance-kit/validators/crosscheck.py` (CI stage 2). Failure =
non-conformant. All joins are string-equality unless noted.

| # | Spec-443 field | Spec-444 field | Spec-445 field | Rule |
|---|---|---|---|---|
| C1 | `id` | `id` | `id` (suffix `-bootstrap`/`-card` allowed on artifact ids; base id must match) | equal |
| C2 | `uuid` | `uuid` | `uuid` | equal, UUID v4 |
| C3 | `version` | `version` | `version` | equal |
| C4 | `provider` | `provider` | `provider.organization` | equal |
| C5 | `content_identifier_cid` | `content_identifier_cid` | `content_identifier_cid` | equal when production-bound |
| C6 | `integrity_wrapper` | `security_config.sigstore_integration` | `integrity_wrapper` | consistent issuer/transparency_log |
| C7 | §4.2 skill IDs | `skill_bindings[*].skill_id` | `skills[*].id` | set equality; TMF prefix mandatory, no normalization |
| C8 | §4.1 core tasks | `skill_bindings[*].bound_core_task` | `skills[*].bound_core_task` | equal per skill_id |
| C9 | §5.2 systems | `tool_bindings` keys | `defaultDataContracts[*].tmForumApiRef` | join on system/API ref |
| C10 | §6.1 posture + protocol | `protocol_handlers` keys | `coordination.coordinationProtocol` | consistent |
| C11 | §6.2 variables | — | `coordination.coordinationVariables` | subset match |
| C12 | §6.4 topology | §4 protocol handlers | `coordination.topology_ref` | topology_ref points at this profile's §6.4 |
| C13 | §8.3 `auth_scheme` | `security_config.auth.provider` | `authentication.schemes` | OAuth2/OIDC maps to oauth2_oidc or keycloak |
| C14 | §8.1 deontic tokens | — | `deonticConstraints.embargoes/burdens` | subset match |
| C15 | §8.4 impact radius | — | `impactRadius` | equal (low/medium/high) |
| C16 | §9 metrics | `testing.acceptance_criteria` | — | metric names + thresholds match |
| C17 | §10.4 `autonomy_case_ref` | `lifecycle_hooks.post_bootstrap` autonomy artifact | `autonomyCaseRef` | same URL; required at L3+ |
| C18 | companion refs | companion refs | `spec443_profile_ref` / `spec444_bootstrap_ref` | **bidirectional** |
| C19 | §3.1/§9.2 model refs | `model_bindings` | `modelGovernance` extension | model id + version + CID equal |
| C20 | §10.1a environments | `environments[*].name` | `environment-instances` extension environments | environment names match |
