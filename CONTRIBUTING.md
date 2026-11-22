# Contributing

## Workflow

1. Create a branch: `vibe/<short-slug>-5a1ad6` (e.g. `vibe/comms-pack-5a1ad6`).
2. Make focused commits with clear messages.
3. Open a **draft PR** while work is in progress; mark ready-for-review when done.
4. All checks (docs lint now; schema + cross-check + secret scan once the conformance-kit lands) must pass.

## Proposing changes to the spec

- Open an issue using the **Extension proposal** template for any change to `spec/`.
- Every extension must be recorded in `spec/annexes/delta-vs-TMF44X.md` with its TMF44X origin section.
- Conformance classes ([M]/[R]/[O]/[M-conditional]) are normative — instances cannot reassign them;
  propose class changes only via a spec-level issue with rationale.

## Triad consistency

Changes here that affect join keys (identity fields, skill IDs, companion pointers, cross-check
manifest) must be mirrored in the sibling repos:
[`agent-bootstrap-management`](https://github.com/Agentic-Operation/agent-bootstrap-management) and
[`agent-discovery-card`](https://github.com/Agentic-Operation/agent-discovery-card).
The cross-check validators in each repo's `conformance-kit/` will fail CI on drift.

## Code of conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
