# Pre-submission self-check (Spec-443 instance)

Run `conformance-kit/validators/profile_lint.py` first — it automates most of these.

- [ ] Cover block complete; status accurate.
- [ ] Identity & Integrity populated (id, uuid v4, version, provider, CID for production).
- [ ] Classification: six axes present; Non-Agentic ⇒ ≤ L2; Agentic ⇒ Learning+Reasoning+Planning active in §3.1; Orchestrator role ⇒ §6.1 "Orchestrates".
- [ ] Impact radius consistent with autonomy (High ⇒ L4/L5, not L1).
- [ ] Companion refs declared (or TBD+date at draft) and bidirectional.
- [ ] Executive summary: 150–250 words + exactly 3 outcomes, each mapped to a §9.3 row.
- [ ] §2.1 has 4–10 responsibilities with eTOM mapping; §2.2 exclusions name alternative owners; §2.3 assumptions testable.
- [ ] §3.1 addresses all 8 components; §3.3 four memory layers; §3.4 names engine + logic structure; §3.5 covers every interface.
- [ ] §4.2: every core task has ≥1 skill; skill IDs carry the TMF prefix; source_taxonomy declared.
- [ ] §5.2 entries name protocol + failure mode + Open API ref (no "various internal APIs").
- [ ] §6: posture declared with protocol; variables have publisher+consumer; signals are conditional; §6.4 topology present if posture ≠ Solo.
- [ ] §8.1: ≥1 embargo + ≥1 burden at L3+ (ODP-EL tokens); §8.2 covers AI 100-1 and AI 100-3.
- [ ] §9.2 learning metrics present iff Learning Module declared; model refs present ([EXT]).
- [ ] §10.1a per-environment prerequisites present if Cross-Environment; §10.4 maintenance plan + autonomy_case_ref at L3+; last_updated ISO 8601.
- [ ] Deviation register records every [R]/[O] deviation.
