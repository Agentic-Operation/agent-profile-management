# Quickstart: author your first Spec-443 profile

1. Copy the worked example: `examples/loyalty-agent/` (populated in Phase 1) or start from
   `user-tools/` templates.
2. Fill the Front Matter: cover block, **Identity & Integrity** (`id`, `uuid` v4, `version` semver +
   stability tag, `provider`, `content_identifier_cid`, `integrity_wrapper`), **Classification** (six axes),
   companion refs to Spec-444/Spec-445 (TBD with date allowed at draft).
3. Write the Executive Summary (150–250 words + exactly 3 measurable outcomes).
4. Complete sections 1–10 per [docs/communication/01-define-your-agent.md](../communication/01-define-your-agent.md).
5. Validate: `pre-commit run --all-files`; in Phase 1 also `conformance-kit/validators` + the CI gate.
6. Publish via the profile API (`api/openapi/`, Phase 1) so the Spec-445 card can point back at it.

Note: the profile's `tmf444_bootstrap_ref` / `tmf445_agent_card_ref` and the sibling artifacts' back-references
must be bidirectional — one-way pointers fail the cross-check.
