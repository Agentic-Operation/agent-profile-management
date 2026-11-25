# agent-profile-management — Spec-443: AI Agent Profile

**Spec-443** is the *define* contract of the agent triad: the human-readable profile that states what
an AI agent is, what it may do, and under which constraints — classification (autonomy L1–L5, agency,
role, mobility, ODA relationship), scope, architecture, capabilities (core tasks ↔ skills), data
ecosystem, coordination/multi-agent behavior, UX, security & governance (ODP-EL deontic constraints,
impact radius), metrics, and deployment considerations.

- **Status:** Draft — Phase 0 comms pack merged-pending; **Phase 1**: normative `spec/SPEC-443.md` v1.0.0-alpha on `vibe/spec-draft-5a1ad6`. Successor of TM Forum **TMF443 v1.0.0** (alpha);
  extensions are tracked in `spec/annexes/delta-vs-TMF44X.md`.
- **License:** Apache-2.0

## The triad (sibling repos)

| Verb | Spec | Repo |
|---|---|---|
| **Define** (this repo) | Spec-443 | `Agentic-Operation/agent-profile-management` |
| Onboard | Spec-444 | [`agent-bootstrap-management`](https://github.com/Agentic-Operation/agent-bootstrap-management) |
| Source | Spec-445 | [`agent-discovery-card`](https://github.com/Agentic-Operation/agent-discovery-card) |

Join keys across the triad: identity fields (`id`, `uuid`, `version`, `provider`, CID, `integrity_wrapper`),
skill IDs (`TMF-OASF <n>` / `TMF-GB1033 F-xxxx`), bidirectional companion pointers — see
[docs/communication/00-triad-overview.md](docs/communication/00-triad-overview.md).

## Repository map

| Directory | Purpose |
|---|---|
| `spec/SPEC-443.md` | Normative Spec-443 v1.0.0-alpha + annexes (delta vs TMF443, cross-check manifest C1–C20, self-check) — **populated in Phase 1** |
| `schemas/` | Machine-readable profile schema + valid/invalid test vectors |
| `examples/loyalty-agent/` | Worked example instance of this artifact |
| `conformance-kit/` | Validators, test suites, CI templates, runtime integrity check |
| `api/openapi/` | Profile publication & validation API |
| `tools/cli/` | `spec443 lint/publish` CLI |
| `integrations/` | Model authority refs, ODA/eTOM/SID mappings |
| `user-tools/` | Authoring templates, SDK snippets |
| `docs/communication/` | Audience one-pagers (canonical triad pack lives here) |
| `docs/guides/` | Task guides and quickstarts |
| `docs/architecture/` | Mermaid diagrams (triad, lifecycle) |
| `docs/references/` | Related sources + authority precedence (canonical) |

## Quickstart

See [docs/guides/quickstart-author-a-profile.md](docs/guides/quickstart-author-a-profile.md) and the
audience one-pager [docs/communication/01-define-your-agent.md](docs/communication/01-define-your-agent.md).

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Branch convention `vibe/<slug>-5a1ad6`, draft PRs.

## Runtime services (this org)

| Service | Repo |
|---|---|
| Agent Card Registry | [Agent-Registry](https://github.com/Agentic-Operation/Agent-Registry) |
| Model Management Authority | [model-authority](https://github.com/Agentic-Operation/model-authority) |
| Rollout controller | [agent-rollout-controller](https://github.com/Agentic-Operation/agent-rollout-controller) |
| Orchestrator (swarm/hierarchy; consumes this repo's §6.4 topology) | [agent-orchestrator](https://github.com/Agentic-Operation/agent-orchestrator) |
| Tool & MCP manager | [tool-mcp-manager](https://github.com/Agentic-Operation/tool-mcp-manager) |
| Conformance kit | [agent-conformance](https://github.com/Agentic-Operation/agent-conformance) |
| Published docs / comms pack (canonical) | [agent-standard-docs](https://github.com/Agentic-Operation/agent-standard-docs) |
