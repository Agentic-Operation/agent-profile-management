# spec443 CLI

`python tools/cli/spec443.py <subcommand>` — lint / publish / status / report against a profile JSON or
the profile API (`api/openapi/profile-api.yaml`, default `http://localhost:8080/v1`). Lint always runs
locally first via `conformance-kit/validators/profile_lint.py`.
